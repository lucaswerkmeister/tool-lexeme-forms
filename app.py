import copy
import flask
import jinja2
import json
import mwapi
import mwoauth
import os
import re
import requests
import requests_oauthlib
import toolforge
import yaml
from templates import templates
from translations import translations

app = flask.Flask(__name__)

app.before_request(toolforge.redirect_to_https)

toolforge.set_user_agent('lexeme-forms', email='mail@lucaswerkmeister.de')
user_agent = requests.utils.default_user_agent()

__dir__ = os.path.dirname(__file__)
try:
    with open(os.path.join(__dir__, 'config.yaml')) as config_file:
        app.config.update(yaml.safe_load(config_file))
        consumer_token = mwoauth.ConsumerToken(app.config['oauth']['consumer_key'], app.config['oauth']['consumer_secret'])
except FileNotFoundError:
    print('config.yaml file not found, assuming local development setup')

@app.template_filter('form2input')
@jinja2.contextfilter
def form2input(context, form):
    example = form['example']
    match = re.match(r'^(.*)\[(.*)\](.*)$', example)
    if match:
        (prefix, placeholder, suffix) = match.groups()
        return (flask.Markup.escape(prefix) +
                flask.Markup(r'<input type="text" name="form_representation" placeholder="') +
                flask.Markup.escape(placeholder) +
                flask.Markup(r'"') +
                (flask.Markup(r' required') if 'advanced' not in context else flask.Markup('')) +
                (flask.Markup(r' value="') + flask.Markup.escape(form['value']) + flask.Markup(r'"') if 'value' in form else flask.Markup('')) +
                flask.Markup(r'>') +
                flask.Markup.escape(suffix))
    else:
        raise Exception('Invalid template: missing [placeholder]: ' + example)

@app.route('/')
def index():
    return flask.render_template(
        'index.html',
        templates=templates,
    )

@app.route('/template/<template_name>/', methods=['GET', 'POST'])
def process_template(template_name):
    return process_template_advanced(template_name=template_name, advanced=False)

@app.route('/template/<template_name>/advanced/', methods=['GET', 'POST'])
def process_template_advanced(template_name, advanced=True):
    response = if_no_such_template_redirect(template_name)
    if response:
        return response

    response = if_needs_oauth_redirect()
    if response:
        return response

    template = templates[template_name]

    if flask.request.method == 'POST':
        form_data = flask.request.form

        response = if_has_duplicates_redirect(template, form_data)
        if response:
            return response

        lexeme_data = build_lexeme(template, form_data)

        if 'oauth' in app.config:
            return submit_lexeme(template, lexeme_data)
        else:
            return flask.Response(lexeme_data, mimetype='application/json')
    else:
        return flask.render_template(
            'template.html',
            template=template,
            template_name=template_name,
            translations=translations[template['language_code']],
            advanced=advanced,
        )

def if_no_such_template_redirect(template_name):
    if template_name not in templates:
        return flask.render_template(
            'no-such-template.html',
            template_name=template_name,
        )
    else:
        return None

def if_needs_oauth_redirect():
    if 'oauth' in app.config and 'oauth_access_token' not in flask.session:
        (redirect, request_token) = mwoauth.initiate('https://www.wikidata.org/w/index.php', consumer_token, user_agent=user_agent)
        flask.session['oauth_request_token'] = dict(zip(request_token._fields, request_token))
        flask.session['oauth_redirect_target'] = flask.request.path
        return flask.redirect(redirect)
    else:
        return None

@app.route('/oauth/callback')
def oauth_callback():
    access_token = mwoauth.complete('https://www.wikidata.org/w/index.php', consumer_token, mwoauth.RequestToken(**flask.session['oauth_request_token']), flask.request.query_string, user_agent=user_agent)
    flask.session['oauth_access_token'] = dict(zip(access_token._fields, access_token))
    return flask.redirect(flask.session['oauth_redirect_target'])

def if_has_duplicates_redirect(template, form_data):
    if 'no_duplicate' in form_data:
        return None

    duplicates = find_duplicates(template, form_data)
    if duplicates:
        return flask.render_template(
            'template.html',
            template=add_form_data_to_template(form_data, template),
            translations=translations[template['language_code']],
            duplicates=duplicates,
        )
    else:
        return None

def find_duplicates(template, form_data):
    if 'test' in template:
        host = 'https://test.wikidata.org'
    else:
        host = 'https://www.wikidata.org'
    session = mwapi.Session(
        host,
        user_agent=user_agent,
    )

    lemma = get_lemma(form_data)
    language = template['language_code']
    response = session.get(
        action='wbsearchentities',
        search=lemma,
        language=language,
        uselang=language, # for the result descriptions
        type='lexeme',
        limit=50,
    )
    matches = []
    for result in response['search']:
        if result['label'] == lemma and result['match']['language'] == language:
            matches.append({'id': result['id'], 'uri': result['concepturi'], 'label': result['label'], 'description': result['description']})
    return matches

def get_lemma(form_data):
    for form_representation in form_data.getlist('form_representation'):
        if form_representation is not '':
            return form_representation
    flask.abort(400)

def add_form_data_to_template(form_data, template):
    template = copy.deepcopy(template)
    for (form_representation, form) in zip(form_data.getlist('form_representation'), template['forms']):
        form['value'] = form_representation
    return template

def build_lexeme(template, form_data):
    lang = template['language_code']
    return json.dumps({
        'type': 'lexeme',
        'lemmas': {lang: {'language': lang, 'value': get_lemma(form_data)}},
        'language': template['language_item_id'],
        'lexicalCategory': template['lexical_category_item_id'],
        'claims': template['claims'],
        'forms': [
            {'add': '', 'representations': {lang: {'language': lang, 'value': form_representation}}, 'grammaticalFeatures': grammaticalFeatures, 'claims': []}
            for (form_representation, grammaticalFeatures) in zip(
                    form_data.getlist('form_representation'),
                    map(lambda form: form['grammatical_features_item_ids'], template['forms'])
            )
            if form_representation is not ''
        ]
    })

def submit_lexeme(template, lexeme_data):
    if 'test' in template:
        host = 'https://test.wikidata.org'
    else:
        host = 'https://www.wikidata.org'
    session = mwapi.Session(
        host=host,
        auth=generate_auth(),
        user_agent=user_agent,
    )

    token = session.get(action='query', meta='tokens')['query']['tokens']['csrftoken']
    response = session.post(
        action='wbeditentity',
        new='lexeme',
        data=lexeme_data,
        token=token,
    )
    return flask.redirect(host + '/entity/' + response['entity']['id'], code=303)

def generate_auth():
    access_token = mwoauth.AccessToken(**flask.session['oauth_access_token'])
    return requests_oauthlib.OAuth1(
        client_key=consumer_token.key,
        client_secret=consumer_token.secret,
        resource_owner_key=access_token.key,
        resource_owner_secret=access_token.secret,
    )
