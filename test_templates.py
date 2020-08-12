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
    session = mwapi.Session('https://www.wikidata.org', user_agent='lexeme-forms test (https://lexeme-forms.toolforge.org/; mail@lucaswerkmeister.de)')
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


@pytest.mark.parametrize('template_name, form', [
    (template_name, form)
    for template_name in templates.templates.keys()
    for form in templates.templates[template_name]['forms']
])
def test_labels_not_valid_examples(template_name, form):
    fake_form = {'example': form['label']}
    with pytest.raises(Exception):
        app.split_example(fake_form)


@pytest.mark.parametrize('template_name, form', [
    (template_name, form)
    for template_name in templates.templates.keys()
    for form in templates.templates[template_name]['forms']
])
def test_examples_valid(template_name, form):
    prefix, placeholder, suffix = app.split_example(form)
    assert placeholder != ''


expected_example_counts = {
    'bengali-verb': {
        'তুমি [দেখো]।': 2,
        'সে [দেখুক]।': 2,
        'তিনি [দেখুন]।': 2,
        'তুই [দেখিস]।': 3,
        'সে [দেখবে]।': 2,
        'সে [দেখিবে]।': 2,
        'তিনি [দেখবেন]।': 2,
        'তিনি [দেখিবেন]।': 2,
    },
    'bengali-verb-ano': {
        'তুমি [দেখাও]।': 3,
        'তুই [দেখাস]।': 3,
        'তিনি [দেখান]।': 3,
        'সে [দেখাক]।': 2,
        'সে [দেখাবে]।': 2,
        'সে [দেখাইবে]।': 2,
        'তিনি [দেখাবেন]।': 2,
        'তিনি [দেখাইবেন]।': 2,
    },
    'czech-verb-perfective': {
        'Ona by [zazpívala].': 2,
    }
}


@pytest.mark.parametrize('template_name', templates.templates.keys())
def test_examples_distinct(template_name):
    template = templates.templates[template_name]
    examples = {}
    for form in template['forms']:
        example = form['example']
        examples[example] = examples.get(example, 0) + 1
    actual_counts = { example: count for example, count in examples.items() if count > 1 }
    expected_counts = expected_example_counts.get(template_name, {})
    assert actual_counts == expected_counts


@pytest.mark.parametrize('template_name, form', [
    (template_name, form)
    for template_name in templates.templates.keys()
    for form in templates.templates[template_name]['forms']
])
def test_grammatical_feature_item_ids_distinct(template_name, form):
    grammatical_features_item_ids = form['grammatical_features_item_ids']
    assert len(set(grammatical_features_item_ids)) == len(grammatical_features_item_ids)


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


@pytest.mark.parametrize('template_name', templates.templates.keys())
def test_sections_declared(template_name):
    """Check that every template whose forms contain section breaks also
    declares that it has sections in the header.

    The inverse case, that a template declares sections but has no
    section breaks, is allowed, since it can be useful to have all
    forms in a single two-column section.
    """
    template = templates.templates[template_name]
    has_sections = False
    for form in template['forms']:
        if form.get('section_break', False):
            has_sections = True
            break
    if has_sections:
        assert template.get('has_sections', False)
