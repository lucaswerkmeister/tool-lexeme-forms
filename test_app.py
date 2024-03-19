import copy
import flask
from html.parser import HTMLParser
import json
import pytest
import re
from toolforge_i18n.language_info import bcp47
import werkzeug

import app as lexeme_forms
import matching
from templates import templates_without_redirects

def test_form2input_basic():
    markup = lexeme_forms.form2input({'advanced': False}, {'example': 'Left [placeholder] right.'})
    assert str(markup) == r'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^\/]+(?:\/[^\/]+)*" required spellcheck="true"> right.'

def test_form2input_advanced():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.'})
    assert str(markup) == r'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^\/]+(?:\/[^\/]+)*" spellcheck="true"> right.'

def test_form2input_optional():
    markup = lexeme_forms.form2input({'advanced': False}, {'example': 'Left [placeholder] right.', 'optional': True})
    assert str(markup) == r'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^\/]+(?:\/[^\/]+)*" spellcheck="true"> right.'

def test_form2input_first():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.'}, first=True)
    assert str(markup) == r'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^\/]+(?:\/[^\/]+)*" autofocus spellcheck="true"> right.'

def test_form2input_readonly():
    markup = lexeme_forms.form2input({'advanced': False}, {'example': 'Left [placeholder] right.'}, readonly=True)
    assert str(markup) == r'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^\/]+(?:\/[^\/]+)*" required disabled spellcheck="true"> right.'

def test_form2input_preserve_value():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.', 'value': 'value'})
    assert str(markup) == r'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^\/]+(?:\/[^\/]+)*" value="value" spellcheck="true"> right.'

def test_form2input_escape_value():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.', 'value': '"<>&'})
    assert str(markup) == r'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^\/]+(?:\/[^\/]+)*" value="&#34;&lt;&gt;&amp;" spellcheck="true"> right.'

def test_form2input_invalid():
    with pytest.raises(Exception) as excinfo:
        markup = lexeme_forms.form2input({'advanced': True}, {'example': 'No placeholder.'})  # noqa:F841
    assert 'missing [placeholder]' in str(excinfo.value)

@pytest.mark.parametrize('example, expected_prefix, expected_placeholder, expected_suffix', [
    ('Left [placeholder] right.', 'Left ', 'placeholder', ' right.'),
    ('[placeholder] right.', '', 'placeholder', ' right.'),
    ('Left [placeholder]', 'Left ', 'placeholder', ''),
    ('[placeholder]', '', 'placeholder', ''),
    ('Left [] right.', 'Left ', '', ' right.'),
])
def test_split_example(example, expected_prefix, expected_placeholder, expected_suffix):
    form = {'example': example}
    (actual_prefix, actual_placeholder, actual_suffix) = lexeme_forms.split_example(form)
    assert (expected_prefix, expected_placeholder, expected_suffix) \
        == (actual_prefix, actual_placeholder, actual_suffix)

@pytest.mark.parametrize('example', [
    'Left right.',
    'Left [placeholder right.',
    'Left placeholder] right.',
    'Left ]placeholder[ right.',
])
def test_split_example_error(example):
    form = {'example': example}
    with pytest.raises(Exception):
        lexeme_forms.split_example(form)

def test_csrf_token_generate():
    with lexeme_forms.app.test_request_context():
        token = lexeme_forms.csrf_token()
        assert token != ''

def test_csrf_token_save():
    with lexeme_forms.app.test_request_context() as context:
        token = lexeme_forms.csrf_token()
        assert token == context.session['_csrf_token']

def test_csrf_token_load():
    with lexeme_forms.app.test_request_context() as context:
        context.session['_csrf_token'] = 'test token'
        assert lexeme_forms.csrf_token() == 'test token'

def test_template_group():
    with lexeme_forms.app.test_request_context():
        flask.g.html_language_codes = []
        group = lexeme_forms.template_group({'language_code': 'de'})
    assert group == '<span lang="de" dir="ltr">Deutsch (<span lang=zxx>de</span>)</span>'

def test_template_group_test():
    with lexeme_forms.app.test_request_context():
        flask.g.html_language_codes = []
        group = lexeme_forms.template_group({'language_code': 'de', 'test': True})
    assert group == '<span lang="de" dir="ltr">Deutsch (<span lang=zxx>de</span>)</span>, test.wikidata.org'

@pytest.mark.parametrize('language_code', lexeme_forms.translations.keys())
@pytest.mark.parametrize('number', range(-1, 5))
def test_message(language_code, number):
    with lexeme_forms.app.test_request_context():
        flask.g.interface_language_code = language_code
        flask.g.html_language_codes = [bcp47(language_code)]
        message = lexeme_forms.message(  # noqa: F841
            'description-with-forms-and-senses',
            description='',
            num_forms=number,
            num_senses=number,
        )
    # should not have failed

def test_if_no_such_template_redirect_known_template():
    assert lexeme_forms.if_no_such_template_redirect('english-noun') is None

def test_if_no_such_template_redirect_renamed_template():
    with lexeme_forms.app.test_client() as client:
        response = client.get('/template/dutch-feminine-noun/')
    assert response.status_code == 307
    assert response.headers['location'].endswith('/template/dutch-noun-feminine/')

def test_if_no_such_template_redirect_unknown_template():
    template_name = 'no-such-template'
    with lexeme_forms.app.test_request_context():
        lexeme_forms.init_interface_language_code()  # manual call because we bypass @app.before_request below
        response = lexeme_forms.if_no_such_template_redirect(template_name)
    assert response is not None
    assert type(response) is str
    assert 'alert' in response
    assert template_name in response

def test_if_has_duplicates_redirect_checkbox_checked():
    assert lexeme_forms.if_has_duplicates_redirect(
        {},
        False,
        werkzeug.datastructures.ImmutableMultiDict({'no_duplicate': True}),
    ) is None

