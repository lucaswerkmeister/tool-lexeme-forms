import collections

templates = collections.OrderedDict([
    # template by Lucas Werkmeister
    ('german-noun-masculine', {
        'label': 'deutsches Substantiv (Maskulinum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist der [Hund].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum des [Hundes].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört dem [Hund].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag den [Hund].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind die [Hunde].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum der [Hunde].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört den [Hunden].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag die [Hunde].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q499327',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by Lucas Werkmeister
    ('german-noun-feminine', {
        'label': 'deutsches Substantiv (Femininum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist die [Katze].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum der [Katze].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört der [Katze].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag die [Katze].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind die [Katzen].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum der [Katzen].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört den [Katzen].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag die [Katzen].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1775415',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by Lucas Werkmeister
    ('german-noun-neuter', {
        'label': 'deutsches Substantiv (Neutrum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist das [Kind].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum des [Kindes].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört dem [Kind].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag das [Kind].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind die [Kinder].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum der [Kinder].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört den [Kindern].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag die [Kinder].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1775461',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by Lucas Werkmeister
    ('german-noun-pluraletantum', {
        'label': 'deutsches Substantiv (Pluraletantum, kein Genus)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind die [Großeltern].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum der [Großeltern].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört den [Großeltern].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag die [Großeltern].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
       ],
        'claims': {
            'P31': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P31',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q138246',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by Lucas Werkmeister
    ('english-noun', {
        'label': 'English noun',
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singular',
                'example': 'This is the [dog].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plural',
                'example': 'These are the [dogs].',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
    }),
    # template by Lucas Werkmeister
    ('latin-noun-masculine', {
        'label': 'nomen Latinum (masculinum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [puer].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [pueri].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativus singularis',
                'example': 'Pater [puero] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puella ad [puerum] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puella cum [puero] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
            },
            {
                'label': 'vocativus singularis',
                'example': 'Et tu, [puer]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [pueri].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [puerorum].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Pater [pueris] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puella ad [pueros] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puella cum [pueris] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q146786'],
            },
            {
                'label': 'vocativus pluralis',
                'example': 'Et vos, [pueri]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q499327',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by Lucas Werkmeister
    ('latin-noun-feminine', {
        'label': 'nomen Latinum (femininum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [puella].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [puellae].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativus singularis',
                'example': 'Mater [puellae] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puer ad [puellam] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puer cum [puella] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
            },
            {
                'label': 'vocativus singularis',
                'example': 'Et tu, [puella]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [puellae].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [puellarum].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Mater [puellis] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puer ad [puellas] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puer cum [puellis] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q146786'],
            },
            {
                'label': 'vocativus pluralis',
                'example': 'Et vos, [puellae]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1775415',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by Lucas Werkmeister
    ('latin-noun-neuter', {
        'label': 'nomen Latinum (neutrum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [forum].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [fori].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativus singularis',
                'example': 'Pater [foro] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puer ad [forum] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puer cum [foro] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
            },
            {
                'label': 'vocativus singularis',
                'example': 'Et tu, [forum]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [fora].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [fororum].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Pater [foris] favet.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puer ad [fora] adit.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puer cum [foris] ludet.',
                'grammatical_features_item_ids': ['Q156986', 'Q146786'],
            },
            {
                'label': 'vocativus pluralis',
                'example': 'Et vos, [fora]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
       ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1775461',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by User:KaMan, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Polish
    ('polish-noun', {
        'label': 'polski rzeczownik, prosta odmiana bez wariantów w żadnym z przypadków',
        'language_item_id': 'Q809',
        'language_code': 'pl',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Liczba pojedyncza, mianownik',
                'example': 'To jest [rzeczownik].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, dopełniacz',
                'example': 'Wśród nas nie ma [rzeczownika].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, celownik',
                'example': 'Przyglądam się [rzeczownikowi].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, biernik',
                'example': 'Widzę [rzeczownik].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, narzędnik',
                'example': 'Idę z [rzeczownikiem].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, miejscownik',
                'example': 'Myślę o [rzeczowniku].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, wołacz',
                'example': '[rzeczowniku]',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'Liczba mnoga, mianownik',
                'example': 'To są [rzeczowniki].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, dopełniacz',
                'example': 'Wśród nas nie ma [rzeczowników].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, celownik',
                'example': 'Przyglądam się [rzeczownikom].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, biernik',
                'example': 'Widzę [rzeczowniki].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, narzędnik',
                'example': 'Idę z [rzeczownikami].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, miejscownik',
                'example': 'Myślę o [rzeczownikach].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, wołacz',
                'example': '[rzeczowniki]',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
        ],
    }),
    # template by User:KaMan, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Polish
    ('polish-noun-masculine-personal-with-depreciative-forms', {
        'label': 'polski rzeczownik, rodzaj męskoosobowy z formami ndepr. i depr. w M. i W. lm',
        'language_item_id': 'Q809',
        'language_code': 'pl',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'mianownik, liczba pojedyncza',
                'example': 'To jest [robotnik].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'dopełniacz, liczba pojedyncza',
                'example': 'Wśród nas nie ma [robotnika].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'celownik, liczba pojedyncza',
                'example': 'Przyglądam się [robotnikowi].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'biernik, liczba pojedyncza',
                'example': 'Widzę [robotnika].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'narzędnik, liczba pojedyncza',
                'example': 'Idę z [robotnikiem].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'miejscownik, liczba pojedyncza',
                'example': 'Myślę o [robotniku].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': 'wołacz, liczba pojedyncza',
                'example': '[robotniku]',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'mianownik, liczba mnoga, forma niedeprecjatywna',
                'example': 'To są ci [robotnicy].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54948995',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'mianownik, liczba mnoga, forma deprecjatywna',
                'example': 'To są te [robotniki].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54948374',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'dopełniacz, liczba mnoga',
                'example': 'Wśród nas nie ma [robotników].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'celownik, liczba mnoga',
                'example': 'Przyglądam się [robotnikom].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'biernik, liczba mnoga',
                'example': 'Widzę [robotników].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'narzędnik, liczba mnoga',
                'example': 'Idę z [robotnikami].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'miejscownik, liczba mnoga',
                'example': 'Myślę o [robotnikach].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': 'wołacz, liczba mnoga, forma niedeprecjatywna',
                'example': 'ci [robotnicy]',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54948995',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'wołacz, liczba mnoga, forma deprecjatywna',
                'example': 'te [robotniki]',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54948374',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
        ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q27918551',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by User:KaMan, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Polish
    ('polish-noun-with-potential-plural-forms', {
        'label': 'polski rzeczownik, potencjalna liczba mnoga',
        'language_item_id': 'Q809',
        'language_code': 'pl',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'mianownik, liczba pojedyncza',
                'example': 'To jest [językoznawstwo].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'dopełniacz, liczba pojedyncza',
                'example': 'Wśród nas nie ma [językoznawstwa].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'celownik, liczba pojedyncza',
                'example': 'Przyglądam się [językoznawstwu].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'biernik, liczba pojedyncza',
                'example': 'Widzę [językoznawstwo].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'narzędnik, liczba pojedyncza',
                'example': 'Idę z [językoznawstwem].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'miejscownik, liczba pojedyncza',
                'example': 'Myślę o [językoznawstwie].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': 'wołacz, liczba pojedyncza',
                'example': '[językoznawstwo]',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'mianownik, liczba mnoga, forma potencjalna',
                'example': 'To są [językoznawstwa].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54944750',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'dopełniacz, liczba mnoga, forma potencjalna',
                'example': 'Wśród nas nie ma [językoznawstw].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54944750',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'celownik, liczba mnoga, forma potencjalna',
                'example': 'Przyglądam się [językoznawstwom].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54944750',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'biernik, liczba mnoga, forma potencjalna',
                'example': 'Widzę [językoznawstwa].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54944750',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'narzędnik, liczba mnoga, forma potencjalna',
                'example': 'Idę z [językoznawstwami].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54944750',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'miejscownik, liczba mnoga, forma potencjalna',
                'example': 'Myślę o [językoznawstwach].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54944750',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
            {
                'label': 'wołacz, liczba mnoga, forma potencjalna',
                'example': '[językoznawstwa]',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
                'claims': {
                    'P31': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P31',
                                'datatype': 'wikibase-item',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q54944750',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ]
                },
            },
        ],
    }),
    # template by Lucas Werkmeister
    ('german-noun-neuter-test', {
        'test': True,
        'label': 'deutsches Substantiv (Neutrum), test.wikidata.org',
        'language_item_id': 'Q348',
        'language_code': 'de',
        'lexical_category_item_id': 'Q92595',
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist das [Kind].',
                'grammatical_features_item_ids': ['Q163012', 'Q163014'],
                'claims': {
                    'P82': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P82',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q1249',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ],
                },
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum des [Kindes].',
                'grammatical_features_item_ids': ['Q163013', 'Q163014'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört dem [Kind].',
                'grammatical_features_item_ids': ['Q163016', 'Q163014'],
                'claims': {
                    'P82': [
                        {
                            'mainsnak': {
                                'snaktype': 'value',
                                'property': 'P82',
                                'datavalue': {
                                    'type': 'wikibase-entityid',
                                    'value': {
                                        'entity-type': 'item',
                                        'id': 'Q74568',
                                    },
                                },
                            },
                            'type': 'statement',
                            'rank': 'normal',
                        }
                    ],
                },
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag das [Kind].',
                'grammatical_features_item_ids': ['Q163017', 'Q163014'],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind die [Kinder].',
                'grammatical_features_item_ids': ['Q163012', 'Q160570'],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum der [Kinder].',
                'grammatical_features_item_ids': ['Q163013', 'Q160570'],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört den [Kindern].',
                'grammatical_features_item_ids': ['Q163016', 'Q160570'],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag die [Kinder].',
                'grammatical_features_item_ids': ['Q163017', 'Q160570'],
            },
        ],
        'claims': {
            'P73601': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P73601',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q163008',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
])
