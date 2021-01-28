import babel
import collections
import copy
import decorator
import flask
import jinja2
import json
import mwapi
import mwoauth
import os
import random
import re
import requests_oauthlib
import string
import toolforge
import yaml
import werkzeug.datastructures

from flask_utils import OrderedFlask, TagOrderedMultiDict, TagImmutableOrderedMultiDict
from formatters import I18nFormatter
from language_names import autonym
from matching import match_template_to_lexeme_data, match_lexeme_forms_to_template, match_template_entity_to_lexeme_entity
from parse_tpsv import parse_lexemes
from templates import templates
from translations import translations

app = OrderedFlask(__name__)
app.session_interface.serializer.register(TagOrderedMultiDict, index=0)
app.session_interface.serializer.register(TagImmutableOrderedMultiDict, index=0)

user_agent = toolforge.set_user_agent('lexeme-forms', email='mail@lucaswerkmeister.de')

__dir__ = os.path.dirname(__file__)
try:
    with open(os.path.join(__dir__, 'config.yaml')) as config_file:
        app.config.update(yaml.safe_load(config_file))
        consumer_token = mwoauth.ConsumerToken(app.config['oauth']['consumer_key'], app.config['oauth']['consumer_secret'])
except FileNotFoundError:
    print('config.yaml file not found, assuming local development setup')
    app.secret_key = 'fake'

@decorator.decorator
def enableCORS(func, *args, **kwargs):
    rv = func(*args, **kwargs)
    response = flask.make_response(rv)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.after_request
def denyFrame(response):
    """Disallow embedding the tool’s pages in other websites.

    If other websites can embed this tool’s pages, e. g. in <iframe>s,
    other tools hosted on tools.wmflabs.org can send arbitrary web
    requests from this tool’s context, bypassing the referrer-based
    CSRF protection.
    """
    response.headers['X-Frame-Options'] = 'deny'
    return response

@app.template_filter()
@jinja2.contextfilter
def form2input(context, form, first=False, template_language_code=None, representation_language_code=None):
    (prefix, placeholder, suffix) = split_example(form)
    if 'lexeme_forms' in form and template_language_code != representation_language_code:
        placeholder = '/'.join(lexeme_form['representations'][template_language_code]['value']
                               for lexeme_form in form['lexeme_forms']
                               if template_language_code in lexeme_form['representations'])
    return (flask.Markup.escape(prefix) +
            flask.Markup(r'<input type="text" name="form_representation" placeholder="') +
            flask.Markup.escape(placeholder) +
            flask.Markup(r'"') +
            flask.Markup(r' pattern="[^/]+(?:/[^/]+)*"') +
            (flask.Markup(r' required') if not context['advanced'] else flask.Markup('')) +
            (flask.Markup(r' autofocus') if first else flask.Markup('')) +
            (flask.Markup(r' value="') + flask.Markup.escape(form['value']) + flask.Markup(r'"') if 'value' in form else flask.Markup('')) +
            flask.Markup(r' spellcheck="true"') +
            (flask.Markup(r' lang="') + flask.Markup.escape(representation_language_code) + flask.Markup(r'"') if representation_language_code != template_language_code else flask.Markup('')) +
            flask.Markup(r'>') +
            flask.Markup.escape(suffix))

def split_example(form):
    example = form['example']
    match = re.match(r'^(.*)\[(.*)\](.*)$', example)
    if match:
        (prefix, placeholder, suffix) = match.groups()
        return (prefix, placeholder, suffix)
    else:
        raise Exception('Invalid template: missing [placeholder]: ' + example)

@app.template_filter()
def render_duplicates(duplicates, language_code, actionable, template_name=None, form_representations=[]):
    return flask.render_template(
        'duplicates.html',
        duplicates=duplicates,
        actionable=actionable,
        template_name=template_name,
        form_representations=form_representations,
    )

@app.template_filter()
def augment_description(description, forms_count, senses_count):
    if forms_count is None or senses_count is None:
        return description
    return message_with_kwargs(
        'description_with_forms_and_senses',
        description=description,
        forms=int(forms_count),
        senses=int(senses_count),
    )