def test_if_has_duplicates_redirect_lexeme_id_specified():
    assert lexeme_forms.if_has_duplicates_redirect(
        {},
        False,
        werkzeug.datastructures.ImmutableMultiDict({'lexeme_id': 'L123'}),
    ) is None

def test_if_has_duplicates_redirect_lexeme_id_blank(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: ['duplicate'])
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: True)
    assert lexeme_forms.if_has_duplicates_redirect(
        minimal_template,
        False,
        werkzeug.datastructures.ImmutableMultiDict({'lexeme_id': ''}),
    ) is not None

def test_if_has_duplicates_redirect_some_duplicates(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: ['duplicate'])
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered duplicates')
    assert lexeme_forms.if_has_duplicates_redirect(
        minimal_template,
        False,
        werkzeug.datastructures.ImmutableMultiDict(),
    ) == 'rendered duplicates'

def test_if_has_duplicates_redirect_no_duplicates(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: [])
    assert lexeme_forms.if_has_duplicates_redirect(
        {},
        False,
        werkzeug.datastructures.ImmutableMultiDict(),
    ) is None

def test_if_has_duplicates_redirect_submitted_form_representations(monkeypatch):
    def render_template(template_file_name, **kwargs):
        assert template_file_name == 'template.html'
        assert kwargs['submitted_form_representations'] == ['noun', 'nouns']
        return 'rendered duplicates'
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: ['duplicate'])
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', render_template)
    assert lexeme_forms.if_has_duplicates_redirect(
        copy.deepcopy(templates_without_redirects['english-noun']),
        False,
        werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun'), ('form_representation', 'nouns')]),
    ) == 'rendered duplicates'

def test_get_lemma_first_form_representation():
    template = templates_without_redirects['english-noun']
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun'), ('form_representation', 'nouns')])
    lemma = lexeme_forms.get_lemma(template, form_data)
    assert lemma == 'noun'

def test_get_lemma_second_form_representation():
    template = templates_without_redirects['english-noun']
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', ''), ('form_representation', 'nouns')])
    lemma = lexeme_forms.get_lemma(template, form_data)
    assert lemma == 'nouns'

def test_get_lemma_no_form_representation():
    template = templates_without_redirects['english-noun']
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', ''), ('form_representation', '')])
    lemma = lexeme_forms.get_lemma(template, form_data)
    assert lemma is None

def test_get_lemma_first_marked_form_representation():
    template = {'forms': [
        {},
        {'lemma': True},
        {'lemma': True},
    ]}
    form_data = werkzeug.datastructures.ImmutableMultiDict([
        ('form_representation', 'a'),
        ('form_representation', 'b'),
        ('form_representation', 'c'),
    ])
    lemma = lexeme_forms.get_lemma(template, form_data)
    assert lemma == 'b'

def test_get_lemma_second_marked_form_representation():
    template = {'forms': [
        {},
        {'lemma': True},
        {'lemma': True},
    ]}
    form_data = werkzeug.datastructures.ImmutableMultiDict([
        ('form_representation', 'a'),
        ('form_representation', ''),
        ('form_representation', 'c'),
    ])
    lemma = lexeme_forms.get_lemma(template, form_data)
    assert lemma == 'c'

def test_get_lemma_no_marked_form_representation():
    template = {'forms': [
        {},
        {'lemma': True},
        {'lemma': True},
    ]}
    form_data = werkzeug.datastructures.ImmutableMultiDict([
        ('form_representation', 'a'),
        ('form_representation', ''),
        ('form_representation', ''),
    ])
    lemma = lexeme_forms.get_lemma(template, form_data)
    assert lemma == 'a'

def test_build_lemmas():
    template = templates_without_redirects['english-noun']
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun')])
    lemmas = lexeme_forms.build_lemmas(template, form_data)
    assert lemmas == {'en': {'language': 'en', 'value': 'noun'}}

def test_get_duplicates_api_json(monkeypatch):
    duplicates = [{'id': 'L1', 'uri': 'http://www.wikidata.org/wiki/Lexeme:L1', 'label': 'lemma', 'description': 'a lexeme', 'forms_count': None, 'senses_count': None}]
    monkeypatch.setattr(lexeme_forms, 'get_duplicates', lambda wiki, language_code, lemma: duplicates)
    with lexeme_forms.app.test_client() as client:
        response = client.get('/api/v1/duplicates/www/en/lemma')
    assert response.content_type == 'application/json'
    assert json.loads(response.get_data(as_text=True)) == duplicates

def test_get_duplicates_api_html_two(monkeypatch):
    duplicates = [{'id': 'L1', 'uri': 'http://www.wikidata.org/wiki/Lexeme:L1', 'label': 'test1 lemma', 'description': 'a test1 lexeme', 'forms_count': None, 'senses_count': None},
                  {'id': 'L2', 'uri': 'http://www.wikidata.org/wiki/Lexeme:L2', 'label': 'test2 lemma', 'description': 'a test2 lexeme', 'forms_count': None, 'senses_count': None}]
    monkeypatch.setattr(lexeme_forms, 'get_duplicates', lambda wiki, language_code, lemma: duplicates)
    with lexeme_forms.app.test_client() as client:
        with client.session_transaction() as session:
            session['interface_language_code'] = 'de'
        response = client.get('/api/v1/duplicates/www/de/lemma', headers={'Accept': 'text/html'})
    assert response.content_type == 'text/html; charset=utf-8'
    response_text = response.get_data(as_text=True)
    assert 'haben das gleiche Lemma' in response_text
    assert 'kreuze das Kästchen' in response_text
    assert 'test1 lemma' in response_text
    assert 'a test1 lexeme' in response_text
    assert 'test2 lemma' in response_text
    assert 'a test2 lexeme' in response_text

