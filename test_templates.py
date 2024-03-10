import mwapi  # type: ignore
import pytest

import app
from language import lang_lex2int
import templates
import translations
from wikibase_types import Statements


test_user_agent = 'lexeme-forms test (https://lexeme-forms.toolforge.org/; mail@lucaswerkmeister.de)'


def test_statement_value():
    assert templates.statement('P1', 'Q1') == {
        'type': 'statement',
        'rank': 'normal',
        'mainsnak': {
            'snaktype': 'value',
            'property': 'P1',
            'datatype': 'wikibase-item',
            'datavalue': {
                'type': 'wikibase-entityid',
                'value': {
                    'entity-type': 'item',
                    'id': 'Q1',
                },
            },
        },
    }


def test_statement_somevalue():
    assert templates.statement('P1', 'somevalue') == {
        'type': 'statement',
        'rank': 'normal',
        'mainsnak': {
            'snaktype': 'somevalue',
            'property': 'P1',
            'datatype': 'wikibase-item',
        },
    }


def test_statement_novalue():
    assert templates.statement('P1', 'novalue') == {
        'type': 'statement',
        'rank': 'normal',
        'mainsnak': {
            'snaktype': 'novalue',
            'property': 'P1',
            'datatype': 'wikibase-item',
        },
    }


def test_statements_pair():
    assert templates.statements('P1', 'Q1') == {
        'P1': [
            {
                'type': 'statement',
                'rank': 'normal',
                'mainsnak': {
                    'snaktype': 'value',
                    'property': 'P1',
                    'datatype': 'wikibase-item',
                    'datavalue': {
                        'type': 'wikibase-entityid',
                        'value': {
                            'entity-type': 'item',
                            'id': 'Q1',
                        },
                    },
                },
            },
        ],
    }


def test_statements_dict():
    assert templates.statements({
        'P1': 'somevalue',
        'P2': ['novalue', 'Q2'],
    }) == {
        'P1': [
            {
                'type': 'statement',
                'rank': 'normal',
                'mainsnak': {
                    'snaktype': 'somevalue',
                    'property': 'P1',
                    'datatype': 'wikibase-item',
                },
            },
        ],
        'P2': [
            {
                'type': 'statement',
                'rank': 'normal',
                'mainsnak': {
                    'snaktype': 'novalue',
                    'property': 'P2',
                    'datatype': 'wikibase-item',
                },
            },
            {
                'type': 'statement',
                'rank': 'normal',
                'mainsnak': {
                    'snaktype': 'value',
                    'property': 'P2',
                    'datatype': 'wikibase-item',
                    'datavalue': {
                        'type': 'wikibase-entityid',
                        'value': {
                            'entity-type': 'item',
                            'id': 'Q2',
                        },
                    },
                },
            },
        ],
    }


def test_entities_exist():
    entity_ids = set()

    def add_from_statements(statements: Statements):
        for property_id, statement_group in statements.items():
            entity_ids.add(property_id)
            for statement in statement_group:
                if statement['mainsnak']['snaktype'] == 'value':
                    entity_ids.add(statement['mainsnak']['datavalue']['value']['id'])

    for template in templates.templates_without_redirects.values():
        if template.get('test', False):
            continue
        entity_ids.add(template['language_item_id'])
        entity_ids.add(template['lexical_category_item_id'])
        for form in template['forms']:
            entity_ids.update(form['grammatical_features_item_ids'])
            add_from_statements(form.get('statements', {}))
        add_from_statements(template.get('statements', {}))

    entity_ids = list(entity_ids)
    session = mwapi.Session('https://www.wikidata.org', user_agent=test_user_agent)
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
        for entity_id in chunk:
            if entity_id not in result['entities']:
                missing_entity_ids.add(entity_id)

    assert not missing_entity_ids


