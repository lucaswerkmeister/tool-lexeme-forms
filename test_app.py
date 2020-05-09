import copy
import flask
import json
import mwoauth
import pytest
import werkzeug

import app as lexeme_forms
import matching
from templates import templates

def test_form2input_basic():
    markup = lexeme_forms.form2input({'advanced': False}, {'example': 'Left [placeholder] right.'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^/]+(?:/[^/]+)*" required spellcheck="true"> right.'

def test_form2input_advanced():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^/]+(?:/[^/]+)*" spellcheck="true"> right.'

def test_form2input_first():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.'}, first=True)
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^/]+(?:/[^/]+)*" autofocus spellcheck="true"> right.'

def test_form2input_preserve_value():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.', 'value': 'value'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^/]+(?:/[^/]+)*" value="value" spellcheck="true"> right.'

def test_form2input_escape_value():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.', 'value': '"<>&'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" pattern="[^/]+(?:/[^/]+)*" value="&#34;&lt;&gt;&amp;" spellcheck="true"> right.'

def test_form2input_invalid():
    with pytest.raises(Exception) as excinfo:
        markup = lexeme_forms.form2input({'advanced': True}, {'example': 'No placeholder.'})
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
    group = lexeme_forms.template_group({'language_code': 'de'})
    assert group == 'de'

def test_template_group_test():
    group = lexeme_forms.template_group({'language_code': 'de', 'test': True})
    assert group == 'de, test.wikidata.org'

@pytest.mark.parametrize('template_name', templates.keys())
@pytest.mark.parametrize('number', range(-1,5))
def test_message_with_plural(template_name, number):
    template = templates[template_name]
    with lexeme_forms.app.test_request_context():
        flask.g.language_code = template['language_code']
        message = lexeme_forms.message_with_plural('description_with_forms_and_senses', description='', forms=number, senses=number)
    # should not have failed

@pytest.mark.parametrize('language_code, expected_direction', [
    ('en', 'ltr'),
    ('fa', 'rtl'),
    ('mis', 'auto'),
    ('mis-x-Q401', 'auto'),
])
def test_text_direction(language_code, expected_direction):
    assert lexeme_forms.text_direction(language_code) == expected_direction

def test_if_no_such_template_redirect_known_template():
    assert lexeme_forms.if_no_such_template_redirect('english-noun') is None

def test_if_no_such_template_redirect_unknown_template():
    template_name = 'no-such-template'
    with lexeme_forms.app.test_request_context():
        response = lexeme_forms.if_no_such_template_redirect(template_name)
    assert response is not None
    assert type(response) is str
    assert 'alert' in response
    assert template_name in response

def test_if_needs_oauth_redirect_not_configured(monkeypatch):
    monkeypatch.delitem(lexeme_forms.app.config, 'oauth', raising=False)
    assert lexeme_forms.if_needs_oauth_redirect() is None

def test_if_needs_oauth_redirect_logged_in(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'oauth', {})
    with lexeme_forms.app.test_request_context() as context:
        context.session['oauth_access_token'] = 'test token'
        assert lexeme_forms.if_needs_oauth_redirect() is None

def test_if_needs_oauth_redirect_not_logged_in(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'oauth', {})
    monkeypatch.setattr(lexeme_forms, 'consumer_token', mwoauth.ConsumerToken('test key', 'test secret'), raising=False)
    monkeypatch.setattr(mwoauth, 'initiate', lambda mw_uri, consumer_token, user_agent: ('test redirect', mwoauth.RequestToken('test key', 'test secret')))
    with lexeme_forms.app.test_request_context() as context:
        response = lexeme_forms.if_needs_oauth_redirect()
    assert response is not None
    assert str(response.status_code).startswith('3')

def test_if_has_duplicates_redirect_checkbox_checked():
    assert lexeme_forms.if_has_duplicates_redirect({}, False, {'no_duplicate': True}) is None

def test_if_has_duplicates_redirect_lexeme_id_specified():
    assert lexeme_forms.if_has_duplicates_redirect({}, False, {'lexeme_id': 'L123'}) is None