def test_get_duplicates_api_html_one(monkeypatch):
    duplicates = [{'id': 'L1', 'uri': 'http://www.wikidata.org/wiki/Lexeme:L1', 'label': 'test lemma', 'description': 'a test lexeme', 'forms_count': None, 'senses_count': None}]
    monkeypatch.setattr(lexeme_forms, 'get_duplicates', lambda wiki, language_code, lemma: duplicates)
    with lexeme_forms.app.test_client() as client:
        with client.session_transaction() as session:
            session['interface_language_code'] = 'de'
        response = client.get('/api/v1/duplicates/www/de/lemma', headers={'Accept': 'text/html'})
    assert response.content_type == 'text/html; charset=utf-8'
    response_text = response.get_data(as_text=True)
    assert 'hat das gleiche Lemma' in response_text
    assert 'kreuze das Kästchen' in response_text
    assert 'test lemma' in response_text
    assert 'a test lexeme' in response_text

def test_get_duplicates_api_html_empty(monkeypatch):
    duplicates = []
    monkeypatch.setattr(lexeme_forms, 'get_duplicates', lambda wiki, language_code, lemma: duplicates)
    with lexeme_forms.app.test_client() as client:
        response = client.get('/api/v1/duplicates/www/de/lemma', headers={'Accept': 'text/html'})
    assert response.content_type == 'text/html; charset=utf-8'
    assert response.get_data(as_text=True) == ''


minimal_template = {
    '@template_name': 'minimal-template',
    'language_code': 'en',
}

def test_if_needs_csrf_redirect_no_token(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered template')
    with lexeme_forms.app.test_request_context():
        response = lexeme_forms.if_needs_csrf_redirect(minimal_template, False, {})
    assert response == 'rendered template'
    # TODO instead of monkeypatching, assert that form_data is correctly preserved (possibly in separate test)

def test_if_needs_csrf_redirect_wrong_token(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered template')
    with lexeme_forms.app.test_request_context() as context:
        context.session['_csrf_token'] = 'token 1'
        response = lexeme_forms.if_needs_csrf_redirect(minimal_template, False, {'_csrf_token': 'token 2'})
    assert response == 'rendered template'

def test_if_needs_csrf_redirect_correct_token(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered template')
    with lexeme_forms.app.test_request_context() as context:
        context.session['_csrf_token'] = 'token'
        response = lexeme_forms.if_needs_csrf_redirect(minimal_template, False, {'_csrf_token': 'token'})
    assert response is None

def test_add_form_data_to_template():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun'), ('form_representation', 'nouns')])
    template = {
        'forms': [
            {
                'label': 'singular',
                'example': 'One [thing].',
                'grammatical_features_item_ids': ['Q110786'],
                'value': 'Noun',
            },
            {
                'label': 'plural',
                'example': 'Two [things]',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
        'other_data': 'preserve',
    }
    new_template = lexeme_forms.add_form_data_to_template(form_data, template)
    assert new_template == {
        'forms': [
            {
                'label': 'singular',
                'example': 'One [thing].',
                'grammatical_features_item_ids': ['Q110786'],
                'value': 'noun',
            },
            {
                'label': 'plural',
                'example': 'Two [things]',
                'grammatical_features_item_ids': ['Q146786'],
                'value': 'nouns',
            },
        ],
        'other_data': 'preserve',
    }

def test_add_form_data_to_template_no_overwrite():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun'), ('form_representation', 'nouns')])
    template = {
        'forms': [
            {
                'label': 'singular',
                'example': 'One [thing].',
                'grammatical_features_item_ids': ['Q110786'],
                'value': 'Noun',
            },
            {
                'label': 'plural',
                'example': 'Two [things]',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
        'other_data': 'preserve',
    }
    new_template = lexeme_forms.add_form_data_to_template(form_data, template, overwrite=False)
    assert new_template == {
        'forms': [
            {
                'label': 'singular',
                'example': 'One [thing].',
                'grammatical_features_item_ids': ['Q110786'],
                'value': 'Noun',
            },
            {
                'label': 'plural',
                'example': 'Two [things]',
                'grammatical_features_item_ids': ['Q146786'],
                'value': 'nouns',
            },
        ],
        'other_data': 'preserve',
    }

def test_add_form_data_to_template_lexeme_id():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('lexeme_id', 'L123')])
    template = {'forms': []}
    new_template = lexeme_forms.add_form_data_to_template(form_data, template)
    assert new_template['lexeme_id'] == 'L123'

def test_add_form_data_to_template_generated_via():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('generated_via', 'something')])
    template = {'forms': []}
    new_template = lexeme_forms.add_form_data_to_template(form_data, template)
    assert new_template['generated_via'] == 'something'

def test_add_form_data_to_template_target_hash():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('target_hash', 'something')])
    template = {'forms': []}
    new_template = lexeme_forms.add_form_data_to_template(form_data, template)
    assert new_template['target_hash'] == 'something'

def test_add_form_data_to_template_no_template_modification():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('lexeme_id', 'L123')])
    template = {'forms': []}
    new_template = lexeme_forms.add_form_data_to_template(form_data, template)
    assert template is not new_template
    assert 'lexeme_id' not in template

def test_current_url_index(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'APPLICATION_ROOT', '/')
    with lexeme_forms.app.test_request_context('/'):
        current_url = lexeme_forms.current_url()
        assert current_url == 'http://localhost/'

def test_current_url_template(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'APPLICATION_ROOT', '/')
    with lexeme_forms.app.test_request_context('/template/foo/'):
        current_url = lexeme_forms.current_url()
        assert current_url == 'http://localhost/template/foo/'

def test_current_url_template_advanced(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'APPLICATION_ROOT', '/')
    with lexeme_forms.app.test_request_context('/template/foo/advanced/'):
        current_url = lexeme_forms.current_url()
        assert current_url == 'http://localhost/template/foo/advanced/'

