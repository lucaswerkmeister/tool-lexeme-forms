import pytest
from typing import Optional

from .language_info import autonym, fallbacks
import toolforge_i18n.language_info


toolforge_i18n.language_info.user_agent = 'toolforge-i18n test (not published yet; mail@lucaswerkmeister.de)'


@pytest.mark.parametrize('code, expected', [
    ('en', 'English'),
    ('de', 'Deutsch'),
    ('fa', 'فارسی'),
    ('bn-x-Q6747180', None)
])
def test_autonym(code: str, expected: Optional[str]):
    assert autonym(code) == expected


@pytest.mark.parametrize('code, expected', [
    ('en', []),
    ('de', []),
    ('de-at', ['de']),
    ('sh', ['sh-latn', 'sh-cyrl', 'bs', 'sr-el', 'sr-latn', 'hr']),
])
def test_fallbacks(code: str, expected: list[str]):
    assert fallbacks(code) == expected
