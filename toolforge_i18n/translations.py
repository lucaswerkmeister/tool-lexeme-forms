import babel
import json
import os
import re
from typing import Any

from language import lang_int2babel


def initial_titlecase(s: str) -> str:
    return s[:1].title() + s[1:]


def identity(s: Any) -> Any:
    return s


# Variable names used in messages;
# the source messages use $1, $2 etc., but the Python format strings use named variables.
# The variable name encodes the type:
# * url - hyperlink: [$1 text] => {url!h:text}
# * user_name - gender: {{GENDER:$1|he|she|they}} => {user_name!g:m=he:f=she:n=they}
# * num_* - plural: {{PLURAL:$1|one form|$1 forms}} => {num_forms!p:one=one form:other={num_forms} forms}
# * list_* - list: $1 => {list_grammatical_feature_labels!l}
# * anything else - markup without further formatting: $1 => {description}
# (Note that e.g. form_link is an “anything else” variable:
# the link is formatted separately and the message passes it through as-is.)
variables = {
    'duplicates-warning': ['num_lexemes'],
    'duplicates-instructions': ['num_lexemes'],
    'description-with-forms-and-senses': ['description', 'num_forms', 'num_senses'],
    'bulk-not-allowed': ['user_name'],
    'bulk-first-field-not-lexeme-id': ['num_forms', 'num_fields', 'first_field', 'line_number'],
    'bulk-first-field-lexeme-id': ['num_forms', 'num_fields', 'first_field', 'line_number'],
    'bulk-wrong-number-of-fields': ['num_forms', 'num_fields', 'line_number'],
    'edit-ambiguous-warning': ['num_forms'],
    'edit-unmatched-warning': ['num_forms'],
    'edit-form-list-item': ['form_link', 'list_grammatical_feature_labels', 'num_statements'],
    'title-create': ['template_label'],
    'title-advanced': ['template_label'],
    'title-bulk': ['template_label'],
    'title-edit': ['template_label'],
    'login-hint': ['url'],
    'ambiguous-template': ['template_name', 'num_replacement_templates'],
    'logged-in': ['user_link', 'user_name'],
}
derived_messages = {
    'bulk-button': ('bulk-link', initial_titlecase),
    'bulk-heading': ('bulk-link', identity),
    'edit-button': ('edit-link', initial_titlecase),
}


def mw2py(mw: str, language: str, variables: list[str]) -> str:
    locale = babel.Locale(lang_int2babel(language))

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


skipped_language_codes = {
    'qqq',
}


translations: dict[str, dict[str, str]] = {}
for entry in os.scandir('i18n/'):
    if not entry.is_file():
        continue
    match = re.match(r'(.*)\.json$', entry.name)
    if not match:
        continue
    language = match[1]
    if language in skipped_language_codes:
        continue
    with open(entry.path, 'r') as f:
        data = json.load(f)
    translations[language] = {}
    for key in data:
        if key.startswith('@'):
            continue
        msg = mw2py(data[key], language, variables.get(key, []))
        translations[language][key] = msg
    for key in derived_messages:
        source_key, transformation = derived_messages[key]
        if source_key in translations[language]:
            translations[language][key] = transformation(translations[language][source_key])
