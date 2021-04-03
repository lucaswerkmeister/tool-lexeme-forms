import pytest
from werkzeug.datastructures import ImmutableMultiDict

import parse_tpsv


@pytest.mark.parametrize('line, expected_representations', [
    ('thing|things', ['thing', 'things']),
    ('thing\tthings', ['thing', 'things']),
    (' thing    \t  things  ', ['thing', 'things']),
    ('thing|', ['thing', '']),
    ('|things', ['', 'things']),
])
def test_parse_lexeme_two_forms_no_lexeme_id(line, expected_representations):
    template = {'forms': [{}, {}]}
    actual_data = parse_tpsv.parse_lexeme(line, template, 1)
    actual_representations = actual_data.getlist('form_representation')
    assert expected_representations == actual_representations


@pytest.mark.parametrize('line, expected_representations', [
    ('thing|things\tthinges', ['thing', 'things', 'thinges']),
    ('thing||things', ['thing', '', 'things']),
])
def test_parse_lexeme_three_forms_no_lexeme_id(line, expected_representations):
    template = {'forms': [{}, {}, {}]}
    actual_data = parse_tpsv.parse_lexeme(line, template, 1)
    actual_representations = actual_data.getlist('form_representation')
    assert expected_representations == actual_representations


@pytest.mark.parametrize('line, expected_lexeme_id, expected_representations', [
    ('L123|thing|things', 'L123', ['thing', 'things']),
    ('L123\tthing\tthings', 'L123', ['thing', 'things']),
])
def test_parse_lexeme_two_forms_lexeme_id(line, expected_lexeme_id, expected_representations):
    template = {'forms': [{}, {}]}
    actual_data = parse_tpsv.parse_lexeme(line, template, 1)
    [actual_lexeme_id] = actual_data.getlist('lexeme_id')  # unpack + getlist guards against extra lexeme IDs
    actual_representations = actual_data.getlist('form_representation')
    assert expected_lexeme_id == actual_lexeme_id
    assert expected_representations == actual_representations


def test_parse_lexemes():
    tpsv = '''
thing|things

\r

L123|entity|entities
'''.strip()
    assert parse_tpsv.parse_lexemes(tpsv, {'forms': [{}, {}]}) == [
        ImmutableMultiDict([
            ('form_representation', 'thing'),
            ('form_representation', 'things'),
        ]),
        ImmutableMultiDict([
            ('lexeme_id', 'L123'),
            ('form_representation', 'entity'),
            ('form_representation', 'entities'),
        ]),
    ]


def test_parse_lexemes_FirstFieldNotLexemeIdError():
    tpsv = 'object|objects\nthing|things|thingies'
    with pytest.raises(parse_tpsv.FirstFieldNotLexemeIdError) as exc_info:
        parse_tpsv.parse_lexemes(tpsv, {'forms': [{}, {}]})
    assert exc_info.value.num_forms == 2
    assert exc_info.value.num_fields == 3
    assert exc_info.value.first_field == 'thing'
    assert exc_info.value.line_number == 2


def test_parse_lexemes_FirstFieldLexemeIdError():
    tpsv = 'object|objects\nL123|things'
    with pytest.raises(parse_tpsv.FirstFieldLexemeIdError) as exc_info:
        parse_tpsv.parse_lexemes(tpsv, {'forms': [{}, {}]})
    assert exc_info.value.num_forms == 2
    assert exc_info.value.num_fields == 2
    assert exc_info.value.first_field == 'L123'
    assert exc_info.value.line_number == 2


def test_parse_lexemes_WrongNumberOfFieldsError():
    tpsv = 'object|objects\nthing'
    with pytest.raises(parse_tpsv.WrongNumberOfFieldsError) as exc_info:
        parse_tpsv.parse_lexemes(tpsv, {'forms': [{}, {}]})
    assert exc_info.value.num_forms == 2
    assert exc_info.value.num_fields == 1
    assert exc_info.value.line_number == 2
