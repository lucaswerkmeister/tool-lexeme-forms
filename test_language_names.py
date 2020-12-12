import pytest

from language_names import autonym

@pytest.mark.parametrize('code, expected', [
    ('en', 'English'),
    ('de', 'Deutsch'),
    ('fa', 'فارسی'),
    ('bn-x-Q6747180', None)
])
def test_autonym(code, expected):
    assert autonym(code) == expected