def test_if_has_duplicates_redirect_lexeme_id_blank(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: ['duplicate'])
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: True)
    assert lexeme_forms.if_has_duplicates_redirect(minimal_template, False, {'lexeme_id': ''}) is not None

def test_if_has_duplicates_redirect_some_duplicates(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: ['duplicate'])
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered duplicates')
    assert lexeme_forms.if_has_duplicates_redirect(minimal_template, False, {}) == 'rendered duplicates'

def test_if_has_duplicates_redirect_no_duplicates(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: [])
    assert lexeme_forms.if_has_duplicates_redirect({}, False, {}) is None

def test_get_lemma_first_form_representation():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'noun'), ('form_representation', 'nouns')])
    lemma = lexeme_forms.get_lemma(form_data)
    assert lemma == 'noun'

def test_get_lemma_second_form_representation():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', ''), ('form_representation', 'nouns')])
    lemma = lexeme_forms.get_lemma(form_data)
    assert lemma == 'nouns'

def test_get_lemma_no_form_representation():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', ''), ('form_representation', '')])
    lemma = lexeme_forms.get_lemma(form_data)
    assert lemma is None

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

def test_add_form_data_to_template_lexeme_id():
    form_data = werkzeug.datastructures.ImmutableMultiDict([('lexeme_id', 'L123')])
    template = {'forms': []}
    new_template = lexeme_forms.add_form_data_to_template(form_data, template)
    assert new_template['lexeme_id'] == 'L123'

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

def test_current_url_index_https(monkeypatch):
    monkeypatch.setitem(lexeme_forms.app.config, 'APPLICATION_ROOT', '/')
    with lexeme_forms.app.test_request_context('/', headers=[('X-Forwarded-Proto', 'https')]):
        current_url = lexeme_forms.current_url()
        assert current_url == 'https://localhost/'

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

