import re
import sys
from typing import Optional

import mwapi  # type: ignore
import toolforge

_language_info = None
_labels: dict[str, str] = {}

_user_agent = toolforge.set_user_agent('lexeme-forms', email='mail@lucaswerkmeister.de')

def load_language_info():
    session = mwapi.Session(
        'https://meta.wikimedia.org',
        user_agent=_user_agent,
    )
    response = session.get(action='query',
                           meta='languageinfo',
                           liprop='autonym',
                           formatversion='2')
    if 'continue' in response:
        print('WARNING: MediaWiki languageinfo incomplete, continue={}'.format(response['continue']),
              file=sys.stderr)
    return response['query']['languageinfo']

def autonym(code: str) -> Optional[str]:
    global _language_info
    if _language_info is None:
        _language_info = load_language_info()
    return _language_info.get(code, {}).get('autonym')

def label(code: str) -> Optional[str]:
    """Get the label for an item-based language code.

    Expects a language code in the format abc-x-Q123
    and return Q123’s label for the abc language code."""
    try:
        return _labels[code]
    except KeyError:
        pass
    match = re.fullmatch(r'([a-z]+)-x-(Q[1-9][0-9]*)', code)
    if match is None:
        return None
    language, item_id = match.group(1, 2)
    session = mwapi.Session(
        'https://www.wikidata.org',
        user_agent=_user_agent,
    )
    response = session.get(action='wbgetentities',
                           ids=[item_id],
                           props=['labels'],
                           languages=[language],
                           languagefallback=True,
                           formatversion=2)
    label = response['entities'][item_id].get('labels', {}).get(language, {}).get('value')
    _labels[code] = label
    return label