def test_wikifunctions_signatures():
    """Assert that all referenced Wikifunctions exist, are functions,
    have exactly one string parameter and return a string or list of strings."""
    wikifunctions_ids = set()
    for template in templates.templates_without_redirects.values():
        for form in template['forms']:
            for wikifunctions in form.get('wikifunctions', {}).values():
                wikifunctions_ids.add(wikifunctions)
    type_string = 'Z6'
    type_list_of_strings = {
        'Z1K1': 'Z7',
        'Z7K1': 'Z881',  # list
        'Z881K1': type_string,
    }

    wikifunctions_ids = list(wikifunctions_ids)
    session = mwapi.Session('https://www.wikifunctions.org', user_agent=test_user_agent)
    missing_wikifunctions_ids = set()
    non_function_wikifunctions_ids = set()
    bad_params_wikifunctions_ids = {}
    bad_return_wikifunctions_ids = {}
    while wikifunctions_ids:
        chunk, wikifunctions_ids = wikifunctions_ids[:50], wikifunctions_ids[50:]
        result = session.get(action='query',
                             list='wikilambdaload_zobjects',
                             wikilambdaload_zids=chunk,
                             formatversion=2)
        for wikifunctions_id in chunk:
            if not result['query']['wikilambdaload_zobjects'][wikifunctions_id]['success']:
                missing_wikifunctions_ids.add(wikifunctions_id)
                continue
            zobject = result['query']['wikilambdaload_zobjects'][wikifunctions_id]['data']
            zfunction = zobject['Z2K2']
            if zfunction['Z1K1'] != 'Z8':
                non_function_wikifunctions_ids.add(wikifunctions_id)
                continue
            assert zfunction['Z8K1'][0] == 'Z17'
            parameter_types = [
                parameter['Z17K1']
                for parameter in zfunction['Z8K1'][1:]
            ]
            if parameter_types != [type_string]:
                bad_params_wikifunctions_ids[wikifunctions_id] = parameter_types
                continue
            return_type = zfunction['Z8K2']
            if return_type != type_string and return_type != type_list_of_strings:
                bad_return_wikifunctions_ids[wikifunctions_id] = return_type

    assert not missing_wikifunctions_ids
    assert not non_function_wikifunctions_ids
    assert not bad_params_wikifunctions_ids
    assert not bad_return_wikifunctions_ids


def test_translations_available():
    missing_language_codes = set()
    for template in templates.templates_without_redirects.values():
        language_code = lang_lex2int(template['language_code'])
        if language_code not in translations.translations:
            missing_language_codes.add(language_code)

    # lack of translations accepted for now
    missing_language_codes.remove('an')
    missing_language_codes.remove('mt')

    # special case
    if 'zh' in missing_language_codes:
        if 'zh-hans' in translations.translations or 'zh-hant' in translations.translations:
            missing_language_codes.remove('zh')

    assert not missing_language_codes


@pytest.mark.parametrize('template_name', templates.templates_without_redirects.keys())
def test_template_labels_not_identifiers(template_name):
    template = templates.templates_without_redirects[template_name]
    assert template_name != template['label']


def test_template_labels_distinct_per_language():
    template_names_by_language_and_label = {}
    for template_name, template in templates.templates_without_redirects.items():
        template_names_by_language_and_label\
            .setdefault(template['language_code'], {})\
            .setdefault(template['label'], [])\
            .append(template_name)
    ambiguous_template_names_by_language_and_label = {}
    for language, template_names_by_label in template_names_by_language_and_label.items():
        for template_label, template_names in template_names_by_label.items():
            if len(template_names) > 1:
                ambiguous_template_names_by_language_and_label.setdefault(language, {})[template_label] = template_names
    assert not ambiguous_template_names_by_language_and_label


def test_template_language_lexical_category_item_ids_disjoint():
    language_item_ids = {}
    lexical_category_item_ids = {}
    for template_name, template in templates.templates_without_redirects.items():
        language_item_ids.setdefault(template['language_item_id'], set())\
                         .add(template_name)
        lexical_category_item_ids.setdefault(template['lexical_category_item_id'], set())\
                                 .add(template_name)
    shared = {
        item_id: (language_item_ids[item_id], lexical_category_item_ids[item_id])
        for item_id in language_item_ids
        if item_id in lexical_category_item_ids
    }
    assert not shared


expected_label_counts = {
    'breton-noun-with-mutation-ktp': {
        'unander': 3,
        'liester': 3,
    },
    'breton-noun-with-mutation-gdb': {
        'unander': 3,
        'liester': 3,
    },
    'breton-noun-with-mutation-m': {
        'unander': 2,
        'liester': 2,
    },
    'czech-verb-perfective': {
        'infinitiv': 2,
    },
    'czech-verb-imperfective': {
        'infinitiv': 2,
    },
    'spanish-verb': {
        'segunda persona singular del imperativo': 3,
        'segunda persona plural del imperativo': 2,
    },
}


@pytest.mark.parametrize('template_name', templates.templates_without_redirects.keys())
def test_labels_distinct(template_name):
    template = templates.templates_without_redirects[template_name]
    labels = {}
    for form in template['forms']:
        label = form['label']
        labels[label] = labels.get(label, 0) + 1
    actual_counts = {label: count for label, count in labels.items() if count > 1}
    expected_counts = expected_label_counts.get(template_name, {})
    assert actual_counts == expected_counts