def test_build_summary_localhost(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'http://localhost/template/foo/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == 'foo'

def test_build_summary_internet(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://example.com/lexeme-forms/template/foo/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == 'foo'

def test_build_summary_toolforge_lexeme_forms(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://tools.wmflabs.org/lexeme-forms/template/foo/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:lexeme-forms/template/foo/|foo]]'

def test_build_summary_toolforge_other(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://tools.wmflabs.org/other/template/foo/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:other/template/foo/|foo]]'

def test_build_summary_toolforge_lexeme_forms_advanced(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://tools.wmflabs.org/lexeme-forms/template/foo/advanced/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:lexeme-forms/template/foo/advanced/|foo]]'

def test_build_summary_toolforge_canonical_lexeme_forms(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://lexeme-forms.toolforge.org/template/foo/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:lexeme-forms/template/foo/|foo]]'

def test_build_summary_toolforge_canonical_other(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://other.toolforge.org/template/foo/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:other/template/foo/|foo]]'

def test_build_summary_toolforge_canonical_lexeme_forms_advanced(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://lexeme-forms.toolforge.org/template/foo/advanced/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {}
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:lexeme-forms/template/foo/advanced/|foo]]'

def test_build_summary_generated_via(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://tools.wmflabs.org/lexeme-forms/template/foo/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {
        'generated_via': '[[toolforge:other/bar|other tool, bar]]'
    }
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:lexeme-forms/template/foo/|foo]], generated via [[toolforge:other/bar|other tool, bar]]'

def test_build_summary_canonical_generated_via(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'current_url', lambda: 'https://lexeme-forms.toolforge.org/template/foo/')
    template = {
        '@template_name': 'foo',
    }
    form_data = {
        'generated_via': '[[toolforge:other/bar|other tool, bar]]'
    }
    summary = lexeme_forms.build_summary(template, form_data)
    assert summary == '[[toolforge:lexeme-forms/template/foo/|foo]], generated via [[toolforge:other/bar|other tool, bar]]'

def test_get_all_templates_api():
    with lexeme_forms.app.test_client() as client:
        response = client.get('/api/v1/template/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    for template in json.loads(response.get_data(as_text=True)).values():
        assert '@attribution' in template

def test_get_template_api_exists():
    with lexeme_forms.app.test_client() as client:
        response = client.get('/api/v1/template/german-noun-feminine')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    template = json.loads(response.get_data(as_text=True))
    assert '@attribution' in template

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
    lexeme_data = {'forms': [
        {'id': 'L22936-F1', 'representations': {'en': {'language': 'en', 'value': 'dwarf'}}, 'grammaticalFeatures': ['Q110786']},
        {'id': 'L22936-F2', 'representations': {'en': {'language': 'en', 'value': 'dwarfs'}}, 'grammaticalFeatures': ['Q146786']},
    ]}
    template = copy.deepcopy(templates['english-noun'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    template['forms'][1]['lexeme_forms'] = [lexeme_data['forms'][1]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'dwarf'), ('form_representation', 'dwarfs/dwarves/dwarrows')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data)
    assert updated_lexeme_data == {'forms': [
        {'id': 'L22936-F1', 'representations': {'en': {'language': 'en', 'value': 'dwarf'}}, 'grammaticalFeatures': ['Q110786']},
        {'id': 'L22936-F2', 'representations': {'en': {'language': 'en', 'value': 'dwarfs'}}, 'grammaticalFeatures': ['Q146786']},
        {'add': '', 'representations': {'en': {'language': 'en', 'value': 'dwarves'}}, 'grammaticalFeatures': ['Q146786'], 'claims': {}},
        {'add': '', 'representations': {'en': {'language': 'en', 'value': 'dwarrows'}}, 'grammaticalFeatures': ['Q146786'], 'claims': {}},
    ], 'base_revision_id': 123}

def test_update_lexeme_noop():
    lexeme_data = {'forms': [
        {'id': 'L22936-F1', 'representations': {'en': {'language': 'en', 'value': 'dwarf'}}, 'grammaticalFeatures': ['Q110786']},
        {'id': 'L22936-F2', 'representations': {'en': {'language': 'en', 'value': 'dwarfs'}}, 'grammaticalFeatures': ['Q146786']},
        {'id': 'L22936-F3', 'representations': {'en': {'language': 'en', 'value': 'dwarves'}}, 'grammaticalFeatures': ['Q146786']},
        {'id': 'L22936-F4', 'representations': {'en': {'language': 'en', 'value': 'dwarrows'}}, 'grammaticalFeatures': ['Q146786']},
        {'id': 'L22936-F5', 'representations': {'en': {'language': 'en', 'value': 'dweorgas'}}, 'grammaticalFeatures': ['Q146786']},
    ]}
    template = copy.deepcopy(templates['english-noun'])
    template['lexeme_revision'] = 123
    template['forms'][0]['lexeme_forms'] = [lexeme_data['forms'][0]]
    template['forms'][1]['lexeme_forms'] = [lexeme_data['forms'][1], lexeme_data['forms'][2], lexeme_data['forms'][3], lexeme_data['forms'][4]]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', 'dwarf'), ('form_representation', 'dwarfs/dweorgas/dwarves/dwarrows')])
    updated_lexeme_data = lexeme_forms.update_lexeme(lexeme_data, template, form_data)
    assert updated_lexeme_data == {'forms': lexeme_data['forms'], 'base_revision_id': 123}


@pytest.mark.parametrize('template_name', templates.keys())
def test_integration_edit(template_name):
    """Create a lexeme from a template, then match it against the same template.

    If this fails, then there might be a bug when creating or matching lexemes,
    or the template might have ambiguous forms."""
    template = templates[template_name]
    form_data = werkzeug.datastructures.ImmutableMultiDict([('form_representation', str(index)) for index in range(0, len(template['forms']))])
    lexeme_data = lexeme_forms.build_lexeme(template, form_data)
    matched_template = matching.match_lexeme_forms_to_template(lexeme_data['forms'], template)
    assert matched_template.get('ambiguous_lexeme_forms') is None
    assert matched_template.get('unmatched_lexeme_forms') is None
    for index, form in enumerate(matched_template['forms']):
        assert len(form['lexeme_forms']) == 1
        assert form['lexeme_forms'][0]['representations'][template['language_code']]['value'] == str(index)
