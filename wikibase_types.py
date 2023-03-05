from typing import Literal, TypedDict, Union
from typing_extensions import NotRequired


class Term(TypedDict):
    language: str
    value: str
    remove: NotRequired[Literal['']]  # only needed when editing


WikibaseEntityIdDataValueValue = TypedDict('WikibaseEntityIdDataValueValue', {
    'entity-type': Literal['item'],
    'id': str,
})


class WikibaseEntityIdDataValue(TypedDict):
    type: Literal['wikibase-entityid']
    value: WikibaseEntityIdDataValueValue


class PropertyValueSnak(TypedDict):
    snaktype: Literal['value']
    property: str
    datatype: Literal['wikibase-item']  # other data types not used in this tool
    datavalue: WikibaseEntityIdDataValue


class PropertySomeValueSnak(TypedDict):
    snaktype: Literal['somevalue']
    property: str
    datatype: Literal['wikibase-item']  # other data types not used in this tool
    # no datavalue


class PropertyNoValueSnak(TypedDict):
    snaktype: Literal['novalue']
    property: str
    datatype: Literal['wikibase-item']  # other data types not used in this tool
    # no datavalue


Snak = Union[PropertyValueSnak, PropertySomeValueSnak, PropertyNoValueSnak]


class Statement(TypedDict):
    mainsnak: Snak
    # qualifiers and references not used in this tool
    type: Literal['statement']
    rank: Literal['normal']  # other ranks not used in this tool


StatementGroup = list[Statement]
Statements = dict[str, StatementGroup]


LexemeFormRepresentations = dict[str, Term]
LexemeLemmas = dict[str, Term]


class LexemeForm(TypedDict):
    representations: LexemeFormRepresentations
    grammaticalFeatures: list[str]
    claims: Statements
    add: NotRequired[Literal['']]  # only needed when creating
    remove: NotRequired[Literal['']]  # only needed when editing
    id: NotRequired[Literal['']]  # only present when editing


class Lexeme(TypedDict):
    type: Literal['lexeme']
    lemmas: LexemeLemmas
    language: str
    lexicalCategory: str
    claims: Statements
    forms: list[LexemeForm]
    # senses not used in this tool
    id: NotRequired[str]  # only needed when editing
    base_revision_id: NotRequired[str]  # only needed when editing
    lastrevid: NotRequired[int]  # only available when data returned by API
