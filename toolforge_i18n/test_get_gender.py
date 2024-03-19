import pytest

from .get_gender import get_gender_by_user_name


@pytest.mark.parametrize('user, expected', [
    ('علاء', 'm'),
    ('Harmonia Amanda', 'f'),
    ('Nikki', 'n'),
    (None, 'n'),
])
def test_get_gender(user, expected):
    assert get_gender_by_user_name(user) == expected
