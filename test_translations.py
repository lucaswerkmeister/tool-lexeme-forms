import builtins
import pytest
import re

import formatters
from language import lang_int2babel
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


def test_message_html_elements(language_code: str, message_key: str):
    message = translations.translations[language_code].get(message_key)
    if message is None:
        return
    html_element_names = {tag_name.lower()
                          for tag_name in re.findall('</?([0-9A-Za-z]*)', message)}
    html_element_names.difference_update(allowed_html_element_names)
    assert not html_element_names


def test_message_syntax_valid_duplicates_warning(language_code: str, number: int):
    if 'duplicates_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['duplicates_warning']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            lexemes=number,
        )


def test_message_syntax_valid_duplicates_instructions(language_code: str, number: int):
    if 'duplicates_instructions' in translations.translations[language_code]:
        message = translations.translations[language_code]['duplicates_instructions']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            lexemes=number,
        )


def test_message_syntax_valid_description_with_forms_and_senses(language_code: str, number: int):
    if 'description_with_forms_and_senses' in translations.translations[language_code]:
        message = translations.translations[language_code]['description_with_forms_and_senses']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            description='description',
            forms=number,
            senses=number,
        )


def test_message_syntax_valid_edit_ambiguous_warning(language_code: str, number: int):
    if 'edit_ambiguous_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_ambiguous_warning']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            forms=number,
        )


def test_message_syntax_valid_edit_unmatched_warning(language_code: str, number: int):
    if 'edit_unmatched_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_unmatched_warning']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            forms=number,
        )


def test_message_syntax_valid_edit_form_list_item(language_code: str, list: builtins.list[str], number: int):
    if 'edit_form_list_item' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_form_list_item']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=unused,
        ).format(
            message,
            form_link='',
            grammatical_feature_labels=list,
            statements=number,
        )


def test_message_syntax_valid_bulk_not_allowed(language_code: str, gender: str):
    if 'bulk_not_allowed' in translations.translations[language_code]:
        message = translations.translations[language_code]['bulk_not_allowed']
        formatters.I18nFormatter(
            locale_identifier=lang_int2babel(language_code),
            get_gender=lambda value: gender,
        ).format(
            message,
            user='some user',
        )
