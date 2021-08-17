import sys
from typing import Optional

import mwapi  # type: ignore
import toolforge

_language_info = None

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