@pytest.mark.parametrize('template_name, form', [
    (template_name, form)
    for template_name, template in templates.templates_without_redirects.items()
    for form in template['forms']
])
def test_labels_not_valid_examples(template_name, form):
    fake_form = {'example': form['label']}
    with pytest.raises(Exception):
        app.split_example(fake_form)
        print(form['label'])  # unreachable, prints only if test fails


@pytest.mark.parametrize('template_name, form', [
    (template_name, form)
    for template_name, template in templates.templates_without_redirects.items()
    for form in template['forms']
])
def test_examples_valid(template_name, form):
    prefix, placeholder, suffix = app.split_example(form)
    assert placeholder != ''


@pytest.mark.parametrize('template_name, form', [
    (template_name, form)
    for template_name, template in templates.templates_without_redirects.items()
    for form in template['forms']
])
def test_examples_no_misleading_capitalization(template_name, form):
    """Examples like '[Come] here.' can mislead users
    into entering forms with wrong capitalization."""
    prefix, placeholder, suffix = app.split_example(form)
    assert prefix != '' or placeholder.lower() == placeholder


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
    'manbhumi-verb': {
        'উ [ভাইলবেক]।': 2,
        'উনি [ভাইলবেন]।': 2,
    },
    'czech-verb-imperfective': {
        'Ona byla [zpívána].': 2,
        'Ona to včera [zpívala].': 2,
    },
    'czech-verb-perfective': {
        'Ona by [postavila].': 2,
    },
}


@pytest.mark.parametrize('template_name', templates.templates_without_redirects.keys())
def test_examples_distinct(template_name):
    template = templates.templates_without_redirects[template_name]
    examples = {}
    for form in template['forms']:
        example = form['example']
        examples[example] = examples.get(example, 0) + 1
    actual_counts = {example: count for example, count in examples.items() if count > 1}
    expected_counts = expected_example_counts.get(template_name, {})
    assert actual_counts == expected_counts


@pytest.mark.parametrize('template_name, form', [
    (template_name, form)
    for template_name, template in templates.templates_without_redirects.items()
    for form in template['forms']
])
def test_grammatical_feature_item_ids_distinct(template_name, form):
    grammatical_features_item_ids = form['grammatical_features_item_ids']
    assert len(set(grammatical_features_item_ids)) == len(grammatical_features_item_ids)


@pytest.mark.parametrize('template_name, form', [
    (template_name, form)
    for template_name, template in templates.templates_without_redirects.items()
    for form in template['forms']
    if 'grammatical_features_item_ids_optional' in form
])
def test_optional_grammatical_features_subset(template_name, form):
    """Check that grammatical features specified as optional are actually
    grammatical features of the form.

    It doesn’t make sense to have an optional feature which is not
    going to be added or used for matching."""
    assert form['grammatical_features_item_ids_optional'].issubset(form['grammatical_features_item_ids'])


@pytest.mark.parametrize('template_name', templates.templates_without_redirects.keys())
def test_attribution_available(template_name):
    template = templates.templates_without_redirects[template_name]
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


@pytest.mark.parametrize('template_name', templates.templates_without_redirects.keys())
def test_sections_declared(template_name):
    """Check that every template whose forms contain section breaks also
    declares whether its sections should have two columns or not in
    the header.

    The inverse case, that a template declares two-column sections but
    has no section breaks, is allowed, since it can be useful to have
    all forms in a single two-column section. However, a template may
    not declare that it does *not* use two-column sections in that
    case, since that would be redundant.

    """
    template = templates.templates_without_redirects[template_name]
    has_section_breaks = False
    for form in template['forms']:
        if form.get('section_break', False):
            has_section_breaks = True
            break
    if has_section_breaks:
        assert 'two_column_sections' in template
    else:
        assert template.get('two_column_sections', True)


# exceptions from test_optional_forms_last_in_section
template_names_with_mixed_optional_forms = {
    'malayalam-noun',
    'bokmål-noun-masculine-neuter',
}


@pytest.mark.parametrize('template_name', templates.templates_without_redirects.keys())
def test_optional_forms_last_in_section(template_name):
    """Check that within each section of a template,
    optional forms come after all non-optional forms.

    Templates don’t usually have non-optional forms
    after optional forms until the next section break,
    but forgetting to mark a form as optional
    is a frequent mistake when transcribing templates.
    """
    if template_name in template_names_with_mixed_optional_forms:
        return
    template = templates.templates_without_redirects[template_name]
    had_optional_form = False
    index = 0
    for form in template['forms']:
        index += 1
        if form.get('section_break', False):
            had_optional_form = False
        if form.get('optional', False):
            had_optional_form = True
        else:
            assert not had_optional_form, \
                f'form #{index} ({form["label"]}) is non-optional but follows an optional form without a section break'


