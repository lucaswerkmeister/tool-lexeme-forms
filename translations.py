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


variables = {
    'duplicates-warning': ['lexemes'],
    'duplicates-instructions': ['lexemes'],
    'description-with-forms-and-senses': ['description', 'forms', 'senses'],
    'bulk-not-allowed': ['user'],
    'bulk-first-field-not-lexeme-id': ['num_forms', 'num_fields', 'first_field', 'line_number'],
    'bulk-first-field-lexeme-id': ['num_forms', 'num_fields', 'first_field', 'line_number'],
    'bulk-wrong-number-of-fields': ['num_forms', 'num_fields', 'line_number'],
    'edit-ambiguous-warning': ['forms'],
    'edit-unmatched-warning': ['forms'],
    'edit-form-list-item': ['form_link', 'grammatical_feature_labels', 'statements'],
    'title-create': ['template_label'],
    'title-advanced': ['template_label'],
    'title-bulk': ['template_label'],
    'title-edit': ['template_label'],
    'login-hint': ['url'],
    'ambiguous-template': ['template_name', 'replacement_templates_count'],
}
lists = {
    'edit-form-list-item': {'grammatical_feature_labels'},
}
derived_messages = {
    'bulk-button': ('bulk-link', initial_titlecase),
    'bulk-heading': ('bulk-link', identity),
    'edit-button': ('edit-link', initial_titlecase),
}


def py2mw(py: str, variables: list[str], lists: set[str]) -> str:
    def replace(match: re.Match) -> str:
        nonlocal variables, lists
        inner = match[0][1:-1]  # strip away braces
        variable, _, rest = inner.partition('!')
        number = variables.index(variable) + 1
        if not rest:
            return f'${number}'
        conversion, _, format_spec = rest.partition(':')
        format_spec = format_spec.replace('{' + variable + '}', f'${number}')
        if conversion == 'p':
            args = []
            for plural in format_spec.split(':'):
                key, _, text = plural.partition('=')
                if key.isnumeric():
                    args.append(plural)
                else:
                    args.append(text)
            return '{{PLURAL:$' + str(number) + '|' + '|'.join(args) + '}}'
        elif conversion == 'g':
            args = []
            for replacement in format_spec.split(':'):
                gender, _, text = replacement.partition('=')
                args.append(text)
            return '{{GENDER:$' + str(number) + '|' + '|'.join(args) + '}}'
        elif conversion == 'l':
            assert variable in lists
            return f'${number}'
        elif conversion == 'h':
            return f'[${number} {format_spec}]'
        else:
            raise ValueError(f'Unknown conversion {conversion}')
    return re.sub(r'\{([^{}]|\{[^}]*\})*\}', replace, py)


def mw2py(mw: str, language: str, variables: list[str], lists: set[str]) -> str:
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
        if variable in lists:
            return '{' + variable + '!l}'
        else:
            return '{' + variable + '}'
    py = re.sub(r'\$([1-9][0-9]*)', replace_unconverted, py)
    return py


skipped_language_codes = {
    'anp',
    'ban',
    'io',
    'krc',
    'mrh',
    'pt-br',
    'qqq',
    'roa-tara',
    'sa',
    'xmf',
    'zh-hant',
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
        msg = mw2py(data[key], language, variables.get(key, []), lists.get(key, set()))
        translations[language][key] = msg
    for key in derived_messages:
        source_key, transformation = derived_messages[key]
        if source_key in translations[language]:
            translations[language][key] = transformation(translations[language][source_key])