def test_current_url_application_root(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'APPLICATION_ROOT', '/foo/')
    with lexeme_forms.app.test_request_context('/template/bar/'):
        current_url = lexeme_forms.current_url()
        assert current_url == 'http://localhost/foo/template/bar/'

def test_current_url_arglist(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'APPLICATION_ROOT', '/')
    with lexeme_forms.app.test_request_context('/template/foo/?form_representation=X&form_representation=Y'):
        current_url = lexeme_forms.current_url()
        assert current_url == 'http://localhost/template/foo/?form_representation=X&form_representation=Y'

def test_current_url_space(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'APPLICATION_ROOT', '/')
    with lexeme_forms.app.test_request_context('/template/foo/?form_representation=X%20Y%20Z'):
        current_url = lexeme_forms.current_url()
        assert current_url == 'http://localhost/template/foo/?form_representation=X%20Y%20Z'

def test_current_url_encoded(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'APPLICATION_ROOT', '/')
    with lexeme_forms.app.test_request_context('/template/bokm%C3%A5l-noun-masculine/'):
        current_url = lexeme_forms.current_url()
        assert current_url == 'http://localhost/template/bokm%C3%A5l-noun-masculine/'

def test_build_lexeme():
    template = {
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
    }
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun'), ('form_representation', 'nouns')])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    assert lexeme_data == {
        'type': 'lexeme',
        'forms': [
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'noun'}},
                'grammaticalFeatures': ['Q110786'],
                'claims': {},
            },
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'nouns'}},
                'grammaticalFeatures': ['Q146786'],
                'claims': {},
            },
        ],
        'lemmas': {'en': {'language': 'en', 'value': 'noun'}},
        'language': 'Q1860',
        'lexicalCategory': 'Q1084',
        'claims': {},
    }

def test_build_lexeme_with_empty_lexeme_id():
    template = {
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'grammatical_features_item_ids': ['Q110786'],
            },
        ],
    }
    form_data = werkzeug.datastructures.ImmutableMultiDict([('lexeme_id', ''), ('form_representation', 'noun')])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    assert lexeme_data == {
        'type': 'lexeme',
        'forms': [
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'noun'}},
                'grammaticalFeatures': ['Q110786'],
                'claims': {},
            },
        ],
        'lemmas': {'en': {'language': 'en', 'value': 'noun'}},
        'language': 'Q1860',
        'lexicalCategory': 'Q1084',
        'claims': {},
    }

def test_build_lexeme_with_nonempty_lexeme_id(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'get_lexeme_data', lambda lexeme_id, wiki: {'language': 'Q1860', 'lexicalCategory': 'Q1084'})
    template = {
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'grammatical_features_item_ids': ['Q110786'],
            },
        ],
    }
    form_data = werkzeug.datastructures.ImmutableMultiDict([('lexeme_id', 'L123'), ('form_representation', 'noun')])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    assert lexeme_data == {
        'type': 'lexeme',
        'forms': [
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'noun'}},
                'grammaticalFeatures': ['Q110786'],
                'claims': {},
            },
        ],
        'id': 'L123',
        'claims': {},
    }

def test_build_lexeme_blank_form(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'get_lexeme_data', lambda lexeme_id, wiki: {'language': 'Q1860', 'lexicalCategory': 'Q1084'})
    template = {
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
    }
    form_data = werkzeug.datastructures.ImmutableMultiDict([('lexeme_id', 'L123'), ('form_representation', ''), ('form_representation', 'nouns')])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    assert lexeme_data == {
        'type': 'lexeme',
        'forms': [
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'nouns'}},
                'grammaticalFeatures': ['Q146786'],
                'claims': {},
            },
        ],
        'id': 'L123',
        'claims': {},
    }

def test_build_lexeme_with_statements():
    template = {
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'grammatical_features_item_ids': ['Q110786'],
                'statements': 'singular test statements',
            },
            {
                'grammatical_features_item_ids': ['Q146786'],
                'statements': 'plural test statements',
            },
        ],
        'statements': 'lexeme test statements',
    }
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun'), ('form_representation', 'nouns')])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    assert lexeme_data == {
        'type': 'lexeme',
        'forms': [
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'noun'}},
                'grammaticalFeatures': ['Q110786'],
                'claims': 'singular test statements',
            },
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'nouns'}},
                'grammaticalFeatures': ['Q146786'],
                'claims': 'plural test statements',
            },
        ],
        'lemmas': {'en': {'language': 'en', 'value': 'noun'}},
        'language': 'Q1860',
        'lexicalCategory': 'Q1084',
        'claims': 'lexeme test statements',
    }

def test_build_lexeme_with_variants():
    template = {
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
    }
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun/NOUN'), ('form_representation', 'nouns/NOUNS/nounS')])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    assert lexeme_data == {
        'type': 'lexeme',
        'forms': [
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'noun'}},
                'grammaticalFeatures': ['Q110786'],
                'claims': {},
            },
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'NOUN'}},
                'grammaticalFeatures': ['Q110786'],
                'claims': {},
            },
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'nouns'}},
                'grammaticalFeatures': ['Q146786'],
                'claims': {},
            },
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'NOUNS'}},
                'grammaticalFeatures': ['Q146786'],
                'claims': {},
            },
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'nounS'}},
                'grammaticalFeatures': ['Q146786'],
                'claims': {},
            },
        ],
        'lemmas': {'en': {'language': 'en', 'value': 'noun'}},
        'language': 'Q1860',
        'lexicalCategory': 'Q1084',
        'claims': {},
    }

