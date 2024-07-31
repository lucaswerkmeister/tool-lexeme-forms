from language import lang_int2babel
from toolforge_i18n import TranslationsConfig


def _initial_titlecase(s: str) -> str:
    return s[:1].title() + s[1:]


def _identity(s: str) -> str:
    return s


_variables = {
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


_derived_messages = {
    'bulk-button': ('bulk-link', _initial_titlecase),
    'bulk-heading': ('bulk-link', _identity),
    'edit-button': ('edit-link', _initial_titlecase),
}


config = TranslationsConfig(
    variables=_variables,
    derived_messages=_derived_messages,
    language_code_to_babel=lang_int2babel,
    check_translations=False,
)
