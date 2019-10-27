"""Functions to parse lexeme form representations from tab/pipe-separated values syntax."""

import re
from typing import List
import werkzeug.datastructures


def parse_lexemes(tpsv: str, template: dict) -> List[werkzeug.datastructures.MultiDict]:
    lexemes = []
    for line in tpsv.split('\n'):
        line = line.rstrip('\r')
        if not line:
            continue
        lexemes.append(parse_lexeme(line, template))
    return lexemes


def parse_lexeme(line: str, template: dict) -> werkzeug.datastructures.MultiDict:
    fields = [field.strip() for field in line.replace('\t', '|').split('|')]
    if len(fields) == len(template['forms']) + 1:
        [lexeme_id, *form_representations] = fields
        if not re.fullmatch(r'L[1-9][0-9]*', lexeme_id):
            raise ValueError('n+1 fields but first field is not a lexeme ID')
        return werkzeug.datastructures.ImmutableMultiDict([
            ('lexeme_id', lexeme_id),
            *(('form_representation', form_representation) for form_representation in form_representations)])
    if len(fields) == len(template['forms']):
        form_representations = fields
        if re.fullmatch(r'L[1-9][0-9]*', form_representations[0]):
            raise ValueError('n fields but first field looks like a lexeme ID')
        return werkzeug.datastructures.ImmutableMultiDict(
            [('form_representation', form_representation) for form_representation in form_representations])
    raise ValueError('neither n nor n+1 fields')