def test_build_lexeme_with_statements_for_existing_lexeme(monkeypatch):
    p5185 = [
        {
            'mainsnak': {
                'snaktype': 'value',
                'property': 'P5185',
                'datatype': 'wikibase-item',
                'datavalue': {
                    'type': 'wikibase-entityid',
                    'value': {
                        'entity-type': 'item',
                        'id': 'Q499327',
                    },
                },
            },
            'type': 'statement',
            'rank': 'normal',
        }
    ]
    p31 = [
        {
            'mainsnak': {
                'snaktype': 'value',
                'property': 'P31',
                'datatype': 'wikibase-item',
                'datavalue': {
                    'type': 'wikibase-entityid',
                    'value': {
                        'entity-type': 'item',
                        'id': 'Q604984',
                    },
                },
            },
            'type': 'statement',
            'rank': 'normal',
        }
    ]
    monkeypatch.setattr(lexeme_forms, 'get_lexeme_data', lambda lexeme_id, wiki: {
        'language': 'Q1860',
        'lexicalCategory': 'Q1084',
        'claims': {
            'P5185': p5185,
        },
    })
    template = {
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'grammatical_features_item_ids': ['Q110786'],
                'statements': 'singular test statements',
            },
            {
                'grammatical_features_item_ids': ['Q146786'],
                'statements': 'plural test statements',
            },
        ],
        'statements': {
            'P5185': p5185,
            'P31': p31,
        },
    }
    form_data = werkzeug.datastructures.ImmutableMultiDict([('lexeme_id', 'L123'), ('form_representation', 'noun'), ('form_representation', 'nouns')])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    assert lexeme_data == {
        'id': 'L123',
        'type': 'lexeme',
        'forms': [
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'noun'}},
                'grammaticalFeatures': ['Q110786'],
                'claims': 'singular test statements',
            },
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'nouns'}},
                'grammaticalFeatures': ['Q146786'],
                'claims': 'plural test statements',
            },
        ],
        'claims': {
            'P31': p31,
        },
    }

def test_build_summary_localhost():
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    with lexeme_forms.app.test_request_context(base_url='http://localhost/'):
        summary = lexeme_forms.build_summary(template, form_data)
    assert summary == 'foo'

def test_build_summary_internet():
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    with lexeme_forms.app.test_request_context(base_url='https://example.com/lexeme-forms/'):
        summary = lexeme_forms.build_summary(template, form_data)
    assert summary == 'foo'

def test_build_summary_toolforge_lexeme_forms():
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    with lexeme_forms.app.test_request_context(base_url='https://lexeme-forms.toolforge.org/'):
        summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:lexeme-forms/template/foo/|foo]]'

def test_build_summary_toolforge_other():
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    with lexeme_forms.app.test_request_context(base_url='https://other.toolforge.org/'):
        summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:other/template/foo/|foo]]'

def test_build_summary_generated_via():
    template = {
        '@template_name': 'foo',
    }
    form_data = {
        'generated_via': '[[toolforge:other/bar|other tool, bar]]'
    }
    with lexeme_forms.app.test_request_context(base_url='https://lexeme-forms.toolforge.org/'):
        summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:lexeme-forms/template/foo/|foo]], generated via [[toolforge:other/bar|other tool, bar]]'

@pytest.mark.parametrize('uri, hash, expected', [
    ('https://example.com/', None, 'https://example.com/'),
    ('https://example.com/', 'abc', 'https://example.com/#abc'),
])
def test_add_hash_to_uri(uri, hash, expected):
    assert lexeme_forms.add_hash_to_uri(uri, hash) == expected

def test_get_all_templates_api():
    with lexeme_forms.app.test_client() as client:
        response = client.get('/api/v1/template/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    for template in json.loads(response.get_data(as_text=True)).values():
        assert isinstance(template, (str, list)) or '@attribution' in template

def test_get_template_api_exists():
    with lexeme_forms.app.test_client() as client:
        response = client.get('/api/v1/template/german-noun-feminine')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    template = json.loads(response.get_data(as_text=True))
    assert '@attribution' in template

def test_get_template_api_redirect():
    with lexeme_forms.app.test_client() as client:
        response = client.get('/api/v1/template/dutch-feminine-noun')
    assert response.status_code == 307
    assert response.headers['location'].endswith('/api/v1/template/dutch-noun-feminine')

def test_get_template_api_missing():
    with lexeme_forms.app.test_client() as client:
        response = client.get('/api/v1/template/german-noun')
    assert response.status_code == 404
    # we don’t say that this is JSON,
    # but for the benefit of clients who try to deserialize the response without checking the headers,
    # we still want to reply with valid JSON
    json.loads(response.get_data(as_text=True))
    # the previous statement should not have thrown an exception


def test_update_lexeme_add_dwarves_dwarrows():
    lexeme_data = {
        'lemmas': {'en': {'language': 'en', 'value': 'dwarf'}},
        'forms': [
            {'id': 'L22936-F1', 'representations': {'en': {'language': 'en', 'value': 'dwarf'}}, 'grammaticalFeatures': ['Q110786']},
            {'id': 'L22936-F2', 'representations': {'en': {'language': 'en', 'value': 'dwarfs'}}, 'grammaticalFeatures': ['Q146786']},
        ],
    }
    template = copy.deepcopy(templates_without_redirects['english-noun'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    template['forms'][1]['lexeme_forms'] = [lexeme_data['forms'][1]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'dwarf'), ('form_representation', 'dwarfs/dwarves/dwarrows')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'en')
    assert updated_lexeme_data == {
        'lemmas': {'en': {'language': 'en', 'value': 'dwarf'}},
        'forms': [
            {'id': 'L22936-F1', 'representations': {'en': {'language': 'en', 'value': 'dwarf'}}, 'grammaticalFeatures': ['Q110786']},
            {'id': 'L22936-F2', 'representations': {'en': {'language': 'en', 'value': 'dwarfs'}}, 'grammaticalFeatures': ['Q146786']},
            {'add': '', 'representations': {'en': {'language': 'en', 'value': 'dwarves'}}, 'grammaticalFeatures': ['Q146786'], 'claims': {}},
            {'add': '', 'representations': {'en': {'language': 'en', 'value': 'dwarrows'}}, 'grammaticalFeatures': ['Q146786'], 'claims': {}},
        ],
        'base_revision_id': 123,
    }

def test_update_lexeme_match_forms():
    lexeme_data = {
        'lemmas': {'en': {'language': 'en', 'value': 'dwarf'}},
        'forms': [
            {'id': 'L22936-F1', 'representations': {'en': {'language': 'en', 'value': 'dwarf'}}, 'grammaticalFeatures': []},
            {'id': 'L22936-F2', 'representations': {'en': {'language': 'en', 'value': 'dwarfs'}}, 'grammaticalFeatures': []},
            {'id': 'L22936-F3', 'representations': {'en': {'language': 'en', 'value': 'dwarves'}}, 'grammaticalFeatures': []},
            {'id': 'L22936-F4', 'representations': {'en': {'language': 'en', 'value': 'dwarrows'}}, 'grammaticalFeatures': []},
        ],
    }
    template = copy.deepcopy(templates_without_redirects['english-noun'])
    template['lexeme_revision'] = 123
    template['unmatched_lexeme_forms'] = lexeme_data['forms'][:]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'L22936-F1'), ('form_representation', 'L22936-F2/L22936-F3/L22936-F4')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'en')
    assert updated_lexeme_data == {
        'lemmas': {'en': {'language': 'en', 'value': 'dwarf'}},
        'forms': [
            {'id': 'L22936-F1', 'representations': {'en': {'language': 'en', 'value': 'dwarf'}}, 'grammaticalFeatures': ['Q110786']},
            {'id': 'L22936-F2', 'representations': {'en': {'language': 'en', 'value': 'dwarfs'}}, 'grammaticalFeatures': ['Q146786']},
            {'id': 'L22936-F3', 'representations': {'en': {'language': 'en', 'value': 'dwarves'}}, 'grammaticalFeatures': ['Q146786']},
            {'id': 'L22936-F4', 'representations': {'en': {'language': 'en', 'value': 'dwarrows'}}, 'grammaticalFeatures': ['Q146786']},
        ],
        'base_revision_id': 123,
    }

