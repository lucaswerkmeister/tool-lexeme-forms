"""Functions to parse lexeme form representations from tab/pipe-separated values syntax."""

from typing import List


def parse_lexemes(tpsv: str) -> List[List[str]]:
    lexemes = []
    for line in tpsv.split('\n'):
        line = line.rstrip('\r')
        if not line:
            continue
        lexemes.append(parse_lexeme(line))
    if len(set(len(lexeme) for lexeme in lexemes)) > 1:
        raise ValueError('Inconsistent lengths for different lines!')
    return lexemes


def parse_lexeme(line: str) -> List[str]:
    return [form_representation.strip() for form_representation in line.replace('\t', '|').split('|')]
