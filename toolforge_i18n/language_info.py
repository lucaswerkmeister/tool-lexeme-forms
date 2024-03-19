import mwapi  # type: ignore
import requests
from typing import Literal, Optional

from .user_agent import get_user_agent


_language_info = None


def _load_language_info() -> dict[str, dict]:
    session = mwapi.Session(
        'https://meta.wikimedia.org',
        user_agent=get_user_agent(),
    )
    language_info = {}
    for response in session.get(continuation=True,
                                action='query',
                                meta='languageinfo',
                                liprop=['autonym', 'bcp47', 'dir', 'fallbacks'],
                                formatversion='2'):
        language_info.update(response['query']['languageinfo'])
    return language_info


def autonym(code: str) -> Optional[str]:
    """Get the autonym of the given language code, according to MediaWiki."""
    global _language_info
    if _language_info is None:
        _language_info = _load_language_info()
    return _language_info.get(code, {}).get('autonym')


def bcp47(code: str) -> str:
    """Get the BCP-47 language code of the given MediaWiki language code."""
    global _language_info
    if _language_info is None:
        _language_info = _load_language_info()
    return _language_info.get(code, {}).get('bcp47', code)


def directionality(code: str) -> Literal['ltr', 'rtl', 'auto']:
    """Get the directionality of the given language code, according to MediaWiki."""
    global _language_info
    if _language_info is None:
        _language_info = _load_language_info()
    return _language_info.get(code, {}).get('dir', 'auto')


def fallbacks(code: str) -> list[str]:
    """Get the fallback languages of the given language code, according to MediaWiki."""
    global _language_info
    if _language_info is None:
        _language_info = _load_language_info()
    return _language_info.get(code, {}).get('fallbacks', [])
