import pytest

import formatters
import translations


@pytest.mark.parametrize('language_code', translations.translations.keys())
def test_plural_syntax_valid(language_code):
    if 'description_with_forms_and_senses' in translations.translations[language_code]:
        message = translations.translations[language_code]['description_with_forms_and_senses']
        formatters.PluralFormatter(language_code).format(
            message,
            description='description',
            forms=0,
            senses=0,
        )
