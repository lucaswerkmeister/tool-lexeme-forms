templates = {
    'german-noun-masculine': {
        'label': 'Deutsches Substantiv (Maskulinum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'Nominativ singular',
                'example': 'Das ist der [Hund].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv singular',
                'example': 'Das Eigentum des [Hundes].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ singular',
                'example': 'Das gehört dem [Hund].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ singular',
                'example': 'Ich mag den [Hund].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ plural',
                'example': 'Das sind die [Hunde].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv plural',
                'example': 'Das Eigentum der [Hunde].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ plural',
                'example': 'Das gehört den [Hunden].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ plural',
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
        'submit': 'Anlegen',
    },
    'german-noun-masculine-test': {
        'test': True,
        'label': 'Deutsches Substantiv (Maskulinum), test.wikidata.org',
        'language_item_id': 'Q348',
        'language_code': 'de',
        'lexical_category_item_id': 'Q92595',
        'forms': [
            {
                'label': 'Nominativ singular',
                'example': 'Das ist der [Hund].',
                'grammatical_features_item_ids': ['Q163012', 'Q163014'],
            },
            {
                'label': 'Genitiv singular',
                'example': 'Das Eigentum des [Hundes].',
                'grammatical_features_item_ids': ['Q163013', 'Q163014'],
            },
            {
                'label': 'Dativ singular',
                'example': 'Das gehört dem [Hund].',
                'grammatical_features_item_ids': ['Q163016', 'Q163014'],
            },
            {
                'label': 'Akkusativ singular',
                'example': 'Ich mag den [Hund].',
                'grammatical_features_item_ids': ['Q163017', 'Q163014'],
            },
            {
                'label': 'Nominativ plural',
                'example': 'Das sind die [Hunde].',
                'grammatical_features_item_ids': ['Q163012', 'Q160570'],
            },
            {
                'label': 'Genitiv plural',
                'example': 'Das Eigentum der [Hunde].',
                'grammatical_features_item_ids': ['Q163013', 'Q160570'],
            },
            {
                'label': 'Dativ plural',
                'example': 'Das gehört den [Hunden].',
                'grammatical_features_item_ids': ['Q163016', 'Q160570'],
            },
            {
                'label': 'Akkusativ plural',
                'example': 'Ich mag die [Hunde].',
                'grammatical_features_item_ids': ['Q163017', 'Q160570'],
            },
        ],
        'claims': {
            'P5185': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P73601',
                        'datatype': 'wikibase-item',
                        'datavalue': {
                            'type': 'wikibase-entityid',
                            'value': {
                                'entity-type': 'item',
                                'id': 'Q165755',
                            },
                        },
                    },
                    'type': 'statement',
                    'rank': 'normal',
                }
            ],
        },
        'submit': 'Anlegen',
    },
}
