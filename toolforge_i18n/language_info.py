import mwapi  # type: ignore
import requests
from typing import Optional


user_agent: Optional[str] = None
"""The user agent to use for API requests.

If this is not set, the module will attempt to use a user agent
previously set by toolforge::set_user_agent(), and otherwise fail.
Usually, you should call toolforge::set_user_agent() during
early initialization of your tool;
otherwise, you may set the user_agent here explicitly.
"""


def _user_agent() -> str:
    if user_agent is not None:
        return user_agent
    toolforge_user_agent = requests.utils.default_user_agent()
    if 'toolforge' in toolforge_user_agent:
        return toolforge_user_agent
    raise RuntimeError(
        "Could not determine user agent, "
        "either call toolforge.set_user_agent() "
        "or set toolforge_i18n.language_info.user_agent"
    )


_language_info = None


def _load_language_info() -> dict[str, dict]:
    session = mwapi.Session(
        'https://meta.wikimedia.org',
        user_agent=_user_agent(),
    )
    language_info = {}
    for response in session.get(continuation=True,
                                action='query',
                                meta='languageinfo',
                                liprop=['autonym', 'fallbacks'],
                                formatversion='2'):
        language_info.update(response['query']['languageinfo'])
    return language_info


def autonym(code: str) -> Optional[str]:
    """Get the autonym of the given language code, according to MediaWiki."""
    global _language_info
    if _language_info is None:
        _language_info = _load_language_info()
    return _language_info.get(code, {}).get('autonym')


def fallbacks(code: str) -> list[str]:
    """Get the fallback languages of the given language code, according to MediaWiki."""
    global _language_info
    if _language_info is None:
        _language_info = _load_language_info()
    return _language_info.get(code, {}).get('fallbacks', [])
