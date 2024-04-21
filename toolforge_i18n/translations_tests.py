from bs4 import BeautifulSoup
from collections.abc import Callable
from markupsafe import Markup
import pytest
import re
from typing import Any

import toolforge_i18n.formatters as formatters
from toolforge_i18n.translations import load_translations
import tool_translations_config


translations, documentation = load_translations(tool_translations_config.config)


@pytest.fixture(scope="module", params=translations.keys())
def language_code(request):
    return request.param


@pytest.fixture(scope="module", params=translations['en'].keys())
def message_key(request):
    return request.param


def unused(*args, **kwargs):
    raise RuntimeError('This function should not be called!')


def test_message_keys(language_code: str):
    language_keys = set(translations[language_code].keys())
    english_keys = set(translations['en'].keys())
    extra_keys = language_keys.difference(english_keys)
    assert not extra_keys


@pytest.mark.filterwarnings('ignore::bs4.MarkupResemblesLocatorWarning')
def test_message_html_elements(language_code: str, message_key: str):
    message = translations[language_code].get(message_key)
    if message is None:
        return
    soup = BeautifulSoup(message, features='html.parser')
    for element in soup.find_all():
        assert element.name in tool_translations_config.config.allowed_html_elements
        allowed_attributes = (tool_translations_config.config.allowed_html_elements[element.name] |
                              tool_translations_config.config.allowed_global_attributes)
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
        if variable == 'url' or variable.startswith('url_'):
            assert '{' + variable + '!h:' in message
            assert '{' + variable + '!g:' not in message
            assert '{' + variable + '!p:' not in message
            assert '{' + variable + '!l}' not in message
            assert '{' + variable + '}' not in message
        elif variable == 'user_name' or variable.startswith('user_name_'):
            assert '{' + variable + '!g:' in message or '{' + variable not in message
            assert '{' + variable + '!h:' not in message
            assert '{' + variable + '!p:' not in message
            assert '{' + variable + '!l}' not in message
            assert '{' + variable + '}' not in message
        elif variable == 'num' or variable.startswith('num_'):
            assert '{' + variable + '!p:' in message or '{' + variable not in message
            assert '{' + variable + '!h:' not in message
            assert '{' + variable + '!g:' not in message
            assert '{' + variable + '!l}' not in message
            # assert '{' + variable + '}' not in message  # allowed, e.g. {{PLURAL:$1||$1 forms}}
        elif variable == 'list' or variable.startswith('list_'):
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
