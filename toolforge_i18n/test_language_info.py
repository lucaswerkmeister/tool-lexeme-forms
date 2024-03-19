import pytest
from typing import Optional

from .language_info import autonym, bcp47, directionality, fallbacks
import toolforge_i18n.language_info


toolforge_i18n.user_agent.set_user_agent('toolforge-i18n test (not published yet; mail@lucaswerkmeister.de)')


@pytest.mark.parametrize('code, expected', [
    ('en', 'English'),
    ('de', 'Deutsch'),
    ('fa', 'فارسی'),
    ('bn-x-Q6747180', None)
])
def test_autonym(code: str, expected: Optional[str]):
    assert autonym(code) == expected


@pytest.mark.parametrize('code, expected', [
    ('en', 'en'),
    ('simple', 'en-simple'),
    ('unknown', 'unknown')
])
def test_bcp47(code: str, expected: str):
    assert bcp47(code) == expected


@pytest.mark.parametrize('code, expected', [
    ('en', 'ltr'),
    ('fa', 'rtl'),
    ('unknown', 'auto')
])
def test_directionality(code: str, expected: str):
    assert directionality(code) == expected


@pytest.mark.parametrize('code, expected', [
    ('en', []),
    ('de', []),
    ('de-at', ['de']),
    ('sh', ['sh-latn', 'sh-cyrl', 'bs', 'sr-el', 'sr-latn', 'hr']),
])
def test_fallbacks(code: str, expected: list[str]):
    assert fallbacks(code) == expected
