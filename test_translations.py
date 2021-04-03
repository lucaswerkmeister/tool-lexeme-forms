import pytest
import re

import formatters
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


def test_message_keys(language_code):
    language_keys = set(translations.translations[language_code].keys())
    english_keys = set(translations.translations['en'].keys())
    extra_keys = language_keys.difference(english_keys)
    assert not extra_keys


def test_message_html_elements(language_code, message_key):
    message = translations.translations[language_code].get(message_key)
    if message is None:
        return
    html_element_names = {tag_name.lower()
                          for tag_name in re.findall('</?([0-9A-Za-z]*)', message)}
    html_element_names.difference_update(allowed_html_element_names)
    assert not html_element_names


def test_message_syntax_valid_duplicates_warning(language_code, number):
    if 'duplicates_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['duplicates_warning']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(
            locale_identifier=babel_language_code,
            get_gender=unused,
        ).format(
            message,
            lexemes=number,
        )


def test_message_syntax_valid_duplicates_instructions(language_code, number):
    if 'duplicates_instructions' in translations.translations[language_code]:
        message = translations.translations[language_code]['duplicates_instructions']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(
            locale_identifier=babel_language_code,
            get_gender=unused,
        ).format(
            message,
            lexemes=number,
        )


def test_message_syntax_valid_description_with_forms_and_senses(language_code, number):
    if 'description_with_forms_and_senses' in translations.translations[language_code]:
        message = translations.translations[language_code]['description_with_forms_and_senses']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(
            locale_identifier=babel_language_code,
            get_gender=unused,
        ).format(
            message,
            description='description',
            forms=number,
            senses=number,
        )


def test_message_syntax_valid_edit_ambiguous_warning(language_code, number):
    if 'edit_ambiguous_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_ambiguous_warning']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(
            locale_identifier=babel_language_code,
            get_gender=unused,
        ).format(
            message,
            forms=number,
        )


def test_message_syntax_valid_edit_unmatched_warning(language_code, number):
    if 'edit_unmatched_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_unmatched_warning']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(
            locale_identifier=babel_language_code,
            get_gender=unused,
        ).format(
            message,
            forms=number,
        )


def test_message_syntax_valid_edit_form_list_item(language_code, list, number):
    if 'edit_form_list_item' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_form_list_item']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(
            locale_identifier=babel_language_code,
            get_gender=unused,
        ).format(
            message,
            form_link='',
            grammatical_feature_labels=list,
            statements=number,
        )


def test_message_syntax_valid_bulk_not_allowed(language_code, gender):
    if 'bulk_not_allowed' in translations.translations[language_code]:
        message = translations.translations[language_code]['bulk_not_allowed']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(
            locale_identifier=babel_language_code,
            get_gender=lambda value: gender,
        ).format(
            message,
            user='some user',
        )