@pytest.mark.parametrize('template_name', templates.templates_without_redirects.keys())
def test_wikifunctions_intro_requires_wikifunctions(template_name):
    """Check that templates with a wikifunctions_intro have at least one form with wikifunctions."""
    template = templates.templates_without_redirects[template_name]
    if 'wikifunctions_intro' not in template:
        return
    for form in template['forms']:
        if form.get('wikifunctions', {}):
            return
    assert False, "Template has wikifunctions_intro but no form has nonempty wikifunctions"


@pytest.mark.parametrize('template_name', templates.templates_without_redirects.keys())
def test_labels_examples_trimmed(template_name):
    """Check that labels and examples have no surrounding whitespace.

    These are usually in a <dd> element on the wiki page,
    and Firefox prepends them with four spaces when copying them.
    Those spaces should thus be removed during the transcription process
    (usually with a blanket replace `'    ` → `'`).
    """
    template = templates.templates_without_redirects[template_name]
    assert template['label'].strip() == template['label']
    for form in template['forms']:
        assert form['label'].strip() == form['label']
        assert form['example'].strip() == form['example']


@pytest.mark.parametrize('template_name', [
    template_name
    for template_name, template in templates.templates.items()
    if isinstance(template, (str, list))
])
def test_redirects_resolve_directly(template_name):
    template = templates.templates[template_name]
    if isinstance(template, str):
        template = [template]
    for target in template:
        assert target in templates.templates
        assert target in templates.templates_without_redirects

@pytest.mark.parametrize('template_name', [
    template_name
    for template_name, template in templates.templates.items()
    if isinstance(template, list)
])
def test_ambiguous_templates(template_name):
    """Check that ambiguous templates (where the replacement is a list)
    are actually ambiguous, i.e. have more than one replacement template.

    Otherwise, the single replacement should be specified as a string instead,
    so that we can directly redirect to it."""
    template = templates.templates[template_name]
    assert len(template) > 1


@pytest.mark.parametrize('hi_template_name', [
    template_name
    for template_name, template in templates.templates_without_redirects.items()
    if template['language_code'] == 'hi'
])
def test_hindustani_templates_match(hi_template_name):
    """Test that Hindustani template pairs match.

    Hindustani is modeled via pairs of templates,
    one for Hindi (hi) and one for Urdu (ur);
    apart from the labels and examples (different scripts),
    they should be identical."""
    assert hi_template_name.endswith('-hi')
    ur_template_name = hi_template_name[:-len('-hi')] + '-ur'
    assert ur_template_name in templates.templates
    hi_template = templates.templates[hi_template_name]
    ur_template = templates.templates[ur_template_name]
    assert hi_template['language_item_id'] == 'Q11051'
    assert ur_template['language_item_id'] == 'Q11051'
    assert hi_template['language_code'] == 'hi'
    assert ur_template['language_code'] == 'ur'
    assert_templates_match(hi_template, ur_template)


@pytest.mark.parametrize('pnb_template_name', [
    template_name
    for template_name, template in templates.templates_without_redirects.items()
    if template['language_code'] == 'pnb'
])
def test_punjabi_templates_match(pnb_template_name):
    """Test that Punjabi template pairs match.

    Punjabi is modeled via pairs of templates,
    one for Shahmukhi (pnb) and one for Gurmukhi (pa);
    apart from the labels and examples (different scripts),
    they should be identical."""
    assert pnb_template_name.endswith('-shah')
    pa_template_name = pnb_template_name[:-len('-shah')] + '-guru'
    assert pa_template_name in templates.templates
    pnb_template = templates.templates[pnb_template_name]
    pa_template = templates.templates[pa_template_name]
    assert pnb_template['language_item_id'] == 'Q58635'
    assert pa_template['language_item_id'] == 'Q58635'
    assert pnb_template['language_code'] == 'pnb'
    assert pa_template['language_code'] == 'pa'
    assert_templates_match(pnb_template, pa_template)


def assert_templates_match(a_template, b_template):
    assert a_template['lexical_category_item_id'] == b_template['lexical_category_item_id']
    assert a_template.get('two_column_sections') == b_template.get('two_column_sections')
    assert a_template.get('statements') == b_template.get('statements')
    assert len(a_template['forms']) == len(b_template['forms'])
    for a_form, b_form in zip(a_template['forms'], b_template['forms']):
        assert a_form['grammatical_features_item_ids'] == b_form['grammatical_features_item_ids']
        assert a_form.get('grammatical_features_item_ids_optional') == b_form.get('grammatical_features_item_ids_optional')
        assert a_form.get('optional') == b_form.get('optional')
        assert a_form.get('statements') == b_form.get('statements')
