import flask
from markupsafe import Markup
from toolforge_i18n.formatters import I18nFormatter
from toolforge_i18n.language_info import bcp47, directionality, fallbacks
from toolforge_i18n.translations import load_translations
import tool_translations_config
from typing import Callable, Protocol, Tuple, cast
import werkzeug


def init_html_language_codes() -> None:
    flask.g.html_language_codes = []


def push_html_lang(language_code: str) -> Markup:
    html_language_code = bcp47(language_code)
    flask.g.html_language_codes.append(html_language_code)
    return Markup(r'lang="{}" dir="{}"').format(html_language_code,
                                                directionality(html_language_code))


def add_lang_if_needed(message: Markup, language_code: str) -> Markup:
    if flask.g.html_language_codes and flask.g.html_language_codes[-1] == language_code:
        return message
    return Markup('<span {}>{}</span{}>').format(push_html_lang(language_code),
                                                 message,
                                                 pop_html_lang(language_code))


def pop_html_lang(language_code: str) -> Markup:
    html_language_code = bcp47(language_code)
    assert flask.g.html_language_codes.pop() == html_language_code
    return Markup(r'')


def assert_html_language_codes_empty(response: werkzeug.Response) -> werkzeug.Response:
    assert flask.g.html_language_codes == []
    return response


class _MessageFunction(Protocol):
    def __call__(self, message_code: str, **kwargs) -> Markup:
        ...


def interface_language_code_from_request(translations: dict[str, dict[str, str]]) -> str:
    # TODO: this mixes HTML and MediaWiki language codes :/
    return flask.request.accept_languages.best_match(translations.keys(), 'en')


def setup_toolforge_i18n(
        app: flask.Flask,
        interface_language_code: Callable[[dict[str, dict[str, str]]], str] = interface_language_code_from_request,
) -> _MessageFunction:
    translations = load_translations(tool_translations_config.config)

    def message_with_language(message_code: str) -> Tuple[Markup, str]:
        interface_language_code = cast(str, flask.g.interface_language_code)
        language_codes = ([interface_language_code] +
                          fallbacks(interface_language_code) +
                          ['en'])
        for language_code in language_codes:
            try:
                text = translations[language_code][message_code]
            except LookupError:
                continue
            else:
                return Markup(text), language_code
        raise ValueError(f'Message {message_code} not found in {language_codes}')

    @app.template_global()
    def message(message_code: str, **kwargs) -> Markup:
        message, language = message_with_language(message_code)
        if kwargs:
            formatter = I18nFormatter(locale_identifier=tool_translations_config.config.language_code_to_babel(language),
                                      get_gender=tool_translations_config.config.get_gender)
            # I18nFormatter returns Markup given Markup
            message = cast(Markup, formatter.format(message, **kwargs))
        return add_lang_if_needed(message, language)

    @app.before_request
    def init_interface_language_code() -> None:
        flask.g.interface_language_code = interface_language_code(translations)

    app.add_template_filter(bcp47)
    app.add_template_global(push_html_lang)
    app.add_template_global(pop_html_lang)
    app.before_request(init_html_language_codes)
    app.after_request(assert_html_language_codes_empty)

    return message
