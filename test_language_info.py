import pytest
from typing import Optional

from language_info import autonym, label, fallbacks

@pytest.mark.parametrize('code, expected', [
    ('en', 'English'),
    ('de', 'Deutsch'),
    ('fa', 'فارسی'),
    ('bn-x-Q6747180', None)
])
def test_autonym(code: str, expected: Optional[str]):
    assert autonym(code) == expected

@pytest.mark.parametrize('code, expected', [
    ('bn-x-Q6747180', 'ঝাড়খণ্ডী উপভাষা'),
    ('de-x-Q188', 'Deutsch'),
    ('en-x-Q188', 'German'),
    ('de-x-Q27860798', 'Protein structure comparison by alignment of distance matrices'),
    ('de-x-Q18775580', None),
    ('qqx-x-Q42', None),
    ('en-x-Q0', None),
    ('-x-Q1', None),
    ('en-x-y-z', None),
    ('en', None),
])
def test_label(code: str, expected: Optional[str]):
    assert label(code) == expected

@pytest.mark.parametrize('code, expected', [
    ('en', []),
    ('de', []),
    ('de-at', ['de']),
    ('sh', ['sh-latn', 'sh-cyrl', 'bs', 'sr-el', 'sr-latn', 'hr']),
])
def test_fallbacks(code: str, expected: list[str]):
    assert fallbacks(code) == expected
