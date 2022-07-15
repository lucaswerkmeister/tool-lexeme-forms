from typing import TypedDict


class Term(TypedDict):
    language: str
    value: str


Lemmas = dict[str, Term]
