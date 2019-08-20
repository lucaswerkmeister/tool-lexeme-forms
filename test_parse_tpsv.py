import pytest

import parse_tpsv


@pytest.mark.parametrize('line, expected', [
    ('thing|things', ['thing', 'things']),
    ('thing\tthings', ['thing', 'things']),
    ('thing', ['thing']),
    ('thing|things\tthinges', ['thing', 'things', 'thinges']),
    (' thing    \t  things  ', ['thing', 'things']),
    ('thing||things', ['thing', '', 'things']),
    ('thing|', ['thing', '']),
    ('|things', ['', 'things']),
    ('', ['']), # this isn’t really legal but that should be a later error and still parse successfully
])
def test_parse_lexeme(line, expected):
    actual = parse_tpsv.parse_lexeme(line)
    assert expected == actual


def test_parse_lexemes():
    tpsv = '''
thing|things
entity|entities
object|objects
test|tests
'''.strip()
    assert parse_tpsv.parse_lexemes(tpsv) == [
        ['thing', 'things'],
        ['entity', 'entities'],
        ['object', 'objects'],
        ['test', 'tests'],
    ]

def test_parse_lexemes_skips_empty_lines():
    tpsv = '''

thing|things


entity|entities

'''
    assert parse_tpsv.parse_lexemes(tpsv) == [
        ['thing', 'things'],
        ['entity', 'entities'],
    ]

def test_parse_lexemes_supports_crlf():
    tpsv = '''thing|things\r\nentity|entities'''
    assert parse_tpsv.parse_lexemes(tpsv) == [
        ['thing', 'things'],
        ['entity', 'entities'],
    ]
