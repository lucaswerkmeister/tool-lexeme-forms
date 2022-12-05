"""Module to convert between different kinds of language codes.

There are three kinds of language codes relevant for this tool:
- MediaWiki language codes
- HTML language codes (aka BCP47 language tags)
- Babel language codes

Additionally, MediaWiki language codes differ by usage between:
- lexicographical data language codes
- user interface language codes

Templates specify lexicographical data MediaWiki language codes;
translations are given for user interface language codes.

These language codes cannot be converted to one another losslessly,
and this module does not provide functions for all possible
conversions; rather, it only implements conversions to less specific
codes, which may lose some information."""


def lang_lex2int(code: str) -> str:
    """Convert a MediaWiki language code from lexicographical data usage
    to user interface usage."""

    return {
        # Manbhumi reuses the standard Bengali messages
        'bn-x-Q6747180': 'bn',
        # Hindko reuses the standard Punjabi messages
        'pnb-x-Q382273': 'pnb',
    }.get(code, code)


def lang_int2html(code: str) -> str:
    """Convert a MediaWiki user interface language code to an HTML one."""

    # no changes needed so far
    return code


def lang_int2babel(code: str) -> str:
    """Convert a MediaWiki user interface language code to a Babel one."""

    # remove everything after -, interpreted differently by Babel
    code, separator, rest = code.partition('-')
    return {
        # Latin and Venetian are not in CLDR, Italian is similar for our purposes
        'la': 'it',
        'vec': 'it',
        # pnb (Western Punjabi) is not in CLDR,
        # and its replacement lah (Lahnda) is not in Babel;
        # Urdu seems close for our purposes
        'pnb': 'ur',
        # Serbo-Croatian is not in CLDR, Croatian is closest for our purposes
        'sh': 'hr',
    }.get(code, code)
