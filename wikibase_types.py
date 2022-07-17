from typing import Literal, TypedDict


class Term(TypedDict):
    language: str
    value: str


WikibaseEntityIdDataValueValue = TypedDict('WikibaseEntityIdDataValueValue', {
    'entity-type': Literal['item'],
    'id': str,
})


class WikibaseEntityIdDataValue(TypedDict):
    type: Literal['wikibase-entityid']
    value: WikibaseEntityIdDataValueValue


class Snak(TypedDict):
    snaktype: Literal['value']  # other snak types not used in this tool
    property: str
    datatype: Literal['wikibase-item']  # other data types not used in this tool
    datavalue: WikibaseEntityIdDataValue


class Statement(TypedDict):
    mainsnak: Snak
    # qualifiers and references not used in this tool
    type: Literal['statement']
    rank: Literal['normal']  # other ranks not used in this tool


StatementGroup = list[Statement]
Statements = dict[str, StatementGroup]


LexemeFormRepresentations = dict[str, Term]
LexemeLemmas = dict[str, Term]


class CoreLexemeForm(TypedDict):
    representations: LexemeFormRepresentations
    grammaticalFeatures: list[str]
    claims: Statements


class LexemeForm(CoreLexemeForm, total=False):
    add: Literal['']  # only needed when creating
    remove: Literal['']  # only needed when editing


class CoreLexeme(TypedDict):
    type: Literal['lexeme']
    lemmas: LexemeLemmas
    language: str
    lexicalCategory: str
    claims: Statements
    forms: list[LexemeForm]
    # senses not used in this tool


class Lexeme(CoreLexeme, total=False):
    id: str  # only needed when editing
    base_revision_id: str  # only needed when editing