def test_update_lexeme_match_forms_optional_features():
    lexeme_data = {
        'lemmas': {'de': {'language': 'de', 'value': 'Berlin'}},
        'forms': [
            {'id': 'L297059-F1', 'representations': {'de': {'language': 'de', 'value': 'Berlin'}}, 'grammaticalFeatures': ['Q131105']},
            {'id': 'L297059-F2', 'representations': {'de': {'language': 'de', 'value': 'Berlins'}}, 'grammaticalFeatures': ['Q146233']},
            {'id': 'L297059-F3', 'representations': {'de': {'language': 'de', 'value': 'Berlin'}}, 'grammaticalFeatures': ['Q145599']},
            {'id': 'L297059-F4', 'representations': {'de': {'language': 'de', 'value': 'Berlin'}}, 'grammaticalFeatures': ['Q146078']},
        ],
    }
    template = copy.deepcopy(templates_without_redirects['german-noun-neuter-toponym'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    template['forms'][1]['lexeme_forms'] = [lexeme_data['forms'][1]]
    template['forms'][2]['lexeme_forms'] = [lexeme_data['forms'][2]]
    template['forms'][3]['lexeme_forms'] = [lexeme_data['forms'][3]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'Berlin'), ('form_representation', 'Berlins'), ('form_representation', 'Berlin'), ('form_representation', 'Berlin')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'de')
    assert updated_lexeme_data == {
        'lemmas': {'de': {'language': 'de', 'value': 'Berlin'}},
        'forms': [
            {'id': 'L297059-F1', 'representations': {'de': {'language': 'de', 'value': 'Berlin'}}, 'grammaticalFeatures': ['Q131105', 'Q110786']},
            {'id': 'L297059-F2', 'representations': {'de': {'language': 'de', 'value': 'Berlins'}}, 'grammaticalFeatures': ['Q146233', 'Q110786']},
            {'id': 'L297059-F3', 'representations': {'de': {'language': 'de', 'value': 'Berlin'}}, 'grammaticalFeatures': ['Q145599', 'Q110786']},
            {'id': 'L297059-F4', 'representations': {'de': {'language': 'de', 'value': 'Berlin'}}, 'grammaticalFeatures': ['Q146078', 'Q110786']},
        ],
        'base_revision_id': 123,
    }


def test_update_lexeme_edit_lemma():
    lexeme_data = {
        'lemmas': {'en': {'language': 'en', 'value': 'fuschia'}},
        'forms': [
            {'id': 'L3280-F1', 'representations': {'en': {'language': 'en', 'value': 'fuschia'}}, 'grammaticalFeatures': ['Q3482678']},
        ],
    }
    template = copy.deepcopy(templates_without_redirects['english-adjective'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'fuchsia')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'en')
    assert updated_lexeme_data == {
        'lemmas': {'en': {'language': 'en', 'value': 'fuchsia'}},
        'forms': [
            {'id': 'L3280-F1', 'representations': {'en': {'language': 'en', 'value': 'fuchsia'}}, 'grammaticalFeatures': ['Q3482678']},
        ],
        'base_revision_id': 123,
    }

def test_update_lexeme_edit_lemma_new_form():
    lexeme_data = {
        'lemmas': {'en': {'language': 'en', 'value': 'fuschia'}},
        'forms': [],
    }
    template = copy.deepcopy(templates_without_redirects['english-adjective'])
    template['lexeme_revision'] = 123
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'fuchsia')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'en')
    assert updated_lexeme_data == {
        'lemmas': {'en': {'language': 'en', 'value': 'fuchsia'}},
        'forms': [
            {'add': '', 'claims': {}, 'representations': {'en': {'language': 'en', 'value': 'fuchsia'}}, 'grammaticalFeatures': ['Q3482678']},
        ],
        'base_revision_id': 123,
    }

