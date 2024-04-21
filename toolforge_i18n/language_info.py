import mwapi  # type: ignore
import requests
from typing import Literal, Optional, TypedDict, cast

from .user_agent import get_user_agent


# for easier typing below, pretend that _LanguageInfo members are optional,
# and that _language_info and _by_bcp47 are always dicts
# (they are lazily initialized in _load_language_info)


class _LanguageInfo(TypedDict, total=False):
    bcp47: str
    dir: Literal['ltr', 'rtl']
    autonym: str
    fallbacks: list[str]


_language_info: dict[str, _LanguageInfo] = cast(dict[str, _LanguageInfo], None)
_by_bcp47: dict[str, str] = cast(dict[str, str], None)


def _load_language_info():
    global _language_info, _by_bcp47
    if _language_info is not None:
        return

    session = mwapi.Session(
        'https://meta.wikimedia.org',
        user_agent=get_user_agent(),
    )
    _language_info = {}
    for response in session.get(continuation=True,
                                action='query',
                                meta='languageinfo',
                                liprop=['autonym', 'bcp47', 'dir', 'fallbacks'],
                                formatversion='2'):
        _language_info.update(response['query']['languageinfo'])

    _by_bcp47 = {}
    for code, language in _language_info.items():
        _by_bcp47[language['bcp47']] = code


# lang_mw_to_bcp47 and lang_bcp47_to_mw have both “source” and “destination” type in their name,
# because we need both directions and the names would otherwise be confusing;
# the other functions (lang_autonym, lang_dir, lang_fallbacks)
# all take MediaWiki language codes as the “source”


def lang_mw_to_bcp47(code: str) -> str:
    """Get the BCP-47 language code of the given MediaWiki language code."""
    _load_language_info()
    return _language_info.get(code, {}).get('bcp47', code)


def lang_bcp47_to_mw(code: str) -> str:
    """Get the MediaWiki language code of the given BCP-47 language code."""
    _load_language_info()
    return _by_bcp47.get(code, code)


def lang_autonym(code: str) -> Optional[str]:
    """Get the autonym of the given language code, according to MediaWiki."""
    _load_language_info()
    return _language_info.get(code, {}).get('autonym')


def lang_dir(code: str) -> Literal['ltr', 'rtl', 'auto']:
    """Get the directionality of the given language code, according to MediaWiki."""
    _load_language_info()
    return _language_info.get(code, {}).get('dir', 'auto')


def lang_fallbacks(code: str) -> list[str]:
    """Get the fallback languages of the given language code, according to MediaWiki."""
    _load_language_info()
    return _language_info.get(code, {}).get('fallbacks', [])
