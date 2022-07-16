from typing import Literal, TypedDict


class Term(TypedDict):
    language: str
    value: str


Lemmas = dict[str, Term]


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