def test_update_lexeme_edit_lemma_nonfirst_form():
    lexeme_data = {
        'lemmas': {'en': {'language': 'en', 'value': 'roofs'}},
        'forms': [],
    }
    template = copy.deepcopy(templates_without_redirects['english-noun'])
    template['forms'][1]['lemma'] = True
    template['lexeme_revision'] = 123
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'roof'), ('form_representation', 'rooves')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'en')
    assert updated_lexeme_data == {
        'lemmas': {'en': {'language': 'en', 'value': 'rooves'}},
        'forms': [
            {'add': '', 'claims': {}, 'representations': {'en': {'language': 'en', 'value': 'roof'}}, 'grammaticalFeatures': ['Q110786']},
            {'add': '', 'claims': {}, 'representations': {'en': {'language': 'en', 'value': 'rooves'}}, 'grammaticalFeatures': ['Q146786']},
        ],
        'base_revision_id': 123,
    }

def test_update_lexeme_different_language():
    lexeme_data = {
        'lemmas': {
            'de': {'language': 'de', 'value': 'Straße'},
        },
        'forms': [
            {
                'id': 'L44061-F1',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                },
                'grammaticalFeatures': ['Q110786', 'Q131105'],
            },
        ],
    }
    template = copy.deepcopy(templates_without_redirects['german-noun-feminine'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'Strasse')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'de-ch')
    assert updated_lexeme_data == {
        'lemmas': {
            'de': {'language': 'de', 'value': 'Straße'},
            'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
        },
        'forms': [
            {
                'id': 'L44061-F1',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
                },
                'grammaticalFeatures': ['Q110786', 'Q131105'],
            },
        ],
        'base_revision_id': 123,
    }

def test_update_lexeme_different_language_for_some_forms():
    lexeme_data = {
        'lemmas': {
            'de': {'language': 'de', 'value': 'müssen'},
            'de-1901': {'language': 'de-1901', 'value': 'müßen'},
        },
        'forms': [
            {
                'id': 'L315210-F1',
                'representations': {
                    'de': {'language': 'de', 'value': 'muss'},
                },
                'grammaticalFeatures': ['Q110786', 'Q1317831', 'Q192613', 'Q21714344', 'Q682111'],
            },
            {
                'id': 'L315210-F2',
                'representations': {
                    'de': {'language': 'de', 'value': 'müssen'},
                },
                'grammaticalFeatures': ['Q179230'],
            },
        ],
    }
    template = copy.deepcopy(templates_without_redirects['german-verb'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][1]]
    template['forms'][1]['lexeme_forms'] = [lexeme_data['forms'][0]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', ''), ('form_representation', 'muß')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'de-1901')
    assert updated_lexeme_data == {
        'lemmas': {
            'de': {'language': 'de', 'value': 'müssen'},
        },
        'forms': [
            {
                'id': 'L315210-F1',
                'representations': {
                    'de': {'language': 'de', 'value': 'muss'},
                    'de-1901': {'language': 'de-1901', 'value': 'muß'},
                },
                'grammaticalFeatures': ['Q110786', 'Q1317831', 'Q192613', 'Q21714344', 'Q682111'],
            },
            {
                'id': 'L315210-F2',
                'representations': {
                    'de': {'language': 'de', 'value': 'müssen'},
                },
                'grammaticalFeatures': ['Q179230'],
            },
        ],
        'base_revision_id': 123,
    }

def test_update_lexeme_noop():
    lexeme_data = {
        'lemmas': {'en': {'language': 'en', 'value': 'dwarf'}},
        'forms': [
            {'id': 'L22936-F1', 'representations': {'en': {'language': 'en', 'value': 'dwarf'}}, 'grammaticalFeatures': ['Q110786']},
            {'id': 'L22936-F2', 'representations': {'en': {'language': 'en', 'value': 'dwarfs'}}, 'grammaticalFeatures': ['Q146786']},
            {'id': 'L22936-F3', 'representations': {'en': {'language': 'en', 'value': 'dwarves'}}, 'grammaticalFeatures': ['Q146786']},
            {'id': 'L22936-F4', 'representations': {'en': {'language': 'en', 'value': 'dwarrows'}}, 'grammaticalFeatures': ['Q146786']},
            {'id': 'L22936-F5', 'representations': {'en': {'language': 'en', 'value': 'dweorgas'}}, 'grammaticalFeatures': ['Q146786']},
        ],
    }
    template = copy.deepcopy(templates_without_redirects['english-noun'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    template['forms'][1]['lexeme_forms'] = [lexeme_data['forms'][1], lexeme_data['forms'][2], lexeme_data['forms'][3], lexeme_data['forms'][4]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'dwarf'), ('form_representation', 'dwarfs/dweorgas/dwarves/dwarrows')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'en')
    assert updated_lexeme_data == {
        'lemmas': lexeme_data['lemmas'],
        'forms': lexeme_data['forms'],
        'base_revision_id': 123,
    }

def test_update_lexeme_rematch_already_matched_form():
    lexeme_data = {'forms': [{'id': 'L4592-F1', 'representations': {'en': {'language': 'en', 'value': 'gold'}}, 'grammaticalFeatures': ['Q110786']}]}
    template = copy.deepcopy(templates_without_redirects['english-noun'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'gold'), ('form_representation', 'L4592-F1')])
    with pytest.raises(Exception):
        lexeme_forms.update_lexeme(lexeme_data, template, form_data)

def test_update_lexeme_rematch_same_form_twice():
    lexeme_data = {'forms': [{'id': 'L4592-F1', 'representations': {'en': {'language': 'en', 'value': 'gold'}}, 'grammaticalFeatures': []}]}
    template = copy.deepcopy(templates_without_redirects['english-noun'])
    template['lexeme_revision'] = 123
    template['unmatched_lexeme_forms'] = lexeme_data['forms'][:]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'L4592-F1'), ('form_representation', 'L4592-F1')])
    with pytest.raises(Exception):
        lexeme_forms.update_lexeme(lexeme_data, template, form_data)

