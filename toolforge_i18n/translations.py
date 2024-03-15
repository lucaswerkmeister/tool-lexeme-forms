import babel
from collections.abc import Callable, Container, Mapping, Sequence
from dataclasses import dataclass, field
import json
import os
import re


@dataclass
class TranslationsConfig:
    """Configuration for loading message translations."""

    directory: str = 'i18n/'
    """The path to the directory to load message files from."""

    variables: Mapping[str, Sequence[str]] = field(default_factory=dict)
    """Variable names used in messages.

    The source messages use $1, $2 etc.,
    but the Python format strings use named variables,
    whose names are specified here.
    The variable name encodes the type:
    * url - hyperlink: [$1 text] => {url!h:text}
    * user_name - gender: {{GENDER:$1|he|she|they}} => {user_name!g:m=he:f=she:n=they}
    * num_* - plural: {{PLURAL:$1|one egg|$1 eggs}} => {num_eggs!p:one=one egg:other={num_eggs} eggs}
    * list_* - list: $1 => {list_chicken_names!l}
    * anything else - markup without further formatting: $1 => {description}
    """

    derived_messages: Mapping[str, tuple[str, Callable[[str], str]]] = field(default_factory=dict)
    """Messages that are derived from other messages.

    The key is a message key that is not expected in the JSON files,
    but that is instead generated by taking another message
    (whose key is the first element of the tuple)
    and sending it through the callable in the second element of the tuple.
    Examples for that callable include the identity function
    (to copy a message) or simple case transformations.
    """

    language_code_to_babel: Callable[[str], str] = lambda code: code  # TODO include lang_int2babel in this package?
    """Mapping from MediaWiki to Babel language codes.

    Message files use MediaWiki language codes,
    which are not always standard language codes;
    additionally, MediaWiki supports many languages that Babel does not,
    even when the language code is standard.
    You will need to map these codes to a supported alternative
    if you have any translations for such language codes."""

    skipped_language_codes: Container[str] = field(default_factory=lambda: {'qqq'})
    """Language codes for which translations should not be loaded."""


def mw2py(mw: str, babel_language: str, variables: Sequence[str]) -> str:
    locale = babel.Locale(babel_language)

    def replace_plural(match: re.Match) -> str:
        nonlocal locale, variables
        number = int(match[1])
        variable = variables[number - 1]
        args = match[2].split('|')
        plurals = []
        tag_args = []
        for arg in args:
            key, _, text = arg.partition('=')
            if key.isnumeric():
                plurals.append(arg)
            else:
                tag_args.append(arg)
        tags = [tag
                for tag in ['zero', 'one', 'two', 'few', 'many']
                if tag in locale.plural_form.tags]
        tags = tags[:len(tag_args) - 1] + ['other']
        for tag, tag_arg in zip(tags, tag_args):
            plurals.append(f'{tag}={tag_arg}')
        return '{' + variable + '!p:' + ':'.join(plurals) + '}'
    py = re.sub(r'\{\{PLURAL:\$([1-9][0-9]*)\|([^}]*)\}\}', replace_plural, mw)

    def replace_gender(match: re.Match) -> str:
        nonlocal variables
        number = int(match[1])
        variable = variables[number - 1]
        args = match[2].split('|')
        genders = []
        for gender, arg in zip(['m', 'f', 'n'], args):
            genders.append(f'{gender}={arg}')
        return '{' + variable + '!g:' + ':'.join(genders) + '}'
    py = re.sub(r'\{\{GENDER:\$([1-9][0-9]*)\|([^}]*)\}\}', replace_gender, py)

    def replace_hyperlink(match: re.Match) -> str:
        nonlocal variables
        number = int(match[1])
        variable = variables[number - 1]
        inner_html = match[2]
        assert '{' not in inner_html and '}' not in inner_html
        return '{' + variable + '!h:' + inner_html + '}'
    py = re.sub(r'\[\$([1-9][0-9]*) ([^]]*)\]', replace_hyperlink, py)

    def replace_unconverted(match: re.Match) -> str:
        nonlocal variables
        number = int(match[1])
        variable = variables[number - 1]
        if variable.startswith('list_'):
            return '{' + variable + '!l}'
        else:
            return '{' + variable + '}'
    py = re.sub(r'\$([1-9][0-9]*)', replace_unconverted, py)
    return py


def load_translations(config: TranslationsConfig) -> dict[str, dict[str, str]]:
    translations: dict[str, dict[str, str]] = {}
    for entry in os.scandir(config.directory):
        if not entry.is_file():
            continue
        match = re.match(r'(.*)\.json$', entry.name)
        if not match:
            continue
        language = match[1]
        if language in config.skipped_language_codes:
            continue
        with open(entry.path, 'r') as f:
            data = json.load(f)
        translations[language] = {}
        for key in data:
            if key.startswith('@'):
                continue
            msg = mw2py(data[key], config.language_code_to_babel(language), config.variables.get(key, []))
            translations[language][key] = msg
        for key in config.derived_messages:
            source_key, transformation = config.derived_messages[key]
            if source_key in translations[language]:
                translations[language][key] = transformation(translations[language][source_key])
    return translations
