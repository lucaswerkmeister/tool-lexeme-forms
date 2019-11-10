import mwapi
import pytest

import app
import templates
import translations


def test_entities_exist():
    entity_ids = set()
    def add_from_statements(statements):
        for property_id, statement_group in statements.items():
            entity_ids.add(property_id)
            for statement in statement_group:
                entity_ids.add(statement['mainsnak']['datavalue']['value']['id'])

    for template in templates.templates.values():
        if template.get('test', False):
            continue
        entity_ids.add(template['language_item_id'])
        entity_ids.add(template['lexical_category_item_id'])
        for form in template['forms']:
            entity_ids.update(form['grammatical_features_item_ids'])
            add_from_statements(form.get('statements', {}))
        add_from_statements(template.get('statements', {}))

    entity_ids = list(entity_ids)
    session = mwapi.Session('https://www.wikidata.org', user_agent='lexeme-forms test (https://tools.wmflabs.org/lexeme-forms; mail@lucaswerkmeister.de)')
    missing_entity_ids = set()
    while entity_ids:
        chunk, entity_ids = entity_ids[:50], entity_ids[50:]
        result = session.get(action='wbgetentities',
                             ids=chunk,
                             redirects='no',
                             props=[])
        for entity_id, entity in result['entities'].items():
            if 'missing' in entity:
                missing_entity_ids.add(entity_id)

    assert not missing_entity_ids


def test_translations_available():
    missing_language_codes = set()
    for template in templates.templates.values():
        language_code = template['language_code']
        if language_code not in translations.translations:
            missing_language_codes.add(language_code)

    assert not missing_language_codes


def test_examples_valid():
    for template in templates.templates.values():
        for form in template['forms']:
            app.split_example(form)


def test_examples_distinct():
    for template in templates.templates.values():
        examples = set()
        for form in template['forms']:
            example = form['example']
            if (example == 'Ev [gundek] e.' or
                example == 'Ez [gundekî] dibînim.'):
                # under discussion
                continue
            assert example not in examples
            examples.add(example)


@pytest.mark.parametrize('template_name', templates.templates.keys())
def test_attribution_available(template_name):
    template = templates.templates[template_name]
    assert '@attribution' in template
    attribution = template['@attribution']
    assert isinstance(attribution, dict)
    assert 'users' in attribution
    users = attribution['users']
    assert isinstance(users, list)
    assert users
    if not template.get('test', False):
        assert 'title' in attribution
        title = attribution['title']
        assert isinstance(title, str)
        assert title


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
    match = templates.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert match == {
        'language': True,
        'lexical_category': True,
        'matched_statements': lexeme_data_german_noun_neuter['claims'],
        'missing_statements': {},
        'conflicting_statements': {},
    }

def test_match_template_to_lexeme_data_missing_statement():
    template = templates.templates['german-noun-pluraletantum']
    match = templates.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert match == {
        'language': True,
        'lexical_category': True,
        'matched_statements': {},
        'missing_statements': template['statements'],
        'conflicting_statements': {},
    }

def test_match_template_to_lexeme_data_conflicting_statement():
    template = templates.templates['german-noun-masculine']
    match = templates.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert match == {
        'language': True,
        'lexical_category': True,
        'matched_statements': {},
        'missing_statements': template['statements'],
        'conflicting_statements': lexeme_data_german_noun_neuter['claims'],
    }

def test_match_template_to_lexeme_data_different_lexical_category():
    template = templates.templates['german-verb']
    match = templates.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert match['language']
    assert not match['lexical_category']

def test_match_template_to_lexeme_data_different_language():
    template = templates.templates['english-noun']
    match = templates.match_template_to_lexeme_data(template, lexeme_data_german_noun_neuter)

    assert not match['language']
    assert match['lexical_category']


def test_properties_exclusive_covers_template_claims_properties():
    missing_property_ids = set()
    for template in templates.templates.values():
        wiki = 'test' if 'test' in template else 'www'
        properties_exclusive_for_template = templates.properties_exclusive[wiki]
        for property_id in template.get('statements', {}).keys():
            if property_id not in properties_exclusive_for_template:
                missing_property_ids.add((wiki, property_id))

    assert not missing_property_ids
