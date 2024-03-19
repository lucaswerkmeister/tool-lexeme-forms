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
codes, which may lose some information. (The conversion from
MediaWiki language codes to HTML language codes, previously called
lang_int2html() in this module, is now bcp47() and lives in
toolforge_i18n.language_info.)"""


def lang_lex2int(code: str) -> str:
    """Convert a MediaWiki language code from lexicographical data usage
    to user interface usage."""

    return {
        # Manbhumi reuses the standard Bengali messages
        'bn-x-Q6747180': 'bn',
    }.get(code, code)


def lang_int2babel(code: str) -> str:
    """Convert a MediaWiki user interface language code to a Babel one."""

    # remove everything after -, interpreted differently by Babel
    code, separator, rest = code.partition('-')
    return {
        # Latin and Venetian are not in CLDR, Italian is similar for our purposes
        'la': 'it',
        'vec': 'it',
        # pnb (Western Punjabi) is represented in Babel
        # as pa_Arab (Punjabi in Arabic script);
        # its replacement lah (Lahnda) is not in Babel
        'pnb': 'pa_Arab',
        # Serbo-Croatian is not in CLDR, Croatian is closest for our purposes
        'sh': 'hr',
        # hno (Hindko) is not in Babel, nor is lah (Lahnda);
        # use pa_Arab just like for pnb (Western Punjabi) above,
        # as pnb is said to be mutually intellegible (https://w.wiki/6Nu7)
        'hno': 'pa_Arab',
        # anp (Angika) is not in Babel;
        # hi (Hindi) is the MediaWiki fallback
        'anp': 'hi',
        # ban (Balinese) is not in Babel;
        # id (Indonesian) is the MediaWiki fallback
        'ban': 'id',
        # io (Ido) is not in CLDR;
        # eo (Esperanto) is the MediaWiki fallback
        'io': 'eo',
        # krc (Karachay-Balkar) is not in Babel;
        # ru (Russian) is the MediaWiki fallback
        'krc': 'ru',
        # mrh (Mara) is not in CLDR;
        # MediaWiki has no fallback, so I assume reusing plurals etc. from English is okay
        'mrh': 'en',
        # roa-tara (tarandíne) is not in CLDR;
        # it (Italian) is the MediaWiki fallback
        'roa': 'it',
        # xmf (Mingrelian) is not in Babel;
        # ka (Georgian) is the MediaWiki fallback
        'xmf': 'ka',
        # skr-arab (Saraiki) is not in Babel;
        # ur (Urdu) is the MediaWiki fallback and its .text_direction matches
        'skr': 'ur',
        # ba (Bashkir) is not in Babel;
        # tt (Tatar) is closely related, has the same plural forms,
        # and its list formatting seems to match ba better than MediaWiki’s ba fallback ru (Russian)
        'ba': 'tt',
        # kai (Karai-Karai or Karekare) is not in Babel;
        # MediaWiki support is still in progress (T345807),
        # so the fallback to ha (Hausa) here is just a total guess
        # based on both languages being West Chadic according to Wikipedia
        'kai': 'ha',
        # an (Aragonese) is not in Babel;
        # es (Spanish) is the MediaWiki fallback its .text_direction matches
        'an': 'es',
        # kaa (Karakalpak) is not in Babel;
        # kk (Kazakh) is the closest match for MediaWiki’s first fallback,
        # kk-latn (Kazahn in Latin script – Babel’s kk being in Cyrillic);
        # we should change this to kk_Latn or kaa as soon as Babel lets us!
        'kaa': 'kk',
        # ht (Haitian Creole) is Babel;
        # fr (French) the MediaWiki fallback
        'ht': 'fr',
    }.get(code, code)
