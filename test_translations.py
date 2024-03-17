from bs4 import BeautifulSoup
from collections.abc import Callable
from markupsafe import Markup
import pytest
import re
from typing import Any

from app import translations
from language_info import autonym
import toolforge_i18n.formatters as formatters
import tool_translations_config


@pytest.fixture(scope="module", params=translations.keys())
def language_code(request):
    return request.param


@pytest.fixture(scope="module", params=translations['en'].keys())
def message_key(request):
    return request.param


def unused(*args, **kwargs):
    raise RuntimeError('This function should not be called!')


# maps allowed element names to allowed attributes
allowed_html_elements: dict[str, set[str]] = {
    'abbr': {'title'},
    'kbd': set(),
    'q': set(),
}
# lists allowed attributes on any element
allowed_global_attributes: set[str] = {
    'dir',
    'lang',
}


def test_english_messages_exist():
    """English is hard-coded as the final language fallback,
    so English messages must exist."""
    assert 'en' in translations


def test_language_code_leq_20(language_code: str):
    """We use 20 characters as an arbitrary limit for language setting length,
    so actual language codes must not be longer than that."""
    assert len(language_code) <= 20


def test_message_keys(language_code: str):
    language_keys = set(translations[language_code].keys())
    english_keys = set(translations['en'].keys())
    extra_keys = language_keys.difference(english_keys)
    assert not extra_keys


def test_autonym_exists(language_code: str) -> None:
    """Autonyms are used e.g. in the settings page,
    they should exist and be nonempty."""
    assert autonym(language_code)


@pytest.mark.filterwarnings('ignore::bs4.MarkupResemblesLocatorWarning')
def test_message_html_elements(language_code: str, message_key: str):
    message = translations[language_code].get(message_key)
    if message is None:
        return
    soup = BeautifulSoup(message, features='html.parser')
    for element in soup.find_all():
        assert element.name in allowed_html_elements
        allowed_attributes = (allowed_html_elements[element.name] |
                              allowed_global_attributes)
        for attr in element.attrs:
            assert attr in allowed_attributes


def test_message_variables(language_code: str, message_key: str):
    """Test that the translation uses variables correctly.

    See the TranslationConfig.variables docstring
    for the meaning of the different variable names / prefixes."""
    message = translations[language_code].get(message_key)
    if message is None:
        return
    for variable in tool_translations_config.config.variables.get(message_key, []):
        if variable == 'url':
            assert '{' + variable + '!h:' in message
            assert '{' + variable + '!g:' not in message
            assert '{' + variable + '!p:' not in message
            assert '{' + variable + '!l}' not in message
            assert '{' + variable + '}' not in message
        elif variable == 'user_name':
            assert '{' + variable + '!g:' in message or '{' + variable not in message
            assert '{' + variable + '!h:' not in message
            assert '{' + variable + '!p:' not in message
            assert '{' + variable + '!l}' not in message
            assert '{' + variable + '}' not in message
        elif variable.startswith('num_'):
            assert '{' + variable + '!p:' in message or '{' + variable not in message
            assert '{' + variable + '!h:' not in message
            assert '{' + variable + '!g:' not in message
            assert '{' + variable + '!l}' not in message
            # assert '{' + variable + '}' not in message  # allowed, e.g. {{PLURAL:$1||$1 forms}}
        elif variable.startswith('list_'):
            assert '{' + variable + '!l}' in message
            assert '{' + variable + '!h:' not in message
            assert '{' + variable + '!g:' not in message
            assert '{' + variable + '!p:' not in message
            assert '{' + variable + '}' not in message
        else:
            assert '{' + variable + '}' in message
            assert '{' + variable + '!h:' not in message
            assert '{' + variable + '!g:' not in message
            assert '{' + variable + '!p:' not in message
            assert '{' + variable + '!l}' not in message


def test_message_formatting(language_code: str, message_key: str):
    """Test that the translation uses variables correctly.

    See the TranslationConfig.variables docstring
    for the meaning of the different variable names / prefixes."""
    message = translations[language_code].get(message_key)
    if message is None:
        return

    url = 'https://example.com/test?foo=bar#baz'
    assert_contains = []
    get_gender: Callable[[str], str] = unused
    params: dict[str, Any] = {}
    for variable in tool_translations_config.config.variables.get(message_key, []):
        if variable == 'url':
            params[variable] = url
            assert_contains.append(url)
        elif variable == 'user_name':
            get_gender = lambda user_name: 'n'  # noqa: E731
            params[variable] = 'User name'
        elif variable.startswith('num_'):
            params[variable] = 123
        elif variable.startswith('list_'):
            item_1 = Markup('<a href="{url}">{variable} A</a>').format(url=url, variable=variable)
            item_2 = Markup('<a href="{url}">{variable} B</a>').format(url=url, variable=variable)
            params[variable] = [item_1, item_2]
            assert_contains.append(item_1)
            assert_contains.append(item_2)
        else:
            value = Markup('<a href="{url}">{variable}</a>').format(url=url, variable=variable)
            params[variable] = value
            assert_contains.append(value)

    formatter = formatters.I18nFormatter(
        locale_identifier=tool_translations_config.config.language_code_to_babel(language_code),
        get_gender=get_gender,
    )
    formatted = formatter.format(message, **params)

    for assertion in assert_contains:
        assert assertion in formatted
