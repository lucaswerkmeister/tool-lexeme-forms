from typing import Dict, List, Optional, Set, TypedDict, Union

from wikibase_types import Statement, Statements


class CoreTemplateForm(TypedDict):
    label: str
    example: str
    grammatical_features_item_ids: List[str]

class TemplateForm(CoreTemplateForm, total=False):
    section_break: bool
    optional: bool
    grammatical_features_item_ids_optional: Set[str]
    statements: dict

class CoreTemplate(TypedDict):
    label: str
    language_item_id: str
    language_code: str
    lexical_category_item_id: str
    forms: List[TemplateForm]

class Attribution(TypedDict):
    users: List[str]
    title: Optional[str]

MetaTemplate = TypedDict('MetaTemplate', {
    '@attribution': Attribution,
    '@template_name': str,
}, total=False)

class Template(CoreTemplate, MetaTemplate, total=False):
    test: bool
    two_column_sections: bool
    statements: Statements


def statement(property_id: str, item_id: str) -> Statement:
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


def statements(property_id: str, item_id: str) -> Statements:
    return {
        property_id: [
            statement(property_id, item_id),
        ],
    }


templates: Dict[str, Union[str, list[str], Template]] = {

    'asturian-noun-masculine': {
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
        'statements': statements('P5185', 'Q499327'),
    },

    'asturian-noun-feminine': {
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'bengali-noun-animate': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'প্রাণীবাচক বিশেষ্য',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'কর্তৃকারক',
                'example': 'আমার [কুকুর] ওখানে গিয়েছে।',
                'grammatical_features_item_ids': ['Q131105'],
            },
            {
                'label': 'সম্বন্ধ পদ',
                'example': 'এটা আমার [কুকুরের] নাম।',
                'grammatical_features_item_ids': ['Q146233'],
            },
            {
                'label': 'কর্ম কারক',
                'example': 'আমার [কুকুরকে] পছন্দ হয়েছে?',
                'grammatical_features_item_ids': ['Q146078'],
            },
            {
                'label': 'সম্প্রদান কারক',
                'example': 'আমার [কুকুরকে] মাংস দিন।',
                'grammatical_features_item_ids': ['Q145599'],
            },
        ],
    },

    'bengali-noun-inanimate-othervowels': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'অপ্রাণীবাচক বিশেষ্য (-আ/এ/ও-কারান্ত শব্দ)',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'কর্তৃকারক',
                'example': 'আমার [জামা] রঙিন।',
                'grammatical_features_item_ids': ['Q131105'],
            },
            {
                'label': 'সম্বন্ধ পদ',
                'example': 'এই [জামার] রঙ নীল।',
                'grammatical_features_item_ids': ['Q146233'],
            },
            {
                'label': 'কর্ম কারক',
                'example': 'সে তার [জামাকে] ছিঁড়ে দিয়েছে।',
                'grammatical_features_item_ids': ['Q146078'],
            },
            {
                'label': 'অধিকরণ কারক (-য়-কারান্ত/-তে অক্ষরান্ত)',
                'example': 'ওর [জামায়/জামাতে] একটা দাগ আছে।',
                'grammatical_features_item_ids': ['Q202142'],
            },
        ],
    },

    'bengali-noun-inanimate-highvowels': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'অপ্রাণীবাচক বিশেষ্য (-ই/ঈ/উ/ঊ/ঐ/ঔ-কারান্ত শব্দ)',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'কর্তৃকারক',
                'example': 'এই [গাড়ি] চলতেছে।',
                'grammatical_features_item_ids': ['Q131105'],
            },
            {
                'label': 'সম্বন্ধ পদ',
                'example': 'এই [গাড়ির] রঙ লাল।',
                'grammatical_features_item_ids': ['Q146233'],
            },
            {
                'label': 'কর্ম কারক',
                'example': 'তার [গাড়িকে] লাল রঙ করে দিয়েছে।',
                'grammatical_features_item_ids': ['Q146078'],
            },
            {
                'label': 'অধিকরণ কারক',
                'example': 'শীঘ্রই [গাড়িতে] উঠুন!',
                'grammatical_features_item_ids': ['Q202142'],
            },
        ],
    },

    'bengali-noun-inanimate-consonants': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'অপ্রাণীবাচক বিশেষ্য (ব্যঞ্জনান্ত শব্দ)',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'কর্তৃকারক',
                'example': 'এই [আম] পেকে গেছে।',
                'grammatical_features_item_ids': ['Q131105'],
            },
            {
                'label': 'সম্বন্ধ পদ',
                'example': 'এই [আমের] খোসা লাল।',
                'grammatical_features_item_ids': ['Q146233'],
            },
            {
                'label': 'কর্ম কারক',
                'example': 'সে [আমকে] একটু আগে কাটল।',
                'grammatical_features_item_ids': ['Q146078'],
            },
            {
                'label': 'অধিকরণ কারক',
                'example': 'ওই [আমে] একটা দাগ আছে।',
                'grammatical_features_item_ids': ['Q202142'],
            },
        ],
    },

    'bengali-adjective-tatsama-property': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'তৎসম গুণবাচক বিশেষণ',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'এটি একটি [ক্ষুদ্র] জলাশয়।',
                'grammatical_features_item_ids': ['Q3482678'],
            },
            {
                'label': 'তুলনামূলক',
                'example': 'দুটির মধ্যে এটি [ক্ষুদ্রতর] জলাশয়।',
                'grammatical_features_item_ids': ['Q14169499'],
            },
            {
                'label': 'অতিশয়ার্থমূলক',
                'example': 'এই এলাকায় এটি [ক্ষুদ্রতম] জলাশয়।',
                'grammatical_features_item_ids': ['Q1817208'],
            },
        ],
    },

    'bengali-adjective-others': {
        '@attribution': {'users': ['Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'অন্যান্য বিশেষণ',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'এটি একটি [ছোট] ডোবা।',
                'grammatical_features_item_ids': ['Q3482678'],
            },
        ],
    },

    'bengali-adverb': {
        '@attribution': {'users': ['Mahir256', 'Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'ক্রিয়া বিশেষণ',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'ইনি [দ্রুত] করে দেবেন।',
                'grammatical_features_item_ids': ['Q3482678'],
            },
        ],
    },

    'bengali-verb': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256', 'Tanay barisha'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'ক্রিয়াপদ',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ভাববাচক বিশেষ্য',
                'example': 'আমার [দেখা] হল।',
                'grammatical_features_item_ids': ['Q1350145'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [দেখি]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q21714344'],
            },
            {
                'label': 'সাধারণ বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [দেখ]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650487'],
            },
            {
                'label': 'সাধারণ বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুই [দেখিস]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650485'],
            },
            {
                'label': 'সাধারণ বর্তমান, প্রথম পুরুষ',
                'example': 'সে [দেখে]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q51929074'],
            },
            {
                'label': 'সাধারণ বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'তিনি [দেখেন]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখছি]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিতেছি]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখছ]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিতেছ]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখছিস]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিতেছিস]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখছে]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিতেছে]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখছেন]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিতেছেন]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখেছি]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিয়াছি]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখেছ]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিয়াছ]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখেছিস]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিয়াছিস]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখেছে]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিয়াছে]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখেছেন]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিয়াছেন]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'বর্তমান অনুজ্ঞা, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [দেখো]।',
                'grammatical_features_item_ids': ['Q56650487', 'Q52434162'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুই [দেখ]।',
                'grammatical_features_item_ids': ['Q56650485', 'Q52434162'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখুক]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখুক]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখুন]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখুন]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখলাম]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিলাম]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখলে]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিলে]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখলি]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিলি]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখল]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিল]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখলেন]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিলেন]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখছিলাম]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিতেছিলাম]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখছিলে]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিতেছিলে]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখছিলি]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিতেছিলি]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখছিল]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিতেছিল]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখছিলেন]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিতেছিলেন]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখেছিলাম]।',
                'grammatical_features_item_ids': ['Q623742', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিয়াছিলাম]।',
                'grammatical_features_item_ids': ['Q623742', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখেছিলে]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিয়াছিলে]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখেছিলি]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিয়াছিলি]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখেছিল]।',
                'grammatical_features_item_ids': ['Q623742', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিয়াছিল]।',
                'grammatical_features_item_ids': ['Q623742', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখেছিলেন]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিয়াছিলেন]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখতাম]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিতাম]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখতে]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিতে]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখতিস]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিতিস]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখত]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিত]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখতেন]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিতেন]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখব]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিব]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখবি]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিবি]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখবেন]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিবেন]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখো]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিও]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখিস]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিস]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখবে]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিবে]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখবেন]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিবেন]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': 'আমি [দেখতে] চাই।',
                'grammatical_features_item_ids': ['Q1423674', 'Q1050494', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': 'আমি [দেখিতে] চাই।',
                'grammatical_features_item_ids': ['Q1423674', 'Q1050494', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': '[দেখে] গেছি।',
                'grammatical_features_item_ids': ['Q1424306', 'Q1050494', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': '[দেখিয়া] গিয়াছি।',
                'grammatical_features_item_ids': ['Q1424306', 'Q1050494', 'Q20613396'],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': 'এটা [দেখলে] ভালো লাগে।',
                'grammatical_features_item_ids': ['Q625581', 'Q1050494', 'Q75242466'],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': 'ইহা [দেখিলে] ভালো লাগে।',
                'grammatical_features_item_ids': ['Q625581', 'Q1050494', 'Q20613396'],
            },
            {
                'label': 'সম্বন্ধবাচক ভাববিশেষ্য, চলিত ভাষা',
                'example': 'আমি সেটা [দেখার/দেখবার] জন্য গেছিলাম।',
                'grammatical_features_item_ids': ['Q146233', 'Q1350145', 'Q75242466'],
            },
            {
                'label': 'সম্বন্ধবাচক ভাববিশেষ্য, সাধু ভাষা',
                'example': 'আমি তাহা [দেখিবার] জন্য গিয়াছিলাম।',
                'grammatical_features_item_ids': ['Q146233', 'Q1350145', 'Q20613396'],
            },
        ],
    },

    'bengali-verb-ano': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256', 'Tanay barisha'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'ক্রিয়াপদ (সাধিত ধাতু)',
        'language_item_id': 'Q9610',
        'language_code': 'bn',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ভাববাচক বিশেষ্য',
                'example': 'আমার [দেখানো] হল।',
                'grammatical_features_item_ids': ['Q1350145'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [দেখাই]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q21714344'],
            },
            {
                'label': 'সাধারণ বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [দেখাও]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650487'],
            },
            {
                'label': 'সাধারণ বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুই [দেখাস]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650485'],
            },
            {
                'label': 'সাধারণ বর্তমান, প্রথম পুরুষ',
                'example': 'সে [দেখায়]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q51929074'],
            },
            {
                'label': 'সাধারণ বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'তিনি [দেখান]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখাচ্ছি]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইতেছি]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাচ্ছ]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইতেছ]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাচ্ছিস]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইতেছিস]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাচ্ছে]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইতেছে]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাচ্ছেন]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইতেছেন]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখিয়েছি]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইয়াছি]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখিয়েছ]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইয়াছ]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখিয়েছিস]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইয়াছিস]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখিয়েছে]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইয়াছে]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখিয়েছেন]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইয়াছেন]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'বর্তমান অনুজ্ঞা, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [দেখাও]।',
                'grammatical_features_item_ids': ['Q56650487', 'Q52434162'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুই [দেখা]।',
                'grammatical_features_item_ids': ['Q56650485', 'Q52434162'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাক]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাক]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখান]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখান]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখালাম]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইলাম]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখালে]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইলে]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখালি]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইলি]।',
                'grammatical_features_item_ids': ['Q1305037', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাল]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইল]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখালেন]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইলেন]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখাচ্ছিলাম]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইতেছিলাম]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাচ্ছিলে]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইতেছিলে]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাচ্ছিলি]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইতেছিলি]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাচ্ছিল]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইতেছিল]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাচ্ছিলেন]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইতেছিলেন]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখিয়েছিলাম]।',
                'grammatical_features_item_ids': ['Q623742', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইয়াছিলাম]।',
                'grammatical_features_item_ids': ['Q623742', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখিয়েছিলে]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইয়াছিলে]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখিয়েছিলি]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইয়াছিলি]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখিয়েছিল]।',
                'grammatical_features_item_ids': ['Q623742', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইয়াছিল]।',
                'grammatical_features_item_ids': ['Q623742', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখিয়েছিলেন]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইয়াছিলেন]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখাতাম]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইতাম]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাতে]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইতে]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাতিস]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইতিস]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাত]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইত]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাতেন]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইতেন]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখাব]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q21714344', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইব]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q21714344', 'Q20613396'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাবি]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইবি]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাবেন]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইবেন]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাও]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650487', 'Q75242466'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইও]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650487', 'Q20613396'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাস]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650485', 'Q75242466'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাস]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650485', 'Q20613396'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাবে]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q51929074', 'Q75242466'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইবে]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q51929074', 'Q20613396'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাবেন]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650512', 'Q75242466'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইবেন]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650512', 'Q20613396'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': 'আমি [দেখাতে] চাই।',
                'grammatical_features_item_ids': ['Q1423674', 'Q1050494', 'Q75242466'],
            },
            {
                'label': 'ঘটমান অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': 'আমি [দেখাইতে] চাই।',
                'grammatical_features_item_ids': ['Q1423674', 'Q1050494', 'Q20613396'],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': '[দেখিয়ে] গেছি।',
                'grammatical_features_item_ids': ['Q1424306', 'Q1050494', 'Q75242466'],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': '[দেখাইয়া] গিয়াছি।',
                'grammatical_features_item_ids': ['Q1424306', 'Q1050494', 'Q20613396'],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': 'এটা [দেখালে] ভালো লাগে।',
                'grammatical_features_item_ids': ['Q625581', 'Q1050494', 'Q75242466'],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': 'ইহা [দেখাইলে] ভালো লাগে।',
                'grammatical_features_item_ids': ['Q625581', 'Q1050494', 'Q20613396'],
            },
            {
                'label': 'সম্বন্ধবাচক ভাববিশেষ্য, চলিত ভাষা',
                'example': 'আমি সেটা [দেখাবার] জন্য গেছিলাম।',
                'grammatical_features_item_ids': ['Q146233', 'Q1350145', 'Q75242466'],
            },
            {
                'label': 'সম্বন্ধবাচক ভাববিশেষ্য, সাধু ভাষা',
                'example': 'আমি তাহা [দেখাইবার] জন্য গিয়াছিলাম।',
                'grammatical_features_item_ids': ['Q146233', 'Q1350145', 'Q20613396'],
            },
        ],
    },

    'manbhumi-adjective': {
        '@attribution': {'users': ['Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Manbhumi'},
        'label': 'বিশেষণ',
        'language_item_id': 'Q6747180',
        'language_code': 'bn-x-Q6747180',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'উ [বেহায়া] লক বটে।',
                'grammatical_features_item_ids': ['Q3482678'],
            },
        ],
    },

    'manbhumi-adverb': {
        '@attribution': {'users': ['Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Manbhumi'},
        'label': 'ক্রিয়া বিশেষণ',
        'language_item_id': 'Q6747180',
        'language_code': 'bn-x-Q6747180',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'উ [ঝট্‌] কর‍্যে চল্যে যাবেক।',
                'grammatical_features_item_ids': ['Q3482678'],
            },
        ],
    },

    'manbhumi-verb': {
        '@attribution': {'users': ['Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Manbhumi'},
        'label': 'ক্রিয়াপদ',
        'language_item_id': 'Q6747180',
        'language_code': 'bn-x-Q6747180',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ভাববাচক বিশেষ্য',
                'example': 'আমার [ভালা] হল।',
                'grammatical_features_item_ids': ['Q1350145'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [ভালি]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q21714344'],
            },
            {
                'label': 'সাধারণ বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাল]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650487'],
            },
            {
                'label': 'সাধারণ বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভালিস]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650485'],
            },
            {
                'label': 'সাধারণ বর্তমান, প্রথম পুরুষ',
                'example': 'উ [ভালে]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q51929074'],
            },
            {
                'label': 'সাধারণ বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভালেন]।',
                'grammatical_features_item_ids': ['Q3910936', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [ভাইলছি]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q21714344'],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলছ]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650487'],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলছিস]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650485'],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ',
                'example': 'উ [ভাইলছে]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q51929074'],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলছেন]।',
                'grammatical_features_item_ids': ['Q7240943', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [ভাইলেছি]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q21714344'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলেছ]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650487'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলেছিস]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650485'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ',
                'example': 'উ [ভাইলেছে]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q51929074'],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলেছেন]।',
                'grammatical_features_item_ids': ['Q1240211', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'বর্তমান অনুজ্ঞা, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভালো]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q56650487'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাল্‌]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q56650485'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ',
                'example': 'উ [ভালুক]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q51929074'],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভালুন]।',
                'grammatical_features_item_ids': ['Q52434162', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ অতীত, উত্তম পুরুষ',
                'example': 'আমি [ভাইললম/ভাইললি]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q21714344'],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইললে]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650487'],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইললি/ভাইললিস]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650485'],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ',
                'example': 'উ [ভাইলল/ভাইললক/ভাইললেক]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q51929074'],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইললেন]।',
                'grammatical_features_item_ids': ['Q1392475', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অতীত, উত্তম পুরুষ',
                'example': 'আমি [ভাইলছিলম/ভাইলতেছিলম/ভাইলছিলি/ভাইলতেছিলি]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q21714344'],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলছিলে/ভাইলতেছিলে]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650487'],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলছিলি/ভাইলছিলিস/ভাইলতেছিলি/ভাইলতেছিলিস]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650485'],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ',
                'example': 'উ [ভাইলছিল/ভাইলতেছিল/ভাইলছিলক/ভাইলতেছিলক/ভাইলছিলেক/ভাইলতেছিলেক]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q51929074'],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলছিলেন/ভাইলতেছিলেন]।',
                'grammatical_features_item_ids': ['Q56650537', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ',
                'example': 'আমি [ভাইলেছিলম/ভাইলেছিলি]।',
                'grammatical_features_item_ids': ['Q623742', 'Q21714344'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলেছিলে]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650487'],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলেছিলি/ভাইলেছিলিস]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650485'],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ',
                'example': 'উ [ভাইলেছিল/ভাইলেছিলক/ভাইলেছিলেক]।',
                'grammatical_features_item_ids': ['Q623742', 'Q51929074'],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলেছিলেন]।',
                'grammatical_features_item_ids': ['Q623742', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ',
                'example': 'আমি [ভাইলতম/ভাইলতি/ভাইলথম/ভাইলথি]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q21714344'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলতে/ভাইলথে]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650487'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলতি/ভাইলতিস/ভাইলথি/ভাইলথিস]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650485'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ',
                'example': 'উ [ভাইলত/ভাইলতক/ভাইলতেক/ভাইলথ/ভাইলথক/ভাইলথেক]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q51929074'],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলতেন]।',
                'grammatical_features_item_ids': ['Q75243920', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ',
                'example': 'আমি [ভাইলব]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q21714344'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলবে]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650487'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলবি/ভাইলবিস]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650485'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ',
                'example': 'উ [ভাইলবেক]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q51929074'],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলবেন]।',
                'grammatical_features_item_ids': ['Q96323395', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলো]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650487'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলিস]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650485'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ',
                'example': 'উ [ভাইলবেক]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q51929074'],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলবেন]।',
                'grammatical_features_item_ids': ['Q75244800', 'Q56650512'],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অসমাপিকা ক্রিয়া',
                'example': 'আমি [ভাইলতে] চাই।',
                'grammatical_features_item_ids': ['Q1423674', 'Q1050494'],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া',
                'example': 'উয়ার পানে [ভালি/ভাইলে/ভালাঁই] গেইলছি।',
                'grammatical_features_item_ids': ['Q1424306', 'Q1050494'],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া',
                'example': 'ইটা [ভাইললে] ভালো লাগে।',
                'grammatical_features_item_ids': ['Q625581', 'Q1050494'],
            },
        ],
    },

    'breton-noun-without-mutation': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (hep kemmadur)',
        'language_item_id': 'Q12107',
        'language_code': 'br',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'unander',
                'example': 'Ma [levr] zo amañ.',
                'grammatical_features_item_ids': ['Q110786'],
            },
            {
                'label': 'liester',
                'example': 'Ma [levrioù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786'],
            },
        ],
    },

    'breton-noun-without-mutation-collective': {
        '@attribution': {'users': ['VIGNERON'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (strollder, hep kemmadur)',
        'language_item_id': 'Q12107',
        'language_code': 'br',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'strollder',
                'example': 'Ma [stered] zo amañ.',
                'grammatical_features_item_ids': ['Q694268'],
            },
            {
                'label': 'unanderenn',
                'example': 'Ma [steredenn] zo amañ.',
                'grammatical_features_item_ids': ['Q1450795'],
            },
        ],
    },

    'breton-noun-with-mutation-ktp': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (gant kemmadur, ktp)',
        'language_item_id': 'Q12107',
        'language_code': 'br',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'unander',
                'example': 'Ho [tad] zo amañ.',
                'grammatical_features_item_ids': ['Q110786', 'Q101252532'],
            },
            {
                'label': 'unander',
                'example': 'Da [dad] zo amañ.',
                'grammatical_features_item_ids': ['Q110786', 'Q56648699'],
            },
            {
                'label': 'unander',
                'example': 'Ma [zad] zo amañ.',
                'grammatical_features_item_ids': ['Q110786', 'Q56648701'],
            },
            {
                'label': 'liester',
                'example': 'Hon [tadoù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786', 'Q101252532'],
            },
            {
                'label': 'liester',
                'example': 'Da [dadoù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786', 'Q56648699'],
            },
            {
                'label': 'liester',
                'example': 'Ma [zadoù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786', 'Q56648701'],
            },
        ],
    },

    'breton-noun-with-mutation-gdb': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (gant kemmadur, gdb)',
        'language_item_id': 'Q12107',
        'language_code': 'br',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'unander',
                'example': 'Ma [bag] zo amañ.',
                'grammatical_features_item_ids': ['Q110786', 'Q101252532'],
            },
            {
                'label': 'unander',
                'example': 'Da [vag] zo amañ.',
                'grammatical_features_item_ids': ['Q110786', 'Q56648699'],
            },
            {
                'label': 'unander',
                'example': 'Ho [pag] zo amañ.',
                'grammatical_features_item_ids': ['Q110786', 'Q56648701'],
            },
            {
                'label': 'liester',
                'example': 'Ma [bagoù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786', 'Q101252532'],
            },
            {
                'label': 'liester',
                'example': 'Da [vagoù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786', 'Q56648699'],
            },
            {
                'label': 'liester',
                'example': 'Ho [pagoù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786', 'Q56648701'],
            },
        ],
    },

    'breton-noun-with-mutation-m': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (gant kemmadur, m)',
        'language_item_id': 'Q12107',
        'language_code': 'br',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'unander',
                'example': 'Ho [mamm] zo amañ.',
                'grammatical_features_item_ids': ['Q110786', 'Q101252532'],
            },
            {
                'label': 'unander',
                'example': 'Ma [vamm] zo amañ.',
                'grammatical_features_item_ids': ['Q110786', 'Q56648699'],
            },
            {
                'label': 'liester',
                'example': 'Ho [mammoù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786', 'Q101252532'],
            },
            {
                'label': 'liester',
                'example': 'Ma [vammoù] zo amañ.',
                'grammatical_features_item_ids': ['Q146786', 'Q56648699'],
            },
        ],
    },

    'breton-adjective-without-mutation': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-gwan (hep kemmadur)',
        'language_item_id': 'Q12107',
        'language_code': 'br',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'derez-plaen',
                'example': 'Un dra [ledan] eo.',
                'grammatical_features_item_ids': ['Q3482678'],
            },
            {
                'label': 'derez-uheloc\'h',
                'example': 'Un dra [ledanoc\'h] eo.',
                'grammatical_features_item_ids': ['Q14169499'],
            },
            {
                'label': 'derez-uhelañ',
                'example': 'An dra [ledanañ] eo.',
                'grammatical_features_item_ids': ['Q1817208'],
            },
            {
                'label': 'derez-estlammiñ',
                'example': '[ledanat] tra !',
                'grammatical_features_item_ids': ['Q93868909'],
            },
        ],
    },

    'breton-adverb': {
        '@attribution': {'users': ['VIGNERON'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'adverb',
        'language_item_id': 'Q12107',
        'language_code': 'br',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'adverb',
                'example': 'Un dra zo [ivez].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'czech-noun-masculine-animate': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod mužský životný)',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                statement('P5185', 'Q499327'),
                statement('P5185', 'Q54020116'),
            ],
        },
    },

    'czech-noun-masculine-inanimate': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod mužský neživotný)',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                statement('P5185', 'Q499327'),
                statement('P5185', 'Q52943434'),
            ],
        },
    },

    'czech-noun-feminine': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod ženský)',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'czech-noun-neuter': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod střední)',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775461'),
    },

    'czech-adverb': {
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
    },

    'czech-adjective': {
        '@attribution': {'users': ['Strepon', 'Adrijaned'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české přídavné jméno',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q34698',
        'two_column_sections': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
    },

    'czech-verb-perfective': {
        '@attribution': {'users': ['Adrijaned', 'Strepon', 'Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české sloveso dokonavé',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': False,
        'forms': [
            {
                'label': 'infinitiv',
                'example': '[postavit].',
                'grammatical_features_item_ids': ['Q179230'],
            },
            {
                'label': 'infinitiv',
                'example': '[postaviti].',
                'grammatical_features_item_ids': ['Q179230'],
                'statements': statements('P6191', 'Q61857234'),
            },
            {
                'section_break': True,
                'label': '1. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Já teď [postavím].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q682111', 'Q192613'],
            },
            {
                'label': '2. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Ty teď [postavíš].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q682111', 'Q192613'],
            },
            {
                'label': '3. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Ono to teď [postaví].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q682111', 'Q192613'],
            },
            {
                'label': '1. osoba, množné číslo, oznamovací způsob',
                'example': 'My teď [postavíme].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q682111', 'Q192613'],
            },
            {
                'label': '2. osoba, množné číslo, oznamovací způsob',
                'example': 'Vy teď [postavíte].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q682111', 'Q192613'],
            },
            {
                'label': '3. osoba, množné číslo, oznamovací způsob',
                'example': 'Oni teď [postaví].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q682111', 'Q192613'],
            },
            {
                'section_break': True,
                'label': 'rozkazovací způsob, 2. osoba, jednotné číslo',
                'example': 'Ty [postav]!',
                'grammatical_features_item_ids': ['Q22716', 'Q51929049', 'Q110786'],
            },
            {
                'label': 'rozkazovací způsob, 1. osoba, množné číslo',
                'example': 'My [postavme]!',
                'grammatical_features_item_ids': ['Q22716', 'Q21714344', 'Q146786'],
            },
            {
                'label': 'rozkazovací způsob, 2. osoba, množné číslo',
                'example': 'Vy [postavte]!',
                'grammatical_features_item_ids': ['Q22716', 'Q51929049', 'Q146786'],
            },
            {
                'section_break': True,
                'label': 'příčestí činné, rod mužský životný, jednotné číslo',
                'example': 'On by [postavil].',
                'grammatical_features_item_ids': ['Q72249355', 'Q54020116', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, jednotné číslo',
                'example': 'Ten by [postavil].',
                'grammatical_features_item_ids': ['Q72249355', 'Q52943434', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod ženský, jednotné číslo',
                'example': 'Ona by [postavila].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod střední, jednotné číslo',
                'example': 'Ono by [postavilo].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod mužský životný, množné číslo',
                'example': 'Oni muži by [postavili].',
                'grammatical_features_item_ids': ['Q72249355', 'Q54020116', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, množné číslo',
                'example': 'Ty hrady by [postavily].',
                'grammatical_features_item_ids': ['Q72249355', 'Q52943434', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod ženský, množné číslo',
                'example': 'Ony by [postavily].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775415', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod střední, množné číslo',
                'example': 'Ona by [postavila].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775461', 'Q146786'],
            },
            {
                'section_break': True,
                'label': 'příčestí trpné, rod mužský životný, jednotné číslo',
                'example': 'On bude [postaven].',
                'grammatical_features_item_ids': ['Q72249544', 'Q54020116', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, jednotné číslo',
                'example': 'Ten bude [postaven].',
                'grammatical_features_item_ids': ['Q72249544', 'Q52943434', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod ženský, jednotné číslo',
                'example': 'Ona bude [postavena].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod střední, jednotné číslo',
                'example': 'Ono bude [postaveno].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod mužský životný, množné číslo',
                'example': 'Oni muži budou [postaveni].',
                'grammatical_features_item_ids': ['Q72249544', 'Q54020116', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, množné číslo',
                'example': 'Ty hrady budou [postaveny].',
                'grammatical_features_item_ids': ['Q72249544', 'Q52943434', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod ženský, množné číslo',
                'example': 'Ony budou [postaveny].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775415', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod střední, množné číslo',
                'example': 'Ona budou [postavena].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775461', 'Q146786'],
            },
            {
                'section_break': True,
                'label': 'přechodník minulý, rod mužský životný, jednotné číslo',
                'example': 'On [postaviv], odešel.',
                'grammatical_features_item_ids': ['Q65540485', 'Q54020116', 'Q110786'],
            },
            {
                'label': 'přechodník minulý, rod mužský neživotný, jednotné číslo',
                'example': 'Ten [postaviv], zmizel.',
                'grammatical_features_item_ids': ['Q65540485', 'Q52943434', 'Q110786'],
            },
            {
                'label': 'přechodník minulý, rod ženský, jednotné číslo',
                'example': 'Ona [postavivši], odešla.',
                'grammatical_features_item_ids': ['Q65540485', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'přechodník minulý, rod střední, jednotné číslo',
                'example': 'Ono [postavivši], odešlo.',
                'grammatical_features_item_ids': ['Q65540485', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'přechodník minulý, rod mužský životný, množné číslo',
                'example': 'Oni [postavivše], odešli.',
                'grammatical_features_item_ids': ['Q65540485', 'Q54020116', 'Q146786'],
            },
            {
                'label': 'přechodník minulý, rod mužský neživotný, množné číslo',
                'example': 'Ty [postavivše], zmizely.',
                'grammatical_features_item_ids': ['Q65540485', 'Q52943434', 'Q146786'],
            },
            {
                'label': 'přechodník minulý, rod ženský, množné číslo',
                'example': 'Ony [postavivše], odešly.',
                'grammatical_features_item_ids': ['Q65540485', 'Q1775415', 'Q146786'],
            },
            {
                'label': 'přechodník minulý, rod střední, množné číslo',
                'example': 'Ona [postavivše], odešla.',
                'grammatical_features_item_ids': ['Q65540485', 'Q1775461', 'Q146786'],
            },
        ],
        'statements': statements('P7486', 'Q1424306'),
    },

    'czech-verb-imperfective': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české sloveso nedokonavé',
        'language_item_id': 'Q9056',
        'language_code': 'cs',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': False,
        'forms': [
            {
                'label': 'infinitiv',
                'example': '[zpívat].',
                'grammatical_features_item_ids': ['Q179230'],
            },
            {
                'label': 'infinitiv',
                'example': '[zpívati].',
                'grammatical_features_item_ids': ['Q179230'],
                'statements': statements('P6191', 'Q61857234'),
            },
            {
                'section_break': True,
                'label': '1. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Já [zpívám].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q682111', 'Q192613'],
            },
            {
                'label': '2. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Ty [zpíváš].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q682111', 'Q192613'],
            },
            {
                'label': '3. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Ona [zpívá].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q682111', 'Q192613'],
            },
            {
                'label': '1. osoba, množné číslo, oznamovací způsob',
                'example': 'My [zpíváme].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q682111', 'Q192613'],
            },
            {
                'label': '2. osoba, množné číslo, oznamovací způsob',
                'example': 'Vy [zpíváte].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q682111', 'Q192613'],
            },
            {
                'label': '3. osoba, množné číslo, oznamovací způsob',
                'example': 'Oni [zpívají].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q682111', 'Q192613'],
            },
            {
                'section_break': True,
                'label': 'rozkazovací způsob, 2. osoba, jednotné číslo',
                'example': '(Ty) [zpívej]!',
                'grammatical_features_item_ids': ['Q22716', 'Q51929049', 'Q110786'],
            },
            {
                'label': 'rozkazovací způsob, 1. osoba, množné číslo',
                'example': '(My) [zpívejme]!',
                'grammatical_features_item_ids': ['Q22716', 'Q21714344', 'Q146786'],
            },
            {
                'label': 'rozkazovací způsob, 2. osoba, množné číslo',
                'example': '(Vy) [zpívejte]!',
                'grammatical_features_item_ids': ['Q22716', 'Q51929049', 'Q146786'],
            },
            {
                'section_break': True,
                'label': 'příčestí činné, rod mužský životný, jednotné číslo',
                'example': 'On to včera [zpíval].',
                'grammatical_features_item_ids': ['Q72249355', 'Q54020116', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, jednotné číslo',
                'example': 'Celý sál to včera [zpíval].',
                'grammatical_features_item_ids': ['Q72249355', 'Q52943434', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod ženský, jednotné číslo',
                'example': 'Ona to včera [zpívala].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod střední, jednotné číslo',
                'example': 'Ono to včera [zpívalo].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'příčestí činné, rod mužský životný, množné číslo',
                'example': 'Oni to včera [zpívali].',
                'grammatical_features_item_ids': ['Q72249355', 'Q54020116', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, množné číslo',
                'example': 'Celé sály to včera [zpívaly].',
                'grammatical_features_item_ids': ['Q72249355', 'Q52943434', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod ženský, množné číslo',
                'example': 'Ony to včera [zpívaly].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775415', 'Q146786'],
            },
            {
                'label': 'příčestí činné, rod střední, množné číslo',
                'example': 'Ona to včera [zpívala].',
                'grammatical_features_item_ids': ['Q72249355', 'Q1775461', 'Q146786'],
            },
            {
                'section_break': True,
                'label': 'příčestí trpné, rod mužský životný, jednotné číslo',
                'example': 'On byl [zpíván].',
                'grammatical_features_item_ids': ['Q72249544', 'Q54020116', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, jednotné číslo',
                'example': 'Ten byl [zpíván].',
                'grammatical_features_item_ids': ['Q72249544', 'Q52943434', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod ženský, jednotné číslo',
                'example': 'Ona byla [zpívána].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod střední, jednotné číslo',
                'example': 'Ono bylo [zpíváno].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'příčestí trpné, rod mužský životný, množné číslo',
                'example': 'Oni byli [zpíváni].',
                'grammatical_features_item_ids': ['Q72249544', 'Q54020116', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, množné číslo',
                'example': 'Hrady byly [zpívány].',
                'grammatical_features_item_ids': ['Q72249544', 'Q52943434', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod ženský, množné číslo',
                'example': 'Ony byly [zpívány].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775415', 'Q146786'],
            },
            {
                'label': 'příčestí trpné, rod střední, množné číslo',
                'example': 'Ona byla [zpívána].',
                'grammatical_features_item_ids': ['Q72249544', 'Q1775461', 'Q146786'],
            },
            {
                'section_break': True,
                'label': 'přechodník přítomný, rod mužský životný, jednotné číslo',
                'example': 'On [zpívaje] odešel.',
                'grammatical_features_item_ids': ['Q65540125', 'Q54020116', 'Q110786'],
            },
            {
                'label': 'přechodník přítomný, rod mužský neživotný, jednotné číslo',
                'example': 'Hrad [zpívaje] zmizel.',
                'grammatical_features_item_ids': ['Q65540125', 'Q52943434', 'Q110786'],
            },
            {
                'label': 'přechodník přítomný, rod ženský, jednotné číslo',
                'example': 'Ona [zpívajíc] odešla.',
                'grammatical_features_item_ids': ['Q65540125', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'přechodník přítomný, rod střední, jednotné číslo',
                'example': 'Ono [zpívajíc] odešlo.',
                'grammatical_features_item_ids': ['Q65540125', 'Q1775461', 'Q110786'],
            },
            {
                'label': 'přechodník přítomný, rod mužský životný, množné číslo',
                'example': 'Oni [zpívajíce] odešli.',
                'grammatical_features_item_ids': ['Q65540125', 'Q54020116', 'Q146786'],
            },
            {
                'label': 'přechodník přítomný, rod mužský neživotný, množné číslo',
                'example': 'Hrady [zpívajíce] zmizely.',
                'grammatical_features_item_ids': ['Q65540125', 'Q52943434', 'Q146786'],
            },
            {
                'label': 'přechodník přítomný, rod ženský, množné číslo',
                'example': 'Ony [zpívajíce] odešly.',
                'grammatical_features_item_ids': ['Q65540125', 'Q1775415', 'Q146786'],
            },
            {
                'label': 'přechodník přítomný, rod střední, množné číslo',
                'example': 'Ona [zpívajíce] odešla.',
                'grammatical_features_item_ids': ['Q65540125', 'Q1775461', 'Q146786'],
            },
        ],
        'statements': statements('P7486', 'Q371427'),
    },

    'danish-noun-common': {
        '@attribution': {'users': ['So9q', 'Fnielsen'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk substantiv (fælleskøn)',
        'language_item_id': 'Q9035',
        'language_code': 'da',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1305037'),
    },

    'danish-noun-neuter': {
        '@attribution': {'users': ['So9q', 'Fnielsen'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk substantiv (intetkøn)',
        'language_item_id': 'Q9035',
        'language_code': 'da',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775461'),
    },

    'danish-verb': {
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
                'grammatical_features_item_ids': ['Q12717679'],
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
    },

    'german-noun-masculine': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Maskulinum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist ein [Hund].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum eines [Hunds/Hundes].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört einem [Hund/Hunde].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag einen [Hund].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind mehrere [Hunde].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum mehrerer [Hunde].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört mehreren [Hunden].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag mehrere [Hunde].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
        ],
        'statements': statements('P5185', 'Q499327'),
    },

    'german-noun-feminine': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Femininum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist eine [Katze].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum einer [Katze].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört einer [Katze].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag eine [Katze].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind mehrere [Katzen].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum mehrerer [Katzen].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört mehreren [Katzen].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag mehrere [Katzen].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
        ],
        'statements': statements('P5185', 'Q1775415'),
    },

    'german-noun-neuter': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Neutrum)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist ein [Kind].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum eines [Kindes/Kinds].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört einem [Kind/Kinde].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag ein [Kind].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind mehrere [Kinder].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum mehrerer [Kinder].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört mehreren [Kindern].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag mehrere [Kinder].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
        ],
        'statements': statements('P5185', 'Q1775461'),
    },

    'german-noun-neuter-toponym': {
        '@attribution': {'users': ['Lucas Werkmeister', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Neutrum, Toponym)',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q147276',
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das heutige [Berlin].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Fotos des damaligen [Berlins/Berlin].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'Dativ Singular',
                'example': 'Fotos vom damaligen [Berlin].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Pläne für das zukünftige [Berlin].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
        ],
        'statements': {
            'P5185': [
                statement('P5185', 'Q1775461'),
            ],
            'P31': [
                statement('P31', 'Q604984'),
                statement('P31', 'Q7884789'),
            ],
        },
    },

    'german-noun-pluraletantum': {
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
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum der [Großeltern].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört den [Großeltern].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag die [Großeltern].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
        ],
        'statements': statements('P31', 'Q138246'),
    },

    'german-verb': {
        '@attribution': {'users': ['Lucas Werkmeister', 'Andreasmperu', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Verb',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Infinitiv',
                'example': '[tragen]',
                'grammatical_features_item_ids': ['Q179230'],
            },
            {
                'label': 'Infinitiv mit zu',
                'example': 'Es ist gut, [zu tragen].',
                'grammatical_features_item_ids': ['Q100952920'],
            },
            {
                'section_break': True,
                'label': '1. Person Singular Präsens',
                'example': 'Ich [trage] heute.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q682111', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '2. Person Singular Präsens',
                'example': 'Du [trägst] heute.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q682111', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '3. Person Singular Präsens',
                'example': 'Er/sie/es [trägt] heute.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q682111', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '1. Person Plural Präsens',
                'example': 'Wir [tragen] heute.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q682111', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '2. Person Plural Präsens',
                'example': 'Ihr [tragt] heute.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q682111', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '3. Person Plural Präsens',
                'example': 'Sie [tragen] heute.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q682111', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'section_break': True,
                'label': '1. Person Singular Präteritum',
                'example': 'Ich [trug] gestern.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q682111', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '2. Person Singular Präteritum',
                'example': 'Du [trugst] gestern.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q682111', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '3. Person Singular Präteritum',
                'example': 'Er/sie/es [trug] gestern.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q682111', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '1. Person Plural Präteritum',
                'example': 'Wir [trugen] gestern.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q682111', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '2. Person Plural Präteritum',
                'example': 'Ihr [trugt] gestern.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q682111', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '3. Person Plural Präteritum',
                'example': 'Sie [trugen] gestern.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q682111', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'section_break': True,
                'label': '1. Person Singular Konjunktiv I',
                'example': 'Angenommen, ich [trage].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q55685962', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '2. Person Singular Konjunktiv I',
                'example': 'Angenommen, du [tragest].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q55685962', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '3. Person Singular Konjunktiv I',
                'example': 'Angenommen, er/sie/es [trage].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q55685962', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '1. Person Plural Konjunktiv I',
                'example': 'Angenommen, wir [tragen].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q55685962', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '2. Person Plural Konjunktiv I',
                'example': 'Angenommen, ihr [traget].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q55685962', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '3. Person Plural Konjunktiv I',
                'example': 'Angenommen, sie [tragen].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q55685962', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'section_break': True,
                'label': '1. Person Singular Konjunktiv II',
                'example': 'Ich dachte, ich [trüge].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q54671845', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '2. Person Singular Konjunktiv II',
                'example': 'Ich dachte, du [trügest/trügst].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q54671845', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '3. Person Singular Konjunktiv II',
                'example': 'Ich dachte, er/sie/es [trüge].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q54671845', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '1. Person Plural Konjunktiv II',
                'example': 'Ich dachte, wir [trügen].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q54671845', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '2. Person Plural Konjunktiv II',
                'example': 'Ich dachte, ihr [trüget/trügt].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q54671845', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'label': '3. Person Plural Konjunktiv II',
                'example': 'Ich dachte, sie [trügen].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q54671845', 'Q442485', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831']),
            },
            {
                'section_break': True,
                'label': '2. Person Singular Imperativ',
                'example': 'He du da, [trag/trage]!',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q22716', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831', 'Q192613']),
            },
            {
                'label': '2. Person Plural Imperativ',
                'example': 'He ihr da, [tragt]!',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q22716', 'Q192613', 'Q1317831'],
                'grammatical_features_item_ids_optional': set(['Q1317831', 'Q192613']),
            },
            {
                'section_break': True,
                'label': 'Partizip I',
                'example': 'Es ging vorbei, etwas [tragend].',
                'grammatical_features_item_ids': ['Q10345583'],
            },
            {
                'label': 'Partizip II',
                'example': 'Ich werde [getragen].',
                'grammatical_features_item_ids': ['Q12717679'],
            },
        ],
    },

    'german-adverb': {
        '@attribution': {'users': ['Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Adverb',
        'language_item_id': 'Q188',
        'language_code': 'de',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'Lemma',
                'example': 'Wir machen das [immer].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'english-noun': {
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
    },

    'english-adverb': {
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
    },

    'english-adjective': {
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
    },

    'english-verb': {
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
    },

    'esperanto-noun': {
        '@attribution': {'users': ['KaMan', 'Jens Ohlig'], 'title': 'Wikidata:Wikidata Lexeme Forms/Esperanto'},
        'label': 'esperanta substantivo',
        'language_item_id': 'Q143',
        'language_code': 'eo',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
    },

    'esperanto-adjective': {
        '@attribution': {'users': ['Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Esperanto'},
        'label': 'esperanta adjektivo',
        'language_item_id': 'Q143',
        'language_code': 'eo',
        'lexical_category_item_id': 'Q34698',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ununombro, nominativo',
                'example': 'Ĉi tio estas [esperanta] vorto.',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'ununombro, akuzativo',
                'example': 'Mi ŝatas [esperantan] vorton.',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'multenombro, nominativo',
                'example': 'Ĉi tiuj estas [esperantaj] vortoj.',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'multenombro, akuzativo',
                'example': 'Mi ŝatas [esperantajn] vortojn.',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
        ],
    },

    'esperanto-verb': {
        '@attribution': {'users': ['Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Esperanto'},
        'label': 'esperanta verbo',
        'language_item_id': 'Q143',
        'language_code': 'eo',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': False,
        'forms': [
            {
                'label': 'infinitivo',
                'example': 'Ili volas [dormi].',
                'grammatical_features_item_ids': ['Q179230'],
            },
            {
                'section_break': True,
                'label': 'indikativo, prezenco',
                'example': 'Ili nun [dormas].',
                'grammatical_features_item_ids': ['Q682111', 'Q192613'],
                'grammatical_features_item_ids_optional': set(['Q682111']),
            },
            {
                'label': 'indikativo, preterito',
                'example': 'Ili [dormis] hieraŭ.',
                'grammatical_features_item_ids': ['Q682111', 'Q1994301'],
                'grammatical_features_item_ids_optional': set(['Q682111']),
            },
            {
                'label': 'indikativo, futuro',
                'example': 'Ili [dormos] morgaŭ.',
                'grammatical_features_item_ids': ['Q682111', 'Q501405'],
                'grammatical_features_item_ids_optional': set(['Q682111']),
            },
            {
                'section_break': True,
                'label': 'kondicionalo',
                'example': 'Estus bone, se ili [dormus].',
                'grammatical_features_item_ids': ['Q625581'],
            },
            {
                'label': 'volitivo',
                'example': 'Ne [dormu]!',
                'grammatical_features_item_ids': ['Q2532941'],
            },
        ],
    },

    'spanish-noun-masculine': {
        '@attribution': {'users': ['Andreasmperu', 'Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'sustantivo masculino en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singular',
                'example': 'Este es un [libro].',
                'grammatical_features_item_ids': ['Q110786', 'Q499327'],
            },
            {
                'label': 'plural',
                'example': 'Estos son unos [libros].',
                'grammatical_features_item_ids': ['Q146786', 'Q499327'],
            },
        ],
        'statements': statements('P5185', 'Q499327'),
    },

    'spanish-noun-feminine': {
        '@attribution': {'users': ['Andreasmperu', 'Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'sustantivo femenino en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'singular',
                'example': 'Esta es una [manzana].',
                'grammatical_features_item_ids': ['Q110786', 'Q1775415'],
            },
            {
                'label': 'plural',
                'example': 'Estas son unas [manzanas].',
                'grammatical_features_item_ids': ['Q146786', 'Q1775415'],
            },
        ],
        'statements': statements('P5185', 'Q1775415'),
    },

    'spanish-noun-masculine-feminine': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'sustantivo masculino y femenino en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'masculino singular',
                'example': 'Ese [poeta] es bueno.',
                'grammatical_features_item_ids': ['Q499327', 'Q110786'],
            },
            {
                'label': 'masculino plural',
                'example': 'Esos [poetas] son buenos.',
                'grammatical_features_item_ids': ['Q499327', 'Q146786'],
            },
            {
                'label': 'femenino singular',
                'example': 'Esa [poetisa] es buena.',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786'],
            },
            {
                'label': 'femenino plural',
                'example': 'Esas [poetisas] son buenas.',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786'],
            },
        ],
        'statements': {
            'P5185': [
                statement('P5185', 'Q499327'),
                statement('P5185', 'Q1775415'),
            ],
        },
    },

    'spanish-adjective': {
        '@attribution': {'users': ['Andreasmperu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'adjetivo en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q34698',
        'two_column_sections': True,
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
    },

    'spanish-verb': {
        '@attribution': {'users': ['DemonDays64', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'verbo en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'infinitivo',
                'example': 'Quieres [cantar].',
                'grammatical_features_item_ids': ['Q179230'],
            },
            {
                'section_break': True,
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
                'label': 'segunda persona (vos) singular presente',
                'example': 'Vos [cantás] todos los días.',
                'grammatical_features_item_ids': ['Q192613', 'Q682111', 'Q51929049', 'Q110786', 'Q1070730'],
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
                'section_break': True,
                'label': 'primera persona singular pretérito',
                'example': 'Yo [canté] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q21714344', 'Q110786', 'Q682111'],
            },
            {
                'label': 'segunda persona singular pretérito',
                'example': 'Tú [cantaste] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q51929049', 'Q110786', 'Q682111'],
            },
            {
                'label': 'tercera persona singular pretérito',
                'example': 'Él [cantó] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q51929074', 'Q110786', 'Q682111'],
            },
            {
                'label': 'primera persona plural pretérito',
                'example': 'Nosotros [cantamos] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q21714344', 'Q146786', 'Q682111'],
            },
            {
                'label': 'segunda persona plural pretérito',
                'example': 'Vosotros [cantasteis] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q51929049', 'Q146786', 'Q682111'],
            },
            {
                'label': 'tercera persona plural pretérito',
                'example': 'Ellos [cantaron] mucho durante la semana pasada.',
                'grammatical_features_item_ids': ['Q442485', 'Q51929074', 'Q146786', 'Q682111'],
            },
            {
                'section_break': True,
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
                'section_break': True,
                'label': 'gerundio',
                'example': 'Estoy [cantando].',
                'grammatical_features_item_ids': ['Q1923028'],
            },
            {
                'section_break': True,
                'label': 'participio masculino singular',
                'example': 'Yo he [cantado].',
                'grammatical_features_item_ids': ['Q814722', 'Q499327', 'Q110786'],
            },
            {
                'label': 'participio masculino plural',
                'example': 'Esos fueron [cantados].',
                'grammatical_features_item_ids': ['Q814722', 'Q499327', 'Q146786'],
            },
            {
                'label': 'participio femenino singular',
                'example': 'Esa fue [cantada].',
                'grammatical_features_item_ids': ['Q814722', 'Q1775415', 'Q110786'],
            },
            {
                'label': 'participio femenino plural',
                'example': 'Esas fueron [cantadas].',
                'grammatical_features_item_ids': ['Q814722', 'Q1775415', 'Q146786'],
            },
            {
                'section_break': True,
                'label': 'primera persona singular del futuro',
                'example': 'Yo [cantaré] mañana.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q501405', 'Q682111'],
            },
            {
                'label': 'segunda persona singular del futuro',
                'example': 'Tú [cantarás] mañana.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q501405', 'Q682111'],
            },
            {
                'label': 'tercera persona singular del futuro',
                'example': 'Él [cantará] mañana.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q501405', 'Q682111'],
            },
            {
                'label': 'primera persona plural del futuro',
                'example': 'Nosotros [cantaremos] mañana.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q501405', 'Q682111'],
            },
            {
                'label': 'segunda persona plural del futuro',
                'example': 'Vosotros [cantaréis] mañana.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q501405', 'Q682111'],
            },
            {
                'label': 'tercera persona plural del futuro',
                'example': 'Ellos [cantarán] mañana.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q501405', 'Q682111'],
            },
            {
                'section_break': True,
                'label': 'primera persona singular del condicional',
                'example': 'Yo [cantaría] si pudiera.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q65211247', 'Q682111'],
            },
            {
                'label': 'segunda persona singular del condicional',
                'example': 'Tú [cantarías] si pudieras.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q65211247', 'Q682111'],
            },
            {
                'label': 'tercera persona singular del condicional',
                'example': 'Él [cantaría] si pudiera.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q65211247', 'Q682111'],
            },
            {
                'label': 'primera persona plural del condicional',
                'example': 'Nosotros [cantaríamos] si pudiéramos.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q65211247', 'Q682111'],
            },
            {
                'label': 'segunda persona plural del condicional',
                'example': 'Vosotros [cantaríais] si pudierais.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q65211247', 'Q682111'],
            },
            {
                'label': 'tercera persona plural del condicional',
                'example': 'Ellos [cantarían] si pudieran.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q65211247', 'Q682111'],
            },
            {
                'section_break': True,
                'label': 'primera persona singular del presente de subjuntivo',
                'example': 'Para que yo [cante].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q3502553'],
            },
            {
                'label': 'segunda persona singular del presente de subjuntivo',
                'example': 'Para que tú [cantes].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q3502553'],
            },
            {
                'label': 'segunda persona (vos) singular del presente de subjuntivo',
                'example': 'Para que vos [cantés].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q3502553', 'Q1070730'],
            },
            {
                'label': 'tercera persona singular del presente de subjuntivo',
                'example': 'Para que él [cante].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q3502553'],
            },
            {
                'label': 'primera persona plural del presente de subjuntivo',
                'example': 'Para que nosotros [cantemos].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q3502553'],
            },
            {
                'label': 'segunda persona plural del presente de subjuntivo',
                'example': 'Para que vosotros [cantéis].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q3502553'],
            },
            {
                'label': 'tercera persona plural del presente de subjuntivo',
                'example': 'Para que ellos [canten].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q3502553'],
            },
            {
                'label': 'primera persona singular del pretérito imperfecto de subjuntivo',
                'example': 'Para que yo [cantara/cantase].',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q3502541'],
            },
            {
                'label': 'segunda persona singular del pretérito imperfecto de subjuntivo',
                'example': 'Para que tú [cantaras/cantases].',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q3502541'],
            },
            {
                'label': 'tercera persona singular del pretérito imperfecto de subjuntivo',
                'example': 'Para que él [cantara/cantase].',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q3502541'],
            },
            {
                'label': 'primera persona plural del pretérito imperfecto de subjuntivo',
                'example': 'Para que nosotros [cantáramos/cantásemos].',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q3502541'],
            },
            {
                'label': 'segunda persona plural del pretérito imperfecto de subjuntivo',
                'example': 'Para que vosotros [cantarais/cantaseis].',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q3502541'],
            },
            {
                'label': 'tercera persona plural del pretérito imperfecto de subjuntivo',
                'example': 'Para que ellos [cantaran/cantasen].',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q3502541'],
            },
            {
                'section_break': True,
                'label': 'primera persona singular del futuro de subjuntivo',
                'example': 'Para que yo [cantare] mañana.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'segunda persona singular del futuro de subjuntivo',
                'example': 'Para que tú [cantares] mañana.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'tercera persona singular del futuro de subjuntivo',
                'example': 'Para que él [cantare] mañana.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'primera persona plural del futuro de subjuntivo',
                'example': 'Para que nosotros [cantáremos] mañana.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'segunda persona plural del futuro de subjuntivo',
                'example': 'Para que vosotros [cantareis] mañana.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q501405', 'Q473746'],
            },
            {
                'label': 'tercera persona plural del futuro de subjuntivo',
                'example': 'Para que ellos [cantaren] mañana.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q501405', 'Q473746'],
            },
            {
                'section_break': True,
                'label': 'segunda persona singular del imperativo',
                'example': 'Por favor, [canta] tú.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q22716'],
            },
            {
                'label': 'segunda persona singular del imperativo',
                'example': 'Por favor, [cantá] vos.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q22716', 'Q1070730'],
            },
            {
                'label': 'segunda persona singular del imperativo',
                'example': 'Por favor, [cante] usted.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q22716', 'Q6158182'],
            },
            {
                'label': 'primera persona plural del imperativo',
                'example': 'Por favor, [cantemos] nosotros.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q22716'],
            },
            {
                'label': 'segunda persona plural del imperativo',
                'example': 'Por favor, [cantad] vosotros.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q22716'],
            },
            {
                'label': 'segunda persona plural del imperativo',
                'example': 'Por favor, [canten] ustedes.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q22716', 'Q6158182'],
            },
        ],
    },

    'spanish-adverb': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'adverbio en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'adverbio',
                'example': 'Yo tengo [únicamente] ese libro.',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'spanish-interjection': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'interjección en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q83034',
        'forms': [
            {
                'label': 'interjección',
                'example': 'No me lo esperaba, ¡[cáspita]!.',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'spanish-phrase-nominal-masculine': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución sustantiva masculina en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q29888377',
        'forms': [
            {
                'label': 'singular',
                'example': 'Lo importante es el [santo y seña].',
                'grammatical_features_item_ids': ['Q110786', 'Q499327'],
            },
            {
                'label': 'plural',
                'example': 'Lo importante son los [santos y señas].',
                'grammatical_features_item_ids': ['Q146786', 'Q499327'],
            },
        ],
        'statements': statements('P5185', 'Q499327'),
    },

    'spanish-phrase-nominal-feminine': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución sustantiva femenina en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q29888377',
        'forms': [
            {
                'label': 'singular',
                'example': 'Lo importante es la [caja de caudales].',
                'grammatical_features_item_ids': ['Q110786', 'Q1775415'],
            },
            {
                'label': 'plural',
                'example': 'Lo importante son las [cajas de caudales].',
                'grammatical_features_item_ids': ['Q146786', 'Q1775415'],
            },
        ],
        'statements': statements('P5185', 'Q1775415'),
    },

    'spanish-phrase-attributive': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución adjetiva en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q12734432',
        'forms': [
            {
                'label': 'masculino singular',
                'example': 'Eso está [sano y salvo].',
                'grammatical_features_item_ids': ['Q110786', 'Q499327'],
            },
            {
                'label': 'masculino plural',
                'example': 'Esos están [sanos y salvos].',
                'grammatical_features_item_ids': ['Q146786', 'Q499327'],
            },
            {
                'label': 'femenino singular',
                'example': 'Esa está [sana y salva].',
                'grammatical_features_item_ids': ['Q110786', 'Q1775415'],
            },
            {
                'label': 'femenino plural',
                'example': 'Esas están [sanas y salvas].',
                'grammatical_features_item_ids': ['Q146786', 'Q1775415'],
            },
        ],
        'statements': {
            'P5185': [
                statement('P5185', 'Q499327'),
                statement('P5185', 'Q1775415'),
            ],
        },
    },

    'spanish-locution-prepositional': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución preposicional en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q10319522',
        'forms': [
            {
                'label': 'locución preposicional',
                'example': 'Ellas hablaron [detrás de] (el) edificio.',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'spanish-locution-interjectional': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución interjectiva en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q10319520',
        'forms': [
            {
                'label': 'locución interjectiva',
                'example': 'No me lo esperaba, ¡[vaya por Dios]!.',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'spanish-locution-adverbial': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución adverbial en español',
        'language_item_id': 'Q1321',
        'language_code': 'es',
        'lexical_category_item_id': 'Q5978303',
        'forms': [
            {
                'label': 'locución adverbial',
                'example': 'Él lo dijo [a posteriori].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'estonian-noun': {
        '@attribution': {'users': ['Reosarevok'], 'title': 'Wikidata:Wikidata Lexeme Forms/Estonian'},
        'label': 'eesti keele nimisõna',
        'language_item_id': 'Q9072',
        'language_code': 'et',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
    },

    'basque-verb': {
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
    },

    'basque-adjective-comparative': {
        '@attribution': {'users': ['Theklan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Basque'},
        'label': 'euskal adjektibo konparatibo eta superlatiboak',
        'language_item_id': 'Q8752',
        'language_code': 'eu',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'oina',
                'example': '[gorri]',
                'grammatical_features_item_ids': ['Q332734', 'Q53998049'],
            },
            {
                'label': 'konparatiboa',
                'example': '[gorriago]',
                'grammatical_features_item_ids': ['Q14169499'],
            },
            {
                'label': 'superlatiboa',
                'example': '[gorrien]',
                'grammatical_features_item_ids': ['Q1817208'],
            },
        ],
    },

    'persian-noun': {
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
    },

    'persian-verb': {
        '@attribution': {'users': ['Ladsgroup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Persian'},
        'label': 'فعل فارسی',
        'language_item_id': 'Q9168',
        'language_code': 'fa',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': True,
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
    },

    'finnish-noun': {
        '@attribution': {'users': ['Shinnin'], 'title': 'Wikidata:Wikidata Lexeme Forms/Finnish'},
        'label': 'suomen kielen substantiivi',
        'language_item_id': 'Q1412',
        'language_code': 'fi',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
                'label': 'monikon instruktiivi',
                'example': 'Käsin, jaloin, kissoin ja [koirin].',
                'grammatical_features_item_ids': ['Q1665275', 'Q146786'],
            },
            {
                'section_break': True,
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
    },

    'french-noun-masculine': {
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
        'statements': statements('P5185', 'Q499327'),
    },

    'french-noun-feminine': {
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'french-adjective': {
        '@attribution': {'users': ['Djiboun'], 'title': 'Wikidata:Wikidata Lexeme Forms/French'},
        'label': 'adjectif en français',
        'language_item_id': 'Q150',
        'language_code': 'fr',
        'lexical_category_item_id': 'Q34698',
        'two_column_sections': True,
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
    },

    'hebrew-noun-masculine': {
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
        'statements': statements('P5185', 'Q499327'),
    },

    'hebrew-noun-feminine': {
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'hebrew-adjective': {
        '@attribution': {'users': ['Ijon'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hebrew'},
        'label': 'Hebrew adjective',
        'language_item_id': 'Q9288',
        'language_code': 'he',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'יחיד',
                'example': 'חתול [גדול] חצה את הכביש.',
                'grammatical_features_item_ids': ['Q110786', 'Q3482678', 'Q499327'],
            },
            {
                'label': 'רבים',
                'example': 'חתולים [גדולים] חצו את הכביש.',
                'grammatical_features_item_ids': ['Q146786', 'Q3482678', 'Q499327'],
            },
            {
                'label': 'יחידה',
                'example': 'חתולה [גדולה] חצתה את הכביש.',
                'grammatical_features_item_ids': ['Q110786', 'Q3482678', 'Q1775415'],
            },
            {
                'label': 'רבות',
                'example': 'חתולות [גדולות] חצו את הכביש.',
                'grammatical_features_item_ids': ['Q146786', 'Q3482678', 'Q1775415'],
            },
        ],
    },

    'croatian-noun-masculine': {
        '@attribution': {'users': ['Ivi104'], 'title': 'Wikidata:Wikidata Lexeme Forms/Croatian'},
        'label': 'hrvatske imenice (muški rod)',
        'language_item_id': 'Q6654',
        'language_code': 'hr',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativ jednine',
                'example': 'Ovo je [miš].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitiv jednine',
                'example': 'Nema [miša].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativ jednine',
                'example': 'Prilazim [mišu].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'akuzativ jednine',
                'example': 'Vidim [miša].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'vokativ jednine',
                'example': 'Zar i ti, [mišu]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'lokativ jednine',
                'example': 'Govorim o [mišu].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': 'instrumental jednine',
                'example': 'Vozim se s(a) [mišem].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'nominativ množine',
                'example': 'Ovo su [miševi].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitiv množine',
                'example': 'Nema [miševa].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativ množine',
                'example': 'Prilazim [miševima].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'akuzativ množine',
                'example': 'Vidim [miševe].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'vokativ množine',
                'example': 'Zar i vi, [miševi]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
            {
                'label': 'lokativ množine',
                'example': 'Govorim o [miševima].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': 'instrumental množine',
                'example': 'Vozim se s(a) [miševima].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
        ],
        'statements': statements('P5185', 'Q499327'),
    },

    'croatian-noun-feminine': {
        '@attribution': {'users': ['Ivi104'], 'title': 'Wikidata:Wikidata Lexeme Forms/Croatian'},
        'label': 'hrvatske imenice (ženski rod)',
        'language_item_id': 'Q6654',
        'language_code': 'hr',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativ jednine',
                'example': 'Ovo je [žirafa].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitiv jednine',
                'example': 'Nema [žirafe].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativ jednine',
                'example': 'Prilazim [žirafi].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'akuzativ jednine',
                'example': 'Vidim [žirafu].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'vokativ jednine',
                'example': 'Zar i ti, [žirafo]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'lokativ jednine',
                'example': 'Govorim o [žirafi].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': 'instrumental jednine',
                'example': 'Vozim se s(a) [žirafom].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'nominativ množine',
                'example': 'Ovo su [žirafe].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitiv množine',
                'example': 'Nema [žirafa].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativ množine',
                'example': 'Prilazim [žirafama].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'akuzativ množine',
                'example': 'Vidim [žirafe].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'vokativ množine',
                'example': 'Zar i vi, [žirafe]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
            {
                'label': 'lokativ množine',
                'example': 'Govorim o [žirafama].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': 'instrumental množine',
                'example': 'Vozim se s(a) [žirafama].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
        ],
        'statements': statements('P5185', 'Q1775415'),
    },

    'croatian-noun-neuter': {
        '@attribution': {'users': ['Ivi104'], 'title': 'Wikidata:Wikidata Lexeme Forms/Croatian'},
        'label': 'hrvatske imenice (srednji rod)',
        'language_item_id': 'Q6654',
        'language_code': 'hr',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'nominativ jednine',
                'example': 'Ovo je [staklo].',
                'grammatical_features_item_ids': ['Q131105', 'Q110786'],
            },
            {
                'label': 'genitiv jednine',
                'example': 'Nema [stakla].',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
            },
            {
                'label': 'dativ jednine',
                'example': 'Prilazim [staklu].',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
            },
            {
                'label': 'akuzativ jednine',
                'example': 'Vidim [staklo].',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
            },
            {
                'label': 'vokativ jednine',
                'example': 'Zar i ti, [staklo]?',
                'grammatical_features_item_ids': ['Q185077', 'Q110786'],
            },
            {
                'label': 'lokativ jednine',
                'example': 'Govorim o [staklu].',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
            },
            {
                'label': 'instrumental jednine',
                'example': 'Vozim se s(a) [staklom].',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
            },
            {
                'label': 'nominativ množine',
                'example': 'Ovo su [stakla].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
            },
            {
                'label': 'genitiv množine',
                'example': 'Nema [stakala].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
            },
            {
                'label': 'dativ množine',
                'example': 'Prilazim [staklima].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
            },
            {
                'label': 'akuzativ množine',
                'example': 'Vidim [stakla].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
            },
            {
                'label': 'vokativ množine',
                'example': 'Zar i vi, [stakla]?',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
            },
            {
                'label': 'lokativ množine',
                'example': 'Govorim o [staklima].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
            },
            {
                'label': 'instrumental množine',
                'example': 'Vozim se s(a) [staklima].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
            },
        ],
        'statements': statements('P5185', 'Q1775461'),
    },

    'armenian-noun': {
        '@attribution': {'users': ['Emptyfear'], 'title': 'Wikidata:Wikidata Lexeme Forms/Armenian'},
        'label': 'հայերեն գոյական',
        'language_item_id': 'Q8785',
        'language_code': 'hy',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
    },

    'armenian-noun-singulare-tantum': {
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
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'եզ․ թիվ, սեռ․ հոլով',
                'example': '[Կաթի] նշանակությունը։',
                'grammatical_features_item_ids': ['Q146233', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'եզ․ թիվ, տր․ հոլով',
                'example': '[Կաթին] ավելացնել։',
                'grammatical_features_item_ids': ['Q145599', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'եզ․ թիվ, հայց․ հոլով',
                'example': 'Տեսնում եմ [կաթ]։',
                'grammatical_features_item_ids': ['Q146078', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'եզ․ թիվ, գործ․ հոլով',
                'example': '[Կաթով] պատրաստել։',
                'grammatical_features_item_ids': ['Q192997', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'եզ․ թիվ, բաց․ հոլով',
                'example': '[Կաթից] առանձնացնել։',
                'grammatical_features_item_ids': ['Q156986', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
            {
                'label': 'եզ․ թիվ, ներգ․ հոլով',
                'example': '[Կաթում] լողալ։',
                'grammatical_features_item_ids': ['Q202142', 'Q110786'],
                'grammatical_features_item_ids_optional': set(['Q110786']),
            },
        ],
        'statements': statements('P31', 'Q604984'),
    },

    'igbo-noun': {
        '@attribution': {'users': ['EnaldoSS', 'Tochiprecious'], 'title': 'Wikidata:Wikidata Lexeme Forms/Igbo'},
        'label': 'Aha n\'Igbo',
        'language_item_id': 'Q33578',
        'language_code': 'ig',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'aha',
                'example': 'Ọ nwere [ụlọ].',
                'grammatical_features_item_ids': [],
            }
        ],
    },

    'igbo-verb': {
        '@attribution': {'users': ['EnaldoSS', 'Tochiprecious'], 'title': 'Wikidata:Wikidata Lexeme Forms/Igbo'},
        'label': 'Ngwaa n\'Igbo',
        'language_item_id': 'Q33578',
        'language_code': 'ig',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'ntimiwu',
                'example': 'Biko [rie].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'igbo-pronoun': {
        '@attribution': {'users': ['EnaldoSS', 'Tochiprecious'], 'title': 'Wikidata:Wikidata Lexeme Forms/Igbo'},
        'label': 'Nnọchiaha n\'Igbo',
        'language_item_id': 'Q33578',
        'language_code': 'ig',
        'lexical_category_item_id': 'Q36224',
        'forms': [
            {
                'label': 'nnọchiaha',
                'example': 'Onye nkụzi ka [ọ] bụ.',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'igbo-adjective': {
        '@attribution': {'users': ['EnaldoSS', 'Tochiprecious'], 'title': 'Wikidata:Wikidata Lexeme Forms/Igbo'},
        'label': 'Nkọwaaha n\'Igbo',
        'language_item_id': 'Q33578',
        'language_code': 'ig',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'nkọwaaha',
                'example': 'Nwanyị [ọcha].',
                'grammatical_features_item_ids': [],
            }
        ],
    },

    'italian-noun-feminine': {
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'italian-noun-masculine': {
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
        'statements': statements('P5185', 'Q499327'),
    },

    'italian-adjective': {
        '@attribution': {'users': ['Sannita'], 'title': 'Wikidata:Wikidata Lexeme Forms/Italian'},
        'label': 'aggettivo qualificativo italiano',
        'language_item_id': 'Q652',
        'language_code': 'it',
        'lexical_category_item_id': 'Q34698',
        'two_column_sections': True,
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
    },

    'kurmanji-noun-feminine': {
        '@attribution': {'users': ['Şêr'], 'title': 'Wikidata:Wikidata Lexeme Forms/Kurdish (Kurmancî)'},
        'label': 'navdêra kurdî (mê)',
        'language_item_id': 'Q36163',
        'language_code': 'ku',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'kurmanji-noun-masculine': {
        '@attribution': {'users': ['Şêr'], 'title': 'Wikidata:Wikidata Lexeme Forms/Kurdish (Kurmancî)'},
        'label': 'navdêra kurdî (nêr)',
        'language_item_id': 'Q36163',
        'language_code': 'ku',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
        'statements': statements('P5185', 'Q499327'),
    },

    'latin-noun-masculine': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
        'label': 'nomen Latinum (masculinum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q499327'),
    },

    'latin-noun-feminine': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
        'label': 'nomen Latinum (femininum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'latin-noun-neuter': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
        'label': 'nomen Latinum (neutrum)',
        'language_item_id': 'Q397',
        'language_code': 'la',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775461'),
    },

    'latvian-noun-masculine': {
        '@attribution': {'users': ['Papuass', 'Lucas Werkmeister', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latvian'},
        'label': 'latviešu valodas vīriešu dzimtes lietvārds',
        'language_item_id': 'Q9078',
        'language_code': 'lv',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'vienskaitļa nominatīvs',
                'example': 'Šis ir [suns].',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'daudzskaitļa nominatīvs',
                'example': 'Šie ir [suņi].',
                'grammatical_features_item_ids': ['Q146786', 'Q131105'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa ģenitīvs',
                'example': 'Šī ir [suņa] aste.',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'daudzskaitļa ģenitīvs',
                'example': 'Šīs ir [suņu] astes.',
                'grammatical_features_item_ids': ['Q146786', 'Q146233'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa datīvs',
                'example': 'Manam [sunim] ir aste.',
                'grammatical_features_item_ids': ['Q110786', 'Q145599'],
            },
            {
                'label': 'daudzskaitļa datīvs',
                'example': 'Maniem [suņiem] ir aste.',
                'grammatical_features_item_ids': ['Q146786', 'Q145599'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa akuzatīvs',
                'example': 'Aste luncina [suni].',
                'grammatical_features_item_ids': ['Q110786', 'Q146078'],
            },
            {
                'label': 'daudzskaitļa akuzatīvs',
                'example': 'Aste luncina [suņus].',
                'grammatical_features_item_ids': ['Q146786', 'Q146078'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa instrumentālis',
                'example': 'Vislabāk ir [ar suni].',
                'grammatical_features_item_ids': ['Q110786', 'Q192997'],
            },
            {
                'label': 'daudzskaitļa instrumentālis',
                'example': 'Vislabāk ir [ar suņiem].',
                'grammatical_features_item_ids': ['Q146786', 'Q192997'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa lokatīvs',
                'example': 'Katrā [sunī] blusu nav.',
                'grammatical_features_item_ids': ['Q110786', 'Q202142'],
            },
            {
                'label': 'daudzskaitļa lokatīvs',
                'example': 'Visos [suņos] blusu nav.',
                'grammatical_features_item_ids': ['Q146786', 'Q202142'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa vokatīvs',
                'example': 'Hei, [suni]!',
                'grammatical_features_item_ids': ['Q110786', 'Q185077'],
            },
            {
                'label': 'daudzskaitļa vokatīvs',
                'example': 'Hei, [suņi]!',
                'grammatical_features_item_ids': ['Q146786', 'Q185077'],
            },
        ],
        'statements': statements('P5185', 'Q499327'),
    },

    'latvian-noun-feminine': {
        '@attribution': {'users': ['Papuass', 'Lucas Werkmeister', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latvian'},
        'label': 'latviešu valodas sieviešu dzimtes lietvārds',
        'language_item_id': 'Q9078',
        'language_code': 'lv',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'vienskaitļa nominatīvs',
                'example': 'Šī ir [roka].',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'daudzskaitļa nominatīvs',
                'example': 'Šīs ir [rokas].',
                'grammatical_features_item_ids': ['Q146786', 'Q131105'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa ģenitīvs',
                'example': 'Šie ir kreisās [rokas] pirksti.',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'daudzskaitļa ģenitīvs',
                'example': 'Šis ir [roku] krēms.',
                'grammatical_features_item_ids': ['Q146786', 'Q146233'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa datīvs',
                'example': 'Vienai [rokai] ir pieci pirksti.',
                'grammatical_features_item_ids': ['Q110786', 'Q145599'],
            },
            {
                'label': 'daudzskaitļa datīvs',
                'example': 'Abām [rokām] kopā ir desmit pirksti.',
                'grammatical_features_item_ids': ['Q146786', 'Q145599'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa akuzatīvs',
                'example': 'Viņa paspieda [roku].',
                'grammatical_features_item_ids': ['Q110786', 'Q146078'],
            },
            {
                'label': 'daudzskaitļa akuzatīvs',
                'example': 'Mazgā [rokas] ar ziepēm.',
                'grammatical_features_item_ids': ['Q146786', 'Q146078'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa instrumentālis',
                'example': 'Viņa pamāja [ar roku].',
                'grammatical_features_item_ids': ['Q110786', 'Q192997'],
            },
            {
                'label': 'daudzskaitļa instrumentālis',
                'example': 'Šo kreklu ir jāmazgā [ar rokām].',
                'grammatical_features_item_ids': ['Q146786', 'Q192997'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa lokatīvs',
                'example': 'Karogs [rokā] un uz priekšu.',
                'grammatical_features_item_ids': ['Q110786', 'Q202142'],
            },
            {
                'label': 'daudzskaitļa lokatīvs',
                'example': 'Abās [rokās] ir cimdi.',
                'grammatical_features_item_ids': ['Q146786', 'Q202142'],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa vokatīvs',
                'example': 'Hei, [roka]!',
                'grammatical_features_item_ids': ['Q110786', 'Q185077'],
            },
            {
                'label': 'daudzskaitļa vokatīvs',
                'example': 'Hei, [rokas]!',
                'grammatical_features_item_ids': ['Q146786', 'Q185077'],
            },
        ],
        'statements': statements('P5185', 'Q1775415'),
    },

    'malayalam-noun': {
        '@attribution': {'users': ['Jsamwrites', 'Vis M', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Malayalam'},
        'label': 'മലയാളത്തിലെ സാധാരണ നാമം',
        'language_item_id': 'Q36236',
        'language_code': 'ml',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ഏകവചനം',
                'example': 'ഒരു [പശു].',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'ഏകവചനം പ്രതിഗ്രാഹിക',
                'example': 'ഞാൻ [പശുവിനെ] മെയ്ച്ചു',
                'grammatical_features_item_ids': ['Q110786', 'Q146078'],
            },
            {
                'label': 'ഏകവചനം ഉദ്ദേശിക',
                'example': 'ഞാൻ [പശുവിന്] പുല്ലു കൊടുത്തു',
                'grammatical_features_item_ids': ['Q110786', 'Q145599'],
            },
            {
                'label': 'ഏകവചനം ആധാരിക',
                'example': '[പുഴയിൽ] കുളിച്ചു ',
                'grammatical_features_item_ids': ['Q110786', 'Q202142'],
            },
            {
                'label': 'ഏകവചനം സംയോജിക',
                'example': '[അമ്മയോട്] സംസാരിച്ചു',
                'grammatical_features_item_ids': ['Q110786', 'Q3773161'],
            },
            {
                'label': 'ഏകവചനം പ്രയോജിക',
                'example': 'ചെടികൾ [പശുവാൽ] തിന്നപ്പെട്ടു',
                'grammatical_features_item_ids': ['Q110786', 'Q192997'],
            },
            {
                'label': 'ഏകവചനം സംബന്ധിക',
                'example': '[അമ്മയുടെ] സ്നേഹം',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'ഏകവചനം സംബോധിക',
                'example': '[അമ്മേ]!, നോക്കൂ.',
                'grammatical_features_item_ids': ['Q110786', 'Q185077'],
                'optional': True,
            },
            {
                'label': 'ബഹുവചനം',
                'example': 'അനേകം [പശുക്കൾ].',
                'grammatical_features_item_ids': ['Q146786', 'Q131105'],
            },
            {
                'label': 'ബഹുവചനം പ്രതിഗ്രാഹിക ',
                'example': 'ഞാൻ [പശുക്കളെ] മെയ്ച്ചു',
                'grammatical_features_item_ids': ['Q146786', 'Q146078'],
            },
            {
                'label': 'ബഹുവചനം ഉദ്ദേശിക',
                'example': 'ഞാൻ [പശുക്കൾക്ക്] പുല്ലു കൊടുത്തു',
                'grammatical_features_item_ids': ['Q146786', 'Q145599'],
            },
            {
                'label': 'ബഹുവചനം ആധാരിക',
                'example': 'പല [വയലുകളിൽ] കളിച്ചു',
                'grammatical_features_item_ids': ['Q146786', 'Q202142'],
            },
            {
                'label': 'ബഹുവചനം സംയോജിക',
                'example': '[കുട്ടികളോട്] പറഞ്ഞു',
                'grammatical_features_item_ids': ['Q146786', 'Q3773161'],
            },
            {
                'label': 'ബഹുവചനം പ്രയോജിക',
                'example': 'ചെടികൾ [പശുക്കളാൽ] തിന്നപ്പെട്ടു',
                'grammatical_features_item_ids': ['Q146786', 'Q192997'],
            },
            {
                'label': 'ബഹുവചനം സംബന്ധിക',
                'example': '[കുട്ടികളുടെ] പ്രവർത്തി',
                'grammatical_features_item_ids': ['Q146786', 'Q146233'],
            },
            {
                'label': 'ബഹുവചനം സംബോധിക',
                'example': '[കുട്ടികളേ]!, അവിടെ പോകരുത്.',
                'grammatical_features_item_ids': ['Q146786', 'Q185077'],
                'optional': True,
            },
        ],
    },

    'malayalam-noun-proper': {
        '@attribution': {'users': ['Vis M'], 'title': 'Wikidata:Wikidata Lexeme Forms/Malayalam'},
        'label': 'മലയാളം സംജ്ഞാനാമം (proper noun)',
        'language_item_id': 'Q36236',
        'language_code': 'ml',
        'lexical_category_item_id': 'Q147276',
        'forms': [
            {
                'label': 'ഏകവചനം',
                'example': '[സീത] പഠിക്കുന്നു.',
                'grammatical_features_item_ids': ['Q110786', 'Q131105'],
            },
            {
                'label': 'ഏകവചനം പ്രതിഗ്രാഹിക',
                'example': 'ഞാൻ [സീതയെ] സഹായിച്ചു',
                'grammatical_features_item_ids': ['Q110786', 'Q146078'],
            },
            {
                'label': 'ഏകവചനം ഉദ്ദേശിക',
                'example': 'ഞാൻ [സീതയ്ക്ക്] പണം അയച്ചു',
                'grammatical_features_item_ids': ['Q110786', 'Q145599'],
            },
            {
                'label': 'ഏകവചനം ആധാരിക',
                'example': 'ഞാൻ [കേരളത്തിൽ] എത്തി',
                'grammatical_features_item_ids': ['Q110786', 'Q202142'],
            },
            {
                'label': 'ഏകവചനം സംയോജിക',
                'example': 'ഞാൻ [സീതയോട്] വിവരം പറഞ്ഞു',
                'grammatical_features_item_ids': ['Q110786', 'Q3773161'],
            },
            {
                'label': 'ഏകവചനം പ്രയോജിക',
                'example': 'വാഹനം [സീതയാൽ] ഓടിക്കപ്പെട്ടു',
                'grammatical_features_item_ids': ['Q110786', 'Q192997'],
            },
            {
                'label': 'ഏകവചനം സംബന്ധിക',
                'example': '[സീതയുടെ] പണം',
                'grammatical_features_item_ids': ['Q110786', 'Q146233'],
            },
            {
                'label': 'ഏകവചനം സംബോധിക',
                'example': '[സീതേ]!, നോക്കൂ.',
                'grammatical_features_item_ids': ['Q110786', 'Q185077'],
                'optional': True,
            },
        ],
    },

    'malayalam-verb': {
        '@attribution': {'users': ['Vis M', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Malayalam'},
        'label': 'മലയാളം ക്രിയ',
        'language_item_id': 'Q36236',
        'language_code': 'ml',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'ഇൻഫിനിറ്റീവ്',
                'example': 'അവൾ [എഴുതുക] ആണ്',
                'grammatical_features_item_ids': ['Q52434245'],
            },
            {
                'label': 'സാമാന്യ വർത്തമാനകാലം',
                'example': 'അവൾ [എഴുതുന്നു]',
                'grammatical_features_item_ids': ['Q3910936'],
            },
            {
                'label': 'സാമാന്യ ഭൂതകാലം',
                'example': 'അവൾ [എഴുതി]',
                'grammatical_features_item_ids': ['Q1392475'],
            },
            {
                'label': 'സാമാന്യ ഭാവികാലം',
                'example': 'അവൾ [എഴുതും]',
                'grammatical_features_item_ids': ['Q1475560'],
            },
        ],
    },

    'bokmål-noun-masculine': {
        '@attribution': {'users': ['Danmichaelo'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål hankjønnssubstantiv',
        'language_item_id': 'Q25167',
        'language_code': 'nb',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ubestemt entall',
                'example': 'Dette er en [båt].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'bestemt entall',
                'example': 'Dette er [båten].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851'],
            },
            {
                'label': 'ubestemt flertall',
                'example': 'Dette er noen [båter].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857'],
            },
            {
                'label': 'bestemt flertall',
                'example': 'Dette er [båtene].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851'],
            },
        ],
        'statements': statements('P5185', 'Q499327'),
    },

    'bokmål-noun-feminine': {
        '@attribution': {'users': ['Danmichaelo', 'Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål hunkjønnssubstantiv',
        'language_item_id': 'Q25167',
        'language_code': 'nb',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ubestemt entall',
                'example': 'Dette er ei [liste].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'bestemt entall hunkjønn',
                'example': 'Dette er [lista].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851', 'Q1775415'],
            },
            {
                'label': 'bestemt entall hankjønn',
                'example': 'Dette er [listen].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851', 'Q499327'],
            },
            {
                'label': 'ubestemt flertall',
                'example': 'Dette er noen [lister].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857'],
            },
            {
                'label': 'bestemt flertall',
                'example': 'Dette er [listene].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851'],
            },
        ],
        'statements': statements('P5185', 'Q1775415'),
    },

    'bokmål-noun-neuter': {
        '@attribution': {'users': ['Danmichaelo'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål intetkjønnssubstantiv',
        'language_item_id': 'Q25167',
        'language_code': 'nb',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ubestemt entall',
                'example': 'Dette er et [hus].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'bestemt entall',
                'example': 'Dette er [huset].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851'],
            },
            {
                'label': 'ubestemt flertall',
                'example': 'Dette er noen [hus].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857'],
            },
            {
                'label': 'bestemt flertall',
                'example': 'Dette er [husa].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851'],
            },
        ],
        'statements': statements('P5185', 'Q1775461'),
    },

    'bokmål-noun-masculine-neuter': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål han- og intetkjønnssubstantiv',
        'language_item_id': 'Q25167',
        'language_code': 'nb',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'ubestemt entall',
                'example': 'Nå kommer en/et [rap].',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857'],
            },
            {
                'label': 'bestemt entall, hankjønn',
                'example': 'Den [rapen] var ekkel.',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851', 'Q499327'],
            },
            {
                'label': 'bestemt entall, intetkjønn',
                'example': 'Det [rapet] var ekkelt.',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851', 'Q1775461'],
            },
            {
                'label': 'ubestemt flertall, hankjønn',
                'example': 'Flere [raper] på rad.',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857', 'Q499327'],
            },
            {
                # note: the part in parenetheses here is more usage instructions than label, could maybe be split into a different field later
                'label': 'ubestemt flertall, intetkjønn (utelat denne formen hvis den er identisk med den forrige, og fjern «hankjønn» fra forrige etter at leksemet er opprettet)',
                'example': 'Flere [rap] på rad.',
                'grammatical_features_item_ids': ['Q146786', 'Q53997857', 'Q1775461'],
                'optional': True,
            },
            {
                'label': 'bestemt flertall, han- og intetkjønn',
                'example': 'Alle de illeluktende [rapene].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851', 'Q499327', 'Q1775461'],
            },
            {
                'label': 'bestemt flertall, intetkjønn',
                'example': 'Alle de illeluktende [rapa].',
                'grammatical_features_item_ids': ['Q146786', 'Q53997851', 'Q1775461'],
            },
        ],
        'statements': {
            'P5185': [
                statement('P5185', 'Q499327'),
                statement('P5185', 'Q1775461'),
            ],
        },
    },

    'bokmål-adjective': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål adjektiv',
        'language_item_id': 'Q25167',
        'language_code': 'nb',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'ubestemt hankjønn og hunkjønn',
                'example': 'En [flink] person.',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857', 'Q499327', 'Q1775415'],
            },
            {
                'label': 'ubestemt intetkjønn',
                'example': 'Et [flinkt] barn.',
                'grammatical_features_item_ids': ['Q110786', 'Q53997857', 'Q1775461'],
            },
            {
                'label': 'bestemt entall',
                'example': 'Det [flinke] barnet.',
                'grammatical_features_item_ids': ['Q110786', 'Q53997851'],
            },
            {
                'label': 'flertall',
                'example': 'Alle de [flinke] barna.',
                'grammatical_features_item_ids': ['Q146786'],
            },
            {
                'label': 'komparativ',
                'example': 'Barnet er [flinkere] enn meg.',
                'grammatical_features_item_ids': ['Q14169499'],
                'optional': True,
            },
            {
                'label': 'superlativ',
                'example': 'Barnet var aller [flinkest].',
                'grammatical_features_item_ids': ['Q1817208'],
                'optional': True,
            },
            {
                'label': 'superlativ, bestemt form',
                'example': 'Det aller [flinkeste] barnet.',
                'grammatical_features_item_ids': ['Q1817208', 'Q53997851'],
                'optional': True,
            },
        ],
    },

    'bokmål-verb': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål verb',
        'language_item_id': 'Q25167',
        'language_code': 'nb',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'infinitiv',
                'example': 'Å [hilse].',
                'grammatical_features_item_ids': ['Q179230', 'Q1317831'],
            },
            {
                'label': 'presens',
                'example': 'Jeg [hilser].',
                'grammatical_features_item_ids': ['Q192613', 'Q1317831'],
            },
            {
                'label': 'preteritum',
                'example': 'Jeg [hilste].',
                'grammatical_features_item_ids': ['Q442485'],
            },
            {
                'label': 'presens perfektum',
                'example': 'Jeg har [hilst].',
                'grammatical_features_item_ids': ['Q1240211'],
            },
            {
                'label': 'imperativ',
                'example': 'Vennligst [hils] nå!',
                'grammatical_features_item_ids': ['Q22716'],
            },
            {
                'label': 'perfektum partisipp, hankjønn og hunkjønn',
                'example': 'En [hilst] person.',
                'grammatical_features_item_ids': ['Q12717679', 'Q110786', 'Q53997857', 'Q499327', 'Q1775415'],
            },
            {
                'label': 'perfektum partisipp, intetkjønn',
                'example': 'Et [hilst] barn.',
                'grammatical_features_item_ids': ['Q12717679', 'Q110786', 'Q53997857', 'Q1775461'],
            },
            {
                'label': 'perfektum partisipp, bestemt form',
                'example': 'Den [hilste] personen.',
                'grammatical_features_item_ids': ['Q12717679', 'Q110786', 'Q53997851'],
            },
            {
                'label': 'perfektum partisipp, flertall',
                'example': 'Mange [hilste] personer.',
                'grammatical_features_item_ids': ['Q12717679', 'Q146786'],
            },
            {
                'label': 'presens partisipp',
                'example': 'En [hilsende] person.',
                'grammatical_features_item_ids': ['Q10345583'],
            },
            {
                'label': 'passiv infinitiv',
                'example': 'X må ikke [hilses].',
                'grammatical_features_item_ids': ['Q179230', 'Q1194697'],
            },
            {
                'label': 'passiv presens',
                'example': 'X [hilses] av meg.',
                'grammatical_features_item_ids': ['Q192613', 'Q1194697'],
            },
        ],
    },

    'bokmål-verb-passive': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål s-verb',
        'language_item_id': 'Q25167',
        'language_code': 'nb',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': 'infinitiv',
                'example': 'Det er bra å [trives].',
                'grammatical_features_item_ids': ['Q179230', 'Q1194697'],
            },
            {
                'label': 'presens',
                'example': 'Jeg [trives] på skolen.',
                'grammatical_features_item_ids': ['Q192613', 'Q1194697'],
            },
            {
                'label': 'preteritum',
                'example': 'Jeg [trivdes] med det.',
                'grammatical_features_item_ids': ['Q442485', 'Q1194697'],
            },
            {
                'label': 'presens perfektum',
                'example': 'Jeg har [trivdes] med å være der…',
                'grammatical_features_item_ids': ['Q1240211', 'Q1194697'],
            },
            {
                'label': 'imperativ',
                'example': 'Vennligst [trives] nå!',
                'grammatical_features_item_ids': ['Q22716', 'Q1194697'],
            },
        ],
        'statements': statements('P31', 'Q54557461'),
    },

    'dutch-neuter-noun': 'dutch-noun-neuter',
    'dutch-noun-neuter': {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands onzijdig zelfstandig naamwoord',
        'language_item_id': 'Q7411',
        'language_code': 'nl',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775461'),
    },

    'dutch-masculine-noun': 'dutch-noun-masculine',
    'dutch-noun-masculine': {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands strikt mannelijk zelfstandig naamwoord',
        'language_item_id': 'Q7411',
        'language_code': 'nl',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q499327'),
    },

    'dutch-feminine-noun': 'dutch-noun-feminine',
    'dutch-noun-feminine': {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands strikt vrouwelijk zelfstandig naamwoord',
        'language_item_id': 'Q7411',
        'language_code': 'nl',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'dutch-fem2masc-noun': 'dutch-noun-fem2masc',
    'dutch-noun-fem2masc': {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands v/m zelfstandig naamwoord',
        'language_item_id': 'Q7411',
        'language_code': 'nl',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q64448167'),
    },

    'nynorsk-noun-feminine': {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk hokjønnssubstantiv',
        'language_item_id': 'Q25164',
        'language_code': 'nn',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'nynorsk-noun-masculine': {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk hankjønnssubstantiv',
        'language_item_id': 'Q25164',
        'language_code': 'nn',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q499327'),
    },

    'nynorsk-noun-neuter': {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk inkjekjønnssubstantiv',
        'language_item_id': 'Q25164',
        'language_code': 'nn',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775461'),
    },

    'odia-noun-human': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ବ୍ୟକ୍ତିବାଚକ ବିଶେଷ୍ୟ',
        'language_item_id': 'Q33810',
        'language_code': 'or',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'କର୍ତ୍ତୃବାଚ୍ଯ/କର୍ତ୍ତାକାରକ',
                'example': '[ଖେଳାଳି] ହକି ଖେଳୁଛନ୍ତି ।',
                'grammatical_features_item_ids': ['Q131105'],
            },
            {
                'label': 'କର୍ମ କାରକ',
                'example': 'ସେ [ଖେଳାଳିଙ୍କୁ] ଉତ୍ସାହିତ କଲେ ।',
                'grammatical_features_item_ids': ['Q146078'],
            },
            {
                'label': 'କରଣ କାରକ',
                'example': 'ସେ [ଖେଳାଳିଙ୍କଦ୍ୱାରା] ହକିର ପ୍ରସାର ହୋଇଛି ।',
                'grammatical_features_item_ids': ['Q192997'],
            },
            {
                'label': 'ସମ୍ପ୍ରଦାନ କାରକ',
                'example': 'ସେ [ଖେଳାଳିଙ୍କୁ] ପୁରସ୍କାର ଦେଲେ ।',
                'grammatical_features_item_ids': ['Q145599'],
            },
            {
                'label': 'ଅପାଦାନ କାରକ',
                'example': 'ସେ [ଖେଳାଳିଙ୍କଠାରୁ] ଭଲ ଖେଳାଳି ଏଠି ଆଉ କାହିଁ?',
                'grammatical_features_item_ids': ['Q156986'],
            },
            {
                'label': 'ସମ୍ବନ୍ଧ ପଦ',
                'example': 'ଏ [ଖେଳାଳିଙ୍କ] ସ୍ଥାନ ଫରୱାର୍ଡ଼ ।',
                'grammatical_features_item_ids': ['Q146233'],
            },
            {
                'label': 'ଅଧିକରଣ କାରକ',
                'example': 'ଏ [ଖେଳାଳିଙ୍କଠାରେ] ଦଳର ଭାରି ବିଶ୍ୱାସ ।',
                'grammatical_features_item_ids': ['Q202142'],
            },
        ],
    },

    'odia-noun-nonhuman': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ପ୍ରାଣୀବାଚକ ଓ ଅପ୍ରାଣୀବାଚକ ବିଶେଷ୍ୟ',
        'language_item_id': 'Q33810',
        'language_code': 'or',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'କର୍ତ୍ତୃବାଚ୍ଯ/କର୍ତ୍ତାକାରକ',
                'example': '[କୁକୁରଟି] ମାଂସ ଖାଉଛି ।',
                'grammatical_features_item_ids': ['Q131105'],
            },
            {
                'label': 'କର୍ମ କାରକ',
                'example': 'ସେ [କୁକୁରକୁ] ଖେଳାଉଛନ୍ତି ।',
                'grammatical_features_item_ids': ['Q146078'],
            },
            {
                'label': 'କରଣ କାରକ',
                'example': '[କୁକୁରଦ୍ୱାରା] ପୋଲିସ ଅନୁସନ୍ଧାନ କରୁଛି ।',
                'grammatical_features_item_ids': ['Q192997'],
            },
            {
                'label': 'ସମ୍ପ୍ରଦାନ କାରକ',
                'example': '[କୁକୁରକୁ] ଆଉ ଦୁଇଖଣ୍ଡ ମାଂସ ଦିଅ ।',
                'grammatical_features_item_ids': ['Q145599'],
            },
            {
                'label': 'ଅପାଦାନ କାରକ',
                'example': '[କୁକୁରଠାରୁ] ବଳି ସାଙ୍ଗ କିଏ?',
                'grammatical_features_item_ids': ['Q156986'],
            },
            {
                'label': 'ସମ୍ବନ୍ଧ ପଦ',
                'example': 'ଆମ [କୁକୁରର] ଭୁକିବା ଶୁଭୁଛି ।',
                'grammatical_features_item_ids': ['Q146233'],
            },
            {
                'label': 'ଅଧିକରଣ କାରକ',
                'example': 'ତାଙ୍କର ଏ [କୁକୁରଠାରେ] ଭାରୀ ଭାବ ।',
                'grammatical_features_item_ids': ['Q202142'],
            },
            {
                'label': 'ସମ୍ବୋଧକ କାରକ',
                'example': '[କୁକୁରରେ] କୁକୁର! କେଉଁଠି ଅଛୁ?',
                'grammatical_features_item_ids': ['Q185077'],
            },
        ],
    },

    'odia-adjective-nongendered': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ଲିଙ୍ଗବିହୀନ ବିଶେଷଣ',
        'language_item_id': 'Q33810',
        'language_code': 'or',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'ଅସ୍ତିବାଚକ',
                'example': 'ଏଇଟି ଏକ [କ୍ଷୀପ୍ର] କୁକୁର ।',
                'grammatical_features_item_ids': ['Q3482678'],
            },
            {
                'label': 'ତୁଳନାତ୍ମକ-ମଧ୍ୟ',
                'example': 'ଏ କୁକରଟି ଆର କୁକୁରଠାରୁ [କ୍ଷୀପ୍ରତର] ।',
                'grammatical_features_item_ids': ['Q14169499'],
            },
            {
                'label': 'ତୁଳନାତ୍ମକ-ଶ୍ରେଷ୍ଠ',
                'example': 'ଏ କୁକୁର ଦୁନିଆର ସବୁ କୁକୁରଙ୍କ ଭିତରେ [କ୍ଷୀପ୍ରତମ] ।',
                'grammatical_features_item_ids': ['Q1817208'],
            },
        ],
    },

    'odia-adjective-gendered': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ଲିଙ୍ଗସୂଚକ ବିଶେଷଣ',
        'language_item_id': 'Q33810',
        'language_code': 'or',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': 'ବିଶେଷଣ-ମହିଳା',
                'example': 'ସେ ଗୋଟିଏ [ଜ୍ଞାନବତୀ] ଝିଅ ।',
                'grammatical_features_item_ids': ['Q1775415'],
            },
            {
                'label': 'ବିଶେଷଣ-ପୁରୁଷ',
                'example': 'ସେ ଗୋଟିଏ [ଜ୍ଞାନବାନ] ପିଲା ।',
                'grammatical_features_item_ids': ['Q499327'],
            },
        ],
    },

    'odia-adverb': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ଓଡ଼ିଆ କ୍ରିୟା ବିଶେଷଣ',
        'language_item_id': 'Q33810',
        'language_code': 'or',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'କ୍ରିୟା ବିଶେଷଣ',
                'example': 'ସେ [ଧୀରେ] ଚାଲୁଛନ୍ତି ।',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'polish-noun': {
        '@attribution': {'users': ['KaMan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Polish'},
        'label': 'polski rzeczownik, prosta odmiana bez wariantów w żadnym z przypadków',
        'language_item_id': 'Q809',
        'language_code': 'pl',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
    },

    'polish-noun-masculine-personal-with-depreciative-forms': {
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
                'statements': statements('P31', 'Q54948995'),
            },
            {
                'label': 'mianownik, liczba mnoga, forma deprecjatywna',
                'example': 'To są te [robotniki].',
                'grammatical_features_item_ids': ['Q131105', 'Q146786'],
                'statements': statements('P31', 'Q54948374'),
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
                'statements': statements('P31', 'Q54948995'),
            },
            {
                'label': 'wołacz, liczba mnoga, forma deprecjatywna',
                'example': 'te [robotniki]',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
                'statements': statements('P31', 'Q54948374'),
            },
        ],
        'statements': statements('P5185', 'Q27918551'),
    },

    'polish-noun-with-potential-plural-forms': {
        '@attribution': {'users': ['KaMan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Polish'},
        'label': 'polski rzeczownik, potencjalna liczba mnoga',
        'language_item_id': 'Q809',
        'language_code': 'pl',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                'statements': statements('P31', 'Q54944750'),
            },
            {
                'label': 'dopełniacz, liczba mnoga, forma potencjalna',
                'example': 'Wśród nas nie ma [językoznawstw].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
                'statements': statements('P31', 'Q54944750'),
            },
            {
                'label': 'celownik, liczba mnoga, forma potencjalna',
                'example': 'Przyglądam się [językoznawstwom].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
                'statements': statements('P31', 'Q54944750'),
            },
            {
                'label': 'biernik, liczba mnoga, forma potencjalna',
                'example': 'Widzę [językoznawstwa].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
                'statements': statements('P31', 'Q54944750'),
            },
            {
                'label': 'narzędnik, liczba mnoga, forma potencjalna',
                'example': 'Idę z [językoznawstwami].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
                'statements': statements('P31', 'Q54944750'),
            },
            {
                'label': 'miejscownik, liczba mnoga, forma potencjalna',
                'example': 'Myślę o [językoznawstwach].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
                'statements': statements('P31', 'Q54944750'),
            },
            {
                'label': 'wołacz, liczba mnoga, forma potencjalna',
                'example': '[językoznawstwa]',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
                'statements': statements('P31', 'Q54944750'),
            },
        ],
    },

    'portuguese-noun-biform': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'substantivo biforme em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'masculino singular normal',
                'example': 'Eu vi um [amigo] seu.',
                'grammatical_features_item_ids': ['Q499327', 'Q110786', 'Q3482678'],
            },
            {
                'label': 'masculino plural normal',
                'example': 'Eu vi uns [amigos] seus.',
                'grammatical_features_item_ids': ['Q499327', 'Q146786', 'Q3482678'],
            },
            {
                'label': 'feminino singular normal',
                'example': 'Eu vi uma [amiga] sua.',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786', 'Q3482678'],
            },
            {
                'label': 'feminino plural normal',
                'example': 'Eu vi umas [amigas] suas.',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786', 'Q3482678'],
            },
            {
                'section_break': True,
                'label': 'masculino singular diminutivo',
                'example': 'Eu vi um [amiguinho] seu.',
                'grammatical_features_item_ids': ['Q499327', 'q110786', 'Q108709'],
                'optional': True,
            },
            {
                'label': 'masculino plural diminutivo',
                'example': 'Eu vi uns [amiguinhos] seus.',
                'grammatical_features_item_ids': ['Q499327', 'Q146786', 'Q108709'],
                'optional': True,
            },
            {
                'label': 'feminino singular diminutivo',
                'example': 'Eu vi uma [amiguinha] sua.',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786', 'Q108709'],
                'optional': True,
            },
            {
                'label': 'feminino plural diminutivo',
                'example': 'Eu vi umas [amiguinhas] suas.',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786', 'Q108709'],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'masculino singular aumentativo',
                'example': 'Eu vi um [amigão] seu.',
                'grammatical_features_item_ids': ['Q499327', 'Q110786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'masculino plural aumentativo',
                'example': 'Eu vi uns [amigões] seus.',
                'grammatical_features_item_ids': ['Q499327', 'Q146786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'feminino singular aumentativo',
                'example': 'Eu vi uma [amigona] sua.',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'feminino plural aumentativo',
                'example': 'Eu vi umas [amigonas] suas.',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786', 'Q1358239'],
                'optional': True,
            },
        ],
    },

    'portuguese-noun-masculine': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'substantivo masculino em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'singular normal',
                'example': 'Ele tem um [nariz].',
                'grammatical_features_item_ids': ['Q110786', 'Q3482678'],
            },
            {
                'label': 'plural normal',
                'example': 'Eles têm uns [narizes].',
                'grammatical_features_item_ids': ['Q146786', 'Q3482678'],
            },
            {
                'section_break': True,
                'label': 'singular diminutivo',
                'example': 'Ele tem um [narizinho/narizito].',
                'grammatical_features_item_ids': ['Q110786', 'Q108709'],
                'optional': True,
            },
            {
                'label': 'plural diminutivo',
                'example': 'Eles têm uns [narizinhos/narizitos].',
                'grammatical_features_item_ids': ['Q146786', 'Q108709'],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular aumentativo',
                'example': 'Ele tem um [narigão/narizão].',
                'grammatical_features_item_ids': ['Q110786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'plural aumentativo',
                'example': 'Eles têm uns [narigões/narizões].',
                'grammatical_features_item_ids': ['Q146786', 'Q1358239'],
                'optional': True,
            },
        ],
        'statements': statements('P5185', 'Q499327'),
    },

    'portuguese-noun-feminine': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'substantivo feminino em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'singular feminino normal',
                'example': 'Ela tem uma [boca].',
                'grammatical_features_item_ids': ['Q110786', 'Q3482678'],
            },
            {
                'label': 'plural feminino normal',
                'example': 'Elas têm umas [bocas].',
                'grammatical_features_item_ids': ['Q146786', 'Q3482678'],
            },
            {
                'section_break': True,
                'label': 'singular feminino diminutivo',
                'example': 'Ela tem uma [boquinha/boquita].',
                'grammatical_features_item_ids': ['Q110786', 'Q108709'],
                'optional': True,
            },
            {
                'label': 'plural feminino diminutivo',
                'example': 'Elas têm umas [boquinhas/boquitas].',
                'grammatical_features_item_ids': ['Q146786', 'Q108709'],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular feminino aumentativo',
                'example': 'Ela tem uma [bocona/bocarra].',
                'grammatical_features_item_ids': ['Q110786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'plural feminino aumentativo',
                'example': 'Elas têm umas [boconas/bocarras].',
                'grammatical_features_item_ids': ['Q146786', 'Q1358239'],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular masculino aumentativo',
                'example': 'Ela tem um [bocão].',
                'grammatical_features_item_ids': ['Q499327', 'Q110786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'plural masculino aumentativo',
                'example': 'Elas têm uns [bocões].',
                'grammatical_features_item_ids': ['Q499327', 'Q146786', 'Q1358239'],
                'optional': True,
            },
        ],
        'statements': statements('P5185', 'Q1775415'),
    },

    'portuguese-noun-uniform': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'substantivo uniforme em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'uniforme singular normal',
                'example': 'Nós temos que encontrar aquele(a) [motorista] hoje mesmo.',
                'grammatical_features_item_ids': ['Q110786', 'Q3482678'],
            },
            {
                'label': 'uniforme plural normal',
                'example': 'Nós temos que encontrar aqueles(as) [motoristas] hoje mesmo.',
                'grammatical_features_item_ids': ['Q146786', 'Q3482678'],
            },
        ],
        'statements': statements('P5185', 'Q18478758'),
    },

    'portuguese-verb': {
        '@attribution': {'users': ['Carybe', 'EnaldoSS', 'Joalpe', 'Waldir'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'verbo em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q24905',
        'two_column_sections': True,
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
                'section_break': True,
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
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Eu [cantei] ontem no palco.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q64005357', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Tu [cantaste] ontem no palco.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q64005357', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Ele [cantou] ontem no palco.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q64005357', 'Q682111'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Nós [cantamos] ontem no palco.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q64005357', 'Q682111'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Vós [cantastes] ontem no palco.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q64005357', 'Q682111'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Eles [cantaram] ontem no palco.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q64005357', 'Q682111'],
            },
            {
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
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
                'section_break': True,
                'label': 'Segunda Pessoa do Singular do Modo Imperativo Afirmativo',
                'example': '[canta] tu agora que há tempo.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q64012400'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Modo Imperativo Afirmativo',
                'example': '[canta] você agora que há tempo.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q64012400'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[cantemos] nós agora que há tempo.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q64012400'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[cantai] vós agora que há tempo.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q64012400'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[cantem] vocês agora que há tempo.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q64012400'],
            },
            {
                'section_break': True,
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
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantar] eu ganhei vários prêmios.',
                'grammatical_features_item_ids': ['Q21714344', 'Q110786', 'Q106236131'],
            },
            {
                'label': 'Segunda Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantares] tu ganhaste vários prêmios.',
                'grammatical_features_item_ids': ['Q51929049', 'Q110786', 'Q106236131'],
            },
            {
                'label': 'Terceira Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantar] ele ganhou vários prêmios.',
                'grammatical_features_item_ids': ['Q51929074', 'Q110786', 'Q106236131'],
            },
            {
                'label': 'Primeira Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantarmos] nós ganhamos vários prêmios.',
                'grammatical_features_item_ids': ['Q21714344', 'Q146786', 'Q106236131'],
            },
            {
                'label': 'Segunda Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantardes] vós ganhastes vários prêmios.',
                'grammatical_features_item_ids': ['Q51929049', 'Q146786', 'Q106236131'],
            },
            {
                'label': 'Terceira Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantarem] eles ganharam vários prêmios.',
                'grammatical_features_item_ids': ['Q51929074', 'Q146786', 'Q106236131'],
            },
        ],
    },

    'portuguese-adjective': [
        'portuguese-adjective-biform',
        'portuguese-adjective-uniform',
    ],

    'portuguese-adjective-biform': {
        '@attribution': {'users': ['EnaldoSS', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'adjetivo biforme em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q34698',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'singular masculino normal',
                'example': 'Eu vi um homem [alto].',
                'grammatical_features_item_ids': ['Q499327', 'Q110786', 'Q3482678'],
            },
            {
                'label': 'plural masculino normal',
                'example': 'Eu vi uns homens [altos].',
                'grammatical_features_item_ids': ['Q499327', 'Q146786', 'Q3482678'],
            },
            {
                'label': 'singular feminino normal',
                'example': 'Eu vi uma mulher [alta].',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786', 'Q3482678'],
            },
            {
                'label': 'plural feminino normal',
                'example': 'Eu vi umas mulheres [altas].',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786', 'Q3482678'],
            },
            {
                'section_break': True,
                'label': 'singular masculino superlativo',
                'example': 'Eu vi um homem [altíssimo].',
                'grammatical_features_item_ids': ['Q499327', 'Q110786', 'Q1817208'],
                'optional': True,
            },
            {
                'label': 'plural masculino superlativo',
                'example': 'Eu vi uns homens [altíssimos].',
                'grammatical_features_item_ids': ['Q499327', 'Q146786', 'Q1817208'],
                'optional': True,
            },
            {
                'label': 'singular feminino superlativo',
                'example': 'Eu vi uma mulher [altíssima].',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786', 'Q1817208'],
                'optional': True,
            },
            {
                'label': 'plural feminino superlativo',
                'example': 'Eu vi umas mulheres [altíssimas].',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786', 'Q1817208'],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular masculino diminutivo',
                'example': 'Eu vi um homem [altinho].',
                'grammatical_features_item_ids': ['Q499327', 'Q110786', 'Q108709'],
                'optional': True,
            },
            {
                'label': 'plural masculino diminutivo',
                'example': 'Eu vi uns homens [altinhos].',
                'grammatical_features_item_ids': ['Q499327', 'Q146786', 'Q108709'],
                'optional': True,
            },
            {
                'label': 'singular feminino diminutivo',
                'example': 'Eu vi uma mulher [altinha].',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786', 'Q108709'],
                'optional': True,
            },
            {
                'label': 'plural feminino diminutivo',
                'example': 'Eu vi umas mulheres [altinhas].',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786', 'Q108709'],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular masculino aumentativo',
                'example': 'Eu vi um homem [altão].',
                'grammatical_features_item_ids': ['Q499327', 'Q110786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'plural masculino aumentativo',
                'example': 'Eu vi uns homens [altões].',
                'grammatical_features_item_ids': ['Q499327', 'Q146786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'singular feminino aumentativo',
                'example': 'Eu vi uma mulher [altona].',
                'grammatical_features_item_ids': ['Q1775415', 'Q110786', 'Q1358239'],
                'optional': True,
            },
            {
                'label': 'plural feminino aumentativo',
                'example': 'Eu vi umas mulheres [altonas].',
                'grammatical_features_item_ids': ['Q1775415', 'Q146786', 'Q1358239'],
                'optional': True,
            },
        ],
    },

    'portuguese-adjective-uniform': {
        '@attribution': {'users': ['EnaldoSS', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'adjetivo uniforme em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q34698',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'uniforme singular normal',
                'example': 'Acho sim que ele(a) é um(a) bom(a) [artista].',
                'grammatical_features_item_ids': ['Q110786', 'Q3482678'],
            },
            {
                'label': 'uniforme plural normal',
                'example': 'Acho sim que eles(as) são bons(as) [artistas].',
                'grammatical_features_item_ids': ['Q146786', 'Q3482678'],
            },
        ],
        'statements': statements('P5185', 'Q18478758'),
    },

    'portuguese-adverb-modal': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'advérbio de modo em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': 'Advérbio de modo',
                'example': 'A prova estava [extremamente] difícil.',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements('P31', 'Q1941737'),
    },

    'portuguese-idiom': [
        'portuguese-phrase-nominal',
        'portuguese-phrase-verbal',
        'portuguese-phrase-adjectival',
        'portuguese-phrase-adverbial',
    ],

    'portuguese-phrase-nominal': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'frase nominal em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q1401131',
        'forms': [
            {
                'label': 'Frase nominal',
                'example': 'João não entendeu muito bem o que ela quis dizer com [fundo do poço].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'portuguese-phrase-verbal': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'frase verbal em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q1778442',
        'forms': [
            {
                'label': 'Frase verbal',
                'example': 'João não entendeu muito bem o que ela quis dizer com [abandonar o barco].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'portuguese-phrase-adjectival': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'frase adjetival em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q357760',
        'forms': [
            {
                'label': 'Frase adjetival',
                'example': 'João não entendeu muito bem o que ela quis dizer com [fora de moda].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'portuguese-phrase-adverbial': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'frase adverbial em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q3734650',
        'forms': [
            {
                'label': 'Frase adverbial',
                'example': 'João não entendeu muito bem o que ela quis dizer com [no dia de São Nunca].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'portuguese-proverb': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'provérbio em português',
        'language_item_id': 'Q5146',
        'language_code': 'pt',
        'lexical_category_item_id': 'Q35102',
        'forms': [
            {
                'label': 'Provérbio',
                'example': 'Se ela estivesse aqui, diria que [em boca fechada não entra mosca].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'russian-noun-masculine': {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
        'label': 'русское существительное, мужской род',
        'language_item_id': 'Q7737',
        'language_code': 'ru',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q499327'),
    },

    'russian-noun-feminine': {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
        'label': 'русское существительное, женский род',
        'language_item_id': 'Q7737',
        'language_code': 'ru',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'russian-noun-neuter': {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
        'label': 'русское существительное, средний род',
        'language_item_id': 'Q7737',
        'language_code': 'ru',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775461'),
    },

    'russian-noun-pluraletantum': {
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
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет [ножниц].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать [ножницам].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу [ножницы].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу [ножницами].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о [ножницах].',
                'grammatical_features_item_ids': ['Q2114906', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
        ],
        'statements': statements('P31', 'Q138246'),
    },

    'russian-adjective': {
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
    },

    'swedish-noun-common': {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt substantiv (utrum)',
        'language_item_id': 'Q9027',
        'language_code': 'sv',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                'section_break': True,
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
        'statements': statements('P5185', 'Q1305037'),
    },

    'swedish-noun-neuter': {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt substantiv (neutrum)',
        'language_item_id': 'Q9027',
        'language_code': 'sv',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
                'section_break': True,
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
        'statements': statements('P5185', 'Q1775461'),
    },

    'swedish-noun-proper': {
        '@attribution': {'users': ['LA2'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt egennamn',
        'language_item_id': 'Q9027',
        'language_code': 'sv',
        'lexical_category_item_id': 'Q147276',
        'forms': [
            {
                'label': 'nominativ',
                'example': 'Jag ser [Sara].',
                'grammatical_features_item_ids': ['Q131105'],
            },
            {
                'label': 'genitiv',
                'example': 'Jag imponeras av [Saras] utseende.',
                'grammatical_features_item_ids': ['Q146233'],
            },
        ],
        'statements': statements('P5185', 'Q1775461'),
    },

    'swedish-verb': {
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
    },

    'swedish-absolute-adjective': 'swedish-adjective-absolute',
    'swedish-adjective-absolute': {
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
                'grammatical_features_item_ids_optional': set(['Q3482678']),
            },
            {
                'label': 'obestämd singular, neutrum',
                'example': 'ett [tolvårigt] barn',
                'grammatical_features_item_ids': ['Q53997857', 'Q110786', 'Q1775461', 'Q3482678'],
                'grammatical_features_item_ids_optional': set(['Q3482678']),
            },
            {
                'label': 'bestämd singular, maskulinum',
                'example': 'den [tolvårige] pojken',
                'grammatical_features_item_ids': ['Q53997851', 'Q110786', 'Q499327', 'Q3482678'],
                'grammatical_features_item_ids_optional': set(['Q3482678']),
            },
            {
                'label': 'bestämd singular, utrum/neutrum',
                'example': 'det [tolvåriga] barnet',
                'grammatical_features_item_ids': ['Q53997851', 'Q110786', 'Q3482678'],
                'grammatical_features_item_ids_optional': set(['Q3482678']),
            },
            {
                'label': 'bestämd plural',
                'example': 'de [tolvåriga] barnen',
                'grammatical_features_item_ids': ['Q53997851', 'Q146786', 'Q3482678'],
                'grammatical_features_item_ids_optional': set(['Q3482678']),
            },
        ],
        'statements': statements('P31', 'Q332375'),
    },

    'swedish-adjective': {
        '@attribution': {'users': ['Belteshassar', 'Ainali'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt adjektiv (med komparativ)',
        'language_item_id': 'Q9027',
        'language_code': 'sv',
        'lexical_category_item_id': 'Q34698',
        'two_column_sections': False,
        'forms': [
            {
                'label': 'positiv obestämd singular, utrum',
                'example': 'en [ung] pojke',
                'grammatical_features_item_ids': ['Q53997857', 'Q110786', 'Q1305037', 'Q3482678'],
            },
            {
                'label': 'positiv obestämd singular, neutrum',
                'example': 'ett [ungt] barn',
                'grammatical_features_item_ids': ['Q53997857', 'Q110786', 'Q1775461', 'Q3482678'],
            },
            {
                'label': 'positiv bestämd singular, maskulinum',
                'example': 'den [unge] pojken',
                'grammatical_features_item_ids': ['Q53997851', 'Q110786', 'Q499327', 'Q3482678'],
            },
            {
                'label': 'positiv bestämd singular, utrum/neutrum',
                'example': 'det [unga] barnet',
                'grammatical_features_item_ids': ['Q53997851', 'Q110786', 'Q3482678'],
            },
            {
                'label': 'positiv plural',
                'example': 'de [unga] barnen',
                'grammatical_features_item_ids': ['Q146786', 'Q3482678'],
            },
            {
                'section_break': True,
                'label': 'komparativ (kongruensböjs inte)',
                'example': 'pojken är [yngre] än flickan',
                'grammatical_features_item_ids': ['Q14169499'],
            },
            {
                'section_break': True,
                'label': 'superlativ predikativ',
                'example': 'pojken är [yngst] av alla barnen',
                'grammatical_features_item_ids': ['Q1817208', 'Q1931259'],
            },
            {
                'label': 'superlativ singular attributiv bestämd maskulinum',
                'example': 'den [yngste] pojken i klassen',
                'grammatical_features_item_ids': ['Q1817208', 'Q110786', 'Q53997851', 'Q499327', 'Q4818723'],
            },
            {
                'label': 'superlativ singular attributiv bestämd',
                'example': 'det [yngsta] barnet i klassen',
                'grammatical_features_item_ids': ['Q1817208', 'Q110786', 'Q53997851', 'Q4818723'],
            },
            {
                'label': 'superlativ plural attributiv',
                'example': 'de [yngsta] pojkarna i klassen',
                'grammatical_features_item_ids': ['Q1817208', 'Q146786', 'Q4818723'],
            },
        ],
    },

    'ukrainian-noun-masculine': {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, чоловічий рід',
        'language_item_id': 'Q8798',
        'language_code': 'uk',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q499327'),
    },

    'ukrainian-noun-feminine': {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, жіночий рід',
        'language_item_id': 'Q8798',
        'language_code': 'uk',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775415'),
    },

    'ukrainian-noun-neuter': {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, середній рід',
        'language_item_id': 'Q8798',
        'language_code': 'uk',
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
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
        'statements': statements('P5185', 'Q1775461'),
    },

    'ukrainian-noun-pluraletantum': {
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
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'родовий відмінок',
                'example': 'Ніде нема [ножиць].',
                'grammatical_features_item_ids': ['Q146233', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'давальний відмінок',
                'example': 'Віддати це [ножицям].',
                'grammatical_features_item_ids': ['Q145599', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'знахідний відмінок',
                'example': 'Я бачу [ножиці].',
                'grammatical_features_item_ids': ['Q146078', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'орудний відмінок',
                'example': 'Я користуюсь цими [ножицями].',
                'grammatical_features_item_ids': ['Q192997', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'місцевий відмінок',
                'example': 'Папір застряг в [ножицях].',
                'grammatical_features_item_ids': ['Q202142', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
            {
                'label': 'кличний відмінок',
                'example': 'Привіт, [ножиці].',
                'grammatical_features_item_ids': ['Q185077', 'Q146786'],
                'grammatical_features_item_ids_optional': set(['Q146786']),
            },
        ],
        'statements': statements('P31', 'Q138246'),
    },

    'yoruba-noun': {
        '@attribution': {'users': ['T Cells'], 'title': 'Wikidata:Wikidata Lexeme Forms/Yoruba'},
        'label': 'Orúkọ Yorùbá',
        'language_item_id': 'Q34311',
        'language_code': 'yo',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': 'kan',
                'example': 'mo tẹ̀lé ọkunrin [kan] lọ oko.',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-noun': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語名詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q1084',
        'forms': [
            {
                'label': '形音一',
                'example': '這就是[大夫]。',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-pronoun': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語代詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q36224',
        'forms': [
            {
                'label': '形音一',
                'example': '就是[這兒]。',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-verb': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語動詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q24905',
        'forms': [
            {
                'label': '形音一',
                'example': '那個[看]了嗎？',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-adjective': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語形容詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': '形音一',
                'example': '這東西很[好]。',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-adjective-non-predicative': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語區別詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q34698',
        'forms': [
            {
                'label': '形音一',
                'example': '這東西是[雄]的。',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements('P1552', 'Q110106987'),
    },

    'mandarin-adverb': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語副詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q380057',
        'forms': [
            {
                'label': '形音一',
                'example': '這[已經]做了。',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-interjection': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語感歎詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q83034',
        'forms': [
            {
                'label': '形音一',
                'example': '[啊]，這個……。',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-preposition': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語介詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q4833830',
        'forms': [
            {
                'label': '形音一',
                'example': '這個[跟]那個這樣發生了。',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-classifier': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語量詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q63153',
        'forms': [
            {
                'label': '形音一',
                'example': '這是一[件]什麽東西來著？',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements('P1552', 'Q849760'),
    },

    'mandarin-numeral': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語數詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q63116',
        'forms': [
            {
                'label': '形音一',
                'example': '這裡有[一]個字。',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'mandarin-particle': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語助詞',
        'language_item_id': 'Q727694',
        'language_code': 'zh',
        'lexical_category_item_id': 'Q184943',
        'forms': [
            {
                'label': '形音一',
                'example': '[了]',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'german-noun-neuter-test': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': None},
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
                'statements': statements('P82', 'Q1249'),
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
                'statements': statements('P82', 'Q74568'),
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
        'statements': statements('P73601', 'Q163008'),
    },

}


templates_without_redirects = {
    template_name: template
    for template_name, template in templates.items()
    if isinstance(template, dict)
}


for template_name, template in templates_without_redirects.items():
    template['@template_name'] = template_name
