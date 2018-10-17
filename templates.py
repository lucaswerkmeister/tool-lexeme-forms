import collections

templates = collections.OrderedDict([
    # template by User:Oriciu, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Asturian
    ('asturian-noun-masculine', {
        'label': 'nome común masculín asturianu',
        'language_item_id': 'Q29507',
        'language_code': 'ast',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singular',
                'example': 'Esti ye un [perru].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plural',
                'example': 'Estos son unos [perros].',
                'grammatical_features_item_ids': ['Q146786'],
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
    # template by User:Oriciu, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Asturian
    ('asturian-noun-feminine', {
        'label': 'nome común femenín asturianu',
        'language_item_id': 'Q29507',
        'language_code': 'ast',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singular',
                'example': 'Esta ye una [perra].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plural',
                'example': 'Estes son unes [perres].',
                'grammatical_features_item_ids': ['Q146786'],
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
    # template by User:Lexicolover, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Czech
    ('czech-noun-masculine-animate', {
        'label': 'České podstatné jméno (rod mužský životný)',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': '1. pád, jednotné číslo',
                'example': 'To je můj [pes].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': '2. pád, jednotné číslo',
                'example': 'Má strach z mého [psa].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': '3. pád, jednotné číslo',
                'example': 'Dej to mému [psu/psovi].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': '4. pád, jednotné číslo',
                'example': 'Vidím jednoho [psa].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': '5. pád, jednotné číslo',
                'example': 'Kam kráčíš, [pse]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': '6. pád, jednotné číslo',
                'example': 'Pověz mi něco o tvém [psu/psovi].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': '7. pád, jednotné číslo',
                'example': 'Seznámil jsem se s tvým [psem].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': '1. pád, množné číslo',
                'example': 'To jsou moji [psi/psové].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': '2. pád, množné číslo',
                'example': 'Má strach z mých [psů].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': '3. pád, množné číslo',
                'example': 'Dej to mým [psům].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': '4. pád, množné číslo',
                'example': 'Vidím dva [psy].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': '5. pád, množné číslo',
                'example': 'Kam kráčíte, [psi/psové]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
            {
                'label': '6. pád, množné číslo',
                'example': 'Pověz mi něco o tvých [psech].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': '7. pád, množné číslo',
                'example': 'Seznámil jsem se s tvými [psy].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
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
                },
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q54020116',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by User:Lexicolover, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Czech
    ('czech-noun-masculine-inanimate', {
        'label': 'České podstatné jméno (rod mužský neživotný)',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': '1. pád, jednotné číslo',
                'example': 'To je můj [hrad].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': '2. pád, jednotné číslo',
                'example': 'Má strach z mého [hradu].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': '3. pád, jednotné číslo',
                'example': 'Dej to k mému [hradu].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': '4. pád, jednotné číslo',
                'example': 'Vidím jeden [hrad].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': '5. pád, jednotné číslo',
                'example': 'Kam směřuješ, [hrade]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': '6. pád, jednotné číslo',
                'example': 'Pověz mi něco o svém [hradu/hradě].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': '7. pád, jednotné číslo',
                'example': 'Seznámil jsem se s tvým [hradem].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': '1. pád, množné číslo',
                'example': 'To jsou mé [hrady].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': '2. pád, množné číslo',
                'example': 'Má strach z mých [hradů].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': '3. pád, množné číslo',
                'example': 'Dej to k mým [hradům].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': '4. pád, množné číslo',
                'example': 'Vidím dva [hrady].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': '5. pád, množné číslo',
                'example': 'Kam směřujete, [hrady]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
            {
                'label': '6. pád, množné číslo',
                'example': 'Pověz mi něco o svých [hradech].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': '7. pád, množné číslo',
                'example': 'Seznámil jsem se s tvými [hrady].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
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
                },
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P5185',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q54020181',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),
    # template by User:Lexicolover, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Czech
    ('czech-noun-feminine', {
        'label': 'České podstatné jméno (rod ženský)',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': '1. pád, jednotné číslo',
                'example': 'To je má [žena].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': '2. pád, jednotné číslo',
                'example': 'Má strach z mé [ženy].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': '3. pád, jednotné číslo',
                'example': 'Dej to mé [ženě].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': '4. pád, jednotné číslo',
                'example': 'Vidím jednu [ženu].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': '5. pád, jednotné číslo',
                'example': 'Kam kráčíš, [ženo]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': '6. pád, jednotné číslo',
                'example': 'Pověz mi něco o tvé [ženě].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': '7. pád, jednotné číslo',
                'example': 'Seznámil jsem se s tvou [ženou].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': '1. pád, množné číslo',
                'example': 'To jsou mé [ženy].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': '2. pád, množné číslo',
                'example': 'Má strach z mých [žen].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': '3. pád, množné číslo',
                'example': 'Dej to mým [ženám].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': '4. pád, množné číslo',
                'example': 'Vidím dvě [ženy].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': '5. pád, množné číslo',
                'example': 'Kam kráčíte, [ženy]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
            {
                'label': '6. pád, množné číslo',
                'example': 'Pověz mi něco o tvých [ženách].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': '7. pád, množné číslo',
                'example': 'Seznámil jsem se s tvými [ženami].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
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
    # template by User:Lexicolover, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Czech
    ('czech-noun-neuter', {
        'label': 'České podstatné jméno (rod střední)',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': '1. pád, jednotné číslo',
                'example': 'To je mé [kuře].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': '2. pád, jednotné číslo',
                'example': 'Má strach z mého [kuřete].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': '3. pád, jednotné číslo',
                'example': 'Dej to mému [kuřeti].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': '4. pád, jednotné číslo',
                'example': 'Vidím jedno [kuře].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': '5. pád, jednotné číslo',
                'example': 'Kam kráčíš, [kuře]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': '6. pád, jednotné číslo',
                'example': 'Pověz mi něco o tvém [kuřeti].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': '7. pád, jednotné číslo',
                'example': 'Seznámil jsem se s tvým [kuřetem].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': '1. pád, množné číslo',
                'example': 'To jsou má [kuřata].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': '2. pád, množné číslo',
                'example': 'Má strach z mých [kuřat].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': '3. pád, množné číslo',
                'example': 'Dej to mým [kuřatům].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': '4. pád, množné číslo',
                'example': 'Vidím dvě [kuřata].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': '5. pád, množné číslo',
                'example': 'Kam kráčíte, [kuřata]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
            {
                'label': '6. pád, množné číslo',
                'example': 'Pověz mi něco o tvých [kuřatech].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': '7. pád, množné číslo',
                'example': 'Seznámil jsem se s tvými [kuřaty].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
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
    # template by User:Lexicolover, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Czech
    ('czech-adverb', {
        'label': 'České příslovce',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'pozitiv (1. stupeň)',
                'example': 'Udělal jsi to [dobře].',
                'grammatical_features_item_ids': ['Q3482678'],
            },
            {
                'label': 'komparativ (2. stupeň)',
                'example': 'Udělal jsi to [lépe] než já.',
                'grammatical_features_item_ids': ['Q14169499'],
            },
            {
                'label': 'superlativ (3. stupeň)',
                'example': 'Udělal jsi to ze všech [nejlépe].',
                'grammatical_features_item_ids': ['Q1817208'],
            },
        ],
    }),
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
                'example': 'Das Eigentum des [Hunds/Hundes].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört dem [Hund/Hunde].',
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
                'example': 'Das Eigentum des [Kindes/Kinds].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört dem [Kind/Kinde].',
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
    ('german-verb', {
        'label': 'deutsches Verb',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'Infinitiv',
                'example': '[tragen]',
                'grammatical_features_item_ids': ['Q179230'],
            },
            {
                'label': '1. Person Singular Präsens',
                'example': 'Ich [trage] heute.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q682111', 'Q192613', 'Q1317831'],
            },
            {
                'label': '2. Person Singular Präsens',
                'example': 'Du [trägst] heute.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q682111', 'Q192613', 'Q1317831'],
            },
            {
                'label': '3. Person Singular Präsens',
                'example': 'Er/sie/es [trägt] heute.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q682111', 'Q192613', 'Q1317831'],
            },
            {
                'label': '1. Person Plural Präsens',
                'example': 'Wir [tragen] heute.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q682111', 'Q192613', 'Q1317831'],
            },
            {
                'label': '2. Person Plural Präsens',
                'example': 'Ihr [tragt] heute.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q682111', 'Q192613', 'Q1317831'],
            },
            {
                'label': '3. Person Plural Präsens',
                'example': 'Sie [tragen] heute.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q682111', 'Q192613', 'Q1317831'],
            },
            {
                'label': '1. Person Singular Präteritum',
                'example': 'Ich [trug] gestern.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q682111', 'Q442485', 'Q1317831'],
            },
            {
                'label': '2. Person Singular Präteritum',
                'example': 'Du [trugst] gestern.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q682111', 'Q442485', 'Q1317831'],
            },
            {
                'label': '3. Person Singular Präteritum',
                'example': 'Er/sie/es [trug] gestern.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q682111', 'Q442485', 'Q1317831'],
            },
            {
                'label': '1. Person Plural Präteritum',
                'example': 'Wir [trugen] gestern.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q682111', 'Q442485', 'Q1317831'],
            },
            {
                'label': '2. Person Plural Präteritum',
                'example': 'Ihr [trugt] gestern.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q682111', 'Q442485', 'Q1317831'],
            },
            {
                'label': '3. Person Plural Präteritum',
                'example': 'Sie [trugen] gestern.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q682111', 'Q442485', 'Q1317831'],
            },
            {
                'label': '1. Person Singular Konjunktiv I',
                'example': 'Angenommen, ich [trage].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q55685962', 'Q192613', 'Q1317831'],
            },
            {
                'label': '2. Person Singular Konjunktiv I',
                'example': 'Angenommen, du [tragest].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q55685962', 'Q192613', 'Q1317831'],
            },
            {
                'label': '3. Person Singular Konjunktiv I',
                'example': 'Angenommen, er/sie/es [trage].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q55685962', 'Q192613', 'Q1317831'],
            },
            {
                'label': '1. Person Plural Konjunktiv I',
                'example': 'Angenommen, wir [tragen].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q55685962', 'Q192613', 'Q1317831'],
            },
            {
                'label': '2. Person Plural Konjunktiv I',
                'example': 'Angenommen, ihr [traget].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q55685962', 'Q192613', 'Q1317831'],
            },
            {
                'label': '3. Person Plural Konjunktiv I',
                'example': 'Angenommen, sie [tragen].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q55685962', 'Q192613', 'Q1317831'],
            },
            {
                'label': '1. Person Singular Konjunktiv II',
                'example': 'Ich dachte, ich [trüge].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q54671845', 'Q442485', 'Q1317831'],
            },
            {
                'label': '2. Person Singular Konjunktiv II',
                'example': 'Ich dachte, du [trügest/trügst].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q54671845', 'Q442485', 'Q1317831'],
            },
            {
                'label': '3. Person Singular Konjunktiv II',
                'example': 'Ich dachte, er/sie/es [trüge].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q54671845', 'Q442485', 'Q1317831'],
            },
            {
                'label': '1. Person Plural Konjunktiv II',
                'example': 'Ich dachte, wir [trügen].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q54671845', 'Q442485', 'Q1317831'],
            },
            {
                'label': '2. Person Plural Konjunktiv II',
                'example': 'Ich dachte, ihr [trüget/trügt].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q54671845', 'Q442485', 'Q1317831'],
            },
            {
                'label': '3. Person Plural Konjunktiv II',
                'example': 'Ich dachte, sie [trügen].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q54671845', 'Q442485', 'Q1317831'],
            },
            {
                'label': '2. Person Singular Imperativ',
                'example': 'He du da, [trag/trage]!',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q22716', 'Q192613', 'Q1317831'],
            },
            {
                'label': '2. Person Plural Imperativ',
                'example': 'He ihr da, [tragt]!',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q22716', 'Q192613', 'Q1317831'],
            },
            {
                'label': 'Partizip II',
                'example': 'Ich werde [getragen].',
                'grammatical_features_item_ids': ['Q1230649'],
            },
        ],
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
    # template by User:ArthurPSmith, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/English
    ('english-adverb', {
        'label': 'English adverb',
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'lexeme',
                'example': 'We walked [slowly].',
                'grammatical_features_item_ids': [],
            },
        ],
    }),
    # template by User:ArthurPSmith, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/English
    ('english-adjective', {
        'label': 'English adjective',
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'positive',
                'example': 'This is a [good] dog.',
                'grammatical_features_item_ids': ['Q3482678'],
            },
            {
                'label': 'comparative',
                'example': 'This is a [better] dog than yours.',
                'grammatical_features_item_ids': ['Q14169499'],
            },
            {
                'label': 'superlative',
                'example': 'This is the [best] dog I\'ve ever seen.',
                'grammatical_features_item_ids': ['Q1817208'],
            },
        ],
    }),
    # template by User:ArthurPSmith, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/English
    ('english-verb', {
        'label': 'English verb',
        'language_item_id': 'Q1860',
        'language_code': 'en',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'present',
                'example': 'They [sing] every day.',
                'grammatical_features_item_ids': ['Q3910936'],
            },
            {
                'label': 'third-person singular',
                'example': 'He [sings] every day.',
                'grammatical_features_item_ids': ['Q3910936', 'Q51929447'],
            },
            {
                'label': 'simple past',
                'example': 'He [sang] every day last week.',
                'grammatical_features_item_ids': ['Q1392475'],
            },
            {
                'label': 'present participle',
                'example': 'They are [singing] right now.',
                'grammatical_features_item_ids': ['Q10345583'],
            },
            {
                'label': 'past participle',
                'example': 'We have [sung] for hours.',
                'grammatical_features_item_ids': ['Q1230649'],
            },
        ],
    }),
    # template by User:KaMan and User:Jens Ohlig, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Esperanto
    ('esperanto-noun', {
        'label': 'esperanta substantivo',
        'language_item_id': 'Q143',
        'language_code': 'eo',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ununombro, nominativo',
                'example': 'Ĉi tio estas [substantivo].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'ununombro, akuzativo',
                'example': 'Mi ŝatas tiun [substantivon].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'multenombro, nominativo',
                'example': 'Ĉi tiuj estas [substantivoj].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'multenombro, akuzativo',
                'example': 'Mi ŝatas tiujn [substantivojn].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
        ],
    }),
    # template by User:Andreasmperu, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Spanish
    ('spanish-noun-masculine', {
        'label': "sustantivo masculino en español",
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': "singular",
                'example': 'Este es un [libro].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plural',
                'example': 'Estos son unos [libros].',
                'grammatical_features_item_ids': ['Q146786'],
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
    # template by User:Andreasmperu, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Spanish
    ('spanish-noun-feminine', {
        'label': "sustantivo femenino en español",
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': "singular",
                'example': 'Esta es una [manzana].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plural',
                'example': 'Estas son unas [manzanas].',
                'grammatical_features_item_ids': ['Q146786'],
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
    # template by User:Andreasmperu, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Spanish
    ('spanish-adjective', {
        'label': "adjetivo en español",
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'masculino singular',
                'example': 'Un pantalón [negro].',
                'grammatical_features_item_ids': ['Q499327', 'Q110786'],
            },
            {
                'label': 'masculino plural',
                'example': 'Unos pantalones [negros].',
                'grammatical_features_item_ids': ['Q499327', 'Q146786'],
            },
            {
                'label': 'femenino singular',
                'example': 'Una falda [negra].',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786'],
            },
            {
                'label': 'femenino plural',
                'example': 'Unas faldas [negras].',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786'],
            },
        ],
    }),
    # template by User:Reosarevok, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Estonian
    ('estonian-noun', {
        'label':     "eesti keele nimisõna",
        'language_item_id': 'Q9072',
        'language_code': 'et',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ainsuse nimetav',
                'example': 'See [auto].',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'mitmuse nimetav',
                'example': 'Need [autod].',
                'grammatical_features_item_ids': ['Q146786', 'Q131105'],
            },
            {
                'label': 'ainsuse omastav',
                'example': 'Selle [auto].',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'mitmuse omastav',
                'example': 'Nende [autode].',
                'grammatical_features_item_ids': ['Q146786', 'Q146233'],
            },
            {
                'label': 'ainsuse osastav',
                'example': 'Seda [autot].',
                'grammatical_features_item_ids': ['Q110786', 'Q857325'],
            },
            {
                'label': 'mitmuse osastav',
                'example': 'Neid [autosid].',
                'grammatical_features_item_ids': ['Q146786', 'Q857325'],
            },
            {
                'label': 'ainsuse sisseütlev',
                'example': 'Sellesse [autosse].',
                'grammatical_features_item_ids': ['Q110786', 'Q474668'],
            },
            {
                'label': 'mitmuse sisseütlev',
                'example': 'Nendesse [autodesse].',
                'grammatical_features_item_ids': ['Q146786', 'Q474668'],
            },
            {
                'label': 'ainsuse seesütlev',
                'example': 'Selles [autos].',
                'grammatical_features_item_ids': ['Q110786', 'Q282031'],
            },
            {
                'label': 'mitmuse seesütlev',
                'example': 'Nendes [autodes].',
                'grammatical_features_item_ids': ['Q146786', 'Q282031'],
            },
            {
                'label': 'ainsuse seestütlev',
                'example': 'Sellest [autost].',
                'grammatical_features_item_ids': ['Q110786', 'Q394253'],
            },
            {
                'label': 'mitmuse seestütlev',
                'example': 'Nendest [autodest].',
                'grammatical_features_item_ids': ['Q146786', 'Q394253'],
            },
            {
                'label': 'ainsuse alaleütlev',
                'example': 'Sellele [autole].',
                'grammatical_features_item_ids': ['Q110786', 'Q655020'],
            },
            {
                'label': 'mitmuse alaleütlev',
                'example': 'Nendele [autodele].',
                'grammatical_features_item_ids': ['Q146786', 'Q655020'],
            },
            {
                'label': 'ainsuse alalütlev',
                'example': 'Sellel [autol].',
                'grammatical_features_item_ids': ['Q110786', 'Q281954'],
            },
            {
                'label': 'mitmuse alalütlev',
                'example': 'Nendel [autodel].',
                'grammatical_features_item_ids': ['Q146786', 'Q281954'],
            },
            {
                'label': 'ainsuse alaltütlev',
                'example': 'Sellelt [autolt].',
                'grammatical_features_item_ids': ['Q110786', 'Q156986'],
            },
            {
                'label': 'mitmuse alaltütlev',
                'example': 'Nendelt [autodelt].',
                'grammatical_features_item_ids': ['Q146786', 'Q156986'],
            },
            {
                'label': 'ainsuse saav',
                'example': 'Selleks [autoks].',
                'grammatical_features_item_ids': ['Q110786', 'Q950170'],
            },
            {
                'label': 'mitmuse saav',
                'example': 'Nendeks [autodeks].',
                'grammatical_features_item_ids': ['Q146786', 'Q950170'],
            },
            {
                'label': 'ainsuse rajav',
                'example': 'Selle [autoni].',
                'grammatical_features_item_ids': ['Q110786', 'Q747019'],
            },
            {
                'label': 'mitmuse rajav',
                'example': 'Nende [autodeni].',
                'grammatical_features_item_ids': ['Q146786', 'Q747019'],
            },
            {
                'label': 'ainsuse olev',
                'example': 'Selle [autona].',
                'grammatical_features_item_ids': ['Q110786', 'Q148465'],
            },
            {
                'label': 'mitmuse olev',
                'example': 'Nende [autodena].',
                'grammatical_features_item_ids': ['Q146786', 'Q148465'],
            },
            {
                'label': 'ainsuse ilmaütlev',
                'example': 'Selle [autota].',
                'grammatical_features_item_ids': ['Q110786', 'Q319822'],
            },
            {
                'label': 'mitmuse ilmaütlev',
                'example': 'Nende [autodeta].',
                'grammatical_features_item_ids': ['Q146786', 'Q319822'],
            },
            {
                'label': 'ainsuse kaasaütlev',
                'example': 'Selle [autoga].',
                'grammatical_features_item_ids': ['Q110786', 'Q838581'],
            },
            {
                'label': 'mitmuse kaasaütlev',
                'example': 'Nende [autodega].',
                'grammatical_features_item_ids': ['Q146786', 'Q838581'],
            },
        ],
    }),
    # template by User:Shinnin, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Finnish
    ('finnish-noun', {
        'label': 'suomen kielen substantiivi',
        'language_item_id': 'Q1412',
        'language_code': 'fi',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'yksikön nominatiivi',
                'example': 'Tämä on [koira].',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'monikon nominatiivi',
                'example': 'Nämä [koirat].',
                'grammatical_features_item_ids': ['Q146786', 'Q131105'],
            },
            {
                'label': 'yksikön genetiivi',
                'example': 'Tämän [koiran].',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'monikon genetiivi',
                'example': 'Näiden [koirien].',
                'grammatical_features_item_ids': ['Q146786', 'Q146233'],
            },
            {
                'label': 'yksikön partitiivi',
                'example': 'Tätä [koiraa].',
                'grammatical_features_item_ids': ['Q110786', 'Q857325'],
            },
            {
                'label': 'monikon partitiivi',
                'example': 'Näitä [koiria].',
                'grammatical_features_item_ids': ['Q146786', 'Q857325'],
            },
            {
                'label': 'yksikön essiivi',
                'example': 'Tällaisena [koirana].',
                'grammatical_features_item_ids': ['Q110786', 'Q148465'],
            },
            {
                'label': 'monikon essiivi',
                'example': 'Tällaisina [koirina].',
                'grammatical_features_item_ids': ['Q146786', 'Q148465'],
            },
            {
                'label': 'yksikön translatiivi',
                'example': 'Yhdeksi [koiraksi].',
                'grammatical_features_item_ids': ['Q110786', 'Q950170'],
            },
            {
                'label': 'monikon translatiivi',
                'example': 'Moniksi [koiriksi].',
                'grammatical_features_item_ids': ['Q146786', 'Q950170'],
            },
            {
                'label': 'yksikön inessiivi',
                'example': 'Tässä [koirassa].',
                'grammatical_features_item_ids': ['Q110786', 'Q282031'],
            },
            {
                'label': 'monikon inessiivi',
                'example': 'Näissä [koirissa].',
                'grammatical_features_item_ids': ['Q146786', 'Q282031'],
            },
            {
                'label': 'yksikön elatiivi',
                'example': 'Tästä [koirasta].',
                'grammatical_features_item_ids': ['Q110786', 'Q394253'],
            },
            {
                'label': 'monikon elatiivi',
                'example': 'Näistä [koirista].',
                'grammatical_features_item_ids': ['Q146786', 'Q394253'],
            },
            {
                'label': 'yksikön illatiivi',
                'example': 'Tähän [koiraan].',
                'grammatical_features_item_ids': ['Q110786', 'Q474668'],
            },
            {
                'label': 'monikon illatiivi',
                'example': 'Näihin [koiriin].',
                'grammatical_features_item_ids': ['Q146786', 'Q474668'],
            },
            {
                'label': 'yksikön adessiivi',
                'example': 'Tällä [koiralla].',
                'grammatical_features_item_ids': ['Q110786', 'Q281954'],
            },
            {
                'label': 'monikon adessiivi',
                'example': 'Näillä [koirilla].',
                'grammatical_features_item_ids': ['Q146786', 'Q281954'],
            },
            {
                'label': 'yksikön ablatiivi',
                'example': 'Tältä [koiralta].',
                'grammatical_features_item_ids': ['Q110786', 'Q156986'],
            },
            {
                'label': 'monikon ablatiivi',
                'example': 'Näiltä [koirilta].',
                'grammatical_features_item_ids': ['Q146786', 'Q156986'],
            },
            {
                'label': 'yksikön allatiivi',
                'example': 'Tälle [koiralle].',
                'grammatical_features_item_ids': ['Q110786', 'Q655020'],
            },
            {
                'label': 'monikon allatiivi',
                'example': 'Näille [koirille].',
                'grammatical_features_item_ids': ['Q146786', 'Q655020'],
            },
        ],
    }),
    # template by User:Djiboun, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/French
    ('french-noun-masculine', {
        'label': 'nom commun masculin en français',
        'language_item_id': 'Q150',
        'language_code': 'fr',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singulier',
                'example': 'Voici un [chien].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'pluriel',
                'example': 'Voici des [chiens].',
                'grammatical_features_item_ids': ['Q146786'],
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
    # template by User:Djiboun, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/French
    ('french-noun-feminine', {
        'label': 'nom commun féminin en français',
        'language_item_id': 'Q150',
        'language_code': 'fr',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singulier',
                'example': 'Voici une [chienne].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'pluriel',
                'example': 'Voici des [chiennes].',
                'grammatical_features_item_ids': ['Q146786'],
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
    # template by User:Djiboun, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/French
    ('french-adjective', {
        'label': 'adjectif en français',
        'language_item_id': 'Q150',
        'language_code': 'fr',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'masculin singulier',
                'example': 'Un arbre [vert].',
                'grammatical_features_item_ids': ['Q499327', 'Q110786'],
            },
            {
                'label': 'masculin pluriel',
                'example': 'Des arbres [verts].',
                'grammatical_features_item_ids': ['Q499327', 'Q146786'],
            },
            {
                'label': 'féminin singulier',
                'example': 'Une plante [verte].',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786'],
            },
            {
                'label': 'féminin pluriel',
                'example': 'Des plantes [vertes].',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786'],
            },
        ],
    }),
    # template by User:Sannita, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Italian
    ('italian-noun-feminine', {
        'label': 'sostantivo femminile italiano',
        'language_item_id': 'Q652',
        'language_code': 'it',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singolare',
                'example': 'Questa è una [rosa].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plurale',
                'example': 'Queste sono delle [rose].',
                'grammatical_features_item_ids': ['Q146786'],
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
    # template by User:Sannita, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Italian
    ('italian-noun-masculine', {
        'label': 'sostantivo maschile italiano',
        'language_item_id': 'Q652',
        'language_code': 'it',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singolare',
                'example': 'Questo è un [cane].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plurale',
                'example': 'Questi sono dei [cani].',
                'grammatical_features_item_ids': ['Q146786'],
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
    # template by User:Sannita, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Italian
    ('italian-adjective', {
        'label': 'aggettivo qualificativo italiano',
        'language_item_id': 'Q652',
        'language_code': 'it',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'maschile singolare',
                'example': 'Il panino è [buono].',
                'grammatical_features_item_ids': ['Q499327', 'Q110786'],
            },
            {
                'label': 'maschile plurale',
                'example': 'I panini sono [buoni].',
                'grammatical_features_item_ids': ['Q499327', 'Q146786'],
            },
            {
                'label': 'femminile singolare',
                'example': 'La maestra è [buona].',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786'],
            },
            {
                'label': 'femminile plurale',
                'example': 'Le maestre sono [buone].',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786'],
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
    # template by User:Njardarlogar, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Norwegian_Nynorsk
    ('nynorsk-noun-feminine', {
        'label': 'nynorsk hokjønnssubstantiv',
        'language_item_id': 'Q25164',
        'language_code': 'nn',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Dette er ei [liste].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'bunde eintal',
                'example': 'Dette er [lista].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851'],
            },
            {
                'label': 'ubunde fleirtal',
                'example': 'Dette er nokre [lister].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857'],
            },
            {
                'label': 'bunde fleirtal',
                'example': 'Dette er [listene].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851'],
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
    # template by User:Njardarlogar, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Norwegian_Nynorsk
    ('nynorsk-noun-masculine', {
        'label': 'nynorsk hankjønnssubstantiv',
        'language_item_id': 'Q25164',
        'language_code': 'nn',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Dette er ein [båt].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'bunde eintal',
                'example': 'Dette er [båten].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851'],
            },
            {
                'label': 'ubunde fleirtal',
                'example': 'Dette er nokre [båtar].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857'],
            },
            {
                'label': 'bunde fleirtal',
                'example': 'Dette er [båtane].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851'],
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
    # template by User:Njardarlogar, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Norwegian_Nynorsk
    ('nynorsk-noun-neuter', {
        'label': 'nynorsk inkjekjønnssubstantiv',
        'language_item_id': 'Q25164',
        'language_code': 'nn',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Dette er eit [hus].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'bunde eintal',
                'example': 'Dette er [huset].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851'],
            },
            {
                'label': 'ubunde fleirtal',
                'example': 'Dette er nokre [hus].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857'],
            },
            {
                'label': 'bunde fleirtal',
                'example': 'Dette er [husa].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851'],
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
                'example': 'To jest [odkurzacz].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, dopełniacz',
                'example': 'Wśród nas nie ma [odkurzacza].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, celownik',
                'example': 'Przyglądam się [odkurzaczowi].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, biernik',
                'example': 'Widzę [odkurzacz].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, narzędnik',
                'example': 'Idę z [odkurzaczem].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, miejscownik',
                'example': 'Myślę o [odkurzaczu].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': 'Liczba pojedyncza, wołacz',
                'example': '[odkurzaczu]',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'Liczba mnoga, mianownik',
                'example': 'To są [odkurzacze].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, dopełniacz',
                'example': 'Wśród nas nie ma [odkurzaczy/odkurzaczów].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, celownik',
                'example': 'Przyglądam się [odkurzaczom].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, biernik',
                'example': 'Widzę [odkurzacze].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, narzędnik',
                'example': 'Idę z [odkurzaczami].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, miejscownik',
                'example': 'Myślę o [odkurzaczach].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': 'Liczba mnoga, wołacz',
                'example': '[odkurzacze]',
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
    # template by User:Infovarius, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Russian
    ('russian-noun-masculine', {
        'label': 'русское существительное, мужской род',
        'language_item_id': 'Q7737',
        'language_code': 'ru',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ед.ч. им.п.',
                'example': 'Это [дом].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'ед.ч. род.п.',
                'example': 'Нет [дома].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'ед.ч. дат.п.',
                'example': 'Дать [дому].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'ед.ч. вин.п.',
                'example': 'Вижу [дом].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ед.ч. твор.п.',
                'example': 'Руковожу [домом].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'ед.ч. предл.п.',
                'example': 'Говорить о [доме].',
                'grammatical_features_item_ids': ['Q2114906', 'Q110786'],
            },
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это разные [дома].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет разных [домов].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать разным [домам].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу разные (разных) [дома].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу разными [домами].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о разных [домах].',
                'grammatical_features_item_ids': ['Q2114906', 'Q146786'],
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
    # template by User:Infovarius, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Russian
    ('russian-noun-feminine', {
        'label': 'русское существительное, женский род',
        'language_item_id': 'Q7737',
        'language_code': 'ru',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ед.ч. им.п.',
                'example': 'Это [собака].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'ед.ч. род.п.',
                'example': 'Нет [собаки].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'ед.ч. дат.п.',
                'example': 'Дать [собаке].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'ед.ч. вин.п.',
                'example': 'Вижу [собаку].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ед.ч. твор.п.',
                'example': 'Руковожу [собакой].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'ед.ч. предл.п.',
                'example': 'Говорить о [собаке].',
                'grammatical_features_item_ids': ['Q2114906', 'Q110786'],
            },
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это разные [собаки].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет разных [собак].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать разным [собакам].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу разных (разные) [собак].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу разными [собаками].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о разных [собаках].',
                'grammatical_features_item_ids': ['Q2114906', 'Q146786'],
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
    # template by User:Infovarius and others, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Russian
    ('russian-noun-neuter', {
        'label': 'русское существительное, средний род',
        'language_item_id': 'Q7737',
        'language_code': 'ru',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ед.ч. им.п.',
                'example': 'Это [облако].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'ед.ч. род.п.',
                'example': 'Нет [облака].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'ед.ч. дат.п.',
                'example': 'Дать [облаку].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'ед.ч. вин.п.',
                'example': 'Вижу [облако].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'ед.ч. твор.п.',
                'example': 'Руковожу [облаком].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'ед.ч. предл.п.',
                'example': 'Говорить о(б) [облаке].',
                'grammatical_features_item_ids': ['Q2114906', 'Q110786'],
            },
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это разные [облака].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет разных [облаков].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать разным [облакам].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу разные (разных) [облака].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу разными [облаками].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о(б) [облаках].',
                'grammatical_features_item_ids': ['Q2114906', 'Q146786'],
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
    # template by User:Infovarius, see https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms/Russian
    ('russian-noun-pluraletantum', {
        'label': 'имя существительное (Pluralia tantum, без рода)',
        'language_item_id': 'Q7737',
        'language_code': 'ru',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это [ножницы].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет [ножниц].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать [ножницам].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу [ножницы].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу [ножницами].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о [ножницах].',
                'grammatical_features_item_ids': ['Q2114906', 'Q146786'],
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