def test_update_lexeme_remove_form_representation():
    lexeme_data = {
        'lemmas': {
            'de': {'language': 'de', 'value': 'Straße'},
            'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
        },
        'forms': [
            {
                'id': 'L44061-F1',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
                },
                'grammaticalFeatures': ['Q110786', 'Q131105'],
            },
            {
                'id': 'L44061-F2',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
                },
                'grammaticalFeatures': ['Q110786', 'Q146233'],
            },
        ],
    }
    template = copy.deepcopy(templates_without_redirects['german-noun-feminine'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    template['forms'][1]['lexeme_forms'] = [lexeme_data['forms'][1]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', ''), ('form_representation', 'Strasse')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'de-ch')
    assert updated_lexeme_data == {
        'lemmas': {
            'de': {'language': 'de', 'value': 'Straße'},
            'de-ch': {'language': 'de-ch', 'value': 'Strasse', 'remove': ''},
        },
        'forms': [
            {
                'id': 'L44061-F1',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse', 'remove': ''},
                },
                'grammaticalFeatures': ['Q110786', 'Q131105'],
            },
            {
                'id': 'L44061-F2',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
                },
                'grammaticalFeatures': ['Q110786', 'Q146233'],
            },
        ],
        'base_revision_id': 123,
    }

def test_update_lexeme_remove_main_form_representation():
    lexeme_data = {
        'lemmas': {
            'de': {'language': 'de', 'value': 'Straße'},
            'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
        },
        'forms': [
            {
                'id': 'L44061-F1',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
                },
                'grammaticalFeatures': ['Q110786', 'Q131105'],
            },
            {
                'id': 'L44061-F2',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
                },
                'grammaticalFeatures': ['Q110786', 'Q146233'],
            },
        ],
    }
    template = copy.deepcopy(templates_without_redirects['german-noun-feminine'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    template['forms'][1]['lexeme_forms'] = [lexeme_data['forms'][1]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', ''), ('form_representation', 'Straße')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data, 'de')
    assert updated_lexeme_data == {
        'lemmas': {
            'de': {'language': 'de', 'value': 'Straße', 'remove': ''},
            'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
        },
        'forms': [
            {
                'id': 'L44061-F1',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße', 'remove': ''},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
                },
                'grammaticalFeatures': ['Q110786', 'Q131105'],
            },
            {
                'id': 'L44061-F2',
                'representations': {
                    'de': {'language': 'de', 'value': 'Straße'},
                    'de-ch': {'language': 'de-ch', 'value': 'Strasse'},
                },
                'grammaticalFeatures': ['Q110786', 'Q146233'],
            },
        ],
        'base_revision_id': 123,
    }


@pytest.mark.parametrize('user, expected', [
    ('علاء', 'm'),
    ('Harmonia Amanda', 'f'),
    ('Nikki', 'n'),
    (None, 'n'),
])
def test_get_gender(user, expected):
    with lexeme_forms.app.test_request_context():
        assert lexeme_forms.get_gender(user) == expected


@pytest.mark.parametrize('template_name', templates_without_redirects.keys())
def test_integration_edit(template_name):
    """Create a lexeme from a template, then match it against the same template.

    If this fails, then there might be a bug when creating or matching lexemes,
    or the template might have ambiguous forms."""
    template = templates_without_redirects[template_name]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', str(index)) for index in range(0, len(template['forms']))])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    matched_template = matching.match_lexeme_forms_to_template(lexeme_data['forms'], template)
    assert matched_template.get('ambiguous_lexeme_forms') is None
    assert matched_template.get('unmatched_lexeme_forms') is None
    for index, form in enumerate(matched_template['forms']):
        assert len(form['lexeme_forms']) == 1
        assert form['lexeme_forms'][0]['representations'][template['language_code']]['value'] == str(index)


def test_bulk_error_no_xss(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'can_use_bulk_mode', lambda *args, **kwargs: True)
    monkeypatch.setattr(lexeme_forms, 'csrf_token_matches', lambda *args, **kwargs: True)
    with lexeme_forms.app.test_client() as client:
        response = client.post('/template/english-noun/bulk/',
                               data={
                                   'lexemes': '<script>alert("xss")</script>|thing|things',
                                   '_bulk_mode': '',
                               })
    response_text = response.get_data(as_text=True)
    assert 'script' in response_text
    assert 'xss' in response_text
    assert '<script>' not in response_text


def test_index_lang_dir():
    """Test the lang= and dir= attributes of at least one group and template.

    The group and template being tested are arbitrary,
    but we should at least test one each."""

    with lexeme_forms.app.test_client() as client:
        response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'
    response_text = response.get_data(as_text=True)

    # group
    assert '<span lang="fa" dir="rtl">فارسی (<span lang=zxx>fa</span>)</span>' in response_text
    # template
    print(response_text)
    assert re.search(r'<span lang="fa" dir="rtl">\s*<a href="[^"]*/template/persian-noun/">اسم فارسی</a>', response_text)


def test_index_ids_distinct():
    """Test that all id attributes on the index page are distinct.

    We use the language code of a group of templates as the ID,
    so that people can easily navigate to that group.
    This test ensures this ID doesn’t accidentally collide with another one,
    e.g. a hard-coded one (this is <span id=it>it</span>!)."""

    ids = set()

    class UniqueIdsHtmlParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            for name, value in attrs:
                if name == 'id':
                    id = value
                    assert id not in ids
                    ids.add(id)

    with lexeme_forms.app.test_client() as client:
        response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'
    response_text = response.get_data(as_text=True)

    UniqueIdsHtmlParser().feed(response_text)
