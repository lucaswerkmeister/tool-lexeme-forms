import collections

templates = collections.OrderedDict([

    ('asturian-noun-masculine', {
        '@attribution': {'users': ['Oriciu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Asturian'},
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
        'statements': {
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

    ('asturian-noun-feminine', {
        '@attribution': {'users': ['Oriciu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Asturian'},
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
        'statements': {
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

    ('czech-noun-masculine-animate', {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod mužský životný)',
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
        'statements': {
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

    ('czech-noun-masculine-inanimate', {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod mužský neživotný)',
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
        'statements': {
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
                                'id': 'Q52943434',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),

    ('czech-noun-feminine', {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod ženský)',
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
        'statements': {
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

    ('czech-noun-neuter', {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod střední)',
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
        'statements': {
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

    ('czech-adverb', {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české příslovce',
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

    ('czech-adjective', {
        '@attribution': {'users': ['Strepon', 'Adrijaned'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české přídavné jméno',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': '1. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'To je můj [velký] pes.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '2. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Má strach z mého [velkého] psa.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '3. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Dej to mému [velkému] psu.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '4. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Vidím jednoho [velkého] psa.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '5. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Kam kráčíš, [velký] pse?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '6. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svém [velkém] psu.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '7. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvým [velkým] psem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '1. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'To je můj [velký] hrad.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '2. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Má strach z mého [velkého] hradu.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '3. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Dej to k mému [velkému] hradu.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '4. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Vidím jeden [velký] hrad.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '5. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Kam směřuješ, [velký] hrade?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '6. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svém [velkém] hradu.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '7. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvým [velkým] hradem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '1. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'To je má [velká] žena.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '2. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Má strach z mé [velké] ženy.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '3. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Dej to mé [velké] ženě.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '4. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Vidím jednu [velkou] ženu.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '5. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Kam kráčíš, [velká] ženo?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '6. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Pověz mi něco o své [velké] ženě.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '7. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvou [velkou] ženou.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '1. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'To je mé [velké] kuře.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '2. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Má strach z mého [velkého] kuřete.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '3. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Dej to mému [velkému] kuřeti.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '4. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Vidím jedno [velké] kuře.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '5. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Kam kráčíš, [velké] kuře?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '6. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svém [velkém] kuřeti.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '7. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvým [velkým] kuřetem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '1. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'To jsou moji [velcí] psi.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '2. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Má strach z mých [velkých] psů.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '3. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Dej to mým [velkým] psům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '4. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Vidím dva [velké] psy.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '5. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Kam kráčíte, [velcí] psi?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '6. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svých [velkých] psech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '7. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvými [velkými] psy.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q54020116', 'Q3482678'],
            },
            {
                'label': '1. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'To jsou mé [velké] hrady.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '2. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Má strach z mých [velkých] hradů.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '3. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Dej to k mým [velkým] hradům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '4. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Vidím dva [velké] hrady.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '5. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Kam směřujete, [velké] hrady?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '6. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svých [velkých] hradech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '7. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvými [velkými] hrady.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q52943434', 'Q3482678'],
            },
            {
                'label': '1. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'To jsou mé [velké] ženy.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '2. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Má strach z mých [velkých] žen.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '3. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Dej to mým [velkým] ženám.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '4. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Vidím dvě [velké] ženy.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '5. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Kam kráčíte, [velké] ženy?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '6. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svých [velkých] ženách.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '7. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvými [velkými] ženami.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q1775415', 'Q3482678'],
            },
            {
                'label': '1. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'To jsou má [velká] kuřata.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '2. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Má strach z mých [velkých] kuřat.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '3. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Dej to mým [velkým] kuřatům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '4. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Vidím dvě [velká] kuřata.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '5. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Kam kráčíte, [velká] kuřata?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '6. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svých [velkých] kuřatech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '7. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvými [velkými] kuřaty.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': '1. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'To je můj [větší] pes.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '2. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Má strach z mého [většího] psa.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '3. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Dej to mému [většímu] psu.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '4. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Vidím jednoho [většího] psa.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '5. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Kam kráčíš, [větší] pse?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '6. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svém [větším] psu.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '7. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvým [větším] psem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '1. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'To je můj [větší] hrad.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '2. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Má strach z mého [většího] hradu.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '3. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Dej to k mému [většímu] hradu.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '4. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Vidím jeden [větší] hrad.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '5. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Kam směřuješ, [větší] hrade?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '6. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svém [větším] hradu.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '7. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvým [větším] hradem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '1. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'To je má [větší] žena.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '2. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Má strach z mé [větší] ženy.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '3. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Dej to mé [větší] ženě.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '4. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Vidím jednu [větší] ženu.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '5. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Kam kráčíš, [větší] ženo?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '6. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Pověz mi něco o své [větší] ženě.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '7. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvou [větší] ženou.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '1. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'To je mé [větší] kuře.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '2. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Má strach z mého [většího] kuřete.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '3. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Dej to mému [většímu] kuřeti.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '4. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Vidím jedno [větší] kuře.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '5. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Kam kráčíš, [větší] kuře?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '6. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svém [větším] kuřeti.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '7. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvým [větším] kuřetem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '1. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'To jsou moji [větší] psi.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '2. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Má strach z mých [větších] psů.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '3. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Dej to mým [větším] psům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '4. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Vidím dva [větší] psy.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '5. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Kam kráčíte, [větší] psi?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '6. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svých [větších] psech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '7. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvými [většími] psy.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q54020116', 'Q14169499'],
            },
            {
                'label': '1. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'To jsou mé [větší] hrady.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '2. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Má strach z mých [větších] hradů.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '3. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Dej to k mým [větším] hradům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '4. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Vidím dva [větší] hrady.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '5. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Kam směřujete, [větší] hrady?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '6. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svých [větších] hradech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '7. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvými [většími] hrady.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q52943434', 'Q14169499'],
            },
            {
                'label': '1. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'To jsou mé [větší] ženy.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '2. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Má strach z mých [větších] žen.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '3. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Dej to mým [větším] ženám.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '4. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Vidím dvě [větší] ženy.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '5. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Kam kráčíte, [větší] ženy?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '6. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svých [větších] ženách.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '7. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvými [většími] ženami.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q1775415', 'Q14169499'],
            },
            {
                'label': '1. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'To jsou má [větší] kuřata.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '2. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Má strach z mých [větších] kuřat.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '3. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Dej to mým [větším] kuřatům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '4. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Vidím dvě [větší] kuřata.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '5. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Kam kráčíte, [větší] kuřata?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '6. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svých [větších] kuřatech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '7. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvými [většími] kuřaty.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q1775461', 'Q14169499'],
            },
            {
                'label': '1. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'To je můj [největší] pes.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '2. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Má strach z mého [největšího] psa.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '3. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Dej to mému [největšímu] psu.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '4. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Vidím jednoho [největšího] psa.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '5. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Kam kráčíš, [největší] pse?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '6. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svém [největším] psu.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '7. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvým [největším] psem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '1. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'To je můj [největší] hrad.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '2. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Má strach z mého [největšího] hradu.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '3. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Dej to k mému [největšímu] hradu.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '4. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Vidím jeden [největší] hrad.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '5. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Kam směřuješ, [největší] hrade?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '6. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svém [největším] hradu.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '7. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvým [největším] hradem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '1. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'To je má [největší] žena.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '2. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Má strach z mé [největší] ženy.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '3. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Dej to mé [největší] ženě.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '4. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Vidím jednu [největší] ženu.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '5. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Kam kráčíš, [největší] ženo?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '6. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Pověz mi něco o své [největší] ženě.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '7. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvou [největší] ženou.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '1. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'To je mé [největší] kuře.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '2. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Má strach z mého [největšího] kuřete.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '3. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Dej to mému [největšímu] kuřeti.',
                'grammatical_features_item_ids': ['Q145599', 'Q110786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '4. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Vidím jedno [největší] kuře.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '5. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Kam kráčíš, [největší] kuře?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '6. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svém [největším] kuřeti.',
                'grammatical_features_item_ids': ['Q202142', 'Q110786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '7. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvým [největším] kuřetem.',
                'grammatical_features_item_ids': ['Q192997', 'Q110786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '1. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'To jsou moji [největší] psi.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '2. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Má strach z mých [největších] psů.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '3. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Dej to mým [největším] psům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '4. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Vidím dva [největší] psy.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '5. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Kam kráčíte, [největší] psi?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '6. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svých [největších] psech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '7. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvými [největšími] psy.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q54020116', 'Q1817208'],
            },
            {
                'label': '1. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'To jsou mé [největší] hrady.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '2. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Má strach z mých [největších] hradů.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '3. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Dej to k mým [největším] hradům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '4. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Vidím dva [největší] hrady.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '5. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Kam směřujete, [největší] hrady?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '6. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svých [největších] hradech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '7. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvými [největšími] hrady.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q52943434', 'Q1817208'],
            },
            {
                'label': '1. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'To jsou mé [největší] ženy.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '2. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Má strach z mých [největších] žen.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '3. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Dej to mým [největším] ženám.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '4. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Vidím dvě [největší] ženy.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '5. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Kam kráčíte, [největší] ženy?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '6. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svých [největších] ženách.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '7. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvými [největšími] ženami.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q1775415', 'Q1817208'],
            },
            {
                'label': '1. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'To jsou má [největší] kuřata.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '2. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Má strach z mých [největších] kuřat.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '3. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Dej to mým [největším] kuřatům.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '4. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Vidím dvě [největší] kuřata.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '5. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Kam kráčíte, [největší] kuřata?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '6. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svých [největších] kuřatech.',
                'grammatical_features_item_ids': ['Q202142', 'Q146786', 'Q1775461', 'Q1817208'],
            },
            {
                'label': '7. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvými [největšími] kuřaty.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786', 'Q1775461', 'Q1817208'],
            },
        ],
    }),

    ('czech-verb-perfective', {
        '@attribution': {'users': ['Adrijaned', 'Strepon'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české sloveso dokonavé',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'infinitiv',
                'example': '[zazpívat].',
                'grammatical_features_item_ids': ['Q179230'],
            },
            {
                'label': '1. osoba, jednotné číslo',
                'example': 'Já teď [zazpívám].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q682111'],
            },
            {
                'label': '2. osoba, jednotné číslo',
                'example': 'Ty teď [zazpíváš].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q682111'],
            },
            {
                'label': '3. osoba, jednotné číslo',
                'example': 'Ono to teď [zazpívá].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q682111'],
            },
            {
                'label': '1. osoba, množné číslo',
                'example': 'My teď [zazpíváme].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q682111'],
            },
            {
                'label': '2. osoba, množné číslo',
                'example': 'Vy teď [zazpíváte].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q682111'],
            },
            {
                'label': '3. osoba, množné číslo',
                'example': 'Oni teď [zazpívají].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q682111'],
            },
            {
                'label': 'rozkazovací způsob, 2. osoba, jednotné číslo',
                'example': 'Ty [zazpívej]!',
                'grammatical_features_item_ids': ['Q22716', 'Q51929049', 'Q110786'],
            },
            {
                'label': 'rozkazovací způsob, 1. osoba, množné číslo',
                'example': 'My [zazpívejme]!',
                'grammatical_features_item_ids': ['Q22716', 'Q21714344', 'Q146786'],
            },
            {
                'label': 'rozkazovací způsob, 2. osoba, množné číslo',
                'example': 'Vy [zazpívejte]!',
                'grammatical_features_item_ids': ['Q22716', 'Q51929049', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod mužský, jednotné číslo',
                'example': 'On by [zazpíval].',
                'grammatical_features_item_ids': ['Q72249355', 'Q499327', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod ženský, jednotné číslo',
                'example': 'Ona by [zazpívala].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod střední, jednotné číslo',
                'example': 'Ono by [zazpívalo].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod mužský životný, množné číslo',
                'example': 'Oni muži by [zazpívali].',
                'grammatical_features_item_ids': ['Q72249355', 'Q499327', 'Q51927507', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, množné číslo',
                'example': 'Ony hrady by [zazpívaly].',
                'grammatical_features_item_ids': ['Q72249355', 'Q499327', 'Q51927539', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod ženský, množné číslo',
                'example': 'Ony by [zazpívaly].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775415', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod střední, množné číslo',
                'example': 'Ona by [zazpívala].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775461', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod mužský, jednotné číslo',
                'example': 'On bude [zazpíván].',
                'grammatical_features_item_ids': ['Q72249544', 'Q499327', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod ženský, jednotné číslo',
                'example': 'Ona bude [zazpívána].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod střední, jednotné číslo',
                'example': 'Ono bude [zazpíváno].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod mužský životný, množné číslo',
                'example': 'Oni muži budou [zazpíváni].',
                'grammatical_features_item_ids': ['Q72249544', 'Q499327', 'Q51927507', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, množné číslo',
                'example': 'Ony hrady budou [zazpívány].',
                'grammatical_features_item_ids': ['Q72249544', 'Q499327', 'Q51927539', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod ženský, množné číslo',
                'example': 'Ony budou [zazpívány].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775415', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod střední, množné číslo',
                'example': 'Ona budou [zazpívána].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775461', 'Q146786'],
            },
            {
                'label': 'přechodník minulý, rod mužský, jednotné číslo',
                'example': 'On [zazpívav], odešel.',
                'grammatical_features_item_ids': ['Q65540485', 'Q499327', 'Q110786'],
            },
            {
                'label': 'přechodník minulý, rod ženský, střední, jednotné číslo',
                'example': 'Ona [zazpívavši], odešla.',
                'grammatical_features_item_ids': ['Q65540485', 'Q1775415', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'přechodník minulý, množné číslo',
                'example': '[Zazpívavše], odešli.',
                'grammatical_features_item_ids': ['Q65540485', 'Q146786'],
            },
            {
                'label': 'přechodník přítomný, rod mužský, jednotné číslo',
                'example': 'On [zazpívaje], odejde.',
                'grammatical_features_item_ids': ['Q65540125', 'Q499327', 'Q110786'],
            },
            {
                'label': 'přechodník přítomný, rod ženský, střední, jednotné číslo',
                'example': 'Ona [zazpívajíc], odejde.',
                'grammatical_features_item_ids': ['Q65540125', 'Q1775415', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'přechodník přítomný, množné číslo',
                'example': '[Zazpívajíce], odejdou.',
                'grammatical_features_item_ids': ['Q65540125', 'Q146786'],
            },
        ],
        'statements': {
            'P7486': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P7486',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q1424306',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),

    ('danish-noun-common', {
        '@attribution': {'users': ['So9q', 'Fnielsen'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk substantiv (fælleskøn)',
        'language_item_id': 'Q9035',
        'language_code': 'da',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativ ental, ubestemt',
                'example': 'Det her er en [bil].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'nominativ ental, bestemt',
                'example': 'Den nye [bil].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851'],
            },
            {
                'label': 'nominativ flertal, ubestemt',
                'example': 'Jag ser flere [biler].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857'],
            },
            {
                'label': 'nominativ flertal, bestemt',
                'example': 'De nye [biler].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851'],
            },
        ],
        'statements': {
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
                                'id': 'Q1305037',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),

    ('danish-noun-neuter', {
        '@attribution': {'users': ['So9q', 'Fnielsen'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk substantiv (intetkøn)',
        'language_item_id': 'Q9035',
        'language_code': 'da',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativ ental, ubestemt',
                'example': 'Det her er et [bord].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'nominativ ental, bestemt',
                'example': 'Det nye [bord].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851'],
            },
            {
                'label': 'nominativ flertal, ubestemt',
                'example': 'Jeg ser flere [bord].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857'],
            },
            {
                'label': 'nominativ flertal, bestemt',
                'example': 'De nye [bord].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851'],
            },
        ],
        'statements': {
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

    ('danish-verb', {
        '@attribution': {'users': ['So9q'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk verb',
        'language_item_id': 'Q9035',
        'language_code': 'da',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'infinitiv aktiv (navnemåde)',
                'example': 'At [læse] er godt.',
                'grammatical_features_item_ids': ['Q179230', 'Q1317831'],
            },
            {
                'label': 'presens aktiv (nutid)',
                'example': 'Hun [læser] hver dag.',
                'grammatical_features_item_ids': ['Q192613', 'Q1317831'],
            },
            {
                'label': 'preteritum aktiv (datid)',
                'example': 'Hun [læste] i går.',
                'grammatical_features_item_ids': ['Q442485', 'Q1317831'],
            },
            {
                'label': 'præteritum participium (kort tillægsform)',
                'example': 'Hen har [læst] hele dagen.',
                'grammatical_features_item_ids': ['Q52434448'],
            },
            {
                'label': 'imperativ (bydeform, bydemåde)',
                'example': '[læs] nu!',
                'grammatical_features_item_ids': ['Q22716'],
            },
            {
                'label': 'presens passiv (nutid lideform)',
                'example': 'Det [læses] hver dag.',
                'grammatical_features_item_ids': ['Q192613', 'Q1194697'],
            },
            {
                'label': 'preteritum passiv (datid lideform)',
                'example': 'Det [læstes] i går.',
                'grammatical_features_item_ids': ['Q442485', 'Q1194697'],
            },
            {
                'label': 'præsens participium (lang tillægsform)',
                'example': 'Sikke meget [læsende] det blev i dag.',
                'grammatical_features_item_ids': ['Q10345583'],
            },
        ],
    }),

    ('german-noun-masculine', {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
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
        'statements': {
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

    ('german-noun-feminine', {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
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
        'statements': {
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

    ('german-noun-neuter', {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
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
        'statements': {
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

    ('german-noun-pluraletantum', {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
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
        'statements': {
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

    ('german-verb', {
        '@attribution': {'users': ['Lucas Werkmeister', 'Andreasmperu'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
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
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q3502553', 'Q192613', 'Q1317831'],
            },
            {
                'label': '2. Person Singular Konjunktiv I',
                'example': 'Angenommen, du [tragest].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q3502553', 'Q192613', 'Q1317831'],
            },
            {
                'label': '3. Person Singular Konjunktiv I',
                'example': 'Angenommen, er/sie/es [trage].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q3502553', 'Q192613', 'Q1317831'],
            },
            {
                'label': '1. Person Plural Konjunktiv I',
                'example': 'Angenommen, wir [tragen].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q3502553', 'Q192613', 'Q1317831'],
            },
            {
                'label': '2. Person Plural Konjunktiv I',
                'example': 'Angenommen, ihr [traget].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q3502553', 'Q192613', 'Q1317831'],
            },
            {
                'label': '3. Person Plural Konjunktiv I',
                'example': 'Angenommen, sie [tragen].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q3502553', 'Q192613', 'Q1317831'],
            },
            {
                'label': '1. Person Singular Konjunktiv II',
                'example': 'Ich dachte, ich [trüge].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q3502544', 'Q442485', 'Q1317831'],
            },
            {
                'label': '2. Person Singular Konjunktiv II',
                'example': 'Ich dachte, du [trügest/trügst].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q3502544', 'Q442485', 'Q1317831'],
            },
            {
                'label': '3. Person Singular Konjunktiv II',
                'example': 'Ich dachte, er/sie/es [trüge].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q3502544', 'Q442485', 'Q1317831'],
            },
            {
                'label': '1. Person Plural Konjunktiv II',
                'example': 'Ich dachte, wir [trügen].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q3502544', 'Q442485', 'Q1317831'],
            },
            {
                'label': '2. Person Plural Konjunktiv II',
                'example': 'Ich dachte, ihr [trüget/trügt].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q3502544', 'Q442485', 'Q1317831'],
            },
            {
                'label': '3. Person Plural Konjunktiv II',
                'example': 'Ich dachte, sie [trügen].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q3502544', 'Q442485', 'Q1317831'],
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
                'grammatical_features_item_ids': ['Q52434448'],
            },
        ],
    }),

    ('english-noun', {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/English'},
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

    ('english-adverb', {
        '@attribution': {'users': ['ArthurPSmith'], 'title': 'Wikidata:Wikidata Lexeme Forms/English'},
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

    ('english-adjective', {
        '@attribution': {'users': ['ArthurPSmith'], 'title': 'Wikidata:Wikidata Lexeme Forms/English'},
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

    ('english-verb', {
        '@attribution': {'users': ['ArthurPSmith', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/English'},
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
                'grammatical_features_item_ids': ['Q3910936', 'Q51929074', 'Q110786'],
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

    ('esperanto-noun', {
        '@attribution': {'users': ['KaMan', 'Jens Ohlig'], 'title': 'Wikidata:Wikidata Lexeme Forms/Esperanto'},
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

    ('spanish-noun-masculine', {
        '@attribution': {'users': ['Andreasmperu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'sustantivo masculino en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singular',
                'example': 'Este es un [libro].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plural',
                'example': 'Estos son unos [libros].',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
        'statements': {
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

    ('spanish-noun-feminine', {
        '@attribution': {'users': ['Andreasmperu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'sustantivo femenino en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singular',
                'example': 'Esta es una [manzana].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'plural',
                'example': 'Estas son unas [manzanas].',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
        'statements': {
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

    ('spanish-adjective', {
        '@attribution': {'users': ['Andreasmperu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'adjetivo en español',
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

    ('spanish-verb', {
        '@attribution': {'users': ['DemonDays64', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'verbo en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'infinitivo',
                'example': 'Quieres [cantar].',
                'grammatical_features_item_ids': ['Q179230'],
            },
            {
                'label': 'primera persona singular presente',
                'example': 'Yo [canto] todos los días.',
                'grammatical_features_item_ids': ['Q192613', 'Q682111', 'Q21714344', 'Q110786'],
            },
            {
                'label': 'segunda persona singular presente',
                'example': 'Tú [cantas] todos los días.',
                'grammatical_features_item_ids': ['Q192613', 'Q682111', 'Q51929049', 'Q110786'],
            },
            {
                'label': 'tercera persona singular presente',
                'example': 'Él [canta] todos los días.',
                'grammatical_features_item_ids': ['Q192613', 'Q682111', 'Q51929074', 'Q110786'],
            },
            {
                'label': 'primera persona plural presente',
                'example': 'Nosotros [cantamos] todos los días.',
                'grammatical_features_item_ids': ['Q192613', 'Q682111', 'Q21714344', 'Q146786'],
            },
            {
                'label': 'segunda persona plural presente',
                'example': 'Vosotros [cantáis] todos los días.',
                'grammatical_features_item_ids': ['Q192613', 'Q682111', 'Q51929049', 'Q146786'],
            },
            {
                'label': 'tercera persona plural presente',
                'example': 'Ellos [cantan] todos los días.',
                'grammatical_features_item_ids': ['Q192613', 'Q682111', 'Q51929074', 'Q146786'],
            },
            {
                'label': 'primera persona singular pretérito',
                'example': 'Yo [canté] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q21714344', 'Q110786'],
            },
            {
                'label': 'segunda persona singular pretérito',
                'example': 'Tú [cantaste] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q51929049', 'Q110786'],
            },
            {
                'label': 'tercera persona singular pretérito',
                'example': 'Él [cantó] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q51929074', 'Q110786'],
            },
            {
                'label': 'primera persona plural pretérito',
                'example': 'Nosotros [cantamos] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q21714344', 'Q146786'],
            },
            {
                'label': 'segunda persona plural pretérito',
                'example': 'Vosotros [cantasteis] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q51929049', 'Q146786'],
            },
            {
                'label': 'tercera persona plural pretérito',
                'example': 'Ellos [cantaron] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q51929074', 'Q146786'],
            },
            {
                'label': 'primera persona singular pretérito imperfecto',
                'example': 'Yo [cantaba] mucho cuándo era niño.',
                'grammatical_features_item_ids': ['Q12547192', 'Q21714344', 'Q110786'],
            },
            {
                'label': 'segunda persona singular pretérito imprefecto',
                'example': 'Tú [cantabas] mucho cuándo eras niño.',
                'grammatical_features_item_ids': ['Q12547192', 'Q51929049', 'Q110786'],
            },
            {
                'label': 'tercera persona singular pretérito imperfecto',
                'example': 'Él [cantaba] mucho cuándo era niño.',
                'grammatical_features_item_ids': ['Q12547192', 'Q51929074', 'Q110786'],
            },
            {
                'label': 'primera persona plural pretérito imperfecto',
                'example': 'Nosotros [cantábamos] mucho cuándo éramos niños.',
                'grammatical_features_item_ids': ['Q12547192', 'Q21714344', 'Q146786'],
            },
            {
                'label': 'segunda persona plural pretérito imperfecto',
                'example': 'Vosotros [cantabais] mucho cuándo erais niños.',
                'grammatical_features_item_ids': ['Q12547192', 'Q51929049', 'Q146786'],
            },
            {
                'label': 'tercera persona plural pretérito imperfecto',
                'example': 'Ellos [cantaban] mucho cuándo eran niños.',
                'grammatical_features_item_ids': ['Q12547192', 'Q51929074', 'Q146786'],
            },
            {
                'label': 'participio presente',
                'example': 'Estoy [cantando].',
                'grammatical_features_item_ids': ['Q10345583', 'Q51929074', 'Q146786'],
            },
        ],
    }),

    ('estonian-noun', {
        '@attribution': {'users': ['Reosarevok'], 'title': 'Wikidata:Wikidata Lexeme Forms/Estonian'},
        'label': 'eesti keele nimisõna',
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

    ('basque-verb', {
        '@attribution': {'users': ['Theklan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Basque'},
        'label': 'euskal aditza',
        'language_item_id': 'Q8752',
        'language_code': 'eu',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'partizipioa',
                'example': 'liburu bat [erosi] dut',
                'grammatical_features_item_ids': ['Q814722'],
            },
            {
                'label': 'aditzoina',
                'example': 'liburu bat [eros] nezake',
                'grammatical_features_item_ids': ['Q74674702'],
            },
            {
                'label': 'aditz izena',
                'example': 'liburu bat [erostea] pentsatu dut',
                'grammatical_features_item_ids': ['Q74674960'],
            },
            {
                'label': 'gerundioa',
                'example': 'liburu bat [erosten] ari naiz',
                'grammatical_features_item_ids': ['Q1923028', 'Q54556033'],
            },
            {
                'label': 'etorkizuneko forma',
                'example': 'liburu bat [erosiko] dut',
                'grammatical_features_item_ids': ['Q501405'],
            },
        ],
    }),

    ('persian-noun', {
        '@attribution': {'users': ['Ladsgroup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Persian'},
        'label': 'اسم فارسی',
        'language_item_id': 'Q9168',
        'language_code': 'fa',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'مفرد',
                'example': '[سگ] غذا می‌خورد.',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'جمع',
                'example': '[سگ‌ها] غذا می‌خورند.',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
    }),

    ('persian-verb', {
        '@attribution': {'users': ['Ladsgroup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Persian'},
        'label': 'فعل فارسی',
        'language_item_id': 'Q9168',
        'language_code': 'fa',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'اول شخص مفرد',
                'example': 'من [می‌روم].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786'],
            },
            {
                'label': 'دوم شخص مفرد',
                'example': 'تو [می‌روی].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786'],
            },
            {
                'label': 'سوم شخص مفرد',
                'example': 'او [می‌رود].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786'],
            },
            {
                'label': 'اول شخص جمع',
                'example': 'ما [می‌رویم].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786'],
            },
            {
                'label': 'دوم شخص جمع',
                'example': 'شما [می‌روید].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786'],
            },
            {
                'label': 'سوم شخص جمع',
                'example': 'آنها [می‌روند].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786'],
            },
        ],
    }),

    ('finnish-noun', {
        '@attribution': {'users': ['Shinnin'], 'title': 'Wikidata:Wikidata Lexeme Forms/Finnish'},
        'label': 'suomen kielen substantiivi',
        'language_item_id': 'Q1412',
        'language_code': 'fi',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'yksikön nominatiivi',
                'example': 'Tämä on [koira/lisää/useampia/muotoja/näin].',
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
            {
                'label': 'monikon instruktiivi',
                'example': 'Käsin, jaloin, kissoin ja [koirin].',
                'grammatical_features_item_ids': ['Q1665275', 'Q146786'],
            },
            {
                'label': 'yksikön abessiivi',
                'example': 'Kädettä, jalatta, kissatta ja [koiratta].',
                'grammatical_features_item_ids': ['Q319822', 'Q110786'],
            },
            {
                'label': 'monikon abessiivi',
                'example': 'Käsittä, jaloitta, kissoitta ja [koiritta].',
                'grammatical_features_item_ids': ['Q319822', 'Q146786'],
            },
        ],
    }),

    ('french-noun-masculine', {
        '@attribution': {'users': ['Djiboun'], 'title': 'Wikidata:Wikidata Lexeme Forms/French'},
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
        'statements': {
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

    ('french-noun-feminine', {
        '@attribution': {'users': ['Djiboun'], 'title': 'Wikidata:Wikidata Lexeme Forms/French'},
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
        'statements': {
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

    ('french-adjective', {
        '@attribution': {'users': ['Djiboun'], 'title': 'Wikidata:Wikidata Lexeme Forms/French'},
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

    ('hebrew-noun-masculine', {
        '@attribution': {'users': ['Uziel302', 'Uzielbot'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hebrew'},
        'label': 'שם עצם זכר',
        'language_item_id': 'Q9288',
        'language_code': 'he',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'יחיד',
                'example': 'זה [כלב].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'רבים',
                'example': 'אלה [כלבים].',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
        'statements': {
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

    ('hebrew-noun-feminine', {
        '@attribution': {'users': ['Uziel302', 'Uzielbot'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hebrew'},
        'label': 'שם עצם נקבה',
        'language_item_id': 'Q9288',
        'language_code': 'he',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'יחידה',
                'example': 'זו [כלבה].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'רבות',
                'example': 'אלה [כלבות].',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
        'statements': {
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

    ('armenian-noun', {
        '@attribution': {'users': ['Emptyfear'], 'title': 'Wikidata:Wikidata Lexeme Forms/Armenian'},
        'label': 'հայերեն գոյական',
        'language_item_id': 'Q8785',
        'language_code': 'hy',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'եզ․ թիվ, ուղղ․ հոլով',
                'example': 'Սա [փողոց] է։',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, սեռ․ հոլով',
                'example': '[Փողոցի] նշանակությունը։',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, տր․ հոլով',
                'example': '[Փողոցին] նայել։',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, հայց․ հոլով',
                'example': 'Տեսնում եմ [փողոց]։',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, գործ․ հոլով',
                'example': '[Փողոցով] գնալ։',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, բաց․ հոլով',
                'example': '[Փողոցից] հեռանալ։',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, ներգ․ հոլով',
                'example': '[Փողոցում] ապրել։',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': 'հոգ․ թիվ, ուղղ․ հոլով',
                'example': 'Սրանք [փողոցներ] են։',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'հոգ․ թիվ, սեռ․ հոլով',
                'example': 'Բազմաթիվ [փողոցների] նշանակությունը։',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'հոգ․ թիվ, տր․ հոլով',
                'example': '[Փողոցներին] նայել։',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'հոգ․ թիվ, հայց․ հոլով',
                'example': 'Տեսնում եմ շատ [փողոցներ]։',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'հոգ․ թիվ, գործ․ հոլով',
                'example': 'Բոլոր [փողոցներով] գնալ։',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'հոգ․ թիվ, բաց․ հոլով',
                'example': 'Բոլոր [փողոցներից] հեռանալ։',
                'grammatical_features_item_ids': ['Q156986', 'Q146786'],
            },
            {
                'label': 'հոգ․ թիվ, ներգ․ հոլով',
                'example': 'Տարբեր [փողոցներում] ապրել։',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
        ],
    }),

    ('armenian-noun-singulare-tantum', {
        '@attribution': {'users': ['Emptyfear'], 'title': 'Wikidata:Wikidata Lexeme Forms/Armenian'},
        'label': 'հայերեն հավաքական անհոգնական եզակի գոյական',
        'language_item_id': 'Q8785',
        'language_code': 'hy',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'եզ․ թիվ, ուղղ․ հոլով',
                'example': 'Սա [կաթ] է։',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, սեռ․ հոլով',
                'example': '[Կաթի] նշանակությունը։',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, տր․ հոլով',
                'example': '[Կաթին] ավելացնել։',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, հայց․ հոլով',
                'example': 'Տեսնում եմ [կաթ]։',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, գործ․ հոլով',
                'example': '[Կաթով] պատրաստել։',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, բաց․ հոլով',
                'example': '[Կաթից] առանձնացնել։',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
            },
            {
                'label': 'եզ․ թիվ, ներգ․ հոլով',
                'example': '[Կաթում] լողալ։',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
        ],
        'statements': {
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
                                'id': 'Q604984',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),

    ('italian-noun-feminine', {
        '@attribution': {'users': ['Sannita'], 'title': 'Wikidata:Wikidata Lexeme Forms/Italian'},
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
        'statements': {
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

    ('italian-noun-masculine', {
        '@attribution': {'users': ['Sannita'], 'title': 'Wikidata:Wikidata Lexeme Forms/Italian'},
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
        'statements': {
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

    ('italian-adjective', {
        '@attribution': {'users': ['Sannita'], 'title': 'Wikidata:Wikidata Lexeme Forms/Italian'},
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

    ('kurmanji-noun-feminine', {
        '@attribution': {'users': ['Şêr'], 'title': 'Wikidata:Wikidata Lexeme Forms/Kurdish (Kurmancî)'},
        'label': 'navdêra kurdî (mê)',
        'language_item_id': 'Q36163',
        'language_code': 'ku',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Rewşa navkî ya yekjimar a binavkirî',
                'example': 'Ev [pisîk] e.',
                'grammatical_features_item_ids': ['Q1751855', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'Rewşa navkî ya pirjimar a binavkirî',
                'example': 'Ev [pisîk] in.',
                'grammatical_features_item_ids': ['Q1751855', 'Q146786', 'Q53997851'],
            },
            {
                'label': 'Rewşa çemandî ya yekjimar a binavkirî',
                'example': 'Ez [pisîkê] dibînim.',
                'grammatical_features_item_ids': ['Q1233197', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'Rewşa çemandî ya pirjimar ya binavkirî',
                'example': 'Ez [pisîkan] dibînim.',
                'grammatical_features_item_ids': ['Q1233197', 'Q146786', 'Q53997851'],
            },
            {
                'label': 'Rewşa îzafe ya yekjimar a binavkirî',
                'example': 'Ev [pisîka] nû ye.',
                'grammatical_features_item_ids': ['Q18794', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'Rewşa îzafe ya pirjimar a binavkirî',
                'example': 'Ev [pisîkên] nû ne.',
                'grammatical_features_item_ids': ['Q18794', 'Q146786', 'Q53997851'],
            },
            {
                'label': 'Rewşa navkî ya yekjimar a nebinavkirî',
                'example': 'Ev [pisîkek] e.',
                'grammatical_features_item_ids': ['Q1751855', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'Rewşa navkî ya pirjimar a nebinavkirî',
                'example': 'Ev [pisîkin] in.',
                'grammatical_features_item_ids': ['Q1751855', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'Rewşa çemandî ya yekjimar ya nebinavkirî',
                'example': 'Ez [pisîkekê] dibînim.',
                'grammatical_features_item_ids': ['Q1233197', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'Rewşa çemandî ya pirjimar ya nebinavkirî',
                'example': 'Ez [pisîkinan] dibînim.',
                'grammatical_features_item_ids': ['Q1233197', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'Rewşa îzafe ya yekjimar a nebinavkirî',
                'example': 'Ev [pisîkeke] nû ye.',
                'grammatical_features_item_ids': ['Q18794', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'Rewşa îzafe ya pirjimar a nebinavkirî',
                'example': 'Ez [pisîkine] nû dibînim.',
                'grammatical_features_item_ids': ['Q18794', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'Rewşa gazîkirinê ya yekjimar',
                'example': 'Silav [pisîkê]!',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'Rewşa gazîkirinê ya pirjimar',
                'example': 'Silav [pisîkino]!',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
        ],
        'statements': {
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

    ('kurmanji-noun-masculine', {
        '@attribution': {'users': ['Şêr'], 'title': 'Wikidata:Wikidata Lexeme Forms/Kurdish (Kurmancî)'},
        'label': 'navdêra kurdî (nêr)',
        'language_item_id': 'Q36163',
        'language_code': 'ku',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Rewşa navkî ya yekjimar a binavkirî',
                'example': 'Ev [gund] e.',
                'grammatical_features_item_ids': ['Q1751855', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'Rewşa navkî ya pirjimar a binavkirî',
                'example': 'Ev [gund] in.',
                'grammatical_features_item_ids': ['Q1751855', 'Q146786', 'Q53997851'],
            },
            {
                'label': 'Rewşa çemandî ya yekjimar a binavkirî',
                'example': 'Ez [gundî] dibînim.',
                'grammatical_features_item_ids': ['Q1233197', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'Rewşa çemandî ya pirjimar ya binavkirî',
                'example': 'Ez [gundan] dibînim.',
                'grammatical_features_item_ids': ['Q1233197', 'Q146786', 'Q53997851'],
            },
            {
                'label': 'Rewşa îzafe ya yekjimar a binavkirî',
                'example': 'Ev [gundê] kevn e.',
                'grammatical_features_item_ids': ['Q18794', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'Rewşa îzafe ya pirjimar a binavkirî',
                'example': 'Ev [gundên] nû kevn in.',
                'grammatical_features_item_ids': ['Q18794', 'Q146786', 'Q53997851'],
            },
            {
                'label': 'Rewşa navkî ya yekjimar a nebinavkirî',
                'example': 'Ev [gundek] e.',
                'grammatical_features_item_ids': ['Q1751855', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'Rewşa navkî ya pirjimar a nebinavkirî',
                'example': 'Ev [gundin] in.',
                'grammatical_features_item_ids': ['Q1751855', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'Rewşa çemandî ya yekjimar ya nebinavkirî',
                'example': 'Ez [gundekî] dibînim.',
                'grammatical_features_item_ids': ['Q1233197', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'Rewşa çemandî ya pirjimar ya nebinavkirî',
                'example': 'Ez [gundinan] dibînim.',
                'grammatical_features_item_ids': ['Q1233197', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'Rewşa îzafe ya yekjimar a nebinavkirî',
                'example': 'Ev [gundekî] nû ye.',
                'grammatical_features_item_ids': ['Q18794', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'Rewşa îzafe ya pirjimar a nebinavkirî',
                'example': 'Ez [gundine] nû dibînim.',
                'grammatical_features_item_ids': ['Q18794', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'Rewşa gazîkirinê ya yekjimar',
                'example': 'Silav [bavo]!',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'Rewşa gazîkirinê ya pirjimar',
                'example': 'Silav [bavino]!',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
        ],
        'statements': {
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

    ('latin-noun-masculine', {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
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
        'statements': {
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

    ('latin-noun-feminine', {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
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
        'statements': {
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

    ('latin-noun-neuter', {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
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
        'statements': {
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

    ('malayalam-noun', {
        '@attribution': {'users': ['Jsamwrites'], 'title': 'Wikidata:Wikidata Lexeme Forms/Malayalam'},
        'label': 'മലയാളത്തിലെ സാധാരണ നാമം',
        'language_item_id': 'Q36236',
        'language_code': 'ml',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ഏകവചനം',
                'example': 'ഒരു [ഭാഷ].',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'ബഹുവചനം',
                'example': 'പല [ഭാഷകൾ].',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
    }),

    ('dutch-neuter-noun', {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands onzijdig zelfstandig naamwoord',
        'language_item_id': 'Q7411',
        'language_code': 'nl',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'enkelvoud',
                'example': 'Dit is het [huis].',
                'grammatical_features_item_ids': ['Q110786', 'Q1775461'],
            },
            {
                'label': 'meervoud',
                'example': 'Dit zijn de [huizen].',
                'grammatical_features_item_ids': ['Q146786'],
            },
            {
                'label': 'verkleinwoord, enkelvoud',
                'example': 'Dit is het kleine [huisje].',
                'grammatical_features_item_ids': ['Q108709', 'Q110786', 'Q1775461'],
            },
            {
                'label': 'verkleinwoord, meervoud',
                'example': 'Dit zijn de kleine [huisjes].',
                'grammatical_features_item_ids': ['Q108709', 'Q146786'],
            },
        ],
        'statements': {
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

    ('dutch-masculine-noun', {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands strikt mannelijk zelfstandig naamwoord',
        'language_item_id': 'Q7411',
        'language_code': 'nl',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'enkelvoud',
                'example': 'Dit is de [man].',
                'grammatical_features_item_ids': ['Q110786', 'Q499327'],
            },
            {
                'label': 'meervoud',
                'example': 'Dit zijn de [mannen].',
                'grammatical_features_item_ids': ['Q146786'],
            },
            {
                'label': 'verkleinwoord, enkelvoud',
                'example': 'Dit is het kleine [mannetje].',
                'grammatical_features_item_ids': ['Q108709', 'Q110786', 'Q1775461'],
            },
            {
                'label': 'verkleinwoord, meervoud',
                'example': 'Dit zijn de kleine [mannetjes].',
                'grammatical_features_item_ids': ['Q108709', 'Q146786'],
            },
        ],
        'statements': {
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

    ('dutch-feminine-noun', {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands strikt vrouwelijk zelfstandig naamwoord',
        'language_item_id': 'Q7411',
        'language_code': 'nl',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'enkelvoud',
                'example': 'Dit is de [vrouw].',
                'grammatical_features_item_ids': ['Q110786', 'Q1775415'],
            },
            {
                'label': 'meervoud',
                'example': 'Dit zijn de [vrouwen].',
                'grammatical_features_item_ids': ['Q146786'],
            },
            {
                'label': 'verkleinwoord, enkelvoud',
                'example': 'Dit is het kleine [vrouwtje].',
                'grammatical_features_item_ids': ['Q108709', 'Q110786', 'Q1775461'],
            },
            {
                'label': 'verkleinwoord, meervoud',
                'example': 'Dit zijn de kleine [vrouwtjes].',
                'grammatical_features_item_ids': ['Q108709', 'Q146786'],
            },
        ],
        'statements': {
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

    ('dutch-fem2masc-noun', {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands v/m zelfstandig naamwoord',
        'language_item_id': 'Q7411',
        'language_code': 'nl',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'enkelvoud',
                'example': 'Dit is de [tafel].',
                'grammatical_features_item_ids': ['Q110786', 'Q64448167'],
            },
            {
                'label': 'meervoud',
                'example': 'Dit zijn de [tafels].',
                'grammatical_features_item_ids': ['Q146786'],
            },
            {
                'label': 'verkleinwoord, enkelvoud',
                'example': 'Dit is het kleine [tafeltje].',
                'grammatical_features_item_ids': ['Q108709', 'Q110786', 'Q1775461'],
            },
            {
                'label': 'verkleinwoord, meervoud',
                'example': 'Dit zijn de kleine [tafeltjes].',
                'grammatical_features_item_ids': ['Q108709', 'Q146786'],
            },
        ],
        'statements': {
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
                                'id': 'Q64448167',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),

    ('nynorsk-noun-feminine', {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
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
        'statements': {
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

    ('nynorsk-noun-masculine', {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
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
        'statements': {
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

    ('nynorsk-noun-neuter', {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
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
        'statements': {
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

    ('polish-noun', {
        '@attribution': {'users': ['KaMan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Polish'},
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

    ('polish-noun-masculine-personal-with-depreciative-forms', {
        '@attribution': {'users': ['KaMan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Polish'},
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
                'statements': {
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
                'statements': {
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
                'statements': {
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
                'statements': {
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
        'statements': {
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

    ('polish-noun-with-potential-plural-forms', {
        '@attribution': {'users': ['KaMan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Polish'},
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
                'statements': {
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
                'statements': {
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
                'statements': {
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
                'statements': {
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
                'statements': {
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
                'statements': {
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
                'statements': {
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

    ('portuguese-verb', {
        '@attribution': {'users': ['Carybe', 'Joalpe', 'Waldir'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'verbo em Português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'Infinitivo Impessoal',
                'example': 'O [cantar] dos golfinhos é belo.',
                'grammatical_features_item_ids': ['Q64003131'],
            },
            {
                'label': 'Gerúndio',
                'example': 'Ele estava [cantando] no chuveiro.',
                'grammatical_features_item_ids': ['Q1923028'],
            },
            {
                'label': 'Particípio',
                'example': 'Estava sem voz, pois havia [cantado] mais cedo.',
                'grammatical_features_item_ids': ['Q814722'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Presente do Modo Indicativo',
                'example': 'Eu [canto] às segundas-feiras.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q192613', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Presente do Modo Indicativo',
                'example': 'Tu [cantas] às terças-feiras.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q192613', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Presente do Modo Indicativo',
                'example': 'Ele [canta] às quartas-feiras.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q192613', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Presente do Modo Indicativo',
                'example': 'Nós [cantamos] às quintas-feiras.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q192613', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Presente do Modo Indicativo',
                'example': 'Vós [cantais] às sextas-feiras.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q192613', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Presente do Modo Indicativo',
                'example': 'Eles [cantam] aos sábados.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q192613', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Eu [cantei] ontem no palco.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q23663136', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Tu [cantaste] ontem no palco.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q23663136', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Ele [cantou] ontem no palco.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q23663136', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Nós [cantamos] ontem no palco.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q23663136', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Vós [cantastes] ontem no palco.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q23663136', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Eles [cantaram] ontem no palco.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q23663136', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Eu [cantava] no coral quando acabou a luz.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q12547192', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Tu [cantavas] no coral quando acabou a luz.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q12547192', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Ele [cantava] no coral quando acabou a luz.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q12547192', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Nós [cantávamos] no coral quando acabou a luz.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q12547192', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Vós [cantáveis] no coral quando acabou a luz.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q12547192', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Eles [cantavam] no coral quando acabou a luz.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q12547192', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que eu [cantara] antigamente.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q623742', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que tu [cantaras] antigamente.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q623742', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que ele [cantara] antigamente.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q623742', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que nós [cantáramos] antigamente.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q623742', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que ele vós [cantáreis] antigamente.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q623742', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que ele eles [cantaram] antigamente.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q623742', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Futuro do Presente do Modo Indicativo',
                'example': 'Eu [cantarei] amanhã no teatro municipal.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q63997439', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Futuro do Presente do Modo Indicativo',
                'example': 'Tu [cantarás] amanhã no teatro municipal.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q63997439', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Futuro do Presente do Modo Indicativo',
                'example': 'Ele [cantará] amanhã no teatro municipal.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q63997439', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Futuro do Presente do Modo Indicativo',
                'example': 'Nós [cantaremos] amanhã no teatro municipal.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q63997439', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Futuro do Presente do Modo Indicativo',
                'example': 'Vós [cantareis] amanhã no teatro municipal.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q63997439', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Futuro do Presente do Modo Indicativo',
                'example': 'Eles [cantarão] amanhã no teatro municipal.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q63997439', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Futuro do Pretérito do Modo Indicativo',
                'example': 'Eu [cantaria] se fosse possível.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q63997520', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Futuro do Pretérito do Modo Indicativo',
                'example': 'Tu [cantarias] se fosse possível.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q63997520', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Futuro do Pretérito do Modo Indicativo',
                'example': 'Ele [cantaria] se fosse possível.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q63997520', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Futuro do Pretérito do Modo Indicativo',
                'example': 'Nós [cantaríamos] se fosse possível.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q63997520', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Futuro do Pretérito do Modo Indicativo',
                'example': 'Vós [cantaríeis] se fosse possível.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q63997520', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Futuro do Pretérito do Modo Indicativo',
                'example': 'Eles [cantariam] se fosse possível.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q63997520', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Presente do Modo Subjuntivo',
                'example': 'Espero que eu [cante] logo.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q192613', 'Q473746'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Presente do Modo Subjuntivo',
                'example': 'Espero que tu [cantes] logo.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q192613', 'Q473746'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Presente do Modo Subjuntivo',
                'example': 'Espero que ele [cante] logo.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q192613', 'Q473746'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Presente do Modo Subjuntivo',
                'example': 'Espero que nós [cantemos] logo.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q192613', 'Q473746'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Presente do Modo Subjuntivo',
                'example': 'Espero que vós [canteis] logo.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q192613', 'Q473746'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Presente do Modo Subjuntivo',
                'example': 'Espero que eles [cantem] logo.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q192613', 'Q473746'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se eu [cantasse] mais alto, seria melhor.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q12547192', 'Q473746'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se tu [cantasses] mais alto, seria melhor.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q12547192', 'Q473746'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se ele [cantasse] mais alto, seria melhor.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q12547192', 'Q473746'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se nós [cantássemos] mais alto, seria melhor.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q12547192', 'Q473746'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se vós [cantásseis] mais alto, seria melhor.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q12547192', 'Q473746'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se eles [cantassem] mais alto, seria melhor.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q12547192', 'Q473746'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Futuro do Modo Subjuntivo',
                'example': 'Quando eu [cantar] os outros ouvirão.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Futuro do Modo Subjuntivo',
                'example': 'Quando tu [cantares] os outros ouvirão.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Futuro do Modo Subjuntivo',
                'example': 'Quando ele [cantar] os outros ouvirão.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Futuro do Modo Subjuntivo',
                'example': 'Quando nós [cantarmos] os outros ouvirão.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Futuro do Modo Subjuntivo',
                'example': 'Quando vós [cantardes] os outros ouvirão.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Futuro do Modo Subjuntivo',
                'example': 'Quando eles [cantarem] os outros ouvirão.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Modo Imperativo Afirmativo',
                'example': '[Canta] tu agora que há tempo.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q22716'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Modo Imperativo Afirmativo',
                'example': '[Canta] você agora que há tempo.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q22716'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[Cantemos] nós agora que há tempo.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q22716'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[Cantai] vós agora que há tempo.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q22716'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[Cantem] vocês agora que há tempo.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q22716'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Modo Imperativo Negativo',
                'example': 'Não [cantes] tu, ainda não está na hora.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q64004115'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Modo Imperativo Negativo',
                'example': 'Não [cante] você, ainda não está na hora.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q64004115'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Modo Imperativo Negativo',
                'example': 'Não [cantemos] nós, ainda não está na hora.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q64004115'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Modo Imperativo Negativo',
                'example': 'Não [canteis] vós, ainda não está na hora.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q64004115'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Modo Imperativo Negativo',
                'example': 'Não [cantem] vocês, ainda não está na hora.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q64004115'],
            },
            {
                'label': 'Primeira Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantar] eu ganhei vários prêmios.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q179230'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantares] tu ganhaste vários prêmios.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q179230'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantar] ele ganhou vários prêmios.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q179230'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantarmos] nós ganhamos vários prêmios.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q179230'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantardes] vós ganhastes vários prêmios.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q179230'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantarem] eles ganharam vários prêmios.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q179230'],
            },
        ],
    }),

    ('russian-noun-masculine', {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
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
        'statements': {
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

    ('russian-noun-feminine', {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
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
        'statements': {
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

    ('russian-noun-neuter', {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
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
        'statements': {
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

    ('russian-noun-pluraletantum', {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
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
        'statements': {
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

    ('russian-adjective', {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
        'label': 'русское прилагательное',
        'language_item_id': 'Q7737',
        'language_code': 'ru',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'ед.ч. м.р. им.п.',
                'example': 'Это [хороший] дом.',
                'grammatical_features_item_ids': ['Q131105', 'Q499327', 'Q110786'],
            },
            {
                'label': 'ед.ч. м.р. род.п.',
                'example': 'Нет [хорошего] дома.',
                'grammatical_features_item_ids': ['Q146233', 'Q499327', 'Q110786'],
            },
            {
                'label': 'ед.ч. м.р. дат.п.',
                'example': 'Дать [хорошему] дому.',
                'grammatical_features_item_ids': ['Q145599', 'Q499327', 'Q110786'],
            },
            {
                'label': 'ед.ч. м.р. неодушевл. вин.п.',
                'example': 'Вижу [хороший] дом.',
                'grammatical_features_item_ids': ['Q146078', 'Q499327', 'Q51927539', 'Q52943434', 'Q110786'],
            },
            {
                'label': 'ед.ч. м.р. одушевл. вин.п.',
                'example': 'Вижу [хорошего] человека.',
                'grammatical_features_item_ids': ['Q146078', 'Q499327', 'Q51927507', 'Q54020116', 'Q110786'],
            },
            {
                'label': 'ед.ч. м.р. твор.п.',
                'example': 'Руковожу [хорошим] домом.',
                'grammatical_features_item_ids': ['Q192997', 'Q499327', 'Q110786'],
            },
            {
                'label': 'ед.ч. м.р. предл.п.',
                'example': 'Говорить о [хорошем] доме.',
                'grammatical_features_item_ids': ['Q2114906', 'Q499327', 'Q110786'],
            },
            {
                'label': 'ед.ч. ж.р. им.п.',
                'example': 'Это [хорошая] еда.',
                'grammatical_features_item_ids': ['Q131105', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'ед.ч. ж.р. род.п.',
                'example': 'Нет [хорошей] еды.',
                'grammatical_features_item_ids': ['Q146233', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'ед.ч. ж.р. дат.п.',
                'example': 'Дать [хорошей] еде.',
                'grammatical_features_item_ids': ['Q145599', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'ед.ч. ж.р. вин.п.',
                'example': 'Вижу [хорошую] еду.',
                'grammatical_features_item_ids': ['Q146078', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'ед.ч. ж.р. твор.п.',
                'example': 'Восхищаюсь [хорошей] едой.',
                'grammatical_features_item_ids': ['Q192997', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'ед.ч. ж.р. предл.п.',
                'example': 'Говорить о [хорошей] еде.',
                'grammatical_features_item_ids': ['Q2114906', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'ед.ч. ср.р. им.п.',
                'example': 'Это [хорошее] облако.',
                'grammatical_features_item_ids': ['Q131105', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'ед.ч. ср.р. род.п.',
                'example': 'Нет [хорошего] облака.',
                'grammatical_features_item_ids': ['Q146233', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'ед.ч. ср.р. дат.п.',
                'example': 'Дать [хорошему] облаку.',
                'grammatical_features_item_ids': ['Q145599', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'ед.ч. ср.р. вин.п.',
                'example': 'Вижу [хорошее] облако.',
                'grammatical_features_item_ids': ['Q146078', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'ед.ч. ср.р. твор.п.',
                'example': 'Руковожу [хорошим] облаком.',
                'grammatical_features_item_ids': ['Q192997', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'ед.ч. ср.р. предл.п.',
                'example': 'Говорить о [хорошем] облаке.',
                'grammatical_features_item_ids': ['Q2114906', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это [хорошие] дома/девочки/облака.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет [хороших] домов/девочек/облаков.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать [хорошим] домам/девочкам/облакам.',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'мн.ч. одушевл. вин.п.',
                'example': 'Вижу [хороших] людей/девочек.',
                'grammatical_features_item_ids': ['Q146078', 'Q51927507', 'Q146786'],
            },
            {
                'label': 'мн.ч. неодушевл. вин.п.',
                'example': 'Вижу [хорошие] дома/жизни/облака.',
                'grammatical_features_item_ids': ['Q146078', 'Q51927539', 'Q146786'],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу [хорошими] домами/девочками/облаками.',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о [хороших] домах/девочках/облаках.',
                'grammatical_features_item_ids': ['Q2114906', 'Q146786'],
            },
        ],
    }),

    ('swedish-noun-common', {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt substantiv (utrum)',
        'language_item_id': 'Q9027',
        'language_code': 'sv',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativ singular, obestämd',
                'example': 'Det här är en [bil].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'nominativ singular, bestämd',
                'example': 'Den nya [bilen].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'nominativ plural, obestämd',
                'example': 'Jag ser flera [bilar].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'nominativ plural, bestämd',
                'example': 'De nya [bilarna].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q53997851'],
            },
            {
                'label': 'genitiv singular, obestämd',
                'example': 'En [bils] utseende.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'genitiv singular, bestämd',
                'example': 'Den här [bilens] utseende.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'genitiv plural, obestämd',
                'example': 'Många [bilars] utseende.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'genitiv plural, bestämd',
                'example': 'De här [bilarnas] utseende.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q53997851'],
            },
        ],
        'statements': {
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
                                'id': 'Q1305037',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),

    ('swedish-noun-neuter', {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt substantiv (neutrum)',
        'language_item_id': 'Q9027',
        'language_code': 'sv',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativ singular, obestämd',
                'example': 'Det här är ett [bord].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'nominativ singular, bestämd',
                'example': 'Det nya [bordet].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'nominativ plural, obestämd',
                'example': 'Jag ser flera [bord].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'nominativ plural, bestämd',
                'example': 'De nya [borden].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786', 'Q53997851'],
            },
            {
                'label': 'genitiv singular, obestämd',
                'example': 'Ett [bords] utseende.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q53997857'],
            },
            {
                'label': 'genitiv singular, bestämd',
                'example': 'Det här [bordets] utseende.',
                'grammatical_features_item_ids': ['Q146233', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'genitiv plural, obestämd',
                'example': 'Många [bords] utseende.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q53997857'],
            },
            {
                'label': 'genitiv plural, bestämd',
                'example': 'De här [bordens] utseende.',
                'grammatical_features_item_ids': ['Q146233', 'Q146786', 'Q53997851'],
            },
        ],
        'statements': {
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

    ('swedish-verb', {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt verb',
        'language_item_id': 'Q9027',
        'language_code': 'sv',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'infinitiv aktiv',
                'example': 'Att [läsa] är bra.',
                'grammatical_features_item_ids': ['Q179230', 'Q1317831'],
            },
            {
                'label': 'presens aktiv',
                'example': 'Hen [läser] varje dag.',
                'grammatical_features_item_ids': ['Q192613', 'Q1317831'],
            },
            {
                'label': 'preteritum aktiv',
                'example': 'Hen [läste] igår.',
                'grammatical_features_item_ids': ['Q442485', 'Q1317831'],
            },
            {
                'label': 'supinum aktiv',
                'example': 'Hen har [läst] hela dagen.',
                'grammatical_features_item_ids': ['Q548470', 'Q1317831'],
            },
            {
                'label': 'imperativ',
                'example': '[läs] nu!',
                'grammatical_features_item_ids': ['Q22716'],
            },
            {
                'label': 'infinitiv passiv',
                'example': 'Det ska [läsas].',
                'grammatical_features_item_ids': ['Q179230', 'Q1194697'],
            },
            {
                'label': 'presens passiv',
                'example': 'Det [läses] varje dag.',
                'grammatical_features_item_ids': ['Q192613', 'Q1194697'],
            },
            {
                'label': 'preteritum passiv',
                'example': 'Det [lästes] igår.',
                'grammatical_features_item_ids': ['Q442485', 'Q1194697'],
            },
            {
                'label': 'supinum passiv',
                'example': 'Det har [lästs] hela dagen.',
                'grammatical_features_item_ids': ['Q548470', 'Q1194697'],
            },
        ],
    }),

    ('swedish-absolute-adjective', {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt adjektiv (utan komparativ)',
        'language_item_id': 'Q9027',
        'language_code': 'sv',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'obestämd singular, utrum',
                'example': 'en [tolvårig] pojke',
                'grammatical_features_item_ids': ['Q53997857', 'Q110786', 'Q1305037', 'Q3482678'],
            },
            {
                'label': 'obestämd singular, neutrum',
                'example': 'ett [tolvårigt] barn',
                'grammatical_features_item_ids': ['Q53997857', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': 'bestämd singular, maskulinum',
                'example': 'den [tolvårige] pojken',
                'grammatical_features_item_ids': ['Q53997851', 'Q110786', 'Q499327', 'Q3482678'],
            },
            {
                'label': 'bestämd singular, utrum/neutrum',
                'example': 'det [tolvåriga] barnet',
                'grammatical_features_item_ids': ['Q53997851', 'Q110786', 'Q3482678'],
            },
            {
                'label': 'bestämd plural',
                'example': 'de [tolvåriga] barnen',
                'grammatical_features_item_ids': ['Q53997851', 'Q146786', 'Q3482678'],
            },
        ],
        'statements': {
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
                                'id': 'Q332375',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
    }),

    ('ukrainian-noun-masculine', {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, чоловічий рід',
        'language_item_id': 'Q8798',
        'language_code': 'uk',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'однина, називний відмінок',
                'example': 'Це [будинок].',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'однина, родовий відмінок',
                'example': 'Це відноситься до [будинка].',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'однина, давальний відмінок',
                'example': 'Це належить [будинку].',
                'grammatical_features_item_ids': ['Q110786', 'Q145599'],
            },
            {
                'label': 'однина, знахідний відмінок',
                'example': 'Я бачу [будинок].',
                'grammatical_features_item_ids': ['Q110786', 'Q146078'],
            },
            {
                'label': 'однина, орудний відмінок',
                'example': 'Я керую цим [будинком].',
                'grammatical_features_item_ids': ['Q110786', 'Q192997'],
            },
            {
                'label': 'однина, місцевий відмінок',
                'example': 'Воно знаходиться в [будинку].',
                'grammatical_features_item_ids': ['Q110786', 'Q202142'],
            },
            {
                'label': 'однина, кличний відмінок',
                'example': 'Привіт, [будинку].',
                'grammatical_features_item_ids': ['Q110786', 'Q185077'],
            },
            {
                'label': 'множина, називний відмінок',
                'example': 'Це [будинки].',
                'grammatical_features_item_ids': ['Q146786', 'Q131105'],
            },
            {
                'label': 'множина, родовий відмінок',
                'example': 'Це відноситься до [будинків].',
                'grammatical_features_item_ids': ['Q146786', 'Q146233'],
            },
            {
                'label': 'множина, давальний відмінок',
                'example': 'Це належить [будинкам].',
                'grammatical_features_item_ids': ['Q146786', 'Q145599'],
            },
            {
                'label': 'множина, знахідний відмінок',
                'example': 'Я бачу [будинки].',
                'grammatical_features_item_ids': ['Q146786', 'Q146078'],
            },
            {
                'label': 'множина, орудний відмінок',
                'example': 'Я керую цими [будинками].',
                'grammatical_features_item_ids': ['Q146786', 'Q192997'],
            },
            {
                'label': 'множина, місцевий відмінок',
                'example': 'Вони знаходиться в [будинках].',
                'grammatical_features_item_ids': ['Q146786', 'Q202142'],
            },
            {
                'label': 'множина, кличний відмінок',
                'example': 'Привіт, [будинки].',
                'grammatical_features_item_ids': ['Q146786', 'Q185077'],
            },
        ],
        'statements': {
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

    ('ukrainian-noun-feminine', {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, жіночий рід',
        'language_item_id': 'Q8798',
        'language_code': 'uk',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'однина, називний відмінок',
                'example': 'Це [будівля].',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'однина, родовий відмінок',
                'example': 'Це відноситься до [будівлі].',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'однина, давальний відмінок',
                'example': 'Це належить [будівлі].',
                'grammatical_features_item_ids': ['Q110786', 'Q145599'],
            },
            {
                'label': 'однина, знахідний відмінок',
                'example': 'Я бачу [будівлю].',
                'grammatical_features_item_ids': ['Q110786', 'Q146078'],
            },
            {
                'label': 'однина, орудний відмінок',
                'example': 'Я керую цією [будівлею].',
                'grammatical_features_item_ids': ['Q110786', 'Q192997'],
            },
            {
                'label': 'однина, місцевий відмінок',
                'example': 'Воно знаходиться в [будівлі].',
                'grammatical_features_item_ids': ['Q110786', 'Q202142'],
            },
            {
                'label': 'однина, кличний відмінок',
                'example': 'Привіт, [будівле].',
                'grammatical_features_item_ids': ['Q110786', 'Q185077'],
            },
            {
                'label': 'множина, називний відмінок',
                'example': 'Це [будівлі].',
                'grammatical_features_item_ids': ['Q146786', 'Q131105'],
            },
            {
                'label': 'множина, родовий відмінок',
                'example': 'Це відноситься до [будівель].',
                'grammatical_features_item_ids': ['Q146786', 'Q146233'],
            },
            {
                'label': 'множина, давальний відмінок',
                'example': 'Це належить [будівлям].',
                'grammatical_features_item_ids': ['Q146786', 'Q145599'],
            },
            {
                'label': 'множина, знахідний відмінок',
                'example': 'Я бачу [будівлі].',
                'grammatical_features_item_ids': ['Q146786', 'Q146078'],
            },
            {
                'label': 'множина, орудний відмінок',
                'example': 'Я керую цими [будівлями].',
                'grammatical_features_item_ids': ['Q146786', 'Q192997'],
            },
            {
                'label': 'множина, місцевий відмінок',
                'example': 'Вони знаходиться в [будівлях].',
                'grammatical_features_item_ids': ['Q146786', 'Q202142'],
            },
            {
                'label': 'множина, кличний відмінок',
                'example': 'Привіт, [будівлі].',
                'grammatical_features_item_ids': ['Q146786', 'Q185077'],
            },
        ],
        'statements': {
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

    ('ukrainian-noun-neuter', {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, середній рід',
        'language_item_id': 'Q8798',
        'language_code': 'uk',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'однина, називний відмінок',
                'example': 'Це [серце].',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'однина, родовий відмінок',
                'example': 'Це відноситься до [серця].',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'однина, давальний відмінок',
                'example': 'Це належить [серцю].',
                'grammatical_features_item_ids': ['Q110786', 'Q145599'],
            },
            {
                'label': 'однина, знахідний відмінок',
                'example': 'Я бачу [серце].',
                'grammatical_features_item_ids': ['Q110786', 'Q146078'],
            },
            {
                'label': 'однина, орудний відмінок',
                'example': 'Я живу із цим [серцем].',
                'grammatical_features_item_ids': ['Q110786', 'Q192997'],
            },
            {
                'label': 'однина, місцевий відмінок',
                'example': 'Воно знаходиться в [серці].',
                'grammatical_features_item_ids': ['Q110786', 'Q202142'],
            },
            {
                'label': 'однина, кличний відмінок',
                'example': 'Привіт, [серцю].',
                'grammatical_features_item_ids': ['Q110786', 'Q185077'],
            },
            {
                'label': 'множина, називний відмінок',
                'example': 'Це [серця].',
                'grammatical_features_item_ids': ['Q146786', 'Q131105'],
            },
            {
                'label': 'множина, родовий відмінок',
                'example': 'Це відноситься до [сердець].',
                'grammatical_features_item_ids': ['Q146786', 'Q146233'],
            },
            {
                'label': 'множина, давальний відмінок',
                'example': 'Це належить [серцям].',
                'grammatical_features_item_ids': ['Q146786', 'Q145599'],
            },
            {
                'label': 'множина, знахідний відмінок',
                'example': 'Я бачу [серця].',
                'grammatical_features_item_ids': ['Q146786', 'Q146078'],
            },
            {
                'label': 'множина, орудний відмінок',
                'example': 'Кохання між цими [серцями].',
                'grammatical_features_item_ids': ['Q146786', 'Q192997'],
            },
            {
                'label': 'множина, місцевий відмінок',
                'example': 'Вони знаходиться в [серцях].',
                'grammatical_features_item_ids': ['Q146786', 'Q202142'],
            },
            {
                'label': 'множина, кличний відмінок',
                'example': 'Привіт, [серця].',
                'grammatical_features_item_ids': ['Q146786', 'Q185077'],
            },
        ],
        'statements': {
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

    ('ukrainian-noun-pluraletantum', {
        '@attribution': {'users': ['Tohaomg', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, тільки множина (pluralia tantum)',
        'language_item_id': 'Q8798',
        'language_code': 'uk',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'називний відмінок',
                'example': 'Це [ножиці].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'родовий відмінок',
                'example': 'Ніде нема [ножиць].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'давальний відмінок',
                'example': 'Віддати це [ножицям].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'знахідний відмінок',
                'example': 'Я бачу [ножиці].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'орудний відмінок',
                'example': 'Я користуюсь цими [ножицями].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
            {
                'label': 'місцевий відмінок',
                'example': 'Папір застряг в [ножицях].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': 'кличний відмінок',
                'example': 'Привіт, [ножиці].',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
        ],
        'statements': {
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

    ('german-noun-neuter-test', {
        '@attribution': {'users': ['Lucas Werkmeister']},
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
                'statements': {
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
                'statements': {
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
        'statements': {
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

for template_name, template in templates.items():
    template['@template_name'] = template_name
