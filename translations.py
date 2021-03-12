import babel
import json
import os
import re


def initial_titlecase(s):
    return s[:1].title() + s[1:]


def identity(s):
    return s


variables = {
    'duplicates_warning': ['lexemes'],
    'duplicates_instructions': ['lexemes'],
    'description_with_forms_and_senses': ['description', 'forms', 'senses'],
    'bulk_not_allowed': ['user'],
    'edit_ambiguous_warning': ['forms'],
    'edit_unmatched_warning': ['forms'],
    'edit_form_list_item': ['form_link', 'grammatical_feature_labels', 'statements'],
}
lists = {
    'edit_form_list_item': {'grammatical_feature_labels'},
}
derived_messages = {
    'bulk_button': ('bulk_link', initial_titlecase),
    'bulk_heading': ('bulk_link', identity),
    'edit_button': ('edit_link', initial_titlecase),
}


def py2mw(py, variables, lists):
    def replace(match):
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
        else:
            raise ValueError(f'Unknown conversion {conversion}')
    return re.sub(r'\{([^{}]|\{[^}]*\})*\}', replace, py)


def mw2py(mw, language, variables, lists):
    if language == 'la':
        language = 'en'  # Latin is not in CLDR, English has same plural forms
    locale = babel.Locale(language)

    def replace_plural(match):
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

    def replace_gender(match):
        nonlocal variables
        number = int(match[1])
        variable = variables[number - 1]
        args = match[2].split('|')
        genders = []
        for gender, arg in zip(['m', 'f', 'n'], args):
            genders.append(f'{gender}={arg}')
        return '{' + variable + '!g:' + ':'.join(genders) + '}'
    py = re.sub(r'\{\{GENDER:\$([1-9][0-9]*)\|([^}]*)\}\}', replace_gender, py)

    def replace_unconverted(match):
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
    'pt-br',
    'qqq',
    'sa',
    'zh-hant',
}


translations = {}
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
    for key_json in data:
        if key_json.startswith('@'):
            continue
        key_py = key_json.replace('-', '_')
        msg = mw2py(data[key_json], language, variables.get(key_py, []), lists.get(key_py, set()))
        translations[language][key_py] = msg
    for key_py in derived_messages:
        source_key_py, transformation = derived_messages[key_py]
        if source_key_py in translations[language]:
            translations[language][key_py] = transformation(translations[language][source_key_py])
