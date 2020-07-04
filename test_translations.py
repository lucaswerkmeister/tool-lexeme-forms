import pytest

import formatters
import translations


@pytest.mark.parametrize('language_code', translations.translations.keys())
def test_message_syntax_valid_duplicates_warning(language_code):
    if 'duplicates_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['duplicates_warning']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(babel_language_code).format(
            message,
            lexemes=1,
        )


@pytest.mark.parametrize('language_code', translations.translations.keys())
def test_message_syntax_valid_duplicates_instructions(language_code):
    if 'duplicates_instructions' in translations.translations[language_code]:
        message = translations.translations[language_code]['duplicates_instructions']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(babel_language_code).format(
            message,
            lexemes=1,
        )


@pytest.mark.parametrize('language_code', translations.translations.keys())
def test_message_syntax_valid_description_with_forms_and_senses(language_code):
    if 'description_with_forms_and_senses' in translations.translations[language_code]:
        message = translations.translations[language_code]['description_with_forms_and_senses']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(babel_language_code).format(
            message,
            description='description',
            forms=0,
            senses=0,
        )


@pytest.mark.parametrize('language_code', translations.translations.keys())
def test_message_syntax_valid_edit_ambiguous_warning(language_code):
    if 'edit_ambiguous_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_ambiguous_warning']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(babel_language_code).format(
            message,
            forms=1,
        )


@pytest.mark.parametrize('language_code', translations.translations.keys())
def test_message_syntax_valid_edit_unmatched_warning(language_code):
    if 'edit_unmatched_warning' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_unmatched_warning']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(babel_language_code).format(
            message,
            forms=1,
        )


@pytest.mark.parametrize('language_code', translations.translations.keys())
def test_message_syntax_valid_edit_form_list_item(language_code):
    if 'edit_form_list_item' in translations.translations[language_code]:
        message = translations.translations[language_code]['edit_form_list_item']
        babel_language_code = 'en' if language_code == 'la' else language_code
        formatters.I18nFormatter(babel_language_code).format(
            message,
            form_link='',
            grammatical_feature_labels=[],
            statements=0,
        )
