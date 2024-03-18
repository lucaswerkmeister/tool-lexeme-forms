import pytest
from typing import Optional

from language_info import label

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
