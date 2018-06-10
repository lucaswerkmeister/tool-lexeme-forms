import flask
import json
import os
import re
import yaml
from templates import templates

app = flask.Flask(__name__)

__dir__ = os.path.dirname(__file__)
try:
    with open(os.path.join(__dir__, 'config.yaml')) as config_file:
        app.config.update(yaml.safe_load(config_file))
except FileNotFoundError:
    print('config.yaml file not found, assuming local development setup')

@app.template_filter('example2input')
def example2input(example):
    match = re.match(r'^(.*)\[(.*)\](.*)$', example)
    if match:
        (prefix, placeholder, suffix) = match.groups()
        return (flask.Markup.escape(prefix) +
                flask.Markup(r'<input type="text" name="form_representation" required placeholder="') +
                flask.Markup.escape(placeholder) +
                flask.Markup(r'">') +
                flask.Markup.escape(suffix))
    else:
        raise Exception('Invalid template: missing [placeholder]: ' + example)

@app.route('/')
def index():
    return flask.render_template(
        'index.html',
        templates=templates,
    )

@app.route('/<template_name>/', methods=['GET', 'POST'])
def process_template(template_name):
    if template_name not in templates:
        return flask.render_template(
            'no-such-template.html',
            template_name=template_name,
        )

    template = templates[template_name]

    if flask.request.method == 'POST':
        return flask.Response(build_lexeme(template, flask.request.form), mimetype='application/json')
    else:
        return flask.render_template(
            'template.html',
            template=template,
        )

def build_lexeme(template, form_data):
    lang = template['language_code']
    return json.dumps({
        'type': 'lexeme',
        'lemmas': {lang: {'language': lang, 'value': form_data['form_representation']}},
        'language': template['language_item_id'],
        'lexicalCategory': template['lexical_category_item_id'],
        'claims': template['claims'],
        'forms': [
            {'add': '', 'representations': {lang: {'language': lang, 'value': form_representation}}, 'grammaticalFeatures': grammaticalFeatures, 'claims': []}
            for (form_representation, grammaticalFeatures) in zip(
                    form_data.getlist('form_representation'),
                    map(lambda form: form['grammatical_features_item_ids'], template['forms'])
            )
        ]
    })
