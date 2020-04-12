import matching
import templates


lexeme_data_german_noun_neuter = {
    'lexicalCategory': 'Q1084',
    'language': 'Q188',
    'claims': {
        'P5185': [
            {
                'mainsnak': {
                    'snaktype': 'value',
                    'property': 'P5185',
                    'datavalue': {
                        'value': {
                            'entity-type': 'item',
                            'id': 'Q1775461',
                        },
                        'type': 'wikibase-entityid',
                    },
                    'datatype': 'wikibase-item',
                },
                'rank': 'normal',
                'this_comes_from_lexeme_data': True,
            },
        ],
    },
}

def test_match_template_to_lexeme_data_full_match():
    template = templates.templates['german-noun-neuter']
    match = matching.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert match == {
        'language': True,
        'lexical_category': True,
        'matched_statements': lexeme_data_german_noun_neuter['claims'],
        'missing_statements': {},
        'conflicting_statements': {},
    }

def test_match_template_to_lexeme_data_missing_statement():
    template = templates.templates['german-noun-pluraletantum']
    match = matching.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert match == {
        'language': True,
        'lexical_category': True,
        'matched_statements': {},
        'missing_statements': template['statements'],
        'conflicting_statements': {},
    }

def test_match_template_to_lexeme_data_conflicting_statement():
    template = templates.templates['german-noun-masculine']
    match = matching.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert match == {
        'language': True,
        'lexical_category': True,
        'matched_statements': {},
        'missing_statements': template['statements'],
        'conflicting_statements': lexeme_data_german_noun_neuter['claims'],
    }

def test_match_template_to_lexeme_data_different_lexical_category():
    template = templates.templates['german-verb']
    match = matching.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert match['language']
    assert not match['lexical_category']

def test_match_template_to_lexeme_data_different_language():
    template = templates.templates['english-noun']
    match = matching.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert not match['language']
    assert match['lexical_category']


def test_properties_exclusive_covers_template_claims_properties():
    missing_property_ids = set()
    for template in templates.templates.values():
        wiki = 'test' if 'test' in template else 'www'
        properties_exclusive_for_template = matching.properties_exclusive[wiki]
        for property_id in template.get('statements', {}).keys():
            if property_id not in properties_exclusive_for_template:
                missing_property_ids.add((wiki, property_id))
        for form in template['forms']:
            for property_id in form.get('statements', {}).keys():
                if property_id not in properties_exclusive_for_template:
                    missing_property_ids.add((wiki, property_id))

    assert not missing_property_ids
