import flask
import mwoauth
import pytest
import werkzeug

import app as lexeme_forms

def test_form2input_basic():
    markup = lexeme_forms.form2input({'advanced': False}, {'example': 'Left [placeholder] right.'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" required> right.'

def test_form2input_advanced():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder"> right.'

def test_form2input_first():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.'}, first=True)
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" autofocus> right.'

def test_form2input_preserve_value():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.', 'value': 'value'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" value="value"> right.'

def test_form2input_escape_value():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.', 'value': '"<>&'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" value="&#34;&lt;&gt;&amp;"> right.'

def test_form2input_invalid():
    with pytest.raises(Exception) as excinfo:
        markup = lexeme_forms.form2input({'advanced': True}, {'example': 'No placeholder.'})
    assert 'missing [placeholder]' in str(excinfo.value)

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
    assert lexeme_forms.if_has_duplicates_redirect({}, {}, False, {'no_duplicate': True}) is None

def test_if_has_duplicates_redirect_lexeme_id_specified():
    assert lexeme_forms.if_has_duplicates_redirect({}, {}, False, {'lexeme_id': 'L123'}) is None

def test_if_has_duplicates_redirect_lexeme_id_blank(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: ['duplicate'])
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: True)
    assert lexeme_forms.if_has_duplicates_redirect({'language_code': 'en'}, {}, False, {'lexeme_id': ''}) is not None

def test_if_has_duplicates_redirect_some_duplicates(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: ['duplicate'])
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered duplicates')
    assert lexeme_forms.if_has_duplicates_redirect({'language_code': 'en'}, {}, False, {}) == 'rendered duplicates'

def test_if_has_duplicates_redirect_no_duplicates(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'find_duplicates', lambda template, form_data: [])
    assert lexeme_forms.if_has_duplicates_redirect({}, {}, False, {}) is None

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

def test_if_needs_csrf_redirect_no_token(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered template')
    with lexeme_forms.app.test_request_context():
        response = lexeme_forms.if_needs_csrf_redirect({'language_code': 'en'}, 'template name', False, {})
    assert response == 'rendered template'
    # TODO instead of monkeypatching, assert that form_data is correctly preserved (possibly in separate test)

def test_if_needs_csrf_redirect_wrong_token(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered template')
    with lexeme_forms.app.test_request_context() as context:
        context.session['_csrf_token'] = 'token 1'
        response = lexeme_forms.if_needs_csrf_redirect({'language_code': 'en'}, 'template name', False, {'_csrf_token': 'token 2'})
    assert response == 'rendered template'

def test_if_needs_csrf_redirect_correct_token(monkeypatch):
    monkeypatch.setattr(lexeme_forms, 'add_form_data_to_template', lambda form_data, template: True)
    monkeypatch.setattr(flask, 'render_template', lambda template_file_name, **kwargs: 'rendered template')
    with lexeme_forms.app.test_request_context() as context:
        context.session['_csrf_token'] = 'token'
        response = lexeme_forms.if_needs_csrf_redirect({'language_code': 'en'}, 'template name', False, {'_csrf_token': 'token'})
    assert response is None

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

def test_build_lexeme_with_nonempty_lexeme_id():
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
    }

def test_build_lexeme_blank_form():
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
    }

def test_build_lexeme_with_claims():
    template = {
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'grammatical_features_item_ids': ['Q110786'],
                'claims': 'singular test claims',
            },
            {
                'grammatical_features_item_ids': ['Q146786'],
                'claims': 'plural test claims',
            },
        ],
        'claims': 'lexeme test claims',
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
                'claims': 'singular test claims',
            },
            {
                'add': '',
                'representations': {'en': {'language': 'en', 'value': 'nouns'}},
                'grammaticalFeatures': ['Q146786'],
                'claims': 'plural test claims',
            },
        ],
        'lemmas': {'en': {'language': 'en', 'value': 'noun'}},
        'language': 'Q1860',
        'lexicalCategory': 'Q1084',
        'claims': 'lexeme test claims',
    }
