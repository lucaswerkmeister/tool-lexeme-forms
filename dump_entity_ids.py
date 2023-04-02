#!/usr/bin/env python3
import mwapi  # type: ignore
import templates

all_entity_ids = set()

def add_from_statements(statements):
    for property_id, statement_group in statements.items():
        all_entity_ids.add(property_id)
        # for statement in statement_group:
        #     if statement['mainsnak']['snaktype'] == 'value':
        #         all_entity_ids.add(statement['mainsnak']['datavalue']['value']['id'])

for template in templates.templates_without_redirects.values():
    if template.get('test', False):
        continue
    # all_entity_ids.add(template['language_item_id'])
    # all_entity_ids.add(template['lexical_category_item_id'])
    for form in template['forms']:
        # all_entity_ids.update(form['grammatical_features_item_ids'])
        add_from_statements(form.get('statements', {}))
    add_from_statements(template.get('statements', {}))

entity_ids = sorted(all_entity_ids, key=lambda id: int(id[1:]))

session = mwapi.Session('https://www.wikidata.org', user_agent='lexeme-forms dump_entity_ids (https://lexeme-forms.toolforge.org/; mail@lucaswerkmeister.de)')
while entity_ids:
    chunk, entity_ids = entity_ids[:50], entity_ids[50:]
    result = session.get(action='wbgetentities',
                         ids=chunk,
                         redirects='no',
                         props=['labels'],
                         languages=['en'])
    for entity_id, entity in result['entities'].items():
        label = entity.get('labels', {}).get('en', {}).get('value')
        variable_name = label.replace(' ', '_')
        print(f'{variable_name} = {entity_id!r}')
