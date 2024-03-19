import requests


_user_agent = None


def get_user_agent() -> str:
    """Get the user agent string used by toolforge_i18n.

    The user agent string may be set by set_user_agent();
    otherwise, try to get a user agent previously set up
    by toolforge.set_user_agent().

    Code outside of toolforge_i18n generally shouldn’t use this function.
    """
    if _user_agent is not None:
        return _user_agent
    toolforge_user_agent = requests.utils.default_user_agent()
    if 'toolforge' in toolforge_user_agent:
        return toolforge_user_agent
    raise RuntimeError(
        "Could not determine user agent, "
        "call either toolforge.set_user_agent() "
        "or toolforge_i18n.user_agent.set_user_agent()"
    )


def set_user_agent(user_agent: str) -> None:
    """Set the user agent string used by toolforge_i18n.

    Most tools should call toolforge.set_user_agent() instead,
    which also sets the user agent for other code.
    It is typically called during early initialization.

    See the User-Agent policy (https://w.wiki/4PLr) for the format.
    """
    global _user_agent
    _user_agent = user_agent
