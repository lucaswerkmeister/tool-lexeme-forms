"""Functions to parse lexeme form representations from tab/pipe-separated values syntax."""

import re
from typing import List
import werkzeug.datastructures


def parse_lexemes(tpsv: str, template: dict) -> List[werkzeug.datastructures.MultiDict]:
    lexemes = []
    for n, line in enumerate(tpsv.split('\n')):
        line = line.rstrip('\r')
        if not line:
            continue
        lexemes.append(parse_lexeme(line, template, line_number=n + 1))
    return lexemes


def parse_lexeme(line: str, template: dict, line_number: int) -> werkzeug.datastructures.MultiDict:
    fields = [field.strip() for field in line.replace('\t', '|').split('|')]
    if len(fields) == len(template['forms']) + 1:
        [lexeme_id, *form_representations] = fields
        if not re.fullmatch(r'L[1-9][0-9]*', lexeme_id):
            raise FirstFieldNotLexemeIdError(len(template['forms']), len(fields), lexeme_id, line_number)
        return werkzeug.datastructures.ImmutableMultiDict([
            ('lexeme_id', lexeme_id),
            *(('form_representation', form_representation) for form_representation in form_representations)])
    if len(fields) == len(template['forms']):
        form_representations = fields
        if re.fullmatch(r'L[1-9][0-9]*', form_representations[0]):
            raise FirstFieldLexemeIdError(len(template['forms']), len(fields), form_representations[0], line_number)
        return werkzeug.datastructures.ImmutableMultiDict(
            [('form_representation', form_representation) for form_representation in form_representations])
    raise WrongNumberOfFieldsError(len(template['forms']), len(fields), line_number)


class FirstFieldNotLexemeIdError(ValueError):
    """Error raised if there are n+1 fields but the first one is not a lexeme ID."""

    def __init__(self, num_forms: int, num_fields: int, first_field: str, line_number: int):
        assert num_fields == num_forms + 1
        self.num_forms = num_forms
        self.num_fields = num_fields
        self.first_field = first_field
        self.line_number = line_number
        super().__init__('n+1 fields but first field is not a lexeme ID')


class FirstFieldLexemeIdError(ValueError):
    """Error raised if there are n fields but the first one is a lexeme ID."""

    def __init__(self, num_forms: int, num_fields: int, first_field: str, line_number: int):
        assert num_fields == num_forms
        self.num_forms = num_forms
        self.num_fields = num_fields
        self.first_field = first_field
        self.line_number = line_number
        super().__init__('n fields but first field looks like a lexeme ID')


class WrongNumberOfFieldsError(ValueError):
    """Error raised if there are neither n nor n+1 fields."""

    def __init__(self, num_forms: int, num_fields: int, line_number: int):
        assert num_fields not in {num_forms, num_forms + 1}
        self.num_forms = num_forms
        self.num_fields = num_fields
        self.line_number = line_number
        super().__init__('neither n nor n+1 fields')
