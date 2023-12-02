import builtins
import pytest
import re

import formatters
from language import lang_int2babel
from language_info import autonym
import translations


@pytest.fixture(scope="module", params=translations.translations.keys())
def language_code(request):
    return request.param


@pytest.fixture(scope="module", params=translations.translations['en'].keys())
def message_key(request):
    return request.param


@pytest.fixture(scope="module", params=['m', 'f', 'n'])
def gender(request):
    return request.param


@pytest.fixture(scope="module", params=[0, 1, 2, 3, 5, 1000])
def number(request):
    return request.param


@pytest.fixture(scope="module", params=[[], ["list item 1"], ["list item 1", "list item 2"]])
def list(request):
    return request.param


def unused(*args, **kwargs):
    raise RuntimeError('This function should not be called!')


allowed_html_element_names = {
    'abbr',
    'kbd',
    'q',
}


def test_english_messages_exist():
    """English is hard-coded as the final language fallback,
    so English messages must exist."""
    assert 'en' in translations.translations


def test_language_code_leq_20(language_code: str):
    """We use 20 characters as an arbitrary limit for language setting length,
    so actual language codes must not be longer than that."""
    assert len(language_code) <= 20


def test_message_keys(language_code: str):
    language_keys = set(translations.translations[language_code].keys())
    english_keys = set(translations.translations['en'].keys())
    extra_keys = language_keys.difference(english_keys)
    assert not extra_keys


def test_autonym_exists(language_code: str) -> None:
    """Autonyms are used e.g. in the settings page,
    they should exist and be nonempty."""
    assert autonym(language_code)


def test_message_html_elements(language_code: str, message_key: str):
    message = translations.translations[language_code].get(message_key)
    if message is None:
        return
    html_element_names = {tag_name.lower()
                          for tag_name in re.findall('</?([0-9A-Za-z]*)', message)}
    html_element_names.difference_update(allowed_html_element_names)
    assert not html_element_names


def test_message_syntax_valid_duplicates_warning(language_code: str, number: int):
    if 'duplicates-warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['duplicates-warning']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            num_lexemes=number,
        )


def test_message_syntax_valid_duplicates_instructions(language_code: str, number: int):
    if 'duplicates-instructions' in translations.translations[language_code]:
        message = translations.translations[language_code]['duplicates-instructions']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            num_lexemes=number,
        )


def test_message_syntax_valid_description_with_forms_and_senses(language_code: str, number: int):
    if 'description-with-forms-and-senses' in translations.translations[language_code]:
        message = translations.translations[language_code]['description-with-forms-and-senses']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            description='description',
            num_forms=number,
            num_senses=number,
        )


def test_message_syntax_valid_edit_ambiguous_warning(language_code: str, number: int):
    if 'edit-ambiguous-warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit-ambiguous-warning']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            num_forms=number,
        )


def test_message_syntax_valid_edit_unmatched_warning(language_code: str, number: int):
    if 'edit-unmatched-warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit-unmatched-warning']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            num_forms=number,
        )


def test_message_syntax_valid_edit_form_list_item(language_code: str, list: builtins.list[str], number: int):
    if 'edit-form-list-item' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit-form-list-item']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            form_link='',
            list_grammatical_feature_labels=list,
            num_statements=number,
        )


def test_message_syntax_valid_bulk_not_allowed(language_code: str, gender: str):
    if 'bulk-not-allowed' in translations.translations[language_code]:
        message = translations.translations[language_code]['bulk-not-allowed']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=lambda value: gender,
        ).format(
            message,
            user_name='some user',
        )


def test_message_syntax_valid_login_hint(language_code: str):
    if 'login-hint' in translations.translations[language_code]:
        message = translations.translations[language_code]['login-hint']
        formatted = formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            url='https://example.com',
        )
        assert '<a href=' in formatted


def test_link_not_in_gender_logged_in(language_code: str, gender: str):
    """Assert that a message with both {{GENDER:}} and a link renders correctly.

    Currently, this means that the link must not appear inside the gender spec.
    If it does, i.e. {{GENDER:$2|...$1...}} in wikitext or {user_name!g:m=...{user_link}...} in Python,
    then the colon in http:// or https:// in the link will be misinterpreted as a m:f:n separator,
    resulting in the rest of the link (including the closing tag!) being discarded."""
    if 'logged-in' in translations.translations[language_code]:
        user_name = 'some user'
        user_link = f'<a href="https://example.com/">{user_name}</a>'
        message = translations.translations[language_code]['logged-in']
        formatted = formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=lambda value: gender,
        ).format(
            message,
            user_link=user_link,
            user_name=user_name,
        )
        assert user_link in formatted