@app.template_global()
def csrf_token():
    if '_csrf_token' not in flask.session:
        flask.session['_csrf_token'] = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(64))
    return flask.session['_csrf_token']

@app.template_global()
def template_group(template):
    group = language_autonym_with_code(template['language_code'])
    if 'test' in template:
        group += ', test.wikidata.org'
    return group

@app.template_filter()
def user_link(user_name):
    return (flask.Markup(r'<a href="https://www.wikidata.org/wiki/User:') +
            flask.Markup.escape(user_name.replace(' ', '_')) +
            flask.Markup(r'">') +
            flask.Markup(r'<bdi>') +
            flask.Markup.escape(user_name) +
            flask.Markup(r'</bdi>') +
            flask.Markup(r'</a>'))

@app.template_global()
def render_oauth_username():
    identity = identify()
    if identity is None:
        return flask.Markup(r'')
    return (flask.Markup(r'<span class="navbar-text">Logged in as ') +
            user_link(identity['username']) +
            flask.Markup(r'</span>'))

@app.template_global()
def message(message_code, language_code=None):
    message, language = message_with_language(message_code, language_code)
    return message

def message_with_language(message_code, language_code=None):
    if not language_code:
        language_code = flask.g.interface_language_code
    if language_code == 'bn-x-Q6747180':
        # Manbhumi reuses the standard Bengali messages
        language_code = 'bn'
    if message_code not in translations[language_code]:
        language_code = 'en'
    text = translations[language_code][message_code]
    return flask.Markup(text), language_code

@app.template_global()
def message_with_kwargs(message_code, **kwargs):
    template, language = message_with_language(message_code)
    if language == 'la':
        language = 'en' # Latin is not in CLDR, English has same plural forms
    return I18nFormatter(locale_identifier=language,
                         get_gender=get_gender).format(template, **kwargs)

@app.template_filter()
def text_direction(language_code):
    try:
        locale = babel.Locale.parse(language_code.split('-')[0]) # the -x-Qid stuff is not understood by Babel
    except babel.UnknownLocaleError:
        return 'auto'
    else:
        return locale.text_direction

@app.template_filter()
def term_span(term):
    return (flask.Markup(r'<span lang="') +
            flask.Markup.escape(term['language']) +
            flask.Markup(r'" dir="') +
            flask.Markup.escape(text_direction(term['language'])) +
            flask.Markup(r'">') +
            flask.Markup.escape(term['value']) +
            flask.Markup(r'</span>'))

@app.template_filter()
def language_autonym_with_code(language_code):
    code_zxx = (flask.Markup(r'<span lang=zxx>') +
                flask.Markup.escape(language_code) +
                flask.Markup(r'</span>'))
    language_autonym = autonym(language_code)
    if language_autonym is None:
        return code_zxx
    return (flask.Markup(r'<span lang="') +
            flask.Markup.escape(language_code) +
            flask.Markup(r'" dir="') +
            flask.Markup.escape(text_direction(language_code)) +
            flask.Markup(r'">') +
            flask.Markup.escape(language_autonym) +
            flask.Markup(r' (') +
            code_zxx +
            flask.Markup(r')</span>'))

