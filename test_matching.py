import matching
import templates


def make_statement(property_id, item_id):
    return {
        'mainsnak': {
            'snaktype': 'value',
            'property': property_id,
            'datatype': 'wikibase-item',
            'datavalue': {
                'type': 'wikibase-entityid',
                'value': {
                    'entity-type': 'item',
                    'id': item_id,
                },
            },
        },
        'type': 'statement',
        'rank': 'normal',
    }


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


def test_match_lexeme_form_to_template_form_missing_grammatical_feature():
    lexeme_form = {'grammaticalFeatures': ['Q1', 'Q3']}
    template_form = {'grammatical_features_item_ids': ['Q1', 'Q2', 'Q3']}
    assert matching.match_lexeme_form_to_template_form(False, lexeme_form, template_form) == 0

def test_match_lexeme_form_to_template_form_missing_statement():
    lexeme_form = {'grammaticalFeatures': ['Q1']}
    template_form = {
        'grammatical_features_item_ids': ['Q1'],
        'statements': {'P31': [make_statement('P31', 'Q4115189')]},
    }
    assert matching.match_lexeme_form_to_template_form(False, lexeme_form, template_form) == 0

def test_match_lexeme_form_to_template_form_conflicting_statement():
    lexeme_form = {
        'grammaticalFeatures': ['Q1'],
        'claims': {'P5185': [make_statement('P5185', 'Q4115189'), make_statement('P5185', 'Q13406268')]},
    }
    template_form = {
        'grammatical_features_item_ids': ['Q1'],
        'statements': {'P5185': [make_statement('P5185', 'Q4115189')]},
    }
    assert matching.match_lexeme_form_to_template_form(False, lexeme_form, template_form) == 0

def test_match_lexeme_form_to_template_form_counts_grammatical_features_and_statements():
    lexeme_form = {
        'grammaticalFeatures': ['Q1', 'Q2', 'Q3', 'Q4'],
        'claims': {
            'P31': [make_statement('P31', 'Q4115189'), make_statement('P31', 'Q13406268')],
            'P5185': [make_statement('P5185', 'Q4115189')],
        },
    }
    template_form = {
        'grammatical_features_item_ids': ['Q1', 'Q2'],
        'statements': {
            'P31': [make_statement('P31', 'Q4115189')],
            'P5185': [make_statement('P5185', 'Q4115189')],
        },
    }
    assert matching.match_lexeme_form_to_template_form(False, lexeme_form, template_form) == 4
