import pytest
from typing import Optional

from .language_info import lang_autonym, lang_mw_to_bcp47, lang_dir, lang_fallbacks
import toolforge_i18n.language_info


toolforge_i18n.user_agent.set_user_agent('toolforge-i18n test (not published yet; mail@lucaswerkmeister.de)')


@pytest.mark.parametrize('code, expected', [
    ('en', 'English'),
    ('de', 'Deutsch'),
    ('fa', 'فارسی'),
    ('bn-x-Q6747180', None)
])
def test_lang_autonym(code: str, expected: Optional[str]):
    assert lang_autonym(code) == expected


@pytest.mark.parametrize('code, expected', [
    ('en', 'en'),
    ('simple', 'en-simple'),
    ('unknown', 'unknown')
])
def test_lang_mw_to_bcp47(code: str, expected: str):
    assert lang_mw_to_bcp47(code) == expected


@pytest.mark.parametrize('code, expected', [
    ('en', 'ltr'),
    ('fa', 'rtl'),
    ('unknown', 'auto')
])
def test_lang_dir(code: str, expected: str):
    assert lang_dir(code) == expected


@pytest.mark.parametrize('code, expected', [
    ('en', []),
    ('de', []),
    ('de-at', ['de']),
    ('sh', ['sh-latn', 'sh-cyrl', 'bs', 'sr-el', 'sr-latn', 'hr']),
])
def test_lang_fallbacks(code: str, expected: list[str]):
    assert lang_fallbacks(code) == expected
