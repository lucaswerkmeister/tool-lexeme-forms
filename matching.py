# whether the presence of some statement for a property
# rules the lexeme out as a match for a template
# with a different statement for that property
properties_exclusive = {
    'www': {
        # other “instance of” are likely unrelated and okay
        'P31': False,
        # other “grammatical gender” are incompatible
        'P5185': True,
        # other “grammatical aspect” are incompatible
        'P7486': True,
    },
    'test': {
        # other “grammatical gender” are incompatible
        'P73601': False,
    },
}


def match_template_to_lexeme_data(template, lexeme_data):
    language_matches = template['language_item_id'] == lexeme_data['language']
    lexical_category_matches = template['lexical_category_item_id'] == lexeme_data['lexicalCategory']
    matched_statements, missing_statements, conflicting_statements = match_template_entity_to_lexeme_entity('test' in template, template, lexeme_data)

    return {
        'language': language_matches,
        'lexical_category': lexical_category_matches,
        'matched_statements': matched_statements,
        'missing_statements': missing_statements,
        'conflicting_statements': conflicting_statements,
    }


def match_template_entity_to_lexeme_entity(test, template_entity, lexeme_entity):
    matched_statements = {}
    missing_statements = {}
    conflicting_statements = {}

    properties_exclusive_for_template_entity = properties_exclusive['test' if test else 'www']
    for property_id in template_entity.get('statements', {}):
        property_exclusive = properties_exclusive_for_template_entity[property_id]
        for template_statement in template_entity['statements'][property_id]:
            found_matching_statement = False
            for lexeme_statement in lexeme_entity.get('claims', {}).get(property_id, []):
                if match_statement(template_statement, lexeme_statement):
                    found_matching_statement = True
                    if property_id not in matched_statements:
                        matched_statements[property_id] = []
                    matched_statements[property_id].append(lexeme_statement)
                elif property_exclusive:
                    if property_id not in conflicting_statements:
                        conflicting_statements[property_id] = []
                    conflicting_statements[property_id].append(lexeme_statement)

            if not found_matching_statement:
                if property_id not in missing_statements:
                    missing_statements[property_id] = []
                missing_statements[property_id].append(template_statement)

    return matched_statements, missing_statements, conflicting_statements


def match_statement(template_statement, lexeme_statement):
    # so far, we only compare the main snak (ignoring qualifiers and references),
    # and only support entity ID values, because that’s all the templates use
    if lexeme_statement['mainsnak']['snaktype'] == 'value':
        template_statement_value_id = template_statement['mainsnak']['datavalue']['value']['id']
        lexeme_statement_value_id = lexeme_statement['mainsnak']['datavalue']['value']['id']
        return template_statement_value_id == lexeme_statement_value_id
    else:
        return False