@app.route('/')
def index():
    return flask.render_template(
        'index.html',
        templates=templates,
        can_use_bulk_mode=can_use_bulk_mode(),
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
    flask.g.interface_language_code = template['language_code']
    form_data = flask.request.form

    if flask.request.method == 'POST' and flask.request.referrer == current_url():
        response = if_has_duplicates_redirect(template, advanced, form_data)
        if response:
            return response

        response = if_needs_csrf_redirect(template, advanced, form_data)
        if response:
            return response

        lexeme_data = build_lexeme(template, form_data)
        summary = build_summary(template, form_data)

        if 'oauth' in app.config:
            lexeme_uri = submit_lexeme(template, lexeme_data, summary)
            return flask.redirect(lexeme_uri, code=303)
        else:
            print(summary)
            return flask.jsonify(lexeme_data)
    else:
        if not form_data:
            form_data = flask.request.args
        return flask.render_template(
            'template.html',
            template=add_form_data_to_template(form_data, template),
            advanced=advanced,
            can_use_bulk_mode=can_use_bulk_mode(),
        )

@app.route('/template/<template_name>/bulk/', methods=['GET', 'POST'])
def process_template_bulk(template_name):
    response = if_no_such_template_redirect(template_name)
    if response:
        return response

    response = if_needs_oauth_redirect()
    if response:
        return response

    template = templates[template_name]
    flask.g.interface_language_code = template['language_code']

    if not can_use_bulk_mode():
        return flask.render_template(
            'bulk-not-allowed.html',
            template=template,
        )

    if (flask.request.method == 'POST' and
        flask.request.referrer == current_url() and
        csrf_token_matches(flask.request.form)):

        form_data = flask.request.form
        try:
            lexemes = parse_lexemes(form_data.get('lexemes'), template)
        except ValueError as parse_error:
            return flask.render_template(
                'bulk.html',
                template=template,
                value=form_data.get('lexemes'),
                parse_error=parse_error
        )

        results = []

        for lexeme in lexemes:
            if not lexeme.get('lexeme_id'):
                duplicates = find_duplicates(template, lexeme)
                if duplicates:
                    results.append(('duplicates', duplicates))
                    continue
            lexeme_data = build_lexeme(template, lexeme)
            summary = build_summary(template, form_data)

            if 'oauth' in app.config:
                lexeme_uri = submit_lexeme(template, lexeme_data, summary)
                results.append(('lexeme_uri', lexeme_uri))
            else:
                print(summary)
                results.append(('lexeme_data', lexeme_data))

        if 'oauth' in app.config:
            return flask.render_template(
                'bulk-result.html',
                template=template,
                results=results,
            )
        else:
            return flask.jsonify([result[1] for result in results])

    else:
        placeholder = ''
        for form in template['forms']:
            if placeholder:
                placeholder += '|'
            (prefix, form_placeholder, suffix) = split_example(form)
            placeholder += form_placeholder
        placeholder += '\n...'
        csrf_error = False

        if flask.request.method == 'POST':
            form_data = flask.request.form
            if 'form_representation' in form_data:
                # user came from non-bulk mode
                representations = form_data.getlist('form_representation')
                value = '|'.join(representations)
                if value == '|' * (len(representations) - 1):
                    # ...but had not typed anything into non-bulk mode yet,
                    # clear the value so that the placeholder is shown
                    value = ''
                else:
                    value += '\n' # for convenience when adding more
            else:
                # user came from bulk mode with CSRF error
                value = form_data.get('lexemes')
                csrf_error = True
        else:
            value = None

        return flask.render_template(
            'bulk.html',
            template=template,
            placeholder=placeholder,
            value=value,
            csrf_error=csrf_error,
        )

@app.route('/template/<template_name>/edit/<lexeme_id>', methods=['GET', 'POST'])
def process_template_edit(template_name, lexeme_id):
    response = if_no_such_template_redirect(template_name)
    if response:
        return response

    response = if_needs_oauth_redirect()
    if response:
        return response

    template = templates[template_name]
    template_language_code = template['language_code']
    flask.g.interface_language_code = template_language_code
    representation_language_code = flask.request.args.get('language_code', template_language_code)
    wiki = 'test' if 'test' in template else 'www'

    if flask.request.method == 'POST':
        lexeme_revision = flask.request.form['_lexeme_revision']
        lexeme_data = get_lexeme_data(lexeme_id, wiki, lexeme_revision)
    else:
        lexeme_data = get_lexeme_data(lexeme_id, wiki)
        lexeme_revision = lexeme_data['lastrevid']

    lexeme_match = match_template_to_lexeme_data(template, lexeme_data)
    lexeme_matches_template = (
        lexeme_match['language']
        and lexeme_match['lexical_category']
        and not lexeme_match['conflicting_statements']
    )
    template = match_lexeme_forms_to_template(lexeme_data['forms'], template)
    template['lexeme_id'] = lexeme_id
    template['lexeme_revision'] = lexeme_revision

    if (flask.request.method == 'POST' and
        flask.request.referrer == current_url() and
        csrf_token_matches(flask.request.form)):
        form_data = flask.request.form
        lexeme_data = update_lexeme(lexeme_data, template, form_data, representation_language_code, missing_statements=lexeme_match['missing_statements'])
        summary = build_summary(template, form_data)

        if 'oauth' in app.config:
            lexeme_uri = submit_lexeme(template, lexeme_data, summary)
            return flask.redirect(lexeme_uri, code=303)
        else:
            print(summary)
            return flask.jsonify(lexeme_data)

    for template_form in template['forms']:
        lexeme_forms = template_form.get('lexeme_forms')
        if lexeme_forms: # TODO use walrus operator in Python 3.8
            template_form['value'] = '/'.join(lexeme_form['representations'][representation_language_code]['value']
                                              for lexeme_form in lexeme_forms
                                              if representation_language_code in lexeme_form['representations'])
    if flask.request.method == 'POST':
        template = add_form_data_to_template(flask.request.form, template)
    elif flask.request.args:
        template = add_form_data_to_template(flask.request.args, template, overwrite=False)

    add_labels_to_lexeme_forms_grammatical_features(
        mwapi.Session(
            'https://' + wiki + '.wikidata.org',
            user_agent=user_agent,
        ),
        template_language_code,
        template.get('unmatched_lexeme_forms', []) + template.get('ambiguous_lexeme_forms', [])
    )

    return flask.render_template(
        'edit.html',
        template=template,
        lemmas=lexeme_data['lemmas'],
        lexeme_matches_template=lexeme_matches_template,
        template_language_code=template_language_code,
        representation_language_code=representation_language_code,
        advanced=True, # for form2input
        csrf_error=flask.request.method == 'POST',
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
        flask.session['oauth_redirect_target'] = current_url()
        return flask.redirect(redirect)
    else:
        return None

@app.route('/oauth/callback')
def oauth_callback():
    access_token = mwoauth.complete('https://www.wikidata.org/w/index.php', consumer_token, mwoauth.RequestToken(**flask.session.pop('oauth_request_token')), flask.request.query_string, user_agent=user_agent)
    flask.session['oauth_access_token'] = dict(zip(access_token._fields, access_token))
    flask.session.pop('_csrf_token', None)
    return flask.redirect(flask.session.pop('oauth_redirect_target'))

@app.route('/logout')
def logout():
    flask.session.pop('oauth_access_token', None)
    return flask.redirect(flask.url_for('index'))

def if_has_duplicates_redirect(template, advanced, form_data):
    if 'no_duplicate' in form_data:
        return None
    if 'lexeme_id' in form_data and form_data['lexeme_id']:
        return None

    duplicates = find_duplicates(template, form_data)
    if duplicates:
        return flask.render_template(
            'template.html',
            template=add_form_data_to_template(form_data, template),
            advanced=advanced,
            duplicates=duplicates,
            submitted_form_representations=form_data.getlist('form_representation'),
        )
    else:
        return None

def find_duplicates(template, form_data):
    wiki = 'test' if 'test' in template else 'www'
    language_code = template['language_code']
    lemma = get_lemma(form_data)
    if lemma:
        return get_duplicates(wiki, language_code, lemma)
    else:
        flask.abort(400)

def get_lemma(form_data):
    for form_representation in form_data.getlist('form_representation'):
        for form_representation_variant in form_representation.split('/'):
            if form_representation_variant != '':
                return form_representation_variant
    return None

@app.route('/api/v1/duplicates/<any(www,test):wiki>/<language_code>/<path:lemma>')
@enableCORS
def get_duplicates_api(wiki, language_code, lemma):
    flask.g.interface_language_code = language_code
    matches = get_duplicates(wiki, language_code, lemma)
    if not matches:
        return flask.Response(status=204)
    if flask.request.accept_mimetypes.accept_html:
        return render_duplicates(
            matches,
            language_code,
            actionable=True,
            template_name=flask.request.args.get('template_name'),
        )
    else:
        return flask.jsonify(matches)

def get_duplicates(wiki, language_code, lemma):
    host = 'https://' + wiki + '.wikidata.org'
    session = mwapi.Session(
        host,
        user_agent=user_agent,
    )

    api_language_code = 'bn' if language_code == 'bn-x-Q6747180' else language_code

    response = session.get(
        action='wbsearchentities',
        search=lemma,
        language=api_language_code,
        uselang=api_language_code, # for the result descriptions
        type='lexeme',
        limit=50,
    )
    matches = collections.OrderedDict()
    for result in response['search']:
        if (result.get('label') == lemma and
            (result['match']['language'] == language_code or
             result['match']['language'] == 'und')): # T230833
            matches[result['id']] = {'id': result['id'], 'uri': result['concepturi'], 'label': result['label'], 'description': result['description']}

    if matches:
        response = session.get( # no, this can’t be combined with the previous call by using generator=wbsearch – then we don’t get the match language
            action='query',
            titles=['Lexeme:' + id for id in matches],
            prop=['pageprops'],
            ppprop=['wbl-forms', 'wbl-senses'],
        )
        for page in response['query']['pages'].values():
            id = page['title'][len('Lexeme:'):]
            pageprops = page.get('pageprops', {})
            matches[id]['forms_count'] = pageprops.get('wbl-forms')
            matches[id]['senses_count'] = pageprops.get('wbl-senses')

    return list(matches.values()) # list() to turn odict_values (not JSON serializable) into plain list

@app.route('/api/v1/no_duplicate/<language_code>')
@app.template_global()
def render_no_duplicate(language_code):
    flask.g.interface_language_code = language_code
    return flask.render_template(
        'no_duplicate.html',
    )

@app.route('/api/v1/advanced_partial_forms_hint/<language_code>')
def render_advanced_partial_forms_hint(language_code):
    flask.g.interface_language_code = language_code
    return flask.render_template(
        'advanced_partial_forms_hint.html',
    )

@app.route('/api/v1/match_template_to_lexeme/<any(www,test):wiki>/<lexeme_id>')
@enableCORS
def match_templates_to_lexeme_id(wiki, lexeme_id):
    lexeme_data = get_lexeme_data(lexeme_id, wiki)

    return flask.jsonify({
        template_name: match_template_to_lexeme_data(template, lexeme_data)
        for template_name, template in templates.items()
    })

@app.route('/api/v1/match_template_to_lexeme/<any(www,test):wiki>/<lexeme_id>/<template_name>')
@enableCORS
def match_template_to_lexeme_id(wiki, lexeme_id, template_name):
    template = templates.get(template_name)
    if not template:
        return 'no such template\n', 404

    lexeme_data = get_lexeme_data(lexeme_id, wiki)

    return flask.jsonify(match_template_to_lexeme_data(template, lexeme_data))

def get_lexeme_data(lexeme_id, wiki, revision=None):
    host = 'https://' + wiki + '.wikidata.org'
    session = mwapi.Session(
        host,
        user_agent=user_agent,
    )

    if revision:
        entities_data = session.session.get(
            f'{host}/wiki/Special:EntityData/{lexeme_id}.json?revision={revision}',
        ).json()
    else: # TODO when T128486 is fixed, use Special:EntityData without revision too, for better caching
        entities_data = session.get(
            action='wbgetentities',
            ids=[lexeme_id],
        )

    lexeme_data = entities_data['entities'][lexeme_id]
    return lexeme_data

def add_form_data_to_template(form_data, template, overwrite=True):
    template = copy.deepcopy(template)
    for (form_representation, form) in zip(form_data.getlist('form_representation'), template['forms']):
        if overwrite or not form.get('value'):
            form['value'] = form_representation
    if 'lexeme_id' in form_data:
        template['lexeme_id'] = form_data['lexeme_id']
    if 'generated_via' in form_data:
        template['generated_via'] = form_data['generated_via']
    return template

def if_needs_csrf_redirect(template, advanced, form_data):
    if not csrf_token_matches(form_data):
        return flask.render_template(
            'template.html',
            template=add_form_data_to_template(form_data, template),
            advanced=advanced,
            csrf_error=True,
        )
    else:
        return None

def csrf_token_matches(form_data):
    token = flask.session.get('_csrf_token')
    if not token or token != form_data.get('_csrf_token'):
        return False
    else:
        return True

def current_url(include_args=True):
    args = flask.request.args.to_dict(flat=False) if include_args else {}
    return flask.url_for(
        flask.request.endpoint,
        _external=True,
        _scheme=flask.request.headers.get('X-Forwarded-Proto', 'http'),
        **flask.request.view_args,
        **args,
    ).replace('+', '%20')

@app.template_global()
def can_use_bulk_mode():
    if 'oauth' not in app.config:
        return True
    identity = identify()
    if not identity:
        return False
    return 'autoconfirmed' in identity['groups']

def build_lexeme(template, form_data):
    lang = template['language_code']
    forms = []
    form_representations = form_data.getlist('form_representation')
    for form_representation, form in zip(form_representations, template['forms']):
        if not form_representation:
            continue
        for form_representation_variant in form_representation.split('/'):
            if not form_representation_variant:
                flask.abort(400)
            forms.append(build_form(form, lang, form_representation_variant))
    lexeme_data = {
        'type': 'lexeme',
        'forms': forms,
    }
    lexeme_id = form_data.get('lexeme_id', '')
    if lexeme_id:
        lexeme_data['id'] = lexeme_id
        wiki = 'test' if 'test' in template else 'www'
        match = match_template_to_lexeme_data(template, get_lexeme_data(lexeme_id, wiki))
        # TODO warn if match['conflicting_statements']?
        lexeme_data['claims'] = match['missing_statements']
    else:
        lemma = get_lemma(form_data)
        if lemma is None:
            flask.abort(400)
        lexeme_data.update({
            'lemmas': {lang: {'language': lang, 'value': lemma}},
            'language': template['language_item_id'],
            'lexicalCategory': template['lexical_category_item_id'],
            'claims': template.get('statements', {}),
        })
    return lexeme_data

def build_form(template_form, template_language, form_representation):
    return {
        'add': '',
        'representations': {template_language: {'language': template_language, 'value': form_representation}},
        'grammaticalFeatures': template_form['grammatical_features_item_ids'],
        'claims': template_form.get('statements', {})
    }

def update_lexeme(lexeme_data, template, form_data, representation_language_code, missing_statements=None):
    lexeme_data = copy.deepcopy(lexeme_data)
    lexeme_data['base_revision_id'] = template['lexeme_revision']

    for form_data_representation, template_form in zip(form_data.getlist('form_representation'), template['forms']):
        form_data_representation_variants = form_data_representation.split('/')
        if form_data_representation_variants == ['']:
            form_data_representation_variants = []
        lexeme_forms = template_form.get('lexeme_forms', []).copy()
        # process “representations” that actually reference existing forms first
        for form_data_representation_variant in reversed(form_data_representation_variants): # reversed so that the remove within the loop doesn’t disturb the iteration
            if not re.match(r'^L[1-9][0-9]*-F[1-9][0-9]*$', form_data_representation_variant):
                continue
            lexeme_form = find_form(lexeme_data, form_id=form_data_representation_variant)
            if lexeme_form in template.get('unmatched_lexeme_forms', []):
                template['unmatched_lexeme_forms'].remove(lexeme_form)
            elif lexeme_form in template.get('ambiguous_lexeme_forms', []):
                template['ambiguous_lexeme_forms'].remove(lexeme_form)
            else:
                raise Exception('Form %s is neither unmatched nor ambiguous, refusing to re-match it to a different template form' % form_data_representation_variant)
            # add missing grammatical features
            for grammatical_feature_item_id in template_form['grammatical_features_item_ids']:
                if grammatical_feature_item_id not in lexeme_form['grammaticalFeatures']:
                    lexeme_form['grammaticalFeatures'].append(grammatical_feature_item_id)
            # add missing statements (and complain about conflicting ones)
            form_matched_statements, form_missing_statements, form_conflicting_statements = match_template_entity_to_lexeme_entity('test' in template, template_form, lexeme_form)
            if form_conflicting_statements:
                raise Exception('Conflicting statements!') # TODO better error reporting
            for property_id, statements in form_missing_statements.items():
                lexeme_form.setdefault('claims', {}).setdefault(property_id, []).extend(statements)
            form_data_representation_variants.remove(form_data_representation_variant)
        # find and remove matching forms (no modification necessary)
        for lexeme_form in reversed(lexeme_forms): # reversed so that the remove within the loop doesn’t disturb the iteration
            if representation_language_code not in lexeme_form['representations']:
                continue
            lexeme_form_representation = lexeme_form['representations'][representation_language_code]
            if lexeme_form_representation['value'] in form_data_representation_variants:
                lexeme_forms.remove(lexeme_form)
                form_data_representation_variants.remove(lexeme_form_representation['value'])
                break
        # overwrite remaining lexeme forms with form data as long as we have both
        # currently simply in order, cleverer matching via edit distance may be possible but likely not necessary
        overwritten_forms = 0
        for form_data_representation_variant, lexeme_form in zip(form_data_representation_variants, lexeme_forms):
            lexeme_form = find_form(lexeme_data, lexeme_form['id'])
            lexeme_form_representation = lexeme_form['representations'].setdefault(representation_language_code, {'language': representation_language_code})
            assert form_data_representation_variant, 'Representation cannot be empty'
            lexeme_form_representation['value'] = form_data_representation_variant
            overwritten_forms += 1
        form_data_representation_variants = form_data_representation_variants[overwritten_forms:]
        lexeme_forms = lexeme_forms[overwritten_forms:]
        # add remaining form data as new OR delete remaining lexeme forms
        assert not (form_data_representation_variants and lexeme_forms), 'After previous loop, at least one list must be exhausted'
        for form_data_representation_variant in form_data_representation_variants:
            assert form_data_representation_variant, 'Representation cannot be empty'
            lexeme_form = build_form(template_form, representation_language_code, form_data_representation_variant)
            lexeme_data['forms'].append(lexeme_form)
            template_form.setdefault('lexeme_forms', []).append(lexeme_form) # so it can be found as first_form below
        for lexeme_form in lexeme_forms:
            lexeme_form = find_form(lexeme_data, lexeme_form['id'])
            if representation_language_code in lexeme_form['representations']:
                lexeme_form['remove'] = ''
            # otherwise it’s an unrelated form that wasn’t shown to begin with, leave it alone

    for property_id, statements in (missing_statements or {}).items():
        lexeme_data.setdefault('claims', {}).setdefault(property_id, []).extend(statements)

    first_form = next(iter(template['forms'][0].get('lexeme_forms', [])), None)
    if first_form:
        first_form_id = first_form.get('id')
        if first_form_id: # TODO use walrus operator in Python 3.8+
            first_form = find_form(lexeme_data, first_form_id) # find edited version
        else:
            # it’s a new form, first_form is already the edited version
            pass
        if representation_language_code in first_form['representations']:
            lexeme_data['lemmas'][representation_language_code] = first_form['representations'][representation_language_code]
        else:
            lexeme_data['lemmas'].pop(representation_language_code, None)

    return lexeme_data

def find_form(lexeme_data, form_id):
    for form in lexeme_data['forms']:
        if form['id'] == form_id:
            return form
    raise LookupError(f'Form {form_id} not found in lexeme data for {lexeme_data["id"]}')

def build_summary(template, form_data):
    template_name = template['@template_name']
    url = current_url()
    toolforge_match = re.match(r'https://([a-z0-9-_]+).toolforge.org/(.*)$', url)
    if toolforge_match: # TODO use walrus operator in Python 3.8+
        tool_name = toolforge_match.group(1)
        rest = toolforge_match.group(2)
        summary = '[[toolforge:%s/%s|%s]]' % (tool_name, rest, template_name)
    elif url.startswith('https://tools.wmflabs.org/'):
        relative = url[len('https://tools.wmflabs.org/'):]
        summary = '[[toolforge:%s|%s]]' % (relative, template_name)
    else:
        summary = template_name

    if 'generated_via' in form_data:
        summary += ', generated via ' + form_data['generated_via']

    return summary

def submit_lexeme(template, lexeme_data, summary):
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
    selector = {'id': lexeme_data['id']} if 'id' in lexeme_data else {'new': 'lexeme'}
    if 'base_revision_id' in lexeme_data:
        selector['baserevid'] = lexeme_data['base_revision_id']
    response = session.post(
        action='wbeditentity',
        data=json.dumps(lexeme_data),
        summary=summary,
        token=token,
        **selector
    )
    lexeme_id = response['entity']['id']
    revid = response['entity']['lastrevid']

    return host + '/entity/' + lexeme_id

def add_labels_to_lexeme_forms_grammatical_features(session, language, lexeme_forms):
    grammatical_features_item_ids = set()
    for lexeme_form in lexeme_forms:
        grammatical_features_item_ids.update(lexeme_form['grammaticalFeatures'])
    grammatical_features_item_ids = list(grammatical_features_item_ids)
    labels_map = {} # item ID to label
    while grammatical_features_item_ids:
        chunk, grammatical_features_item_ids = grammatical_features_item_ids[:50], grammatical_features_item_ids[50:]
        response = session.get(action='wbgetentities',
                               ids=chunk,
                               props=['labels'],
                               languages=[language],
                               languagefallback=1, # TODO use True once mediawiki-utilities/python-mwapi#38 is in a released version
                               formatversion=2)
        for item_id, item in response['entities'].items():
            labels_map[item_id] = item['labels'].get(language, {'language': 'zxx', 'value': item_id})
    for lexeme_form in lexeme_forms:
        lexeme_form['grammaticalFeatures_labels'] = [labels_map[grammatical_feature_item_id]
                                                     for grammatical_feature_item_id in lexeme_form['grammaticalFeatures']]

@app.route('/api/v1/template/')
@enableCORS
def get_all_templates_api():
    return flask.jsonify(templates)

@app.route('/api/v1/template/<template_name>')
@enableCORS
def get_template_api(template_name):
    template = templates.get(template_name)
    if template:
        return flask.jsonify(template)
    else:
        return '"no such template"\n', 404

def get_gender(user):
    if user is None:
        gender_option = gender_option_of_user()
    else:
        gender_option = gender_option_of_user_name(user)
    return {
        'male': 'm',
        'female': 'f',
        'unknown': 'n',
    }[gender_option]

def gender_option_of_user_name(user_name):
    session = mwapi.Session(
        host='https://www.wikidata.org',
        user_agent=user_agent,
    )
    response = session.get(action='query',
                           list=['users'],
                           usprop=['gender'],
                           ususers=[user_name],
                           formatversion=2)
    return response['query']['users'][0]['gender']

def gender_option_of_user():
    if 'oauth_access_token' not in flask.session:
        return 'unknown'

    session = mwapi.Session(
        host='https://www.wikidata.org',
        auth=generate_auth(),
        user_agent=user_agent,
    )
    response = session.get(action='query',
                           meta=['userinfo'],
                           uiprop=['options'],
                           formatversion=2)
    return response['query']['userinfo']['options']['gender']

def generate_auth():
    access_token = mwoauth.AccessToken(**flask.session['oauth_access_token'])
    return requests_oauthlib.OAuth1(
        client_key=consumer_token.key,
        client_secret=consumer_token.secret,
        resource_owner_key=access_token.key,
        resource_owner_secret=access_token.secret,
    )

def identify():
    if 'oauth_access_token' not in flask.session:
        return None
    access_token = mwoauth.AccessToken(**flask.session['oauth_access_token'])
    return mwoauth.identify(
        'https://www.wikidata.org/w/index.php',
        consumer_token,
        access_token,
    )
