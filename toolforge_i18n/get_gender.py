import mwapi  # type: ignore
from typing import Literal, Optional

from .user_agent import get_user_agent


def get_gender_by_user_name(user_name: Optional[str]) -> Literal['m', 'f', 'n']:
    """Get the gender of a named user on Wikimedia sites.

    This gets the gender from Meta-Wiki –
    hopefully the user set it as a global preference,
    not just on one other wiki.
    None may be used to represent an unknown user (e.g. not logged in),
    who will be treated as having neuter gender.
    """
    if user_name is None:
        return 'n'
    session = mwapi.Session('https://meta.wikimedia.org',
                            user_agent=get_user_agent())
    response = session.get(action='query',
                           list=['users'],
                           usprop=['gender'],
                           ususers=[user_name],
                           formatversion=2)
    mapping: dict[str, Literal['m', 'f', 'n']] = {
        'male': 'm',
        'female': 'f',
        'unknown': 'n',
    }
    return mapping[response['query']['users'][0]['gender']]
