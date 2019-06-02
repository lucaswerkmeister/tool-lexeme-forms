import mwapi

import templates
import translations


def test_entities_exist():
    entity_ids = set()
    for template in templates.templates.values():
        if template.get('test', False):
            continue
        entity_ids.add(template['language_item_id'])
        entity_ids.add(template['lexical_category_item_id'])
        for form in template['forms']:
            entity_ids.update(form['grammatical_features_item_ids'])
        for property_id, statement_group in template.get('claims', {}).items():
            entity_ids.add(property_id)
            for statement in statement_group:
                entity_ids.add(statement['mainsnak']['datavalue']['value']['id'])

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
