from typing import Dict, List, Literal, NewType, Optional, Set, TypedDict, Union
from typing_extensions import NotRequired

from entity_ids import *
from wikibase_types import Snak, Statement, Statements


class TemplateForm(TypedDict):
    section_break: NotRequired[bool]
    label: str
    example: str
    grammatical_features_item_ids: List[str]
    grammatical_features_item_ids_optional: NotRequired[Set[str]]
    optional: NotRequired[bool]
    statements: NotRequired[Statements]

class Attribution(TypedDict):
    users: List[str]
    title: Optional[str]

class Language(TypedDict):
    language_item_id: str
    language_code: str

_InternalTemplate = TypedDict('_InternalTemplate', {
    '@attribution': NotRequired[Attribution],
    'test': NotRequired[bool],
    'label': str,
    'language': Language,
    'lexical_category_item_id': str,
    'two_column_sections': NotRequired[bool],
    'forms': List[TemplateForm],
    'statements': NotRequired[Statements],
    '@template_name': NotRequired[str],
})

Template = TypedDict('Template', {
    '@attribution': NotRequired[Attribution],
    'test': NotRequired[bool],
    'label': str,
    'language_item_id': str,
    'language_code': str,
    'lexical_category_item_id': str,
    'two_column_sections': NotRequired[bool],
    'forms': List[TemplateForm],
    'statements': NotRequired[Statements],
    '@template_name': NotRequired[str],
})

StatementValue = Union[str, Literal['somevalue'], Literal['novalue']]

def statement(property_id: str, item_id: StatementValue) -> Statement:
    snak: Snak
    if item_id == 'novalue':
        snak = {
            'snaktype': 'novalue',
            'property': property_id,
            'datatype': 'wikibase-item',
        }
    elif item_id == 'somevalue':
        snak = {
            'snaktype': 'somevalue',
            'property': property_id,
            'datatype': 'wikibase-item',
        }
    else:
        snak = {
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
        }
    return {
        'mainsnak': snak,
        'type': 'statement',
        'rank': 'normal',
    }


def statements(property_id: str, item_id: StatementValue) -> Statements:
    return {
        property_id: [
            statement(property_id, item_id),
        ],
    }


language_Esperanto: Language = {
    'language_item_id': Esperanto,
    'language_code': 'eo',
}
language_French: Language = {
    'language_item_id': French,
    'language_code': 'fr',
}
language_German: Language = {
    'language_item_id': German,
    'language_code': 'de',
}
language_Latin: Language = {
    'language_item_id': Latin,
    'language_code': 'la',
}
language_Italian: Language = {
    'language_item_id': Italian,
    'language_code': 'it',
}
language_Polish: Language = {
    'language_item_id': Polish,
    'language_code': 'pl',
}
language_Spanish: Language = {
    'language_item_id': Spanish,
    'language_code': 'es',
}
language_Finnish: Language = {
    'language_item_id': Finnish,
    'language_code': 'fi',
}
language_English: Language = {
    'language_item_id': English,
    'language_code': 'en',
}
language_Portuguese: Language = {
    'language_item_id': Portuguese,
    'language_code': 'pt',
}
language_Croatian: Language = {
    'language_item_id': Croatian,
    'language_code': 'hr',
}
language_Dutch: Language = {
    'language_item_id': Dutch,
    'language_code': 'nl',
}
language_Russian: Language = {
    'language_item_id': Russian,
    'language_code': 'ru',
}
language_Basque: Language = {
    'language_item_id': Basque,
    'language_code': 'eu',
}
language_Armenian: Language = {
    'language_item_id': Armenian,
    'language_code': 'hy',
}
language_Ukrainian: Language = {
    'language_item_id': Ukrainian,
    'language_code': 'uk',
}
language_Swedish: Language = {
    'language_item_id': Swedish,
    'language_code': 'sv',
}
language_Danish: Language = {
    'language_item_id': Danish,
    'language_code': 'da',
}
language_Czech: Language = {
    'language_item_id': Czech,
    'language_code': 'cs',
}
language_Estonian: Language = {
    'language_item_id': Estonian,
    'language_code': 'et',
}
language_Latvian: Language = {
    'language_item_id': Latvian,
    'language_code': 'lv',
}
language_Persian: Language = {
    'language_item_id': Persian,
    'language_code': 'fa',
}
language_Hebrew: Language = {
    'language_item_id': Hebrew,
    'language_code': 'he',
}
language_Bengali: Language = {
    'language_item_id': Bengali,
    'language_code': 'bn',
}
language_Hindi: Language = {
    'language_item_id': Hindustani,
    'language_code': 'hi',
}
language_Urdu: Language = {
    'language_item_id': Hindustani,
    'language_code': 'ur',
}
language_Breton: Language = {
    'language_item_id': Breton,
    'language_code': 'br',
}
language_Nynorsk: Language = {
    'language_item_id': Nynorsk,
    'language_code': 'nn',
}
language_Bokmål: Language = {
    'language_item_id': Bokmål,
    'language_code': 'nb',
}
language_Asturian: Language = {
    'language_item_id': Asturian,
    'language_code': 'ast',
}
language_Igbo: Language = {
    'language_item_id': Igbo,
    'language_code': 'ig',
}
language_Odia: Language = {
    'language_item_id': Odia,
    'language_code': 'or',
}
language_Yoruba: Language = {
    'language_item_id': Yoruba,
    'language_code': 'yo',
}
language_Kurmanji: Language = {
    'language_item_id': Kurmanji,
    'language_code': 'ku',
}
language_Malayalam: Language = {
    'language_item_id': Malayalam,
    'language_code': 'ml',
}
language_Shahmukhi: Language = {
    'language_item_id': Punjabi,
    'language_code': 'pnb',
}
language_Gurmukhi: Language = {
    'language_item_id': Punjabi,
    'language_code': 'pa',
}
language_Hindko: Language = {
    'language_item_id': Hindko,
    'language_code': 'hno',
}
language_Standard_Mandarin: Language = {
    'language_item_id': Standard_Mandarin,
    'language_code': 'zh',
}
language_Manbhumi: Language = {
    'language_item_id': Manbhumi,
    'language_code': 'bn-x-Q6747180',
}


_internal_templates: Dict[str, Union[str, list[str], _InternalTemplate]] = {

    'asturian-noun-masculine': {
        '@attribution': {'users': ['Oriciu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Asturian'},
        'label': 'nome común masculín asturianu',
        'language': language_Asturian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singular',
                'example': 'Esti ye un [perru].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'plural',
                'example': 'Estos son unos [perros].',
                'grammatical_features_item_ids': [plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'asturian-noun-feminine': {
        '@attribution': {'users': ['Oriciu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Asturian'},
        'label': 'nome común femenín asturianu',
        'language': language_Asturian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singular',
                'example': 'Esta ye una [perra].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'plural',
                'example': 'Estes son unes [perres].',
                'grammatical_features_item_ids': [plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'bengali-noun-animate': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'প্রাণীবাচক বিশেষ্য',
        'language': language_Bengali,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'কর্তৃকারক',
                'example': 'আমার [কুকুর] ওখানে গিয়েছে।',
                'grammatical_features_item_ids': [nominative_case],
            },
            {
                'label': 'সম্বন্ধ পদ',
                'example': 'এটা আমার [কুকুরের] নাম।',
                'grammatical_features_item_ids': [genitive_case],
            },
            {
                'label': 'কর্ম কারক',
                'example': 'আমার [কুকুরকে] পছন্দ হয়েছে?',
                'grammatical_features_item_ids': [accusative_case],
            },
            {
                'label': 'সম্প্রদান কারক',
                'example': 'আমার [কুকুরকে] মাংস দিন।',
                'grammatical_features_item_ids': [dative_case],
            },
        ],
    },

    'bengali-noun-inanimate-othervowels': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'অপ্রাণীবাচক বিশেষ্য (-আ/এ/ও-কারান্ত শব্দ)',
        'language': language_Bengali,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'কর্তৃকারক',
                'example': 'আমার [জামা] রঙিন।',
                'grammatical_features_item_ids': [nominative_case],
            },
            {
                'label': 'সম্বন্ধ পদ',
                'example': 'এই [জামার] রঙ নীল।',
                'grammatical_features_item_ids': [genitive_case],
            },
            {
                'label': 'কর্ম কারক',
                'example': 'সে তার [জামাকে] ছিঁড়ে দিয়েছে।',
                'grammatical_features_item_ids': [accusative_case],
            },
            {
                'label': 'অধিকরণ কারক (-য়-কারান্ত/-তে অক্ষরান্ত)',
                'example': 'ওর [জামায়/জামাতে] একটা দাগ আছে।',
                'grammatical_features_item_ids': [locative_case],
            },
        ],
    },

    'bengali-noun-inanimate-highvowels': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'অপ্রাণীবাচক বিশেষ্য (-ই/ঈ/উ/ঊ/ঐ/ঔ-কারান্ত শব্দ)',
        'language': language_Bengali,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'কর্তৃকারক',
                'example': 'এই [গাড়ি] চলতেছে।',
                'grammatical_features_item_ids': [nominative_case],
            },
            {
                'label': 'সম্বন্ধ পদ',
                'example': 'এই [গাড়ির] রঙ লাল।',
                'grammatical_features_item_ids': [genitive_case],
            },
            {
                'label': 'কর্ম কারক',
                'example': 'তার [গাড়িকে] লাল রঙ করে দিয়েছে।',
                'grammatical_features_item_ids': [accusative_case],
            },
            {
                'label': 'অধিকরণ কারক',
                'example': 'শীঘ্রই [গাড়িতে] উঠুন!',
                'grammatical_features_item_ids': [locative_case],
            },
        ],
    },

    'bengali-noun-inanimate-consonants': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'অপ্রাণীবাচক বিশেষ্য (ব্যঞ্জনান্ত শব্দ)',
        'language': language_Bengali,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'কর্তৃকারক',
                'example': 'এই [আম] পেকে গেছে।',
                'grammatical_features_item_ids': [nominative_case],
            },
            {
                'label': 'সম্বন্ধ পদ',
                'example': 'এই [আমের] খোসা লাল।',
                'grammatical_features_item_ids': [genitive_case],
            },
            {
                'label': 'কর্ম কারক',
                'example': 'সে [আমকে] একটু আগে কাটল।',
                'grammatical_features_item_ids': [accusative_case],
            },
            {
                'label': 'অধিকরণ কারক',
                'example': 'ওই [আমে] একটা দাগ আছে।',
                'grammatical_features_item_ids': [locative_case],
            },
        ],
    },

    'bengali-adjective-tatsama-property': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'তৎসম গুণবাচক বিশেষণ',
        'language': language_Bengali,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'এটি একটি [ক্ষুদ্র] জলাশয়।',
                'grammatical_features_item_ids': [positive],
            },
            {
                'label': 'তুলনামূলক',
                'example': 'দুটির মধ্যে এটি [ক্ষুদ্রতর] জলাশয়।',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'অতিশয়ার্থমূলক',
                'example': 'এই এলাকায় এটি [ক্ষুদ্রতম] জলাশয়।',
                'grammatical_features_item_ids': [superlative],
            },
        ],
    },

    'bengali-adjective-others': {
        '@attribution': {'users': ['Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'অন্যান্য বিশেষণ',
        'language': language_Bengali,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'এটি একটি [ছোট] ডোবা।',
                'grammatical_features_item_ids': [positive],
            },
        ],
    },

    'bengali-adverb': {
        '@attribution': {'users': ['Mahir256', 'Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'ক্রিয়া বিশেষণ',
        'language': language_Bengali,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'ইনি [দ্রুত] করে দেবেন।',
                'grammatical_features_item_ids': [positive],
            },
        ],
    },

    'bengali-verb': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256', 'Tanay barisha'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'ক্রিয়াপদ',
        'language': language_Bengali,
        'lexical_category_item_id': verb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ভাববাচক বিশেষ্য',
                'example': 'আমার [দেখা] হল।',
                'grammatical_features_item_ids': [verbal_noun],
            },
            {
                'section_break': True,
                'label': 'সাধারণ বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [দেখি]।',
                'grammatical_features_item_ids': [simple_present, first_person],
            },
            {
                'label': 'সাধারণ বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [দেখ]।',
                'grammatical_features_item_ids': [simple_present, second_person_familiar],
            },
            {
                'label': 'সাধারণ বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুই [দেখিস]।',
                'grammatical_features_item_ids': [simple_present, second_person_informal],
            },
            {
                'label': 'সাধারণ বর্তমান, প্রথম পুরুষ',
                'example': 'সে [দেখে]।',
                'grammatical_features_item_ids': [simple_present, third_person],
            },
            {
                'label': 'সাধারণ বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'তিনি [দেখেন]।',
                'grammatical_features_item_ids': [simple_present, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখছি]।',
                'grammatical_features_item_ids': [present_continuous, first_person, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিতেছি]।',
                'grammatical_features_item_ids': [present_continuous, first_person, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখছ]।',
                'grammatical_features_item_ids': [present_continuous, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিতেছ]।',
                'grammatical_features_item_ids': [present_continuous, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখছিস]।',
                'grammatical_features_item_ids': [present_continuous, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিতেছিস]।',
                'grammatical_features_item_ids': [present_continuous, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখছে]।',
                'grammatical_features_item_ids': [present_continuous, third_person, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিতেছে]।',
                'grammatical_features_item_ids': [present_continuous, third_person, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখছেন]।',
                'grammatical_features_item_ids': [present_continuous, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিতেছেন]।',
                'grammatical_features_item_ids': [present_continuous, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখেছি]।',
                'grammatical_features_item_ids': [present_perfect, first_person, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিয়াছি]।',
                'grammatical_features_item_ids': [present_perfect, first_person, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখেছ]।',
                'grammatical_features_item_ids': [present_perfect, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিয়াছ]।',
                'grammatical_features_item_ids': [present_perfect, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখেছিস]।',
                'grammatical_features_item_ids': [present_perfect, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিয়াছিস]।',
                'grammatical_features_item_ids': [present_perfect, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখেছে]।',
                'grammatical_features_item_ids': [present_perfect, third_person, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিয়াছে]।',
                'grammatical_features_item_ids': [present_perfect, third_person, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখেছেন]।',
                'grammatical_features_item_ids': [present_perfect, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিয়াছেন]।',
                'grammatical_features_item_ids': [present_perfect, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'বর্তমান অনুজ্ঞা, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [দেখো]।',
                'grammatical_features_item_ids': [second_person_familiar, present_imperative],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুই [দেখ]।',
                'grammatical_features_item_ids': [second_person_informal, present_imperative],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখুক]।',
                'grammatical_features_item_ids': [present_imperative, third_person, Chalit_bhasha],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখুক]।',
                'grammatical_features_item_ids': [present_imperative, third_person, Sadhu_bhasha],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখুন]।',
                'grammatical_features_item_ids': [present_imperative, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখুন]।',
                'grammatical_features_item_ids': [present_imperative, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'সাধারণ অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখলাম]।',
                'grammatical_features_item_ids': [simple_past, first_person, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিলাম]।',
                'grammatical_features_item_ids': [simple_past, first_person, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখলে]।',
                'grammatical_features_item_ids': [simple_past, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিলে]।',
                'grammatical_features_item_ids': [simple_past, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখলি]।',
                'grammatical_features_item_ids': [simple_past, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিলি]।',
                'grammatical_features_item_ids': [simple_past, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখল]।',
                'grammatical_features_item_ids': [simple_past, third_person, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিল]।',
                'grammatical_features_item_ids': [simple_past, third_person, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখলেন]।',
                'grammatical_features_item_ids': [simple_past, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিলেন]।',
                'grammatical_features_item_ids': [simple_past, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখছিলাম]।',
                'grammatical_features_item_ids': [past_continuous, first_person, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিতেছিলাম]।',
                'grammatical_features_item_ids': [past_continuous, first_person, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখছিলে]।',
                'grammatical_features_item_ids': [past_continuous, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিতেছিলে]।',
                'grammatical_features_item_ids': [past_continuous, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখছিলি]।',
                'grammatical_features_item_ids': [past_continuous, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিতেছিলি]।',
                'grammatical_features_item_ids': [past_continuous, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখছিল]।',
                'grammatical_features_item_ids': [past_continuous, third_person, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিতেছিল]।',
                'grammatical_features_item_ids': [past_continuous, third_person, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখছিলেন]।',
                'grammatical_features_item_ids': [past_continuous, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিতেছিলেন]।',
                'grammatical_features_item_ids': [past_continuous, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখেছিলাম]।',
                'grammatical_features_item_ids': [pluperfect, first_person, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিয়াছিলাম]।',
                'grammatical_features_item_ids': [pluperfect, first_person, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখেছিলে]।',
                'grammatical_features_item_ids': [pluperfect, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিয়াছিলে]।',
                'grammatical_features_item_ids': [pluperfect, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখেছিলি]।',
                'grammatical_features_item_ids': [pluperfect, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিয়াছিলি]।',
                'grammatical_features_item_ids': [pluperfect, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখেছিল]।',
                'grammatical_features_item_ids': [pluperfect, third_person, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিয়াছিল]।',
                'grammatical_features_item_ids': [pluperfect, third_person, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখেছিলেন]।',
                'grammatical_features_item_ids': [pluperfect, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিয়াছিলেন]।',
                'grammatical_features_item_ids': [pluperfect, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখতাম]।',
                'grammatical_features_item_ids': [habitual_past, first_person, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিতাম]।',
                'grammatical_features_item_ids': [habitual_past, first_person, Sadhu_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখতে]।',
                'grammatical_features_item_ids': [habitual_past, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিতে]।',
                'grammatical_features_item_ids': [habitual_past, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখতিস]।',
                'grammatical_features_item_ids': [habitual_past, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিতিস]।',
                'grammatical_features_item_ids': [habitual_past, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখত]।',
                'grammatical_features_item_ids': [habitual_past, third_person, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিত]।',
                'grammatical_features_item_ids': [habitual_past, third_person, Sadhu_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখতেন]।',
                'grammatical_features_item_ids': [habitual_past, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিতেন]।',
                'grammatical_features_item_ids': [habitual_past, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখব]।',
                'grammatical_features_item_ids': ['Q96323395', first_person, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখিব]।',
                'grammatical_features_item_ids': ['Q96323395', first_person, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখবে]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিবে]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখবি]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিবি]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখবে]।',
                'grammatical_features_item_ids': ['Q96323395', third_person, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিবে]।',
                'grammatical_features_item_ids': ['Q96323395', third_person, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখবেন]।',
                'grammatical_features_item_ids': ['Q96323395', Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিবেন]।',
                'grammatical_features_item_ids': ['Q96323395', Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখো]।',
                'grammatical_features_item_ids': [future_imperative, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখিও]।',
                'grammatical_features_item_ids': [future_imperative, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখিস]।',
                'grammatical_features_item_ids': [future_imperative, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখিস]।',
                'grammatical_features_item_ids': [future_imperative, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখবে]।',
                'grammatical_features_item_ids': [future_imperative, third_person, Chalit_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখিবে]।',
                'grammatical_features_item_ids': [future_imperative, third_person, Sadhu_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখবেন]।',
                'grammatical_features_item_ids': [future_imperative, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখিবেন]।',
                'grammatical_features_item_ids': [future_imperative, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': 'আমি [দেখতে] চাই।',
                'grammatical_features_item_ids': [progressive, non_finite_verb, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': 'আমি [দেখিতে] চাই।',
                'grammatical_features_item_ids': [progressive, non_finite_verb, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': '[দেখে] গেছি।',
                'grammatical_features_item_ids': [perfective, non_finite_verb, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': '[দেখিয়া] গিয়াছি।',
                'grammatical_features_item_ids': [perfective, non_finite_verb, Sadhu_bhasha],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': 'এটা [দেখলে] ভালো লাগে।',
                'grammatical_features_item_ids': [conditional, non_finite_verb, Chalit_bhasha],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': 'ইহা [দেখিলে] ভালো লাগে।',
                'grammatical_features_item_ids': [conditional, non_finite_verb, Sadhu_bhasha],
            },
            {
                'label': 'সম্বন্ধবাচক ভাববিশেষ্য, চলিত ভাষা',
                'example': 'আমি সেটা [দেখার/দেখবার] জন্য গেছিলাম।',
                'grammatical_features_item_ids': [genitive_case, verbal_noun, Chalit_bhasha],
            },
            {
                'label': 'সম্বন্ধবাচক ভাববিশেষ্য, সাধু ভাষা',
                'example': 'আমি তাহা [দেখিবার] জন্য গিয়াছিলাম।',
                'grammatical_features_item_ids': [genitive_case, verbal_noun, Sadhu_bhasha],
            },
        ],
    },

    'bengali-verb-ano': {
        '@attribution': {'users': ['Bodhisattwa', 'Mahir256', 'Tanay barisha'], 'title': 'Wikidata:Wikidata Lexeme Forms/Bengali'},
        'label': 'ক্রিয়াপদ (সাধিত ধাতু)',
        'language': language_Bengali,
        'lexical_category_item_id': verb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ভাববাচক বিশেষ্য',
                'example': 'আমার [দেখানো] হল।',
                'grammatical_features_item_ids': [verbal_noun],
            },
            {
                'section_break': True,
                'label': 'সাধারণ বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [দেখাই]।',
                'grammatical_features_item_ids': [simple_present, first_person],
            },
            {
                'label': 'সাধারণ বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [দেখাও]।',
                'grammatical_features_item_ids': [simple_present, second_person_familiar],
            },
            {
                'label': 'সাধারণ বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুই [দেখাস]।',
                'grammatical_features_item_ids': [simple_present, second_person_informal],
            },
            {
                'label': 'সাধারণ বর্তমান, প্রথম পুরুষ',
                'example': 'সে [দেখায়]।',
                'grammatical_features_item_ids': [simple_present, third_person],
            },
            {
                'label': 'সাধারণ বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'তিনি [দেখান]।',
                'grammatical_features_item_ids': [simple_present, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখাচ্ছি]।',
                'grammatical_features_item_ids': [present_continuous, first_person, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইতেছি]।',
                'grammatical_features_item_ids': [present_continuous, first_person, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাচ্ছ]।',
                'grammatical_features_item_ids': [present_continuous, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইতেছ]।',
                'grammatical_features_item_ids': [present_continuous, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাচ্ছিস]।',
                'grammatical_features_item_ids': [present_continuous, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইতেছিস]।',
                'grammatical_features_item_ids': [present_continuous, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাচ্ছে]।',
                'grammatical_features_item_ids': [present_continuous, third_person, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইতেছে]।',
                'grammatical_features_item_ids': [present_continuous, third_person, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাচ্ছেন]।',
                'grammatical_features_item_ids': [present_continuous, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইতেছেন]।',
                'grammatical_features_item_ids': [present_continuous, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখিয়েছি]।',
                'grammatical_features_item_ids': [present_perfect, first_person, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইয়াছি]।',
                'grammatical_features_item_ids': [present_perfect, first_person, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখিয়েছ]।',
                'grammatical_features_item_ids': [present_perfect, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইয়াছ]।',
                'grammatical_features_item_ids': [present_perfect, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখিয়েছিস]।',
                'grammatical_features_item_ids': [present_perfect, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইয়াছিস]।',
                'grammatical_features_item_ids': [present_perfect, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখিয়েছে]।',
                'grammatical_features_item_ids': [present_perfect, third_person, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইয়াছে]।',
                'grammatical_features_item_ids': [present_perfect, third_person, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখিয়েছেন]।',
                'grammatical_features_item_ids': [present_perfect, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইয়াছেন]।',
                'grammatical_features_item_ids': [present_perfect, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'বর্তমান অনুজ্ঞা, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [দেখাও]।',
                'grammatical_features_item_ids': [second_person_familiar, present_imperative],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুই [দেখা]।',
                'grammatical_features_item_ids': [second_person_informal, present_imperative],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাক]।',
                'grammatical_features_item_ids': [present_imperative, third_person, Chalit_bhasha],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাক]।',
                'grammatical_features_item_ids': [present_imperative, third_person, Sadhu_bhasha],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখান]।',
                'grammatical_features_item_ids': [present_imperative, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখান]।',
                'grammatical_features_item_ids': [present_imperative, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'সাধারণ অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখালাম]।',
                'grammatical_features_item_ids': [simple_past, first_person, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইলাম]।',
                'grammatical_features_item_ids': [simple_past, first_person, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখালে]।',
                'grammatical_features_item_ids': [simple_past, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইলে]।',
                'grammatical_features_item_ids': [simple_past, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখালি]।',
                'grammatical_features_item_ids': [simple_past, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইলি]।',
                'grammatical_features_item_ids': [common, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাল]।',
                'grammatical_features_item_ids': [simple_past, third_person, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইল]।',
                'grammatical_features_item_ids': [simple_past, third_person, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখালেন]।',
                'grammatical_features_item_ids': [simple_past, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইলেন]।',
                'grammatical_features_item_ids': [simple_past, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখাচ্ছিলাম]।',
                'grammatical_features_item_ids': [past_continuous, first_person, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইতেছিলাম]।',
                'grammatical_features_item_ids': [past_continuous, first_person, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাচ্ছিলে]।',
                'grammatical_features_item_ids': [past_continuous, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইতেছিলে]।',
                'grammatical_features_item_ids': [past_continuous, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাচ্ছিলি]।',
                'grammatical_features_item_ids': [past_continuous, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইতেছিলি]।',
                'grammatical_features_item_ids': [past_continuous, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাচ্ছিল]।',
                'grammatical_features_item_ids': [past_continuous, third_person, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইতেছিল]।',
                'grammatical_features_item_ids': [past_continuous, third_person, Sadhu_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাচ্ছিলেন]।',
                'grammatical_features_item_ids': [past_continuous, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইতেছিলেন]।',
                'grammatical_features_item_ids': [past_continuous, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখিয়েছিলাম]।',
                'grammatical_features_item_ids': [pluperfect, first_person, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইয়াছিলাম]।',
                'grammatical_features_item_ids': [pluperfect, first_person, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখিয়েছিলে]।',
                'grammatical_features_item_ids': [pluperfect, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইয়াছিলে]।',
                'grammatical_features_item_ids': [pluperfect, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখিয়েছিলি]।',
                'grammatical_features_item_ids': [pluperfect, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইয়াছিলি]।',
                'grammatical_features_item_ids': [pluperfect, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখিয়েছিল]।',
                'grammatical_features_item_ids': [pluperfect, third_person, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইয়াছিল]।',
                'grammatical_features_item_ids': [pluperfect, third_person, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখিয়েছিলেন]।',
                'grammatical_features_item_ids': [pluperfect, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইয়াছিলেন]।',
                'grammatical_features_item_ids': [pluperfect, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখাতাম]।',
                'grammatical_features_item_ids': [habitual_past, first_person, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইতাম]।',
                'grammatical_features_item_ids': [habitual_past, first_person, Sadhu_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাতে]।',
                'grammatical_features_item_ids': [habitual_past, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইতে]।',
                'grammatical_features_item_ids': [habitual_past, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাতিস]।',
                'grammatical_features_item_ids': [habitual_past, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইতিস]।',
                'grammatical_features_item_ids': [habitual_past, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাত]।',
                'grammatical_features_item_ids': [habitual_past, third_person, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইত]।',
                'grammatical_features_item_ids': [habitual_past, third_person, Sadhu_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাতেন]।',
                'grammatical_features_item_ids': [habitual_past, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইতেন]।',
                'grammatical_features_item_ids': [habitual_past, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ, চলিত ভাষা',
                'example': 'আমি [দেখাব]।',
                'grammatical_features_item_ids': ['Q96323395', first_person, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ, সাধু ভাষা',
                'example': 'আমি [দেখাইব]।',
                'grammatical_features_item_ids': ['Q96323395', first_person, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাবে]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইবে]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাবি]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাইবি]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাবে]।',
                'grammatical_features_item_ids': ['Q96323395', third_person, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইবে]।',
                'grammatical_features_item_ids': ['Q96323395', third_person, Sadhu_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাবেন]।',
                'grammatical_features_item_ids': ['Q96323395', Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইবেন]।',
                'grammatical_features_item_ids': ['Q96323395', Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুমি [দেখাও]।',
                'grammatical_features_item_ids': [future_imperative, second_person_familiar, Chalit_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুমি [দেখাইও]।',
                'grammatical_features_item_ids': [future_imperative, second_person_familiar, Sadhu_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ, চলিত ভাষা',
                'example': 'তুই [দেখাস]।',
                'grammatical_features_item_ids': [future_imperative, second_person_informal, Chalit_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ, সাধু ভাষা',
                'example': 'তুই [দেখাস]।',
                'grammatical_features_item_ids': [future_imperative, second_person_informal, Sadhu_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ, চলিত ভাষা',
                'example': 'সে [দেখাবে]।',
                'grammatical_features_item_ids': [future_imperative, third_person, Chalit_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ, সাধু ভাষা',
                'example': 'সে [দেখাইবে]।',
                'grammatical_features_item_ids': [future_imperative, third_person, Sadhu_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ, চলিত ভাষা',
                'example': 'তিনি [দেখাবেন]।',
                'grammatical_features_item_ids': [future_imperative, Bengali_polite_form, Chalit_bhasha],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ, সাধু ভাষা',
                'example': 'তিনি [দেখাইবেন]।',
                'grammatical_features_item_ids': [future_imperative, Bengali_polite_form, Sadhu_bhasha],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': 'আমি [দেখাতে] চাই।',
                'grammatical_features_item_ids': [progressive, non_finite_verb, Chalit_bhasha],
            },
            {
                'label': 'ঘটমান অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': 'আমি [দেখাইতে] চাই।',
                'grammatical_features_item_ids': [progressive, non_finite_verb, Sadhu_bhasha],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': '[দেখিয়ে] গেছি।',
                'grammatical_features_item_ids': [perfective, non_finite_verb, Chalit_bhasha],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': '[দেখাইয়া] গিয়াছি।',
                'grammatical_features_item_ids': [perfective, non_finite_verb, Sadhu_bhasha],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া, চলিত ভাষা',
                'example': 'এটা [দেখালে] ভালো লাগে।',
                'grammatical_features_item_ids': [conditional, non_finite_verb, Chalit_bhasha],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া, সাধু ভাষা',
                'example': 'ইহা [দেখাইলে] ভালো লাগে।',
                'grammatical_features_item_ids': [conditional, non_finite_verb, Sadhu_bhasha],
            },
            {
                'label': 'সম্বন্ধবাচক ভাববিশেষ্য, চলিত ভাষা',
                'example': 'আমি সেটা [দেখাবার] জন্য গেছিলাম।',
                'grammatical_features_item_ids': [genitive_case, verbal_noun, Chalit_bhasha],
            },
            {
                'label': 'সম্বন্ধবাচক ভাববিশেষ্য, সাধু ভাষা',
                'example': 'আমি তাহা [দেখাইবার] জন্য গিয়াছিলাম।',
                'grammatical_features_item_ids': [genitive_case, verbal_noun, Sadhu_bhasha],
            },
        ],
    },

    'manbhumi-adjective': {
        '@attribution': {'users': ['Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Manbhumi'},
        'label': 'বিশেষণ',
        'language': language_Manbhumi,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'উ [বেহায়া] লক বটে।',
                'grammatical_features_item_ids': [positive],
            },
        ],
    },

    'manbhumi-adverb': {
        '@attribution': {'users': ['Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Manbhumi'},
        'label': 'ক্রিয়া বিশেষণ',
        'language': language_Manbhumi,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'সাধারণ',
                'example': 'উ [ঝট্‌] কর‍্যে চল্যে যাবেক।',
                'grammatical_features_item_ids': [positive],
            },
        ],
    },

    'manbhumi-verb': {
        '@attribution': {'users': ['Bodhisattwa'], 'title': 'Wikidata:Wikidata Lexeme Forms/Manbhumi'},
        'label': 'ক্রিয়াপদ',
        'language': language_Manbhumi,
        'lexical_category_item_id': verb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ভাববাচক বিশেষ্য',
                'example': 'আমার [ভালা] হল।',
                'grammatical_features_item_ids': [verbal_noun],
            },
            {
                'section_break': True,
                'label': 'সাধারণ বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [ভালি]।',
                'grammatical_features_item_ids': [simple_present, first_person],
            },
            {
                'label': 'সাধারণ বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাল]।',
                'grammatical_features_item_ids': [simple_present, second_person_familiar],
            },
            {
                'label': 'সাধারণ বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভালিস]।',
                'grammatical_features_item_ids': [simple_present, second_person_informal],
            },
            {
                'label': 'সাধারণ বর্তমান, প্রথম পুরুষ',
                'example': 'উ [ভালে]।',
                'grammatical_features_item_ids': [simple_present, third_person],
            },
            {
                'label': 'সাধারণ বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভালেন]।',
                'grammatical_features_item_ids': [simple_present, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'ঘটমান বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [ভাইলছি]।',
                'grammatical_features_item_ids': [present_continuous, first_person],
            },
            {
                'label': 'ঘটমান বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলছ]।',
                'grammatical_features_item_ids': [present_continuous, second_person_familiar],
            },
            {
                'label': 'ঘটমান বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলছিস]।',
                'grammatical_features_item_ids': [present_continuous, second_person_informal],
            },
            {
                'label': 'ঘটমান বর্তমান, প্রথম পুরুষ',
                'example': 'উ [ভাইলছে]।',
                'grammatical_features_item_ids': [present_continuous, third_person],
            },
            {
                'label': 'ঘটমান বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলছেন]।',
                'grammatical_features_item_ids': [present_continuous, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত বর্তমান, উত্তম পুরুষ',
                'example': 'আমি [ভাইলেছি]।',
                'grammatical_features_item_ids': [present_perfect, first_person],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলেছ]।',
                'grammatical_features_item_ids': [present_perfect, second_person_familiar],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলেছিস]।',
                'grammatical_features_item_ids': [present_perfect, second_person_informal],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, প্রথম পুরুষ',
                'example': 'উ [ভাইলেছে]।',
                'grammatical_features_item_ids': [present_perfect, third_person],
            },
            {
                'label': 'পুরাঘটিত বর্তমান, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলেছেন]।',
                'grammatical_features_item_ids': [present_perfect, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'বর্তমান অনুজ্ঞা, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভালো]।',
                'grammatical_features_item_ids': [present_imperative, second_person_familiar],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাল্‌]।',
                'grammatical_features_item_ids': [present_imperative, second_person_informal],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, প্রথম পুরুষ',
                'example': 'উ [ভালুক]।',
                'grammatical_features_item_ids': [present_imperative, third_person],
            },
            {
                'label': 'বর্তমান অনুজ্ঞা, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভালুন]।',
                'grammatical_features_item_ids': [present_imperative, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'সাধারণ অতীত, উত্তম পুরুষ',
                'example': 'আমি [ভাইললম/ভাইললি]।',
                'grammatical_features_item_ids': [simple_past, first_person],
            },
            {
                'label': 'সাধারণ অতীত, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইললে]।',
                'grammatical_features_item_ids': [simple_past, second_person_familiar],
            },
            {
                'label': 'সাধারণ অতীত, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইললি/ভাইললিস]।',
                'grammatical_features_item_ids': [simple_past, second_person_informal],
            },
            {
                'label': 'সাধারণ অতীত, প্রথম পুরুষ',
                'example': 'উ [ভাইলল/ভাইললক/ভাইললেক]।',
                'grammatical_features_item_ids': [simple_past, third_person],
            },
            {
                'label': 'সাধারণ অতীত, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইললেন]।',
                'grammatical_features_item_ids': [simple_past, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অতীত, উত্তম পুরুষ',
                'example': 'আমি [ভাইলছিলম/ভাইলতেছিলম/ভাইলছিলি/ভাইলতেছিলি]।',
                'grammatical_features_item_ids': [past_continuous, first_person],
            },
            {
                'label': 'ঘটমান অতীত, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলছিলে/ভাইলতেছিলে]।',
                'grammatical_features_item_ids': [past_continuous, second_person_familiar],
            },
            {
                'label': 'ঘটমান অতীত, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলছিলি/ভাইলছিলিস/ভাইলতেছিলি/ভাইলতেছিলিস]।',
                'grammatical_features_item_ids': [past_continuous, second_person_informal],
            },
            {
                'label': 'ঘটমান অতীত, প্রথম পুরুষ',
                'example': 'উ [ভাইলছিল/ভাইলতেছিল/ভাইলছিলক/ভাইলতেছিলক/ভাইলছিলেক/ভাইলতেছিলেক]।',
                'grammatical_features_item_ids': [past_continuous, third_person],
            },
            {
                'label': 'ঘটমান অতীত, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলছিলেন/ভাইলতেছিলেন]।',
                'grammatical_features_item_ids': [past_continuous, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'পুরাঘটিত অতীত, উত্তম পুরুষ',
                'example': 'আমি [ভাইলেছিলম/ভাইলেছিলি]।',
                'grammatical_features_item_ids': [pluperfect, first_person],
            },
            {
                'label': 'পুরাঘটিত অতীত, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলেছিলে]।',
                'grammatical_features_item_ids': [pluperfect, second_person_familiar],
            },
            {
                'label': 'পুরাঘটিত অতীত, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলেছিলি/ভাইলেছিলিস]।',
                'grammatical_features_item_ids': [pluperfect, second_person_informal],
            },
            {
                'label': 'পুরাঘটিত অতীত, প্রথম পুরুষ',
                'example': 'উ [ভাইলেছিল/ভাইলেছিলক/ভাইলেছিলেক]।',
                'grammatical_features_item_ids': [pluperfect, third_person],
            },
            {
                'label': 'পুরাঘটিত অতীত, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলেছিলেন]।',
                'grammatical_features_item_ids': [pluperfect, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'নিত্যবৃত্ত অতীত, উত্তম পুরুষ',
                'example': 'আমি [ভাইলতম/ভাইলতি/ভাইলথম/ভাইলথি]।',
                'grammatical_features_item_ids': [habitual_past, first_person],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলতে/ভাইলথে]।',
                'grammatical_features_item_ids': [habitual_past, second_person_familiar],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলতি/ভাইলতিস/ভাইলথি/ভাইলথিস]।',
                'grammatical_features_item_ids': [habitual_past, second_person_informal],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, প্রথম পুরুষ',
                'example': 'উ [ভাইলত/ভাইলতক/ভাইলতেক/ভাইলথ/ভাইলথক/ভাইলথেক]।',
                'grammatical_features_item_ids': [habitual_past, third_person],
            },
            {
                'label': 'নিত্যবৃত্ত অতীত, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলতেন]।',
                'grammatical_features_item_ids': [habitual_past, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'সাধারণ ভবিষ্যৎ, উত্তম পুরুষ',
                'example': 'আমি [ভাইলব]।',
                'grammatical_features_item_ids': ['Q96323395', first_person],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলবে]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_familiar],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলবি/ভাইলবিস]।',
                'grammatical_features_item_ids': ['Q96323395', second_person_informal],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, প্রথম পুরুষ',
                'example': 'উ [ভাইলবেক]।',
                'grammatical_features_item_ids': ['Q96323395', third_person],
            },
            {
                'label': 'সাধারণ ভবিষ্যৎ, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলবেন]।',
                'grammatical_features_item_ids': ['Q96323395', Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সাধারণ মধ্যমপুরুষ',
                'example': 'তুমি [ভাইলো]।',
                'grammatical_features_item_ids': [future_imperative, second_person_familiar],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, তুচ্ছার্থ মধ্যমপুরুষ',
                'example': 'তুঁই [ভাইলিস]।',
                'grammatical_features_item_ids': [future_imperative, second_person_informal],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, প্রথম পুরুষ',
                'example': 'উ [ভাইলবেক]।',
                'grammatical_features_item_ids': [future_imperative, third_person],
            },
            {
                'label': 'ভবিষ্যৎ অনুজ্ঞা, সম্ভ্রমার্থ রূপ',
                'example': 'উনি [ভাইলবেন]।',
                'grammatical_features_item_ids': [future_imperative, Bengali_polite_form],
            },
            {
                'section_break': True,
                'label': 'ঘটমান অসমাপিকা ক্রিয়া',
                'example': 'আমি [ভাইলতে] চাই।',
                'grammatical_features_item_ids': [progressive, non_finite_verb],
            },
            {
                'label': 'পুরাঘটিত অসমাপিকা ক্রিয়া',
                'example': 'উয়ার পানে [ভালি/ভাইলে/ভালাঁই] গেইলছি।',
                'grammatical_features_item_ids': [perfective, non_finite_verb],
            },
            {
                'label': 'সর্তজ্ঞাপক অসমাপিকা ক্রিয়া',
                'example': 'ইটা [ভাইললে] ভালো লাগে।',
                'grammatical_features_item_ids': [conditional, non_finite_verb],
            },
        ],
    },

    'breton-noun-without-mutation': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (hep kemmadur)',
        'language': language_Breton,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'unander',
                'example': 'Ma [levr] zo amañ.',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'liester',
                'example': 'Ma [levrioù] zo amañ.',
                'grammatical_features_item_ids': [plural],
            },
        ],
    },

    'breton-noun-without-mutation-collective': {
        '@attribution': {'users': ['VIGNERON'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (strollder, hep kemmadur)',
        'language': language_Breton,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'strollder',
                'example': 'Ma [stered] zo amañ.',
                'grammatical_features_item_ids': [collective],
            },
            {
                'label': 'unanderenn',
                'example': 'Ma [steredenn] zo amañ.',
                'grammatical_features_item_ids': [singulative],
            },
        ],
    },

    'breton-noun-with-mutation-ktp': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (gant kemmadur, ktp)',
        'language': language_Breton,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'unander',
                'example': 'Ho [tad] zo amañ.',
                'grammatical_features_item_ids': [singular, no_mutation],
            },
            {
                'label': 'unander',
                'example': 'Da [dad] zo amañ.',
                'grammatical_features_item_ids': [singular, soft_mutation],
            },
            {
                'label': 'unander',
                'example': 'Ma [zad] zo amañ.',
                'grammatical_features_item_ids': [singular, aspirate_mutation],
            },
            {
                'label': 'liester',
                'example': 'Hon [tadoù] zo amañ.',
                'grammatical_features_item_ids': [plural, no_mutation],
            },
            {
                'label': 'liester',
                'example': 'Da [dadoù] zo amañ.',
                'grammatical_features_item_ids': [plural, soft_mutation],
            },
            {
                'label': 'liester',
                'example': 'Ma [zadoù] zo amañ.',
                'grammatical_features_item_ids': [plural, aspirate_mutation],
            },
        ],
    },

    'breton-noun-with-mutation-gdb': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (gant kemmadur, gdb)',
        'language': language_Breton,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'unander',
                'example': 'Ma [bag] zo amañ.',
                'grammatical_features_item_ids': [singular, no_mutation],
            },
            {
                'label': 'unander',
                'example': 'Da [vag] zo amañ.',
                'grammatical_features_item_ids': [singular, soft_mutation],
            },
            {
                'label': 'unander',
                'example': 'Ho [pag] zo amañ.',
                'grammatical_features_item_ids': [singular, aspirate_mutation],
            },
            {
                'label': 'liester',
                'example': 'Ma [bagoù] zo amañ.',
                'grammatical_features_item_ids': [plural, no_mutation],
            },
            {
                'label': 'liester',
                'example': 'Da [vagoù] zo amañ.',
                'grammatical_features_item_ids': [plural, soft_mutation],
            },
            {
                'label': 'liester',
                'example': 'Ho [pagoù] zo amañ.',
                'grammatical_features_item_ids': [plural, aspirate_mutation],
            },
        ],
    },

    'breton-noun-with-mutation-m': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-kadarn (gant kemmadur, m)',
        'language': language_Breton,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'unander',
                'example': 'Ho [mamm] zo amañ.',
                'grammatical_features_item_ids': [singular, no_mutation],
            },
            {
                'label': 'unander',
                'example': 'Ma [vamm] zo amañ.',
                'grammatical_features_item_ids': [singular, soft_mutation],
            },
            {
                'label': 'liester',
                'example': 'Ho [mammoù] zo amañ.',
                'grammatical_features_item_ids': [plural, no_mutation],
            },
            {
                'label': 'liester',
                'example': 'Ma [vammoù] zo amañ.',
                'grammatical_features_item_ids': [plural, soft_mutation],
            },
        ],
    },

    'breton-adjective-without-mutation': {
        '@attribution': {'users': ['VIGNERON', 'Fulup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'anvioù-gwan (hep kemmadur)',
        'language': language_Breton,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'derez-plaen',
                'example': 'Un dra [ledan] eo.',
                'grammatical_features_item_ids': [positive],
            },
            {
                'label': 'derez-uheloc\'h',
                'example': 'Un dra [ledanoc\'h] eo.',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'derez-uhelañ',
                'example': 'An dra [ledanañ] eo.',
                'grammatical_features_item_ids': [superlative],
            },
            {
                'label': 'derez-estlammiñ',
                'example': '[ledanat] tra !',
                'grammatical_features_item_ids': [exclamative],
            },
        ],
    },

    'breton-adverb': {
        '@attribution': {'users': ['VIGNERON'], 'title': 'Wikidata:Wikidata Lexeme Forms/Breton'},
        'label': 'adverb',
        'language': language_Breton,
        'lexical_category_item_id': adverb,
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
        'language': language_Czech,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': '1. pád, jednotné číslo',
                'example': 'To je můj [pes].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': '2. pád, jednotné číslo',
                'example': 'Má strach z mého [psa].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': '3. pád, jednotné číslo',
                'example': 'Dej to mému [psu/psovi].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': '4. pád, jednotné číslo',
                'example': 'Vidím jednoho [psa].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': '5. pád, jednotné číslo',
                'example': 'Kam kráčíš, [pse]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': '6. pád, jednotné číslo',
                'example': 'Pověz mi něco o tvém [psu/psovi].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': '7. pád, jednotné číslo',
                'example': 'Seznámil jsem se s tvým [psem].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': '1. pád, množné číslo',
                'example': 'To jsou moji [psi/psové].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': '2. pád, množné číslo',
                'example': 'Má strach z mých [psů].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': '3. pád, množné číslo',
                'example': 'Dej to mým [psům].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': '4. pád, množné číslo',
                'example': 'Vidím dva [psy].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': '5. pád, množné číslo',
                'example': 'Kam kráčíte, [psi/psové]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
            {
                'label': '6. pád, množné číslo',
                'example': 'Pověz mi něco o tvých [psech].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': '7. pád, množné číslo',
                'example': 'Seznámil jsem se s tvými [psy].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, masculine),
                statement(grammatical_gender, masculine_animate),
            ],
        },
    },

    'czech-noun-masculine-inanimate': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod mužský neživotný)',
        'language': language_Czech,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': '1. pád, jednotné číslo',
                'example': 'To je můj [hrad].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': '2. pád, jednotné číslo',
                'example': 'Má strach z mého [hradu].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': '3. pád, jednotné číslo',
                'example': 'Dej to k mému [hradu].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': '4. pád, jednotné číslo',
                'example': 'Vidím jeden [hrad].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': '5. pád, jednotné číslo',
                'example': 'Kam směřuješ, [hrade]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': '6. pád, jednotné číslo',
                'example': 'Pověz mi něco o svém [hradu/hradě].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': '7. pád, jednotné číslo',
                'example': 'Seznámil jsem se s tvým [hradem].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': '1. pád, množné číslo',
                'example': 'To jsou mé [hrady].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': '2. pád, množné číslo',
                'example': 'Má strach z mých [hradů].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': '3. pád, množné číslo',
                'example': 'Dej to k mým [hradům].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': '4. pád, množné číslo',
                'example': 'Vidím dva [hrady].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': '5. pád, množné číslo',
                'example': 'Kam směřujete, [hrady]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
            {
                'label': '6. pád, množné číslo',
                'example': 'Pověz mi něco o svých [hradech].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': '7. pád, množné číslo',
                'example': 'Seznámil jsem se s tvými [hrady].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, masculine),
                statement(grammatical_gender, masculine_inanimate),
            ],
        },
    },

    'czech-noun-feminine': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod ženský)',
        'language': language_Czech,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': '1. pád, jednotné číslo',
                'example': 'To je má [žena].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': '2. pád, jednotné číslo',
                'example': 'Má strach z mé [ženy].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': '3. pád, jednotné číslo',
                'example': 'Dej to mé [ženě].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': '4. pád, jednotné číslo',
                'example': 'Vidím jednu [ženu].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': '5. pád, jednotné číslo',
                'example': 'Kam kráčíš, [ženo]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': '6. pád, jednotné číslo',
                'example': 'Pověz mi něco o tvé [ženě].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': '7. pád, jednotné číslo',
                'example': 'Seznámil jsem se s tvou [ženou].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': '1. pád, množné číslo',
                'example': 'To jsou mé [ženy].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': '2. pád, množné číslo',
                'example': 'Má strach z mých [žen].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': '3. pád, množné číslo',
                'example': 'Dej to mým [ženám].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': '4. pád, množné číslo',
                'example': 'Vidím dvě [ženy].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': '5. pád, množné číslo',
                'example': 'Kam kráčíte, [ženy]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
            {
                'label': '6. pád, množné číslo',
                'example': 'Pověz mi něco o tvých [ženách].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': '7. pád, množné číslo',
                'example': 'Seznámil jsem se s tvými [ženami].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'czech-noun-neuter': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české podstatné jméno (rod střední)',
        'language': language_Czech,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': '1. pád, jednotné číslo',
                'example': 'To je mé [kuře].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': '2. pád, jednotné číslo',
                'example': 'Má strach z mého [kuřete].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': '3. pád, jednotné číslo',
                'example': 'Dej to mému [kuřeti].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': '4. pád, jednotné číslo',
                'example': 'Vidím jedno [kuře].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': '5. pád, jednotné číslo',
                'example': 'Kam kráčíš, [kuře]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': '6. pád, jednotné číslo',
                'example': 'Pověz mi něco o tvém [kuřeti].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': '7. pád, jednotné číslo',
                'example': 'Seznámil jsem se s tvým [kuřetem].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': '1. pád, množné číslo',
                'example': 'To jsou má [kuřata].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': '2. pád, množné číslo',
                'example': 'Má strach z mých [kuřat].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': '3. pád, množné číslo',
                'example': 'Dej to mým [kuřatům].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': '4. pád, množné číslo',
                'example': 'Vidím dvě [kuřata].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': '5. pád, množné číslo',
                'example': 'Kam kráčíte, [kuřata]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
            {
                'label': '6. pád, množné číslo',
                'example': 'Pověz mi něco o tvých [kuřatech].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': '7. pád, množné číslo',
                'example': 'Seznámil jsem se s tvými [kuřaty].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'czech-adverb': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české příslovce',
        'language': language_Czech,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'pozitiv (1. stupeň)',
                'example': 'Udělal jsi to [dobře].',
                'grammatical_features_item_ids': [positive],
            },
            {
                'label': 'komparativ (2. stupeň)',
                'example': 'Udělal jsi to [lépe] než já.',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'superlativ (3. stupeň)',
                'example': 'Udělal jsi to ze všech [nejlépe].',
                'grammatical_features_item_ids': [superlative],
            },
        ],
    },

    'czech-adjective': {
        '@attribution': {'users': ['Strepon', 'Adrijaned'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české přídavné jméno',
        'language': language_Czech,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': '1. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'To je můj [velký] pes.',
                'grammatical_features_item_ids': [nominative_case, singular, masculine_animate, positive],
            },
            {
                'label': '2. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Má strach z mého [velkého] psa.',
                'grammatical_features_item_ids': [genitive_case, singular, masculine_animate, positive],
            },
            {
                'label': '3. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Dej to mému [velkému] psu.',
                'grammatical_features_item_ids': [dative_case, singular, masculine_animate, positive],
            },
            {
                'label': '4. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Vidím jednoho [velkého] psa.',
                'grammatical_features_item_ids': [accusative_case, singular, masculine_animate, positive],
            },
            {
                'label': '5. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Kam kráčíš, [velký] pse?',
                'grammatical_features_item_ids': [vocative_case, singular, masculine_animate, positive],
            },
            {
                'label': '6. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svém [velkém] psu.',
                'grammatical_features_item_ids': [locative_case, singular, masculine_animate, positive],
            },
            {
                'label': '7. pád, rod mužský životný, jednotné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvým [velkým] psem.',
                'grammatical_features_item_ids': [instrumental_case, singular, masculine_animate, positive],
            },
            {
                'label': '1. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'To je můj [velký] hrad.',
                'grammatical_features_item_ids': [nominative_case, singular, masculine_inanimate, positive],
            },
            {
                'label': '2. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Má strach z mého [velkého] hradu.',
                'grammatical_features_item_ids': [genitive_case, singular, masculine_inanimate, positive],
            },
            {
                'label': '3. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Dej to k mému [velkému] hradu.',
                'grammatical_features_item_ids': [dative_case, singular, masculine_inanimate, positive],
            },
            {
                'label': '4. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Vidím jeden [velký] hrad.',
                'grammatical_features_item_ids': [accusative_case, singular, masculine_inanimate, positive],
            },
            {
                'label': '5. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Kam směřuješ, [velký] hrade?',
                'grammatical_features_item_ids': [vocative_case, singular, masculine_inanimate, positive],
            },
            {
                'label': '6. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svém [velkém] hradu.',
                'grammatical_features_item_ids': [locative_case, singular, masculine_inanimate, positive],
            },
            {
                'label': '7. pád, rod mužský neživotný, jednotné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvým [velkým] hradem.',
                'grammatical_features_item_ids': [instrumental_case, singular, masculine_inanimate, positive],
            },
            {
                'section_break': True,
                'label': '1. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'To je má [velká] žena.',
                'grammatical_features_item_ids': [nominative_case, singular, feminine, positive],
            },
            {
                'label': '2. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Má strach z mé [velké] ženy.',
                'grammatical_features_item_ids': [genitive_case, singular, feminine, positive],
            },
            {
                'label': '3. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Dej to mé [velké] ženě.',
                'grammatical_features_item_ids': [dative_case, singular, feminine, positive],
            },
            {
                'label': '4. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Vidím jednu [velkou] ženu.',
                'grammatical_features_item_ids': [accusative_case, singular, feminine, positive],
            },
            {
                'label': '5. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Kam kráčíš, [velká] ženo?',
                'grammatical_features_item_ids': [vocative_case, singular, feminine, positive],
            },
            {
                'label': '6. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Pověz mi něco o své [velké] ženě.',
                'grammatical_features_item_ids': [locative_case, singular, feminine, positive],
            },
            {
                'label': '7. pád, rod ženský, jednotné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvou [velkou] ženou.',
                'grammatical_features_item_ids': [instrumental_case, singular, feminine, positive],
            },
            {
                'label': '1. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'To je mé [velké] kuře.',
                'grammatical_features_item_ids': [nominative_case, singular, neuter, positive],
            },
            {
                'label': '2. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Má strach z mého [velkého] kuřete.',
                'grammatical_features_item_ids': [genitive_case, singular, neuter, positive],
            },
            {
                'label': '3. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Dej to mému [velkému] kuřeti.',
                'grammatical_features_item_ids': [dative_case, singular, neuter, positive],
            },
            {
                'label': '4. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Vidím jedno [velké] kuře.',
                'grammatical_features_item_ids': [accusative_case, singular, neuter, positive],
            },
            {
                'label': '5. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Kam kráčíš, [velké] kuře?',
                'grammatical_features_item_ids': [vocative_case, singular, neuter, positive],
            },
            {
                'label': '6. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svém [velkém] kuřeti.',
                'grammatical_features_item_ids': [locative_case, singular, neuter, positive],
            },
            {
                'label': '7. pád, rod střední, jednotné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvým [velkým] kuřetem.',
                'grammatical_features_item_ids': [instrumental_case, singular, neuter, positive],
            },
            {
                'section_break': True,
                'label': '1. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'To jsou moji [velcí] psi.',
                'grammatical_features_item_ids': [nominative_case, plural, masculine_animate, positive],
            },
            {
                'label': '2. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Má strach z mých [velkých] psů.',
                'grammatical_features_item_ids': [genitive_case, plural, masculine_animate, positive],
            },
            {
                'label': '3. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Dej to mým [velkým] psům.',
                'grammatical_features_item_ids': [dative_case, plural, masculine_animate, positive],
            },
            {
                'label': '4. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Vidím dva [velké] psy.',
                'grammatical_features_item_ids': [accusative_case, plural, masculine_animate, positive],
            },
            {
                'label': '5. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Kam kráčíte, [velcí] psi?',
                'grammatical_features_item_ids': [vocative_case, plural, masculine_animate, positive],
            },
            {
                'label': '6. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svých [velkých] psech.',
                'grammatical_features_item_ids': [locative_case, plural, masculine_animate, positive],
            },
            {
                'label': '7. pád, rod mužský životný, množné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvými [velkými] psy.',
                'grammatical_features_item_ids': [instrumental_case, plural, masculine_animate, positive],
            },
            {
                'label': '1. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'To jsou mé [velké] hrady.',
                'grammatical_features_item_ids': [nominative_case, plural, masculine_inanimate, positive],
            },
            {
                'label': '2. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Má strach z mých [velkých] hradů.',
                'grammatical_features_item_ids': [genitive_case, plural, masculine_inanimate, positive],
            },
            {
                'label': '3. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Dej to k mým [velkým] hradům.',
                'grammatical_features_item_ids': [dative_case, plural, masculine_inanimate, positive],
            },
            {
                'label': '4. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Vidím dva [velké] hrady.',
                'grammatical_features_item_ids': [accusative_case, plural, masculine_inanimate, positive],
            },
            {
                'label': '5. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Kam směřujete, [velké] hrady?',
                'grammatical_features_item_ids': [vocative_case, plural, masculine_inanimate, positive],
            },
            {
                'label': '6. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svých [velkých] hradech.',
                'grammatical_features_item_ids': [locative_case, plural, masculine_inanimate, positive],
            },
            {
                'label': '7. pád, rod mužský neživotný, množné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvými [velkými] hrady.',
                'grammatical_features_item_ids': [instrumental_case, plural, masculine_inanimate, positive],
            },
            {
                'section_break': True,
                'label': '1. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'To jsou mé [velké] ženy.',
                'grammatical_features_item_ids': [nominative_case, plural, feminine, positive],
            },
            {
                'label': '2. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Má strach z mých [velkých] žen.',
                'grammatical_features_item_ids': [genitive_case, plural, feminine, positive],
            },
            {
                'label': '3. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Dej to mým [velkým] ženám.',
                'grammatical_features_item_ids': [dative_case, plural, feminine, positive],
            },
            {
                'label': '4. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Vidím dvě [velké] ženy.',
                'grammatical_features_item_ids': [accusative_case, plural, feminine, positive],
            },
            {
                'label': '5. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Kam kráčíte, [velké] ženy?',
                'grammatical_features_item_ids': [vocative_case, plural, feminine, positive],
            },
            {
                'label': '6. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svých [velkých] ženách.',
                'grammatical_features_item_ids': [locative_case, plural, feminine, positive],
            },
            {
                'label': '7. pád, rod ženský, množné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvými [velkými] ženami.',
                'grammatical_features_item_ids': [instrumental_case, plural, feminine, positive],
            },
            {
                'label': '1. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'To jsou má [velká] kuřata.',
                'grammatical_features_item_ids': [nominative_case, plural, neuter, positive],
            },
            {
                'label': '2. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Má strach z mých [velkých] kuřat.',
                'grammatical_features_item_ids': [genitive_case, plural, neuter, positive],
            },
            {
                'label': '3. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Dej to mým [velkým] kuřatům.',
                'grammatical_features_item_ids': [dative_case, plural, neuter, positive],
            },
            {
                'label': '4. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Vidím dvě [velká] kuřata.',
                'grammatical_features_item_ids': [accusative_case, plural, neuter, positive],
            },
            {
                'label': '5. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Kam kráčíte, [velká] kuřata?',
                'grammatical_features_item_ids': [vocative_case, plural, neuter, positive],
            },
            {
                'label': '6. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Pověz mi něco o svých [velkých] kuřatech.',
                'grammatical_features_item_ids': [locative_case, plural, neuter, positive],
            },
            {
                'label': '7. pád, rod střední, množné číslo, 1. stupeň',
                'example': 'Seznámil jsem se s tvými [velkými] kuřaty.',
                'grammatical_features_item_ids': [instrumental_case, plural, neuter, positive],
            },
            {
                'section_break': True,
                'label': '1. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'To je můj [větší] pes.',
                'grammatical_features_item_ids': [nominative_case, singular, masculine_animate, comparative],
            },
            {
                'label': '2. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Má strach z mého [většího] psa.',
                'grammatical_features_item_ids': [genitive_case, singular, masculine_animate, comparative],
            },
            {
                'label': '3. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Dej to mému [většímu] psu.',
                'grammatical_features_item_ids': [dative_case, singular, masculine_animate, comparative],
            },
            {
                'label': '4. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Vidím jednoho [většího] psa.',
                'grammatical_features_item_ids': [accusative_case, singular, masculine_animate, comparative],
            },
            {
                'label': '5. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Kam kráčíš, [větší] pse?',
                'grammatical_features_item_ids': [vocative_case, singular, masculine_animate, comparative],
            },
            {
                'label': '6. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svém [větším] psu.',
                'grammatical_features_item_ids': [locative_case, singular, masculine_animate, comparative],
            },
            {
                'label': '7. pád, rod mužský životný, jednotné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvým [větším] psem.',
                'grammatical_features_item_ids': [instrumental_case, singular, masculine_animate, comparative],
            },
            {
                'label': '1. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'To je můj [větší] hrad.',
                'grammatical_features_item_ids': [nominative_case, singular, masculine_inanimate, comparative],
            },
            {
                'label': '2. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Má strach z mého [většího] hradu.',
                'grammatical_features_item_ids': [genitive_case, singular, masculine_inanimate, comparative],
            },
            {
                'label': '3. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Dej to k mému [většímu] hradu.',
                'grammatical_features_item_ids': [dative_case, singular, masculine_inanimate, comparative],
            },
            {
                'label': '4. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Vidím jeden [větší] hrad.',
                'grammatical_features_item_ids': [accusative_case, singular, masculine_inanimate, comparative],
            },
            {
                'label': '5. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Kam směřuješ, [větší] hrade?',
                'grammatical_features_item_ids': [vocative_case, singular, masculine_inanimate, comparative],
            },
            {
                'label': '6. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svém [větším] hradu.',
                'grammatical_features_item_ids': [locative_case, singular, masculine_inanimate, comparative],
            },
            {
                'label': '7. pád, rod mužský neživotný, jednotné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvým [větším] hradem.',
                'grammatical_features_item_ids': [instrumental_case, singular, masculine_inanimate, comparative],
            },
            {
                'section_break': True,
                'label': '1. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'To je má [větší] žena.',
                'grammatical_features_item_ids': [nominative_case, singular, feminine, comparative],
            },
            {
                'label': '2. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Má strach z mé [větší] ženy.',
                'grammatical_features_item_ids': [genitive_case, singular, feminine, comparative],
            },
            {
                'label': '3. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Dej to mé [větší] ženě.',
                'grammatical_features_item_ids': [dative_case, singular, feminine, comparative],
            },
            {
                'label': '4. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Vidím jednu [větší] ženu.',
                'grammatical_features_item_ids': [accusative_case, singular, feminine, comparative],
            },
            {
                'label': '5. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Kam kráčíš, [větší] ženo?',
                'grammatical_features_item_ids': [vocative_case, singular, feminine, comparative],
            },
            {
                'label': '6. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Pověz mi něco o své [větší] ženě.',
                'grammatical_features_item_ids': [locative_case, singular, feminine, comparative],
            },
            {
                'label': '7. pád, rod ženský, jednotné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvou [větší] ženou.',
                'grammatical_features_item_ids': [instrumental_case, singular, feminine, comparative],
            },
            {
                'label': '1. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'To je mé [větší] kuře.',
                'grammatical_features_item_ids': [nominative_case, singular, neuter, comparative],
            },
            {
                'label': '2. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Má strach z mého [většího] kuřete.',
                'grammatical_features_item_ids': [genitive_case, singular, neuter, comparative],
            },
            {
                'label': '3. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Dej to mému [většímu] kuřeti.',
                'grammatical_features_item_ids': [dative_case, singular, neuter, comparative],
            },
            {
                'label': '4. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Vidím jedno [větší] kuře.',
                'grammatical_features_item_ids': [accusative_case, singular, neuter, comparative],
            },
            {
                'label': '5. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Kam kráčíš, [větší] kuře?',
                'grammatical_features_item_ids': [vocative_case, singular, neuter, comparative],
            },
            {
                'label': '6. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svém [větším] kuřeti.',
                'grammatical_features_item_ids': [locative_case, singular, neuter, comparative],
            },
            {
                'label': '7. pád, rod střední, jednotné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvým [větším] kuřetem.',
                'grammatical_features_item_ids': [instrumental_case, singular, neuter, comparative],
            },
            {
                'section_break': True,
                'label': '1. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'To jsou moji [větší] psi.',
                'grammatical_features_item_ids': [nominative_case, plural, masculine_animate, comparative],
            },
            {
                'label': '2. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Má strach z mých [větších] psů.',
                'grammatical_features_item_ids': [genitive_case, plural, masculine_animate, comparative],
            },
            {
                'label': '3. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Dej to mým [větším] psům.',
                'grammatical_features_item_ids': [dative_case, plural, masculine_animate, comparative],
            },
            {
                'label': '4. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Vidím dva [větší] psy.',
                'grammatical_features_item_ids': [accusative_case, plural, masculine_animate, comparative],
            },
            {
                'label': '5. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Kam kráčíte, [větší] psi?',
                'grammatical_features_item_ids': [vocative_case, plural, masculine_animate, comparative],
            },
            {
                'label': '6. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svých [větších] psech.',
                'grammatical_features_item_ids': [locative_case, plural, masculine_animate, comparative],
            },
            {
                'label': '7. pád, rod mužský životný, množné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvými [většími] psy.',
                'grammatical_features_item_ids': [instrumental_case, plural, masculine_animate, comparative],
            },
            {
                'label': '1. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'To jsou mé [větší] hrady.',
                'grammatical_features_item_ids': [nominative_case, plural, masculine_inanimate, comparative],
            },
            {
                'label': '2. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Má strach z mých [větších] hradů.',
                'grammatical_features_item_ids': [genitive_case, plural, masculine_inanimate, comparative],
            },
            {
                'label': '3. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Dej to k mým [větším] hradům.',
                'grammatical_features_item_ids': [dative_case, plural, masculine_inanimate, comparative],
            },
            {
                'label': '4. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Vidím dva [větší] hrady.',
                'grammatical_features_item_ids': [accusative_case, plural, masculine_inanimate, comparative],
            },
            {
                'label': '5. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Kam směřujete, [větší] hrady?',
                'grammatical_features_item_ids': [vocative_case, plural, masculine_inanimate, comparative],
            },
            {
                'label': '6. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svých [větších] hradech.',
                'grammatical_features_item_ids': [locative_case, plural, masculine_inanimate, comparative],
            },
            {
                'label': '7. pád, rod mužský neživotný, množné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvými [většími] hrady.',
                'grammatical_features_item_ids': [instrumental_case, plural, masculine_inanimate, comparative],
            },
            {
                'section_break': True,
                'label': '1. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'To jsou mé [větší] ženy.',
                'grammatical_features_item_ids': [nominative_case, plural, feminine, comparative],
            },
            {
                'label': '2. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Má strach z mých [větších] žen.',
                'grammatical_features_item_ids': [genitive_case, plural, feminine, comparative],
            },
            {
                'label': '3. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Dej to mým [větším] ženám.',
                'grammatical_features_item_ids': [dative_case, plural, feminine, comparative],
            },
            {
                'label': '4. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Vidím dvě [větší] ženy.',
                'grammatical_features_item_ids': [accusative_case, plural, feminine, comparative],
            },
            {
                'label': '5. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Kam kráčíte, [větší] ženy?',
                'grammatical_features_item_ids': [vocative_case, plural, feminine, comparative],
            },
            {
                'label': '6. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svých [větších] ženách.',
                'grammatical_features_item_ids': [locative_case, plural, feminine, comparative],
            },
            {
                'label': '7. pád, rod ženský, množné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvými [většími] ženami.',
                'grammatical_features_item_ids': [instrumental_case, plural, feminine, comparative],
            },
            {
                'label': '1. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'To jsou má [větší] kuřata.',
                'grammatical_features_item_ids': [nominative_case, plural, neuter, comparative],
            },
            {
                'label': '2. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Má strach z mých [větších] kuřat.',
                'grammatical_features_item_ids': [genitive_case, plural, neuter, comparative],
            },
            {
                'label': '3. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Dej to mým [větším] kuřatům.',
                'grammatical_features_item_ids': [dative_case, plural, neuter, comparative],
            },
            {
                'label': '4. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Vidím dvě [větší] kuřata.',
                'grammatical_features_item_ids': [accusative_case, plural, neuter, comparative],
            },
            {
                'label': '5. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Kam kráčíte, [větší] kuřata?',
                'grammatical_features_item_ids': [vocative_case, plural, neuter, comparative],
            },
            {
                'label': '6. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Pověz mi něco o svých [větších] kuřatech.',
                'grammatical_features_item_ids': [locative_case, plural, neuter, comparative],
            },
            {
                'label': '7. pád, rod střední, množné číslo, 2. stupeň',
                'example': 'Seznámil jsem se s tvými [většími] kuřaty.',
                'grammatical_features_item_ids': [instrumental_case, plural, neuter, comparative],
            },
            {
                'section_break': True,
                'label': '1. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'To je můj [největší] pes.',
                'grammatical_features_item_ids': [nominative_case, singular, masculine_animate, superlative],
            },
            {
                'label': '2. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Má strach z mého [největšího] psa.',
                'grammatical_features_item_ids': [genitive_case, singular, masculine_animate, superlative],
            },
            {
                'label': '3. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Dej to mému [největšímu] psu.',
                'grammatical_features_item_ids': [dative_case, singular, masculine_animate, superlative],
            },
            {
                'label': '4. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Vidím jednoho [největšího] psa.',
                'grammatical_features_item_ids': [accusative_case, singular, masculine_animate, superlative],
            },
            {
                'label': '5. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Kam kráčíš, [největší] pse?',
                'grammatical_features_item_ids': [vocative_case, singular, masculine_animate, superlative],
            },
            {
                'label': '6. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svém [největším] psu.',
                'grammatical_features_item_ids': [locative_case, singular, masculine_animate, superlative],
            },
            {
                'label': '7. pád, rod mužský životný, jednotné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvým [největším] psem.',
                'grammatical_features_item_ids': [instrumental_case, singular, masculine_animate, superlative],
            },
            {
                'label': '1. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'To je můj [největší] hrad.',
                'grammatical_features_item_ids': [nominative_case, singular, masculine_inanimate, superlative],
            },
            {
                'label': '2. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Má strach z mého [největšího] hradu.',
                'grammatical_features_item_ids': [genitive_case, singular, masculine_inanimate, superlative],
            },
            {
                'label': '3. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Dej to k mému [největšímu] hradu.',
                'grammatical_features_item_ids': [dative_case, singular, masculine_inanimate, superlative],
            },
            {
                'label': '4. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Vidím jeden [největší] hrad.',
                'grammatical_features_item_ids': [accusative_case, singular, masculine_inanimate, superlative],
            },
            {
                'label': '5. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Kam směřuješ, [největší] hrade?',
                'grammatical_features_item_ids': [vocative_case, singular, masculine_inanimate, superlative],
            },
            {
                'label': '6. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svém [největším] hradu.',
                'grammatical_features_item_ids': [locative_case, singular, masculine_inanimate, superlative],
            },
            {
                'label': '7. pád, rod mužský neživotný, jednotné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvým [největším] hradem.',
                'grammatical_features_item_ids': [instrumental_case, singular, masculine_inanimate, superlative],
            },
            {
                'section_break': True,
                'label': '1. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'To je má [největší] žena.',
                'grammatical_features_item_ids': [nominative_case, singular, feminine, superlative],
            },
            {
                'label': '2. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Má strach z mé [největší] ženy.',
                'grammatical_features_item_ids': [genitive_case, singular, feminine, superlative],
            },
            {
                'label': '3. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Dej to mé [největší] ženě.',
                'grammatical_features_item_ids': [dative_case, singular, feminine, superlative],
            },
            {
                'label': '4. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Vidím jednu [největší] ženu.',
                'grammatical_features_item_ids': [accusative_case, singular, feminine, superlative],
            },
            {
                'label': '5. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Kam kráčíš, [největší] ženo?',
                'grammatical_features_item_ids': [vocative_case, singular, feminine, superlative],
            },
            {
                'label': '6. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Pověz mi něco o své [největší] ženě.',
                'grammatical_features_item_ids': [locative_case, singular, feminine, superlative],
            },
            {
                'label': '7. pád, rod ženský, jednotné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvou [největší] ženou.',
                'grammatical_features_item_ids': [instrumental_case, singular, feminine, superlative],
            },
            {
                'label': '1. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'To je mé [největší] kuře.',
                'grammatical_features_item_ids': [nominative_case, singular, neuter, superlative],
            },
            {
                'label': '2. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Má strach z mého [největšího] kuřete.',
                'grammatical_features_item_ids': [genitive_case, singular, neuter, superlative],
            },
            {
                'label': '3. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Dej to mému [největšímu] kuřeti.',
                'grammatical_features_item_ids': [dative_case, singular, neuter, superlative],
            },
            {
                'label': '4. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Vidím jedno [největší] kuře.',
                'grammatical_features_item_ids': [accusative_case, singular, neuter, superlative],
            },
            {
                'label': '5. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Kam kráčíš, [největší] kuře?',
                'grammatical_features_item_ids': [vocative_case, singular, neuter, superlative],
            },
            {
                'label': '6. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svém [největším] kuřeti.',
                'grammatical_features_item_ids': [locative_case, singular, neuter, superlative],
            },
            {
                'label': '7. pád, rod střední, jednotné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvým [největším] kuřetem.',
                'grammatical_features_item_ids': [instrumental_case, singular, neuter, superlative],
            },
            {
                'section_break': True,
                'label': '1. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'To jsou moji [největší] psi.',
                'grammatical_features_item_ids': [nominative_case, plural, masculine_animate, superlative],
            },
            {
                'label': '2. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Má strach z mých [největších] psů.',
                'grammatical_features_item_ids': [genitive_case, plural, masculine_animate, superlative],
            },
            {
                'label': '3. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Dej to mým [největším] psům.',
                'grammatical_features_item_ids': [dative_case, plural, masculine_animate, superlative],
            },
            {
                'label': '4. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Vidím dva [největší] psy.',
                'grammatical_features_item_ids': [accusative_case, plural, masculine_animate, superlative],
            },
            {
                'label': '5. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Kam kráčíte, [největší] psi?',
                'grammatical_features_item_ids': [vocative_case, plural, masculine_animate, superlative],
            },
            {
                'label': '6. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svých [největších] psech.',
                'grammatical_features_item_ids': [locative_case, plural, masculine_animate, superlative],
            },
            {
                'label': '7. pád, rod mužský životný, množné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvými [největšími] psy.',
                'grammatical_features_item_ids': [instrumental_case, plural, masculine_animate, superlative],
            },
            {
                'label': '1. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'To jsou mé [největší] hrady.',
                'grammatical_features_item_ids': [nominative_case, plural, masculine_inanimate, superlative],
            },
            {
                'label': '2. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Má strach z mých [největších] hradů.',
                'grammatical_features_item_ids': [genitive_case, plural, masculine_inanimate, superlative],
            },
            {
                'label': '3. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Dej to k mým [největším] hradům.',
                'grammatical_features_item_ids': [dative_case, plural, masculine_inanimate, superlative],
            },
            {
                'label': '4. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Vidím dva [největší] hrady.',
                'grammatical_features_item_ids': [accusative_case, plural, masculine_inanimate, superlative],
            },
            {
                'label': '5. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Kam směřujete, [největší] hrady?',
                'grammatical_features_item_ids': [vocative_case, plural, masculine_inanimate, superlative],
            },
            {
                'label': '6. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svých [největších] hradech.',
                'grammatical_features_item_ids': [locative_case, plural, masculine_inanimate, superlative],
            },
            {
                'label': '7. pád, rod mužský neživotný, množné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvými [největšími] hrady.',
                'grammatical_features_item_ids': [instrumental_case, plural, masculine_inanimate, superlative],
            },
            {
                'section_break': True,
                'label': '1. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'To jsou mé [největší] ženy.',
                'grammatical_features_item_ids': [nominative_case, plural, feminine, superlative],
            },
            {
                'label': '2. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Má strach z mých [největších] žen.',
                'grammatical_features_item_ids': [genitive_case, plural, feminine, superlative],
            },
            {
                'label': '3. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Dej to mým [největším] ženám.',
                'grammatical_features_item_ids': [dative_case, plural, feminine, superlative],
            },
            {
                'label': '4. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Vidím dvě [největší] ženy.',
                'grammatical_features_item_ids': [accusative_case, plural, feminine, superlative],
            },
            {
                'label': '5. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Kam kráčíte, [největší] ženy?',
                'grammatical_features_item_ids': [vocative_case, plural, feminine, superlative],
            },
            {
                'label': '6. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svých [největších] ženách.',
                'grammatical_features_item_ids': [locative_case, plural, feminine, superlative],
            },
            {
                'label': '7. pád, rod ženský, množné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvými [největšími] ženami.',
                'grammatical_features_item_ids': [instrumental_case, plural, feminine, superlative],
            },
            {
                'label': '1. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'To jsou má [největší] kuřata.',
                'grammatical_features_item_ids': [nominative_case, plural, neuter, superlative],
            },
            {
                'label': '2. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Má strach z mých [největších] kuřat.',
                'grammatical_features_item_ids': [genitive_case, plural, neuter, superlative],
            },
            {
                'label': '3. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Dej to mým [největším] kuřatům.',
                'grammatical_features_item_ids': [dative_case, plural, neuter, superlative],
            },
            {
                'label': '4. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Vidím dvě [největší] kuřata.',
                'grammatical_features_item_ids': [accusative_case, plural, neuter, superlative],
            },
            {
                'label': '5. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Kam kráčíte, [největší] kuřata?',
                'grammatical_features_item_ids': [vocative_case, plural, neuter, superlative],
            },
            {
                'label': '6. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Pověz mi něco o svých [největších] kuřatech.',
                'grammatical_features_item_ids': [locative_case, plural, neuter, superlative],
            },
            {
                'label': '7. pád, rod střední, množné číslo, 3. stupeň',
                'example': 'Seznámil jsem se s tvými [největšími] kuřaty.',
                'grammatical_features_item_ids': [instrumental_case, plural, neuter, superlative],
            },
        ],
    },

    'czech-verb-perfective': {
        '@attribution': {'users': ['Adrijaned', 'Strepon', 'Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české sloveso dokonavé',
        'language': language_Czech,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'infinitiv',
                'example': '[postavit].',
                'grammatical_features_item_ids': [infinitive],
            },
            {
                'label': 'infinitiv',
                'example': '[postaviti].',
                'grammatical_features_item_ids': [infinitive],
                'statements': statements(language_style, book_expression),
            },
            {
                'section_break': True,
                'label': '1. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Já teď [postavím].',
                'grammatical_features_item_ids': [first_person, singular, indicative, present_tense],
            },
            {
                'label': '2. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Ty teď [postavíš].',
                'grammatical_features_item_ids': [second_person, singular, indicative, present_tense],
            },
            {
                'label': '3. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Ono to teď [postaví].',
                'grammatical_features_item_ids': [third_person, singular, indicative, present_tense],
            },
            {
                'label': '1. osoba, množné číslo, oznamovací způsob',
                'example': 'My teď [postavíme].',
                'grammatical_features_item_ids': [first_person, plural, indicative, present_tense],
            },
            {
                'label': '2. osoba, množné číslo, oznamovací způsob',
                'example': 'Vy teď [postavíte].',
                'grammatical_features_item_ids': [second_person, plural, indicative, present_tense],
            },
            {
                'label': '3. osoba, množné číslo, oznamovací způsob',
                'example': 'Oni teď [postaví].',
                'grammatical_features_item_ids': [third_person, plural, indicative, present_tense],
            },
            {
                'section_break': True,
                'label': 'rozkazovací způsob, 2. osoba, jednotné číslo',
                'example': 'Ty [postav]!',
                'grammatical_features_item_ids': [imperative, second_person, singular],
            },
            {
                'label': 'rozkazovací způsob, 1. osoba, množné číslo',
                'example': 'My [postavme]!',
                'grammatical_features_item_ids': [imperative, first_person, plural],
            },
            {
                'label': 'rozkazovací způsob, 2. osoba, množné číslo',
                'example': 'Vy [postavte]!',
                'grammatical_features_item_ids': [imperative, second_person, plural],
            },
            {
                'section_break': True,
                'label': 'příčestí činné, rod mužský životný, jednotné číslo',
                'example': 'On by [postavil].',
                'grammatical_features_item_ids': [active_participle, masculine_animate, singular],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, jednotné číslo',
                'example': 'Ten by [postavil].',
                'grammatical_features_item_ids': [active_participle, masculine_inanimate, singular],
            },
            {
                'label': 'příčestí činné, rod ženský, jednotné číslo',
                'example': 'Ona by [postavila].',
                'grammatical_features_item_ids': [active_participle, feminine, singular],
            },
            {
                'label': 'příčestí činné, rod střední, jednotné číslo',
                'example': 'Ono by [postavilo].',
                'grammatical_features_item_ids': [active_participle, neuter, singular],
            },
            {
                'label': 'příčestí činné, rod mužský životný, množné číslo',
                'example': 'Oni muži by [postavili].',
                'grammatical_features_item_ids': [active_participle, masculine_animate, plural],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, množné číslo',
                'example': 'Ty hrady by [postavily].',
                'grammatical_features_item_ids': [active_participle, masculine_inanimate, plural],
            },
            {
                'label': 'příčestí činné, rod ženský, množné číslo',
                'example': 'Ony by [postavily].',
                'grammatical_features_item_ids': [active_participle, feminine, plural],
            },
            {
                'label': 'příčestí činné, rod střední, množné číslo',
                'example': 'Ona by [postavila].',
                'grammatical_features_item_ids': [active_participle, neuter, plural],
            },
            {
                'section_break': True,
                'label': 'příčestí trpné, rod mužský životný, jednotné číslo',
                'example': 'On bude [postaven].',
                'grammatical_features_item_ids': [passive_participle, masculine_animate, singular],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, jednotné číslo',
                'example': 'Ten bude [postaven].',
                'grammatical_features_item_ids': [passive_participle, masculine_inanimate, singular],
            },
            {
                'label': 'příčestí trpné, rod ženský, jednotné číslo',
                'example': 'Ona bude [postavena].',
                'grammatical_features_item_ids': [passive_participle, feminine, singular],
            },
            {
                'label': 'příčestí trpné, rod střední, jednotné číslo',
                'example': 'Ono bude [postaveno].',
                'grammatical_features_item_ids': [passive_participle, neuter, singular],
            },
            {
                'label': 'příčestí trpné, rod mužský životný, množné číslo',
                'example': 'Oni muži budou [postaveni].',
                'grammatical_features_item_ids': [passive_participle, masculine_animate, plural],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, množné číslo',
                'example': 'Ty hrady budou [postaveny].',
                'grammatical_features_item_ids': [passive_participle, masculine_inanimate, plural],
            },
            {
                'label': 'příčestí trpné, rod ženský, množné číslo',
                'example': 'Ony budou [postaveny].',
                'grammatical_features_item_ids': [passive_participle, feminine, plural],
            },
            {
                'label': 'příčestí trpné, rod střední, množné číslo',
                'example': 'Ona budou [postavena].',
                'grammatical_features_item_ids': [passive_participle, neuter, plural],
            },
            {
                'section_break': True,
                'label': 'přechodník minulý, rod mužský životný, jednotné číslo',
                'example': 'On [postaviv], odešel.',
                'grammatical_features_item_ids': [past_transgressive, masculine_animate, singular],
            },
            {
                'label': 'přechodník minulý, rod mužský neživotný, jednotné číslo',
                'example': 'Ten [postaviv], zmizel.',
                'grammatical_features_item_ids': [past_transgressive, masculine_inanimate, singular],
            },
            {
                'label': 'přechodník minulý, rod ženský, jednotné číslo',
                'example': 'Ona [postavivši], odešla.',
                'grammatical_features_item_ids': [past_transgressive, feminine, singular],
            },
            {
                'label': 'přechodník minulý, rod střední, jednotné číslo',
                'example': 'Ono [postavivši], odešlo.',
                'grammatical_features_item_ids': [past_transgressive, neuter, singular],
            },
            {
                'label': 'přechodník minulý, rod mužský životný, množné číslo',
                'example': 'Oni [postavivše], odešli.',
                'grammatical_features_item_ids': [past_transgressive, masculine_animate, plural],
            },
            {
                'label': 'přechodník minulý, rod mužský neživotný, množné číslo',
                'example': 'Ty [postavivše], zmizely.',
                'grammatical_features_item_ids': [past_transgressive, masculine_inanimate, plural],
            },
            {
                'label': 'přechodník minulý, rod ženský, množné číslo',
                'example': 'Ony [postavivše], odešly.',
                'grammatical_features_item_ids': [past_transgressive, feminine, plural],
            },
            {
                'label': 'přechodník minulý, rod střední, množné číslo',
                'example': 'Ona [postavivše], odešla.',
                'grammatical_features_item_ids': [past_transgressive, neuter, plural],
            },
        ],
        'statements': statements(grammatical_aspect, perfective),
    },

    'czech-verb-imperfective': {
        '@attribution': {'users': ['Lexicolover'], 'title': 'Wikidata:Wikidata Lexeme Forms/Czech'},
        'label': 'české sloveso nedokonavé',
        'language': language_Czech,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'infinitiv',
                'example': '[zpívat].',
                'grammatical_features_item_ids': [infinitive],
            },
            {
                'label': 'infinitiv',
                'example': '[zpívati].',
                'grammatical_features_item_ids': [infinitive],
                'statements': statements(language_style, book_expression),
            },
            {
                'section_break': True,
                'label': '1. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Já [zpívám].',
                'grammatical_features_item_ids': [first_person, singular, indicative, present_tense],
            },
            {
                'label': '2. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Ty [zpíváš].',
                'grammatical_features_item_ids': [second_person, singular, indicative, present_tense],
            },
            {
                'label': '3. osoba, jednotné číslo, oznamovací způsob',
                'example': 'Ona [zpívá].',
                'grammatical_features_item_ids': [third_person, singular, indicative, present_tense],
            },
            {
                'label': '1. osoba, množné číslo, oznamovací způsob',
                'example': 'My [zpíváme].',
                'grammatical_features_item_ids': [first_person, plural, indicative, present_tense],
            },
            {
                'label': '2. osoba, množné číslo, oznamovací způsob',
                'example': 'Vy [zpíváte].',
                'grammatical_features_item_ids': [second_person, plural, indicative, present_tense],
            },
            {
                'label': '3. osoba, množné číslo, oznamovací způsob',
                'example': 'Oni [zpívají].',
                'grammatical_features_item_ids': [third_person, plural, indicative, present_tense],
            },
            {
                'section_break': True,
                'label': 'rozkazovací způsob, 2. osoba, jednotné číslo',
                'example': '(Ty) [zpívej]!',
                'grammatical_features_item_ids': [imperative, second_person, singular],
            },
            {
                'label': 'rozkazovací způsob, 1. osoba, množné číslo',
                'example': '(My) [zpívejme]!',
                'grammatical_features_item_ids': [imperative, first_person, plural],
            },
            {
                'label': 'rozkazovací způsob, 2. osoba, množné číslo',
                'example': '(Vy) [zpívejte]!',
                'grammatical_features_item_ids': [imperative, second_person, plural],
            },
            {
                'section_break': True,
                'label': 'příčestí činné, rod mužský životný, jednotné číslo',
                'example': 'On to včera [zpíval].',
                'grammatical_features_item_ids': [active_participle, masculine_animate, singular],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, jednotné číslo',
                'example': 'Celý sál to včera [zpíval].',
                'grammatical_features_item_ids': [active_participle, masculine_inanimate, singular],
            },
            {
                'label': 'příčestí činné, rod ženský, jednotné číslo',
                'example': 'Ona to včera [zpívala].',
                'grammatical_features_item_ids': [active_participle, feminine, singular],
            },
            {
                'label': 'příčestí činné, rod střední, jednotné číslo',
                'example': 'Ono to včera [zpívalo].',
                'grammatical_features_item_ids': [active_participle, neuter, singular],
            },
            {
                'label': 'příčestí činné, rod mužský životný, množné číslo',
                'example': 'Oni to včera [zpívali].',
                'grammatical_features_item_ids': [active_participle, masculine_animate, plural],
            },
            {
                'label': 'příčestí činné, rod mužský neživotný, množné číslo',
                'example': 'Celé sály to včera [zpívaly].',
                'grammatical_features_item_ids': [active_participle, masculine_inanimate, plural],
            },
            {
                'label': 'příčestí činné, rod ženský, množné číslo',
                'example': 'Ony to včera [zpívaly].',
                'grammatical_features_item_ids': [active_participle, feminine, plural],
            },
            {
                'label': 'příčestí činné, rod střední, množné číslo',
                'example': 'Ona to včera [zpívala].',
                'grammatical_features_item_ids': [active_participle, neuter, plural],
            },
            {
                'section_break': True,
                'label': 'příčestí trpné, rod mužský životný, jednotné číslo',
                'example': 'On byl [zpíván].',
                'grammatical_features_item_ids': [passive_participle, masculine_animate, singular],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, jednotné číslo',
                'example': 'Ten byl [zpíván].',
                'grammatical_features_item_ids': [passive_participle, masculine_inanimate, singular],
            },
            {
                'label': 'příčestí trpné, rod ženský, jednotné číslo',
                'example': 'Ona byla [zpívána].',
                'grammatical_features_item_ids': [passive_participle, feminine, singular],
            },
            {
                'label': 'příčestí trpné, rod střední, jednotné číslo',
                'example': 'Ono bylo [zpíváno].',
                'grammatical_features_item_ids': [passive_participle, neuter, singular],
            },
            {
                'label': 'příčestí trpné, rod mužský životný, množné číslo',
                'example': 'Oni byli [zpíváni].',
                'grammatical_features_item_ids': [passive_participle, masculine_animate, plural],
            },
            {
                'label': 'příčestí trpné, rod mužský neživotný, množné číslo',
                'example': 'Hrady byly [zpívány].',
                'grammatical_features_item_ids': [passive_participle, masculine_inanimate, plural],
            },
            {
                'label': 'příčestí trpné, rod ženský, množné číslo',
                'example': 'Ony byly [zpívány].',
                'grammatical_features_item_ids': [passive_participle, feminine, plural],
            },
            {
                'label': 'příčestí trpné, rod střední, množné číslo',
                'example': 'Ona byla [zpívána].',
                'grammatical_features_item_ids': [passive_participle, neuter, plural],
            },
            {
                'section_break': True,
                'label': 'přechodník přítomný, rod mužský životný, jednotné číslo',
                'example': 'On [zpívaje] odešel.',
                'grammatical_features_item_ids': [present_transgressive, masculine_animate, singular],
            },
            {
                'label': 'přechodník přítomný, rod mužský neživotný, jednotné číslo',
                'example': 'Hrad [zpívaje] zmizel.',
                'grammatical_features_item_ids': [present_transgressive, masculine_inanimate, singular],
            },
            {
                'label': 'přechodník přítomný, rod ženský, jednotné číslo',
                'example': 'Ona [zpívajíc] odešla.',
                'grammatical_features_item_ids': [present_transgressive, feminine, singular],
            },
            {
                'label': 'přechodník přítomný, rod střední, jednotné číslo',
                'example': 'Ono [zpívajíc] odešlo.',
                'grammatical_features_item_ids': [present_transgressive, neuter, singular],
            },
            {
                'label': 'přechodník přítomný, rod mužský životný, množné číslo',
                'example': 'Oni [zpívajíce] odešli.',
                'grammatical_features_item_ids': [present_transgressive, masculine_animate, plural],
            },
            {
                'label': 'přechodník přítomný, rod mužský neživotný, množné číslo',
                'example': 'Hrady [zpívajíce] zmizely.',
                'grammatical_features_item_ids': [present_transgressive, masculine_inanimate, plural],
            },
            {
                'label': 'přechodník přítomný, rod ženský, množné číslo',
                'example': 'Ony [zpívajíce] odešly.',
                'grammatical_features_item_ids': [present_transgressive, feminine, plural],
            },
            {
                'label': 'přechodník přítomný, rod střední, množné číslo',
                'example': 'Ona [zpívajíce] odešla.',
                'grammatical_features_item_ids': [present_transgressive, neuter, plural],
            },
        ],
        'statements': statements(grammatical_aspect, imperfective),
    },

    'danish-noun-common': {
        '@attribution': {'users': ['So9q', 'Fnielsen'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk substantiv (fælleskøn)',
        'language': language_Danish,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'nominativ ental, ubestemt, ikke-ejefald',
                'example': 'Det her er en [bil].',
                'grammatical_features_item_ids': [singular, indefinite, non_genitive],
            },
            {
                'label': 'nominativ ental, bestemt, ikke-ejefald',
                'example': '[bilen] er ny.',
                'grammatical_features_item_ids': [singular, definite, non_genitive],
            },
            {
                'label': 'nominativ flertal, ubestemt, ikke-ejefald',
                'example': 'Jeg ser flere [biler].',
                'grammatical_features_item_ids': [plural, indefinite, non_genitive],
            },
            {
                'label': 'nominativ flertal, bestemt, ikke-ejefald',
                'example': 'Alle [bilerne] er væk.',
                'grammatical_features_item_ids': [plural, definite, non_genitive],
            },
            {
                'label': 'nominativ ental,  ubestemt, ejefald',
                'example': 'Det her er en [bils] hjul.',
                'grammatical_features_item_ids': [singular, indefinite, genitive_case],
            },
            {
                'label': 'nominativ ental, bestemt, ejefald',
                'example': 'Jeg ser [bilens] hjul.',
                'grammatical_features_item_ids': [singular, definite, genitive_case],
            },
            {
                'label': 'nominativ flertal, ubestemt, ejefald',
                'example': 'Jeg ser flere [bilers] lys.',
                'grammatical_features_item_ids': [plural, indefinite, genitive_case],
            },
            {
                'label': 'nominativ flertal, bestemt, ejefald',
                'example': 'Jeg ser alle [bilernes] lys.',
                'grammatical_features_item_ids': [plural, definite, genitive_case],
            },
        ],
        'statements': statements(grammatical_gender, common),
    },

    'danish-noun-neuter': {
        '@attribution': {'users': ['So9q', 'Fnielsen'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk substantiv (intetkøn)',
        'language': language_Danish,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ental,  ubestemt, ikke-ejefald',
                'example': 'Det her er et [bord].',
                'grammatical_features_item_ids': [singular, indefinite, non_genitive],
            },
            {
                'label': 'ental, bestemt, ikke-ejefald',
                'example': 'Der er [bordet] som det eneste.',
                'grammatical_features_item_ids': [singular, definite, non_genitive],
            },
            {
                'label': 'flertal, ubestemt, ikke-ejefald',
                'example': 'Jeg ser flere [borde].',
                'grammatical_features_item_ids': [plural, indefinite, non_genitive],
            },
            {
                'label': 'flertal, bestemt, ikke-ejefald',
                'example': 'Alle [bordene] er væk.',
                'grammatical_features_item_ids': [plural, definite, non_genitive],
            },
            {
                'label': 'ental,  ubestemt, ejefald',
                'example': 'Her er et [bords] ejer.',
                'grammatical_features_item_ids': [singular, indefinite, genitive_case],
            },
            {
                'label': 'ental, bestemt, ejefald',
                'example': 'Nu er [bordets] ejer gået.',
                'grammatical_features_item_ids': [singular, definite, genitive_case],
            },
            {
                'label': 'flertal, ubestemt, ejefald',
                'example': 'Jeg skriver til flere [bordes] ejere.',
                'grammatical_features_item_ids': [plural, indefinite, genitive_case],
            },
            {
                'label': 'flertal, bestemt, ejefald',
                'example': 'Alle [bordenes] ejere er gået.',
                'grammatical_features_item_ids': [plural, definite, genitive_case],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'danish-verb': {
        '@attribution': {'users': ['So9q'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk verb',
        'language': language_Danish,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'infinitiv aktiv (navnemåde)',
                'example': 'At [læse] er godt.',
                'grammatical_features_item_ids': [infinitive, active],
            },
            {
                'label': 'presens aktiv (nutid)',
                'example': 'Hun [læser] hver dag.',
                'grammatical_features_item_ids': [present_tense, active],
            },
            {
                'label': 'preteritum aktiv (datid)',
                'example': 'Hun [læste] i går.',
                'grammatical_features_item_ids': [preterite, active],
            },
            {
                'label': 'præteritum participium (kort tillægsform)',
                'example': 'Hen har [læst] hele dagen.',
                'grammatical_features_item_ids': [past_participle],
            },
            {
                'label': 'imperativ (bydeform, bydemåde)',
                'example': '[læs] nu!',
                'grammatical_features_item_ids': [imperative],
            },
            {
                'label': 'infinitiv passiv (infinitiv lideform)',
                'example': 'Det kan [læses] hver dag.',
                'grammatical_features_item_ids': [infinitive, passive],
            },
            {
                'label': 'presens passiv (nutid lideform)',
                'example': 'Det [læses] hver dag.',
                'grammatical_features_item_ids': [present_tense, passive],
            },
            {
                'label': 'preteritum passiv (datid lideform)',
                'example': 'Det [læstes] i går.',
                'grammatical_features_item_ids': [preterite, passive],
            },
            {
                'label': 'præsens participium (lang tillægsform)',
                'example': 'Sikke meget [læsende] det blev i dag.',
                'grammatical_features_item_ids': [present_participle],
            },
        ],
    },

    'danish-adjective': {
        '@attribution': {'users': ['Fnielsen', 'So9q'], 'title': 'Wikidata:Wikidata Lexeme Forms/Danish'},
        'label': 'dansk adjektiv',
        'language': language_Danish,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'ubestemt ental fælleskøn 1. grad',
                'example': 'en [høj] dreng',
                'grammatical_features_item_ids': [indefinite, singular, common, positive],
            },
            {
                'label': 'ubestemt ental intetkøn 1. grad',
                'example': 'et [højt] barn',
                'grammatical_features_item_ids': [indefinite, singular, neuter, positive],
            },
            {
                'label': 'bestemt ental 1. grad',
                'example': 'den [høje] dreng',
                'grammatical_features_item_ids': [definite, singular, positive],
            },
            {
                'label': 'flertal 1. grad',
                'example': 'de [høje] børn',
                'grammatical_features_item_ids': [plural, positive],
            },
            {
                'label': '2. grad',
                'example': 'det [højere] barn',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'ubestemt 3. grad',
                'example': 'dit barn er [højest]',
                'grammatical_features_item_ids': [indefinite, superlative],
            },
            {
                'label': 'bestemt 3. grad',
                'example': 'de [højeste] børn',
                'grammatical_features_item_ids': [definite, superlative],
            },
        ],
    },

    'german-noun-masculine': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Maskulinum)',
        'language': language_German,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist ein [Hund].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum eines [Hunds/Hundes].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört einem [Hund/Hunde].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag einen [Hund].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind mehrere [Hunde].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum mehrerer [Hunde].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört mehreren [Hunden].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag mehrere [Hunde].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'german-noun-feminine': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Femininum)',
        'language': language_German,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist eine [Katze].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum einer [Katze].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört einer [Katze].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag eine [Katze].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind mehrere [Katzen].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum mehrerer [Katzen].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört mehreren [Katzen].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag mehrere [Katzen].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'german-noun-neuter': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Neutrum)',
        'language': language_German,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das ist ein [Kind].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Das Eigentum eines [Kindes/Kinds].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'Dativ Singular',
                'example': 'Das gehört einem [Kind/Kinde].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Ich mag ein [Kind].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind mehrere [Kinder].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum mehrerer [Kinder].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört mehreren [Kindern].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag mehrere [Kinder].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'german-noun-neuter-toponym': {
        '@attribution': {'users': ['Lucas Werkmeister', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Neutrum, Toponym)',
        'language': language_German,
        'lexical_category_item_id': proper_noun,
        'forms': [
            {
                'label': 'Nominativ Singular',
                'example': 'Das heutige [Berlin].',
                'grammatical_features_item_ids': [nominative_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'Genitiv Singular',
                'example': 'Fotos des damaligen [Berlins/Berlin].',
                'grammatical_features_item_ids': [genitive_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'Dativ Singular',
                'example': 'Fotos vom damaligen [Berlin].',
                'grammatical_features_item_ids': [dative_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'Akkusativ Singular',
                'example': 'Pläne für das zukünftige [Berlin].',
                'grammatical_features_item_ids': [accusative_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, neuter),
            ],
            instance_of: [
                statement(instance_of, singulare_tantum),
                statement(instance_of, toponym),
            ],
        },
    },

    'german-noun-pluraletantum': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Substantiv (Pluraletantum, kein Genus)',
        'language': language_German,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'Nominativ Plural',
                'example': 'Das sind die [Großeltern].',
                'grammatical_features_item_ids': [nominative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'Genitiv Plural',
                'example': 'Das Eigentum der [Großeltern].',
                'grammatical_features_item_ids': [genitive_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'Dativ Plural',
                'example': 'Das gehört den [Großeltern].',
                'grammatical_features_item_ids': [dative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'Akkusativ Plural',
                'example': 'Ich mag die [Großeltern].',
                'grammatical_features_item_ids': [accusative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
        ],
        'statements': statements(instance_of, plurale_tantum),
    },

    'german-verb': {
        '@attribution': {'users': ['Lucas Werkmeister', 'Andreasmperu', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Verb',
        'language': language_German,
        'lexical_category_item_id': verb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Infinitiv',
                'example': '[tragen]',
                'grammatical_features_item_ids': [infinitive],
            },
            {
                'label': 'Infinitiv mit zu',
                'example': 'Es ist gut, [zu tragen].',
                'grammatical_features_item_ids': [zu_infinitive],
            },
            {
                'section_break': True,
                'label': '1. Person Singular Präsens',
                'example': 'Ich [trage] heute.',
                'grammatical_features_item_ids': [first_person, singular, indicative, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '2. Person Singular Präsens',
                'example': 'Du [trägst] heute.',
                'grammatical_features_item_ids': [second_person, singular, indicative, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '3. Person Singular Präsens',
                'example': 'Er/sie/es [trägt] heute.',
                'grammatical_features_item_ids': [third_person, singular, indicative, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '1. Person Plural Präsens',
                'example': 'Wir [tragen] heute.',
                'grammatical_features_item_ids': [first_person, plural, indicative, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '2. Person Plural Präsens',
                'example': 'Ihr [tragt] heute.',
                'grammatical_features_item_ids': [second_person, plural, indicative, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '3. Person Plural Präsens',
                'example': 'Sie [tragen] heute.',
                'grammatical_features_item_ids': [third_person, plural, indicative, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'section_break': True,
                'label': '1. Person Singular Präteritum',
                'example': 'Ich [trug] gestern.',
                'grammatical_features_item_ids': [first_person, singular, indicative, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '2. Person Singular Präteritum',
                'example': 'Du [trugst] gestern.',
                'grammatical_features_item_ids': [second_person, singular, indicative, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '3. Person Singular Präteritum',
                'example': 'Er/sie/es [trug] gestern.',
                'grammatical_features_item_ids': [third_person, singular, indicative, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '1. Person Plural Präteritum',
                'example': 'Wir [trugen] gestern.',
                'grammatical_features_item_ids': [first_person, plural, indicative, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '2. Person Plural Präteritum',
                'example': 'Ihr [trugt] gestern.',
                'grammatical_features_item_ids': [second_person, plural, indicative, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '3. Person Plural Präteritum',
                'example': 'Sie [trugen] gestern.',
                'grammatical_features_item_ids': [third_person, plural, indicative, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'section_break': True,
                'label': '1. Person Singular Konjunktiv I',
                'example': 'Angenommen, ich [trage].',
                'grammatical_features_item_ids': [first_person, singular, subjunctive_I, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '2. Person Singular Konjunktiv I',
                'example': 'Angenommen, du [tragest].',
                'grammatical_features_item_ids': [second_person, singular, subjunctive_I, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '3. Person Singular Konjunktiv I',
                'example': 'Angenommen, er/sie/es [trage].',
                'grammatical_features_item_ids': [third_person, singular, subjunctive_I, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '1. Person Plural Konjunktiv I',
                'example': 'Angenommen, wir [tragen].',
                'grammatical_features_item_ids': [first_person, plural, subjunctive_I, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '2. Person Plural Konjunktiv I',
                'example': 'Angenommen, ihr [traget].',
                'grammatical_features_item_ids': [second_person, plural, subjunctive_I, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '3. Person Plural Konjunktiv I',
                'example': 'Angenommen, sie [tragen].',
                'grammatical_features_item_ids': [third_person, plural, subjunctive_I, present_tense, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'section_break': True,
                'label': '1. Person Singular Konjunktiv II',
                'example': 'Ich dachte, ich [trüge].',
                'grammatical_features_item_ids': [first_person, singular, subjunctive_II, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '2. Person Singular Konjunktiv II',
                'example': 'Ich dachte, du [trügest/trügst].',
                'grammatical_features_item_ids': [second_person, singular, subjunctive_II, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '3. Person Singular Konjunktiv II',
                'example': 'Ich dachte, er/sie/es [trüge].',
                'grammatical_features_item_ids': [third_person, singular, subjunctive_II, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '1. Person Plural Konjunktiv II',
                'example': 'Ich dachte, wir [trügen].',
                'grammatical_features_item_ids': [first_person, plural, subjunctive_II, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '2. Person Plural Konjunktiv II',
                'example': 'Ich dachte, ihr [trüget/trügt].',
                'grammatical_features_item_ids': [second_person, plural, subjunctive_II, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'label': '3. Person Plural Konjunktiv II',
                'example': 'Ich dachte, sie [trügen].',
                'grammatical_features_item_ids': [third_person, plural, subjunctive_II, preterite, active],
                'grammatical_features_item_ids_optional': set([active]),
            },
            {
                'section_break': True,
                'label': '2. Person Singular Imperativ',
                'example': 'He du da, [trag/trage]!',
                'grammatical_features_item_ids': [second_person, singular, imperative, present_tense, active],
                'grammatical_features_item_ids_optional': set([active, present_tense]),
            },
            {
                'label': '2. Person Plural Imperativ',
                'example': 'He ihr da, [tragt]!',
                'grammatical_features_item_ids': [second_person, plural, imperative, present_tense, active],
                'grammatical_features_item_ids_optional': set([active, present_tense]),
            },
            {
                'section_break': True,
                'label': 'Partizip I',
                'example': 'Es ging vorbei, etwas [tragend].',
                'grammatical_features_item_ids': [present_participle],
            },
            {
                'label': 'Partizip II',
                'example': 'Ich werde [getragen].',
                'grammatical_features_item_ids': [past_participle],
            },
        ],
    },

    'german-adverb': {
        '@attribution': {'users': ['Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/German'},
        'label': 'deutsches Adverb',
        'language': language_German,
        'lexical_category_item_id': adverb,
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
        'language': language_English,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singular',
                'example': 'This is the [dog].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'plural',
                'example': 'These are the [dogs].',
                'grammatical_features_item_ids': [plural],
            },
        ],
    },

    'english-adverb': {
        '@attribution': {'users': ['ArthurPSmith'], 'title': 'Wikidata:Wikidata Lexeme Forms/English'},
        'label': 'English adverb',
        'language': language_English,
        'lexical_category_item_id': adverb,
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
        'language': language_English,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'positive',
                'example': 'This is a [good] dog.',
                'grammatical_features_item_ids': [positive],
            },
            {
                'label': 'comparative',
                'example': 'This is a [better] dog than yours.',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'superlative',
                'example': 'This is the [best] dog I\'ve ever seen.',
                'grammatical_features_item_ids': [superlative],
            },
        ],
    },

    'english-verb': {
        '@attribution': {'users': ['ArthurPSmith', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/English'},
        'label': 'English verb',
        'language': language_English,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'present',
                'example': 'They [sing] every day.',
                'grammatical_features_item_ids': [simple_present],
            },
            {
                'label': 'third-person singular',
                'example': 'He [sings] every day.',
                'grammatical_features_item_ids': [simple_present, third_person, singular],
            },
            {
                'label': 'simple past',
                'example': 'He [sang] every day last week.',
                'grammatical_features_item_ids': [simple_past],
            },
            {
                'label': 'present participle',
                'example': 'They are [singing] right now.',
                'grammatical_features_item_ids': [present_participle],
            },
            {
                'label': 'past participle',
                'example': 'We have [sung] for hours.',
                'grammatical_features_item_ids': [past_participle_in_English],
            },
        ],
    },

    'esperanto-noun': {
        '@attribution': {'users': ['KaMan', 'Jens Ohlig'], 'title': 'Wikidata:Wikidata Lexeme Forms/Esperanto'},
        'label': 'esperanta substantivo',
        'language': language_Esperanto,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ununombro, nominativo',
                'example': 'Ĉi tio estas [substantivo].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'ununombro, akuzativo',
                'example': 'Mi ŝatas tiun [substantivon].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'multenombro, nominativo',
                'example': 'Ĉi tiuj estas [substantivoj].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'multenombro, akuzativo',
                'example': 'Mi ŝatas tiujn [substantivojn].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
        ],
    },

    'esperanto-adjective': {
        '@attribution': {'users': ['Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Esperanto'},
        'label': 'esperanta adjektivo',
        'language': language_Esperanto,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ununombro, nominativo',
                'example': 'Ĉi tio estas [esperanta] vorto.',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'ununombro, akuzativo',
                'example': 'Mi ŝatas [esperantan] vorton.',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'multenombro, nominativo',
                'example': 'Ĉi tiuj estas [esperantaj] vortoj.',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'multenombro, akuzativo',
                'example': 'Mi ŝatas [esperantajn] vortojn.',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
        ],
    },

    'esperanto-verb': {
        '@attribution': {'users': ['Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Esperanto'},
        'label': 'esperanta verbo',
        'language': language_Esperanto,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'infinitivo',
                'example': 'Ili volas [dormi].',
                'grammatical_features_item_ids': [infinitive],
            },
            {
                'section_break': True,
                'label': 'indikativo, prezenco',
                'example': 'Ili nun [dormas].',
                'grammatical_features_item_ids': [indicative, present_tense],
                'grammatical_features_item_ids_optional': set([indicative]),
            },
            {
                'label': 'indikativo, preterito',
                'example': 'Ili [dormis] hieraŭ.',
                'grammatical_features_item_ids': [indicative, past_tense],
                'grammatical_features_item_ids_optional': set([indicative]),
            },
            {
                'label': 'indikativo, futuro',
                'example': 'Ili [dormos] morgaŭ.',
                'grammatical_features_item_ids': [indicative, future_tense],
                'grammatical_features_item_ids_optional': set([indicative]),
            },
            {
                'section_break': True,
                'label': 'kondicionalo',
                'example': 'Estus bone, se ili [dormus].',
                'grammatical_features_item_ids': [conditional],
            },
            {
                'label': 'volitivo',
                'example': 'Ne [dormu]!',
                'grammatical_features_item_ids': [volitive],
            },
        ],
    },

    'spanish-noun-masculine': {
        '@attribution': {'users': ['Andreasmperu', 'Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'sustantivo masculino en español',
        'language': language_Spanish,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singular',
                'example': 'Este es un [libro].',
                'grammatical_features_item_ids': [singular, masculine],
            },
            {
                'label': 'plural',
                'example': 'Estos son unos [libros].',
                'grammatical_features_item_ids': [plural, masculine],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'spanish-noun-feminine': {
        '@attribution': {'users': ['Andreasmperu', 'Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'sustantivo femenino en español',
        'language': language_Spanish,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singular',
                'example': 'Esta es una [manzana].',
                'grammatical_features_item_ids': [singular, feminine],
            },
            {
                'label': 'plural',
                'example': 'Estas son unas [manzanas].',
                'grammatical_features_item_ids': [plural, feminine],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'spanish-noun-masculine-feminine': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'sustantivo masculino y femenino en español',
        'language': language_Spanish,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'masculino singular',
                'example': 'Ese [poeta] es bueno.',
                'grammatical_features_item_ids': [masculine, singular],
            },
            {
                'label': 'masculino plural',
                'example': 'Esos [poetas] son buenos.',
                'grammatical_features_item_ids': [masculine, plural],
            },
            {
                'label': 'femenino singular',
                'example': 'Esa [poetisa] es buena.',
                'grammatical_features_item_ids': [feminine, singular],
            },
            {
                'label': 'femenino plural',
                'example': 'Esas [poetisas] son buenas.',
                'grammatical_features_item_ids': [feminine, plural],
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, masculine),
                statement(grammatical_gender, feminine),
            ],
        },
    },

    'spanish-adjective': {
        '@attribution': {'users': ['Andreasmperu'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'adjetivo en español',
        'language': language_Spanish,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'masculino singular',
                'example': 'Un pantalón [negro].',
                'grammatical_features_item_ids': [masculine, singular],
            },
            {
                'label': 'masculino plural',
                'example': 'Unos pantalones [negros].',
                'grammatical_features_item_ids': [masculine, plural],
            },
            {
                'label': 'femenino singular',
                'example': 'Una falda [negra].',
                'grammatical_features_item_ids': [feminine, singular],
            },
            {
                'label': 'femenino plural',
                'example': 'Unas faldas [negras].',
                'grammatical_features_item_ids': [feminine, plural],
            },
        ],
    },

    'spanish-verb': {
        '@attribution': {'users': ['DemonDays64', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'verbo en español',
        'language': language_Spanish,
        'lexical_category_item_id': verb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'infinitivo',
                'example': 'Quieres [cantar].',
                'grammatical_features_item_ids': [infinitive],
            },
            {
                'section_break': True,
                'label': 'primera persona singular presente',
                'example': 'Yo [canto] todos los días.',
                'grammatical_features_item_ids': [present_tense, indicative, first_person, singular],
            },
            {
                'label': 'segunda persona singular presente',
                'example': 'Tú [cantas] todos los días.',
                'grammatical_features_item_ids': [present_tense, indicative, second_person, singular],
            },
            {
                'label': 'segunda persona (vos) singular presente',
                'example': 'Vos [cantás] todos los días.',
                'grammatical_features_item_ids': [present_tense, indicative, second_person, singular, voseo],
            },
            {
                'label': 'tercera persona singular presente',
                'example': 'Él [canta] todos los días.',
                'grammatical_features_item_ids': [present_tense, indicative, third_person, singular],
            },
            {
                'label': 'primera persona plural presente',
                'example': 'Nosotros [cantamos] todos los días.',
                'grammatical_features_item_ids': [present_tense, indicative, first_person, plural],
            },
            {
                'label': 'segunda persona plural presente',
                'example': 'Vosotros [cantáis] todos los días.',
                'grammatical_features_item_ids': [present_tense, indicative, second_person, plural],
            },
            {
                'label': 'tercera persona plural presente',
                'example': 'Ellos [cantan] todos los días.',
                'grammatical_features_item_ids': [present_tense, indicative, third_person, plural],
            },
            {
                'section_break': True,
                'label': 'primera persona singular pretérito',
                'example': 'Yo [canté] mucho durante la semana pasada.',
                'grammatical_features_item_ids': [preterite, first_person, singular, indicative],
            },
            {
                'label': 'segunda persona singular pretérito',
                'example': 'Tú [cantaste] mucho durante la semana pasada.',
                'grammatical_features_item_ids': [preterite, second_person, singular, indicative],
            },
            {
                'label': 'tercera persona singular pretérito',
                'example': 'Él [cantó] mucho durante la semana pasada.',
                'grammatical_features_item_ids': [preterite, third_person, singular, indicative],
            },
            {
                'label': 'primera persona plural pretérito',
                'example': 'Nosotros [cantamos] mucho durante la semana pasada.',
                'grammatical_features_item_ids': [preterite, first_person, plural, indicative],
            },
            {
                'label': 'segunda persona plural pretérito',
                'example': 'Vosotros [cantasteis] mucho durante la semana pasada.',
                'grammatical_features_item_ids': [preterite, second_person, plural, indicative],
            },
            {
                'label': 'tercera persona plural pretérito',
                'example': 'Ellos [cantaron] mucho durante la semana pasada.',
                'grammatical_features_item_ids': [preterite, third_person, plural, indicative],
            },
            {
                'section_break': True,
                'label': 'primera persona singular pretérito imperfecto',
                'example': 'Yo [cantaba] mucho cuándo era niño.',
                'grammatical_features_item_ids': [past_imperfect, first_person, singular],
            },
            {
                'label': 'segunda persona singular pretérito imprefecto',
                'example': 'Tú [cantabas] mucho cuándo eras niño.',
                'grammatical_features_item_ids': [past_imperfect, second_person, singular],
            },
            {
                'label': 'tercera persona singular pretérito imperfecto',
                'example': 'Él [cantaba] mucho cuándo era niño.',
                'grammatical_features_item_ids': [past_imperfect, third_person, singular],
            },
            {
                'label': 'primera persona plural pretérito imperfecto',
                'example': 'Nosotros [cantábamos] mucho cuándo éramos niños.',
                'grammatical_features_item_ids': [past_imperfect, first_person, plural],
            },
            {
                'label': 'segunda persona plural pretérito imperfecto',
                'example': 'Vosotros [cantabais] mucho cuándo erais niños.',
                'grammatical_features_item_ids': [past_imperfect, second_person, plural],
            },
            {
                'label': 'tercera persona plural pretérito imperfecto',
                'example': 'Ellos [cantaban] mucho cuándo eran niños.',
                'grammatical_features_item_ids': [past_imperfect, third_person, plural],
            },
            {
                'section_break': True,
                'label': 'gerundio',
                'example': 'Estoy [cantando].',
                'grammatical_features_item_ids': [gerund],
            },
            {
                'section_break': True,
                'label': 'participio masculino singular',
                'example': 'Yo he [cantado].',
                'grammatical_features_item_ids': [participle, masculine, singular],
            },
            {
                'label': 'participio masculino plural',
                'example': 'Esos fueron [cantados].',
                'grammatical_features_item_ids': [participle, masculine, plural],
            },
            {
                'label': 'participio femenino singular',
                'example': 'Esa fue [cantada].',
                'grammatical_features_item_ids': [participle, feminine, singular],
            },
            {
                'label': 'participio femenino plural',
                'example': 'Esas fueron [cantadas].',
                'grammatical_features_item_ids': [participle, feminine, plural],
            },
            {
                'section_break': True,
                'label': 'primera persona singular del futuro',
                'example': 'Yo [cantaré] mañana.',
                'grammatical_features_item_ids': [first_person, singular, future_tense, indicative],
            },
            {
                'label': 'segunda persona singular del futuro',
                'example': 'Tú [cantarás] mañana.',
                'grammatical_features_item_ids': [second_person, singular, future_tense, indicative],
            },
            {
                'label': 'tercera persona singular del futuro',
                'example': 'Él [cantará] mañana.',
                'grammatical_features_item_ids': [third_person, singular, future_tense, indicative],
            },
            {
                'label': 'primera persona plural del futuro',
                'example': 'Nosotros [cantaremos] mañana.',
                'grammatical_features_item_ids': [first_person, plural, future_tense, indicative],
            },
            {
                'label': 'segunda persona plural del futuro',
                'example': 'Vosotros [cantaréis] mañana.',
                'grammatical_features_item_ids': [second_person, plural, future_tense, indicative],
            },
            {
                'label': 'tercera persona plural del futuro',
                'example': 'Ellos [cantarán] mañana.',
                'grammatical_features_item_ids': [third_person, plural, future_tense, indicative],
            },
            {
                'section_break': True,
                'label': 'primera persona singular del condicional',
                'example': 'Yo [cantaría] si pudiera.',
                'grammatical_features_item_ids': [first_person, singular, simple_conditional, indicative],
            },
            {
                'label': 'segunda persona singular del condicional',
                'example': 'Tú [cantarías] si pudieras.',
                'grammatical_features_item_ids': [second_person, singular, simple_conditional, indicative],
            },
            {
                'label': 'tercera persona singular del condicional',
                'example': 'Él [cantaría] si pudiera.',
                'grammatical_features_item_ids': [third_person, singular, simple_conditional, indicative],
            },
            {
                'label': 'primera persona plural del condicional',
                'example': 'Nosotros [cantaríamos] si pudiéramos.',
                'grammatical_features_item_ids': [first_person, plural, simple_conditional, indicative],
            },
            {
                'label': 'segunda persona plural del condicional',
                'example': 'Vosotros [cantaríais] si pudierais.',
                'grammatical_features_item_ids': [second_person, plural, simple_conditional, indicative],
            },
            {
                'label': 'tercera persona plural del condicional',
                'example': 'Ellos [cantarían] si pudieran.',
                'grammatical_features_item_ids': [third_person, plural, simple_conditional, indicative],
            },
            {
                'section_break': True,
                'label': 'primera persona singular del presente de subjuntivo',
                'example': 'Para que yo [cante].',
                'grammatical_features_item_ids': [first_person, singular, present_subjunctive],
            },
            {
                'label': 'segunda persona singular del presente de subjuntivo',
                'example': 'Para que tú [cantes].',
                'grammatical_features_item_ids': [second_person, singular, present_subjunctive],
            },
            {
                'label': 'segunda persona (vos) singular del presente de subjuntivo',
                'example': 'Para que vos [cantés].',
                'grammatical_features_item_ids': [second_person, singular, present_subjunctive, voseo],
            },
            {
                'label': 'tercera persona singular del presente de subjuntivo',
                'example': 'Para que él [cante].',
                'grammatical_features_item_ids': [third_person, singular, present_subjunctive],
            },
            {
                'label': 'primera persona plural del presente de subjuntivo',
                'example': 'Para que nosotros [cantemos].',
                'grammatical_features_item_ids': [first_person, plural, present_subjunctive],
            },
            {
                'label': 'segunda persona plural del presente de subjuntivo',
                'example': 'Para que vosotros [cantéis].',
                'grammatical_features_item_ids': [second_person, plural, present_subjunctive],
            },
            {
                'label': 'tercera persona plural del presente de subjuntivo',
                'example': 'Para que ellos [canten].',
                'grammatical_features_item_ids': [third_person, plural, present_subjunctive],
            },
            {
                'label': 'primera persona singular del pretérito imperfecto de subjuntivo',
                'example': 'Para que yo [cantara/cantase].',
                'grammatical_features_item_ids': [first_person, singular, imperfect_subjunctive],
            },
            {
                'label': 'segunda persona singular del pretérito imperfecto de subjuntivo',
                'example': 'Para que tú [cantaras/cantases].',
                'grammatical_features_item_ids': [second_person, singular, imperfect_subjunctive],
            },
            {
                'label': 'tercera persona singular del pretérito imperfecto de subjuntivo',
                'example': 'Para que él [cantara/cantase].',
                'grammatical_features_item_ids': [third_person, singular, imperfect_subjunctive],
            },
            {
                'label': 'primera persona plural del pretérito imperfecto de subjuntivo',
                'example': 'Para que nosotros [cantáramos/cantásemos].',
                'grammatical_features_item_ids': [first_person, plural, imperfect_subjunctive],
            },
            {
                'label': 'segunda persona plural del pretérito imperfecto de subjuntivo',
                'example': 'Para que vosotros [cantarais/cantaseis].',
                'grammatical_features_item_ids': [second_person, plural, imperfect_subjunctive],
            },
            {
                'label': 'tercera persona plural del pretérito imperfecto de subjuntivo',
                'example': 'Para que ellos [cantaran/cantasen].',
                'grammatical_features_item_ids': [third_person, plural, imperfect_subjunctive],
            },
            {
                'section_break': True,
                'label': 'primera persona singular del futuro de subjuntivo',
                'example': 'Para que yo [cantare] mañana.',
                'grammatical_features_item_ids': [first_person, singular, future_tense, subjunctive],
            },
            {
                'label': 'segunda persona singular del futuro de subjuntivo',
                'example': 'Para que tú [cantares] mañana.',
                'grammatical_features_item_ids': [second_person, singular, future_tense, subjunctive],
            },
            {
                'label': 'tercera persona singular del futuro de subjuntivo',
                'example': 'Para que él [cantare] mañana.',
                'grammatical_features_item_ids': [third_person, singular, future_tense, subjunctive],
            },
            {
                'label': 'primera persona plural del futuro de subjuntivo',
                'example': 'Para que nosotros [cantáremos] mañana.',
                'grammatical_features_item_ids': [first_person, plural, future_tense, subjunctive],
            },
            {
                'label': 'segunda persona plural del futuro de subjuntivo',
                'example': 'Para que vosotros [cantareis] mañana.',
                'grammatical_features_item_ids': [second_person, plural, future_tense, subjunctive],
            },
            {
                'label': 'tercera persona plural del futuro de subjuntivo',
                'example': 'Para que ellos [cantaren] mañana.',
                'grammatical_features_item_ids': [third_person, plural, future_tense, subjunctive],
            },
            {
                'section_break': True,
                'label': 'segunda persona singular del imperativo',
                'example': 'Por favor, [canta] tú.',
                'grammatical_features_item_ids': [second_person, singular, imperative],
            },
            {
                'label': 'segunda persona singular del imperativo',
                'example': 'Por favor, [cantá] vos.',
                'grammatical_features_item_ids': [second_person, singular, imperative, voseo],
            },
            {
                'label': 'segunda persona singular del imperativo',
                'example': 'Por favor, [cante] usted.',
                'grammatical_features_item_ids': [second_person, singular, imperative, ustedeo],
            },
            {
                'label': 'primera persona plural del imperativo',
                'example': 'Por favor, [cantemos] nosotros.',
                'grammatical_features_item_ids': [first_person, plural, imperative],
            },
            {
                'label': 'segunda persona plural del imperativo',
                'example': 'Por favor, [cantad] vosotros.',
                'grammatical_features_item_ids': [second_person, plural, imperative],
            },
            {
                'label': 'segunda persona plural del imperativo',
                'example': 'Por favor, [canten] ustedes.',
                'grammatical_features_item_ids': [second_person, plural, imperative, ustedeo],
            },
        ],
    },

    'spanish-adverb': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'adverbio en español',
        'language': language_Spanish,
        'lexical_category_item_id': adverb,
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
        'language': language_Spanish,
        'lexical_category_item_id': interjection,
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
        'language': language_Spanish,
        'lexical_category_item_id': nominal_locution,
        'forms': [
            {
                'label': 'singular',
                'example': 'Lo importante es el [santo y seña].',
                'grammatical_features_item_ids': [singular, masculine],
            },
            {
                'label': 'plural',
                'example': 'Lo importante son los [santos y señas].',
                'grammatical_features_item_ids': [plural, masculine],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'spanish-phrase-nominal-feminine': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución sustantiva femenina en español',
        'language': language_Spanish,
        'lexical_category_item_id': nominal_locution,
        'forms': [
            {
                'label': 'singular',
                'example': 'Lo importante es la [caja de caudales].',
                'grammatical_features_item_ids': [singular, feminine],
            },
            {
                'label': 'plural',
                'example': 'Lo importante son las [cajas de caudales].',
                'grammatical_features_item_ids': [plural, feminine],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'spanish-phrase-attributive': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución adjetiva en español',
        'language': language_Spanish,
        'lexical_category_item_id': attributive_locution,
        'forms': [
            {
                'label': 'masculino singular',
                'example': 'Eso está [sano y salvo].',
                'grammatical_features_item_ids': [singular, masculine],
            },
            {
                'label': 'masculino plural',
                'example': 'Esos están [sanos y salvos].',
                'grammatical_features_item_ids': [plural, masculine],
            },
            {
                'label': 'femenino singular',
                'example': 'Esa está [sana y salva].',
                'grammatical_features_item_ids': [singular, feminine],
            },
            {
                'label': 'femenino plural',
                'example': 'Esas están [sanas y salvas].',
                'grammatical_features_item_ids': [plural, feminine],
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, masculine),
                statement(grammatical_gender, feminine),
            ],
        },
    },

    'spanish-locution-prepositional': {
        '@attribution': {'users': ['Hameryko'], 'title': 'Wikidata:Wikidata Lexeme Forms/Spanish'},
        'label': 'locución preposicional en español',
        'language': language_Spanish,
        'lexical_category_item_id': prepositional_locution,
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
        'language': language_Spanish,
        'lexical_category_item_id': interjectional_locution,
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
        'language': language_Spanish,
        'lexical_category_item_id': adverbial_locution,
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
        'language': language_Estonian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ainsuse nimetav',
                'example': 'See [auto].',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'mitmuse nimetav',
                'example': 'Need [autod].',
                'grammatical_features_item_ids': [plural, nominative_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse omastav',
                'example': 'Selle [auto].',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'mitmuse omastav',
                'example': 'Nende [autode].',
                'grammatical_features_item_ids': [plural, genitive_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse osastav',
                'example': 'Seda [autot].',
                'grammatical_features_item_ids': [singular, partitive_case],
            },
            {
                'label': 'mitmuse osastav',
                'example': 'Neid [autosid].',
                'grammatical_features_item_ids': [plural, partitive_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse sisseütlev',
                'example': 'Sellesse [autosse].',
                'grammatical_features_item_ids': [singular, illative_case],
            },
            {
                'label': 'mitmuse sisseütlev',
                'example': 'Nendesse [autodesse].',
                'grammatical_features_item_ids': [plural, illative_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse seesütlev',
                'example': 'Selles [autos].',
                'grammatical_features_item_ids': [singular, inessive_case],
            },
            {
                'label': 'mitmuse seesütlev',
                'example': 'Nendes [autodes].',
                'grammatical_features_item_ids': [plural, inessive_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse seestütlev',
                'example': 'Sellest [autost].',
                'grammatical_features_item_ids': [singular, elative_case],
            },
            {
                'label': 'mitmuse seestütlev',
                'example': 'Nendest [autodest].',
                'grammatical_features_item_ids': [plural, elative_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse alaleütlev',
                'example': 'Sellele [autole].',
                'grammatical_features_item_ids': [singular, allative_case],
            },
            {
                'label': 'mitmuse alaleütlev',
                'example': 'Nendele [autodele].',
                'grammatical_features_item_ids': [plural, allative_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse alalütlev',
                'example': 'Sellel [autol].',
                'grammatical_features_item_ids': [singular, adessive_case],
            },
            {
                'label': 'mitmuse alalütlev',
                'example': 'Nendel [autodel].',
                'grammatical_features_item_ids': [plural, adessive_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse alaltütlev',
                'example': 'Sellelt [autolt].',
                'grammatical_features_item_ids': [singular, ablative_case],
            },
            {
                'label': 'mitmuse alaltütlev',
                'example': 'Nendelt [autodelt].',
                'grammatical_features_item_ids': [plural, ablative_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse saav',
                'example': 'Selleks [autoks].',
                'grammatical_features_item_ids': [singular, translative_case],
            },
            {
                'label': 'mitmuse saav',
                'example': 'Nendeks [autodeks].',
                'grammatical_features_item_ids': [plural, translative_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse rajav',
                'example': 'Selle [autoni].',
                'grammatical_features_item_ids': [singular, terminative_case],
            },
            {
                'label': 'mitmuse rajav',
                'example': 'Nende [autodeni].',
                'grammatical_features_item_ids': [plural, terminative_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse olev',
                'example': 'Selle [autona].',
                'grammatical_features_item_ids': [singular, essive_case],
            },
            {
                'label': 'mitmuse olev',
                'example': 'Nende [autodena].',
                'grammatical_features_item_ids': [plural, essive_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse ilmaütlev',
                'example': 'Selle [autota].',
                'grammatical_features_item_ids': [singular, abessive_case],
            },
            {
                'label': 'mitmuse ilmaütlev',
                'example': 'Nende [autodeta].',
                'grammatical_features_item_ids': [plural, abessive_case],
            },
            {
                'section_break': True,
                'label': 'ainsuse kaasaütlev',
                'example': 'Selle [autoga].',
                'grammatical_features_item_ids': [singular, comitative_case],
            },
            {
                'label': 'mitmuse kaasaütlev',
                'example': 'Nende [autodega].',
                'grammatical_features_item_ids': [plural, comitative_case],
            },
        ],
    },

    'basque-verb': {
        '@attribution': {'users': ['Theklan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Basque'},
        'label': 'euskal aditza',
        'language': language_Basque,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'partizipioa',
                'example': 'liburu bat [erosi] dut',
                'grammatical_features_item_ids': [participle],
            },
            {
                'label': 'aditzoina',
                'example': 'liburu bat [eros] nezake',
                'grammatical_features_item_ids': ['Q74674702'],
            },
            {
                'label': 'aditz izena',
                'example': 'liburu bat [erostea] pentsatu dut',
                'grammatical_features_item_ids': [nominalized_verb],
            },
            {
                'label': 'gerundioa',
                'example': 'liburu bat [erosten] ari naiz',
                'grammatical_features_item_ids': [gerund, imperfective_verb],
            },
            {
                'label': 'etorkizuneko forma',
                'example': 'liburu bat [erosiko] dut',
                'grammatical_features_item_ids': [future_tense],
            },
        ],
    },

    'basque-adjective-comparative': {
        '@attribution': {'users': ['Theklan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Basque'},
        'label': 'euskal adjektibo konparatibo eta superlatiboak',
        'language': language_Basque,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'oina',
                'example': '[gorri]',
                'grammatical_features_item_ids': [absolutive_case, indefinite_number],
            },
            {
                'label': 'konparatiboa',
                'example': '[gorriago]',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'superlatiboa',
                'example': '[gorrien]',
                'grammatical_features_item_ids': [superlative],
            },
        ],
    },

    'persian-noun': {
        '@attribution': {'users': ['Ladsgroup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Persian'},
        'label': 'اسم فارسی',
        'language': language_Persian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'مفرد',
                'example': '[سگ] غذا می‌خورد.',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'جمع',
                'example': '[سگ‌ها] غذا می‌خورند.',
                'grammatical_features_item_ids': [plural],
            },
        ],
    },

    'persian-verb': {
        '@attribution': {'users': ['Ladsgroup'], 'title': 'Wikidata:Wikidata Lexeme Forms/Persian'},
        'label': 'فعل فارسی',
        'language': language_Persian,
        'lexical_category_item_id': verb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'اول شخص مفرد',
                'example': 'من [می‌روم].',
                'grammatical_features_item_ids': [first_person, singular],
            },
            {
                'label': 'دوم شخص مفرد',
                'example': 'تو [می‌روی].',
                'grammatical_features_item_ids': [second_person, singular],
            },
            {
                'label': 'سوم شخص مفرد',
                'example': 'او [می‌رود].',
                'grammatical_features_item_ids': [third_person, singular],
            },
            {
                'label': 'اول شخص جمع',
                'example': 'ما [می‌رویم].',
                'grammatical_features_item_ids': [first_person, plural],
            },
            {
                'label': 'دوم شخص جمع',
                'example': 'شما [می‌روید].',
                'grammatical_features_item_ids': [second_person, plural],
            },
            {
                'label': 'سوم شخص جمع',
                'example': 'آنها [می‌روند].',
                'grammatical_features_item_ids': [third_person, plural],
            },
        ],
    },

    'finnish-noun': {
        '@attribution': {'users': ['Shinnin'], 'title': 'Wikidata:Wikidata Lexeme Forms/Finnish'},
        'label': 'suomen kielen substantiivi',
        'language': language_Finnish,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'yksikön nominatiivi',
                'example': 'Tämä on [koira/lisää/useampia/muotoja/näin].',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'monikon nominatiivi',
                'example': 'Nämä [koirat].',
                'grammatical_features_item_ids': [plural, nominative_case],
            },
            {
                'section_break': True,
                'label': 'yksikön genetiivi',
                'example': 'Tämän [koiran].',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'monikon genetiivi',
                'example': 'Näiden [koirien].',
                'grammatical_features_item_ids': [plural, genitive_case],
            },
            {
                'section_break': True,
                'label': 'yksikön partitiivi',
                'example': 'Tätä [koiraa].',
                'grammatical_features_item_ids': [singular, partitive_case],
            },
            {
                'label': 'monikon partitiivi',
                'example': 'Näitä [koiria].',
                'grammatical_features_item_ids': [plural, partitive_case],
            },
            {
                'section_break': True,
                'label': 'yksikön essiivi',
                'example': 'Tällaisena [koirana].',
                'grammatical_features_item_ids': [singular, essive_case],
            },
            {
                'label': 'monikon essiivi',
                'example': 'Tällaisina [koirina].',
                'grammatical_features_item_ids': [plural, essive_case],
            },
            {
                'section_break': True,
                'label': 'yksikön translatiivi',
                'example': 'Yhdeksi [koiraksi].',
                'grammatical_features_item_ids': [singular, translative_case],
            },
            {
                'label': 'monikon translatiivi',
                'example': 'Moniksi [koiriksi].',
                'grammatical_features_item_ids': [plural, translative_case],
            },
            {
                'section_break': True,
                'label': 'yksikön inessiivi',
                'example': 'Tässä [koirassa].',
                'grammatical_features_item_ids': [singular, inessive_case],
            },
            {
                'label': 'monikon inessiivi',
                'example': 'Näissä [koirissa].',
                'grammatical_features_item_ids': [plural, inessive_case],
            },
            {
                'section_break': True,
                'label': 'yksikön elatiivi',
                'example': 'Tästä [koirasta].',
                'grammatical_features_item_ids': [singular, elative_case],
            },
            {
                'label': 'monikon elatiivi',
                'example': 'Näistä [koirista].',
                'grammatical_features_item_ids': [plural, elative_case],
            },
            {
                'section_break': True,
                'label': 'yksikön illatiivi',
                'example': 'Tähän [koiraan].',
                'grammatical_features_item_ids': [singular, illative_case],
            },
            {
                'label': 'monikon illatiivi',
                'example': 'Näihin [koiriin].',
                'grammatical_features_item_ids': [plural, illative_case],
            },
            {
                'section_break': True,
                'label': 'yksikön adessiivi',
                'example': 'Tällä [koiralla].',
                'grammatical_features_item_ids': [singular, adessive_case],
            },
            {
                'label': 'monikon adessiivi',
                'example': 'Näillä [koirilla].',
                'grammatical_features_item_ids': [plural, adessive_case],
            },
            {
                'section_break': True,
                'label': 'yksikön ablatiivi',
                'example': 'Tältä [koiralta].',
                'grammatical_features_item_ids': [singular, ablative_case],
            },
            {
                'label': 'monikon ablatiivi',
                'example': 'Näiltä [koirilta].',
                'grammatical_features_item_ids': [plural, ablative_case],
            },
            {
                'section_break': True,
                'label': 'yksikön allatiivi',
                'example': 'Tälle [koiralle].',
                'grammatical_features_item_ids': [singular, allative_case],
            },
            {
                'label': 'monikon allatiivi',
                'example': 'Näille [koirille].',
                'grammatical_features_item_ids': [plural, allative_case],
            },
            {
                'section_break': True,
                'label': 'monikon instruktiivi',
                'example': 'Käsin, jaloin, kissoin ja [koirin].',
                'grammatical_features_item_ids': [instructive_case, plural],
            },
            {
                'section_break': True,
                'label': 'yksikön abessiivi',
                'example': 'Kädettä, jalatta, kissatta ja [koiratta].',
                'grammatical_features_item_ids': [abessive_case, singular],
            },
            {
                'label': 'monikon abessiivi',
                'example': 'Käsittä, jaloitta, kissoitta ja [koiritta].',
                'grammatical_features_item_ids': [abessive_case, plural],
            },
        ],
    },

    'french-noun-masculine': {
        '@attribution': {'users': ['Djiboun'], 'title': 'Wikidata:Wikidata Lexeme Forms/French'},
        'label': 'nom commun masculin en français',
        'language': language_French,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singulier',
                'example': 'Voici un [chien].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'pluriel',
                'example': 'Voici des [chiens].',
                'grammatical_features_item_ids': [plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'french-noun-feminine': {
        '@attribution': {'users': ['Djiboun'], 'title': 'Wikidata:Wikidata Lexeme Forms/French'},
        'label': 'nom commun féminin en français',
        'language': language_French,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singulier',
                'example': 'Voici une [chienne].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'pluriel',
                'example': 'Voici des [chiennes].',
                'grammatical_features_item_ids': [plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'french-adjective': {
        '@attribution': {'users': ['Djiboun'], 'title': 'Wikidata:Wikidata Lexeme Forms/French'},
        'label': 'adjectif en français',
        'language': language_French,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'masculin singulier',
                'example': 'Un arbre [vert].',
                'grammatical_features_item_ids': [masculine, singular],
            },
            {
                'label': 'masculin pluriel',
                'example': 'Des arbres [verts].',
                'grammatical_features_item_ids': [masculine, plural],
            },
            {
                'label': 'féminin singulier',
                'example': 'Une plante [verte].',
                'grammatical_features_item_ids': [feminine, singular],
            },
            {
                'label': 'féminin pluriel',
                'example': 'Des plantes [vertes].',
                'grammatical_features_item_ids': [feminine, plural],
            },
        ],
    },

    'french-verb': {
        '@attribution': {'users': ['Envlh', 'Djiboun', 'VIGNERON'], 'title': 'Wikidata:Wikidata Lexeme Forms/French'},
        'label': 'verbe en français',
        'language': language_French,
        'lexical_category_item_id': verb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'infinitif',
                'example': 'Iel sait [chanter].',
                'grammatical_features_item_ids': [infinitive],
            },
            {
                'section_break': True,
                'label': 'participe présent',
                'example': 'C\'est en [chantant] que l\'on devient forgeron.',
                'grammatical_features_item_ids': [participle, present_tense],
            },
            {
                'section_break': True,
                'label': 'participe passé singulier masculin',
                'example': 'Il est [chanté].',
                'grammatical_features_item_ids': [participle, past_tense, singular, masculine],
            },
            {
                'label': 'participe passé singulier féminin',
                'example': 'Elle est [chantée].',
                'grammatical_features_item_ids': [participle, past_tense, singular, feminine],
            },
            {
                'label': 'participe passé pluriel masculin',
                'example': 'Ils sont [chantés].',
                'grammatical_features_item_ids': [participle, past_tense, plural, masculine],
            },
            {
                'label': 'participe passé pluriel féminin',
                'example': 'Elles sont [chantées].',
                'grammatical_features_item_ids': [participle, past_tense, plural, feminine],
            },
            {
                'section_break': True,
                'label': 'indicatif présent singulier première personne',
                'example': 'Aujourd\'hui, je (j\') [chante].',
                'grammatical_features_item_ids': [indicative, present_tense, singular, first_person],
            },
            {
                'label': 'indicatif présent singulier deuxième personne',
                'example': 'Aujourd\'hui, tu [chantes].',
                'grammatical_features_item_ids': [indicative, present_tense, singular, second_person],
            },
            {
                'label': 'indicatif présent singulier troisième personne',
                'example': 'Aujourd\'hui, iel [chante].',
                'grammatical_features_item_ids': [indicative, present_tense, singular, third_person],
            },
            {
                'label': 'indicatif présent pluriel première personne',
                'example': 'Aujourd\'hui, nous [chantons].',
                'grammatical_features_item_ids': [indicative, present_tense, plural, first_person],
            },
            {
                'label': 'indicatif présent pluriel deuxième personne',
                'example': 'Aujourd\'hui, vous [chantez].',
                'grammatical_features_item_ids': [indicative, present_tense, plural, second_person],
            },
            {
                'label': 'indicatif présent pluriel troisième personne',
                'example': 'Aujourd\'hui, iels [chantent].',
                'grammatical_features_item_ids': [indicative, present_tense, plural, third_person],
            },
            {
                'section_break': True,
                'label': 'indicatif passé simple singulier première personne',
                'example': 'Hier, je (j\') [chantai] une fois.',
                'grammatical_features_item_ids': [indicative, preterite, singular, first_person],
            },
            {
                'label': 'indicatif passé simple singulier deuxième personne',
                'example': 'Hier, tu [chantas] une fois.',
                'grammatical_features_item_ids': [indicative, preterite, singular, second_person],
            },
            {
                'label': 'indicatif passé simple singulier troisième personne',
                'example': 'Hier, iel [chanta] une fois.',
                'grammatical_features_item_ids': [indicative, preterite, singular, third_person],
            },
            {
                'label': 'indicatif passé simple pluriel première personne',
                'example': 'Hier, nous [chantâmes] une fois.',
                'grammatical_features_item_ids': [indicative, preterite, plural, first_person],
            },
            {
                'label': 'indicatif passé simple pluriel deuxième personne',
                'example': 'Hier, vous [chantâtes] une fois.',
                'grammatical_features_item_ids': [indicative, preterite, plural, second_person],
            },
            {
                'label': 'indicatif passé simple pluriel troisième personne',
                'example': 'Hier, iels [chantèrent] une fois.',
                'grammatical_features_item_ids': [indicative, preterite, plural, third_person],
            },
            {
                'section_break': True,
                'label': 'indicatif imparfait singulier première personne',
                'example': 'Hier, je (j\') [chantais] toute la journée.',
                'grammatical_features_item_ids': [indicative, 'Q108524486', singular, first_person],
            },
            {
                'label': 'indicatif imparfait singulier deuxième personne',
                'example': 'Hier, tu [chantais] toute la journée.',
                'grammatical_features_item_ids': [indicative, 'Q108524486', singular, second_person],
            },
            {
                'label': 'indicatif imparfait singulier troisième personne',
                'example': 'Hier, iel [chantait] toute la journée.',
                'grammatical_features_item_ids': [indicative, 'Q108524486', singular, third_person],
            },
            {
                'label': 'indicatif imparfait pluriel première personne',
                'example': 'Hier, nous [chantions] toute la journée.',
                'grammatical_features_item_ids': [indicative, 'Q108524486', plural, first_person],
            },
            {
                'label': 'indicatif imparfait pluriel deuxième personne',
                'example': 'Hier, vous [chantiez] toute la journée.',
                'grammatical_features_item_ids': [indicative, 'Q108524486', plural, second_person],
            },
            {
                'label': 'indicatif imparfait pluriel troisième personne',
                'example': 'Hier, iels [chantaient] toute la journée.',
                'grammatical_features_item_ids': [indicative, 'Q108524486', plural, third_person],
            },
            {
                'section_break': True,
                'label': 'indicatif futur simple singulier première personne',
                'example': 'Demain, je (j\') [chanterai].',
                'grammatical_features_item_ids': [indicative, 'Q1475560', singular, first_person],
            },
            {
                'label': 'indicatif futur simple singulier deuxième personne',
                'example': 'Demain, tu [chanteras].',
                'grammatical_features_item_ids': [indicative, 'Q1475560', singular, second_person],
            },
            {
                'label': 'indicatif futur simple singulier troisième personne',
                'example': 'Demain, iel [chantera].',
                'grammatical_features_item_ids': [indicative, 'Q1475560', singular, third_person],
            },
            {
                'label': 'indicatif futur simple pluriel première personne',
                'example': 'Demain, nous [chanterons].',
                'grammatical_features_item_ids': [indicative, 'Q1475560', plural, first_person],
            },
            {
                'label': 'indicatif futur simple pluriel deuxième personne',
                'example': 'Demain, vous [chanterez].',
                'grammatical_features_item_ids': [indicative, 'Q1475560', plural, second_person],
            },
            {
                'label': 'indicatif futur simple pluriel troisième personne',
                'example': 'Demain, iels [chanteront].',
                'grammatical_features_item_ids': [indicative, 'Q1475560', plural, third_person],
            },
            {
                'section_break': True,
                'label': 'subjonctif présent singulier première personne',
                'example': 'Il faut que je (j\') [chante].',
                'grammatical_features_item_ids': [subjunctive, present_tense, singular, first_person],
            },
            {
                'label': 'subjonctif présent singulier deuxième personne',
                'example': 'Il faut que tu [chantes].',
                'grammatical_features_item_ids': [subjunctive, present_tense, singular, second_person],
            },
            {
                'label': 'subjonctif présent singulier troisième personne',
                'example': 'Il faut qu\'iel [chante].',
                'grammatical_features_item_ids': [subjunctive, present_tense, singular, third_person],
            },
            {
                'label': 'subjonctif présent pluriel première personne',
                'example': 'Il faut que nous [chantions].',
                'grammatical_features_item_ids': [subjunctive, present_tense, plural, first_person],
            },
            {
                'label': 'subjonctif présent pluriel deuxième personne',
                'example': 'Il faut que vous [chantiez].',
                'grammatical_features_item_ids': [subjunctive, present_tense, plural, second_person],
            },
            {
                'label': 'subjonctif présent pluriel troisième personne',
                'example': 'Il faut qu\'iels [chantent].',
                'grammatical_features_item_ids': [subjunctive, present_tense, plural, third_person],
            },
            {
                'section_break': True,
                'label': 'subjonctif imparfait singulier première personne',
                'example': 'Il fallait que je (j\') [chantasse].',
                'grammatical_features_item_ids': [subjunctive, 'Q108524486', singular, first_person],
            },
            {
                'label': 'subjonctif imparfait singulier deuxième personne',
                'example': 'Il fallait que tu [chantasses].',
                'grammatical_features_item_ids': [subjunctive, 'Q108524486', singular, second_person],
            },
            {
                'label': 'subjonctif imparfait singulier troisième personne',
                'example': 'Il fallait qu\'iel [chantât].',
                'grammatical_features_item_ids': [subjunctive, 'Q108524486', singular, third_person],
            },
            {
                'label': 'subjonctif imparfait pluriel première personne',
                'example': 'Il fallait que nous [chantassions].',
                'grammatical_features_item_ids': [subjunctive, 'Q108524486', plural, first_person],
            },
            {
                'label': 'subjonctif imparfait pluriel deuxième personne',
                'example': 'Il fallait que vous [chantassiez].',
                'grammatical_features_item_ids': [subjunctive, 'Q108524486', plural, second_person],
            },
            {
                'label': 'subjonctif imparfait pluriel troisième personne',
                'example': 'Il fallait qu\'iels [chantassent].',
                'grammatical_features_item_ids': [subjunctive, 'Q108524486', plural, third_person],
            },
            {
                'section_break': True,
                'label': 'conditionnel présent singulier première personne',
                'example': 'Si je savais, je (j\') [chanterais].',
                'grammatical_features_item_ids': [conditional, present_tense, singular, first_person],
            },
            {
                'label': 'conditionnel présent singulier deuxième personne',
                'example': 'Si tu savais, tu [chanterais].',
                'grammatical_features_item_ids': [conditional, present_tense, singular, second_person],
            },
            {
                'label': 'conditionnel présent singulier troisième personne',
                'example': 'S\'iel savait, iel [chanterait].',
                'grammatical_features_item_ids': [conditional, present_tense, singular, third_person],
            },
            {
                'label': 'conditionnel présent pluriel première personne',
                'example': 'Si nous savions, nous [chanterions].',
                'grammatical_features_item_ids': [conditional, present_tense, plural, first_person],
            },
            {
                'label': 'conditionnel présent pluriel deuxième personne',
                'example': 'Si vous saviez, vous [chanteriez].',
                'grammatical_features_item_ids': [conditional, present_tense, plural, second_person],
            },
            {
                'label': 'conditionnel présent pluriel troisième personne',
                'example': 'S\'iels savaient, iels [chanteraient].',
                'grammatical_features_item_ids': [conditional, present_tense, plural, third_person],
            },
            {
                'section_break': True,
                'label': 'impératif présent singulier deuxième personne',
                'example': 'Maintenant, [chante] !',
                'grammatical_features_item_ids': [imperative, present_tense, singular, second_person],
            },
            {
                'label': 'impératif présent pluriel première personne',
                'example': 'Maintenant, [chantons] !',
                'grammatical_features_item_ids': [imperative, present_tense, plural, first_person],
            },
            {
                'label': 'impératif présent pluriel deuxième personne',
                'example': 'Maintenant, [chantez] !',
                'grammatical_features_item_ids': [imperative, present_tense, plural, second_person],
            },
        ],
    },

    'hebrew-noun-masculine': {
        '@attribution': {'users': ['Uziel302', 'Uzielbot'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hebrew'},
        'label': 'שם עצם זכר',
        'language': language_Hebrew,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'יחיד',
                'example': 'זה [כלב].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'רבים',
                'example': 'אלה [כלבים].',
                'grammatical_features_item_ids': [plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'hebrew-noun-feminine': {
        '@attribution': {'users': ['Uziel302', 'Uzielbot'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hebrew'},
        'label': 'שם עצם נקבה',
        'language': language_Hebrew,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'יחידה',
                'example': 'זו [כלבה].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'רבות',
                'example': 'אלה [כלבות].',
                'grammatical_features_item_ids': [plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'hebrew-adjective': {
        '@attribution': {'users': ['Ijon'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hebrew'},
        'label': 'שם תואר עברי',
        'language': language_Hebrew,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'יחיד',
                'example': 'חתול [גדול] חצה את הכביש.',
                'grammatical_features_item_ids': [singular, positive, masculine],
            },
            {
                'label': 'רבים',
                'example': 'חתולים [גדולים] חצו את הכביש.',
                'grammatical_features_item_ids': [plural, positive, masculine],
            },
            {
                'label': 'יחידה',
                'example': 'חתולה [גדולה] חצתה את הכביש.',
                'grammatical_features_item_ids': [singular, positive, feminine],
            },
            {
                'label': 'רבות',
                'example': 'חתולות [גדולות] חצו את הכביש.',
                'grammatical_features_item_ids': [plural, positive, feminine],
            },
        ],
    },

    'hindustani-noun-masculine-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी नाउँ पुलिंग',
        'language': language_Hindi,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'एक बचन, फाइली',
                'example': 'वह [परिंदा] खूबसुरत था।',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
                'grammatical_features_item_ids_optional': set([masculine]),
            },
            {
                'label': 'बहु बचन, फाइली',
                'example': 'वह [परिंदे] खूबसुरत थे।',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
                'grammatical_features_item_ids_optional': set([masculine]),
            },
            {
                'label': 'एक बचन, मफऊली',
                'example': 'इस [परिंदे] ने किया।',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
                'grammatical_features_item_ids_optional': set([masculine]),
            },
            {
                'label': 'बहु बचन, मफऊली',
                'example': 'उस [परिंदों] ने किया।',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
                'grammatical_features_item_ids_optional': set([masculine]),
            },
            {
                'section_break': True,
                'label': 'एक बचन, पुकाने',
                'example': 'अए, यहाँ आओ मेरे [परिंदे]!',
                'grammatical_features_item_ids': [masculine, vocative_case, singular],
                'grammatical_features_item_ids_optional': set([masculine]),
                'optional': True,
            },
            {
                'label': 'बहु बचन, पुकाने',
                'example': 'अए, यहाँ आओ मेरे [परिंदो]!',
                'grammatical_features_item_ids': [masculine, vocative_case, plural],
                'grammatical_features_item_ids_optional': set([masculine]),
                'optional': True,
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'hindustani-noun-feminine-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी नाउँ इसतरी लिंग',
        'language': language_Hindi,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'एक बचन, फाइली',
                'example': 'वह [बिल्ली] खूबसुरत थी।',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
                'grammatical_features_item_ids_optional': set([feminine]),
            },
            {
                'label': 'बहु बचन, फाइली',
                'example': 'वह [बिल्लियाँ] खूबसुरत थीं।',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
                'grammatical_features_item_ids_optional': set([feminine]),
            },
            {
                'label': 'एक बचन, मफऊली',
                'example': 'यह इस [बिल्ली] से आया है।',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
                'grammatical_features_item_ids_optional': set([feminine]),
            },
            {
                'label': 'बहु बचन, मफऊली',
                'example': 'यह उन [बिल्लियों] से आया है।',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
                'grammatical_features_item_ids_optional': set([feminine]),
            },
            {
                'section_break': True,
                'label': 'एक बचन, पुकाने',
                'example': 'अए, यहाँ आओ मेरी [बिल्ली]!',
                'grammatical_features_item_ids': [feminine, vocative_case, singular],
                'grammatical_features_item_ids_optional': set([feminine]),
                'optional': True,
            },
            {
                'label': 'बहु बचन, पुकाने',
                'example': 'अए, यहाँ आओ मेरी [बिल्लियो]!',
                'grammatical_features_item_ids': [feminine, vocative_case, plural],
                'grammatical_features_item_ids_optional': set([feminine]),
                'optional': True,
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'hindustani-adjective-red-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी लाल गुन नाउँ',
        'language': language_Hindi,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'मुफरद',
                'example': 'मेरे [लाल] परिंदों को देखो।',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, indeclinable_adjective)],
            paradigm_class: [statement(paradigm_class, lāl_adjective)],
        },
    },

    'hindustani-adjective-black-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी काला गुन नाउँ',
        'language': language_Hindi,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'पुलिंग, एक बचन, फाइली',
                'example': 'मेरा [काला] परिंदा है।',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'पुलिंग, बहु बचन, फाइली',
                'example': 'मेरे [काले] परिंदे हैं।',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'पुलिंग, एक बचन, मफऊली',
                'example': 'मेरे [काले] परिंदे को देखो।',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'पुलिंग, बहु बचन, मफऊली',
                'example': 'मेरे [काले] परिंदों को देखो।',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'label': 'पुलिंग, एक बचन, पुकाने',
                'example': 'अए, यहाँ आओ मेरे [काले] परिंदे!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'पुलिंग, बहु बचन, पुकाने',
                'example': 'अए, यहाँ आओ मेरे [काले] परिंदो!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'इसतरी लिंग, एक बचन, फाइली',
                'example': 'मेरी [काली] बिल्ली है।',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'इसतरी लिंग, बहु बचन, फाइली',
                'example': 'मेरी [काली] बिल्लियाँ हैं।',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'इसतरी लिंग, एक बचन, मफऊली',
                'example': 'मेरी [काली] बिल्ली को देखो।',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'इसतरी लिंग, बहु बचन, मफऊली',
                'example': 'मेरी [काली] बिल्लियाँ को देखो।',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
            {
                'label': 'इसतरी लिंग, एक बचन, पुकाने',
                'example': 'अए, यहाँ आओ मेरी [काली] बिल्ली!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'इसतरी लिंग, बहु बचन, पुकाने',
                'example': 'अए, यहाँ आओ मेरी [काली] बिल्लीओ!',
                'grammatical_features_item_ids': [feminine, vocative_case, plural],
                'optional': True,
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, declinable_adjective)],
            paradigm_class: [statement(paradigm_class, kālā_adjective)],
        },
    },

    'hindustani-adjective-handsomest-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी गुन नाउँ तफजील',
        'language': language_Hindi,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'नफीस',
                'example': 'यह परिंदा [ख़ूब] है।',
                'grammatical_features_item_ids': [positive],
            },
            {
                'label': 'बाज',
                'example': 'यह परिंदा भी [ख़ूब तर] है।',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'कुल',
                'example': 'लेकिन मेरा परिंदा [ख़ूब तरीन] है।',
                'grammatical_features_item_ids': [superlative],
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, comparable_adjective)],
            paradigm_class: [statement(paradigm_class, isam_ē_tafazīl)],
        },
    },

    'hindustani-adverb-indeclinable-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी आम गुन फैल',
        'language': language_Hindi,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'मुफरद',
                'example': 'वे [हौले हौले] चलते हैं।',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements(instance_of, indeclinable_adverb),
    },

    'hindustani-adverb-declinable-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी ऐसा बदल करता गुन फैल',
        'language': language_Hindi,
        'lexical_category_item_id': adverb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'पुलिंग, एक बचन, फाइली',
                'example': 'पकोड़ा [ऐसा] पका खाया न गिया।',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'पुलिंग, बहु बचन, फाइली',
                'example': 'पकोड़े [ऐसे] पके खाये न गये।',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'पुलिंग, एक बचन, मफऊली',
                'example': 'पकोड़े [ऐसे] पके के खाने लिए अच्छा है।',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'पुलिंग, बहु बचन, मफऊली',
                'example': 'पकोड़ों [ऐसे] पके के खाने लिए अच्छा है।',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'section_break': True,
                'label': 'इसतरी लिंग, एक बचन, फाइली',
                'example': 'रोटी [ऐसी] पकी खायी न गयी।',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'इसतरी लिंग, बहु बचन, फाइली',
                'example': 'रोटियाँ [ऐसी] पकी खायीं न गयीं।',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'इसतरी लिंग, एक बचन, मफऊली',
                'example': 'रोटी [ऐसी] पकी के खाने लिए अच्छा है।',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'इसतरी लिंग, बहु बचन, मफऊली',
                'example': 'रोटियाँ [ऐसी] पकी के खाने लिए अच्छा है।',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
        ],
        'statements': statements(instance_of, declinable_adverb),
    },

    'hindustani-verb-basic-intransitive-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी फैल लाजमी',
        'language': language_Hindi,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'इस्म-ए-मस्दर, फाइली',
                'example': 'मुझे [फैलना] पसंद है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'इस्म-ए-मस्दर, मफऊली',
                'example': 'मैं [फैलने] के लिए करता हूँ।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मतऊफ',
                'example': 'हम [फैल] कर सकते हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, मुतलक',
                'example': 'वह [फैलके] रहे हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, तरकीब-ए-मुतलक',
                'example': 'वह [फैलकर] रहे हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'शक्की, पुलिंग, एक बचन',
                'example': 'कुत्ता न [फैलना] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, पुलिंग, बहु बचन',
                'example': 'कुत्ते न [फैलने] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, एक बचन',
                'example': 'बिल्ली न [फैलनी] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, बहु बचन',
                'example': 'बिल्लियाँ न [फैलनीं] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, एक बचन',
                'example': 'वह कुत्ता [फैलता] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, बहु बचन',
                'example': 'वे कुत्ते [फैलते] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, एक बचन',
                'example': 'वह बिल्ली [फैलती] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, बहु बचन',
                'example': 'वे बिल्लियाँ [फैलतीं] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'बईद, पुलिंग, एक बचन',
                'example': 'वह कुत्ता [फैला] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, पुलिंग, बहु बचन',
                'example': 'वे कुत्ते [फैले] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, एक बचन',
                'example': 'वह बिल्ली [फैली] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, बहु बचन',
                'example': 'वे बिल्लियाँ [फैलीं] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'एहतिमाली, कहने वाला, एक बचन',
                'example': 'मैं [फैलूँ] हूँ।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, कहने वाला, बहु बचन',
                'example': 'हम [फैलें] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, एक बचन',
                'example': 'तू [फैले] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, बहु बचन',
                'example': 'तुम [फैलो] हो।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, एक बचन',
                'example': 'वह [फैले] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, बहु बचन',
                'example': 'वे [फैलें] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'मशरूत, कहने वाला, पुलिंग, एक बचन',
                'example': 'मैं [फैलूँगा] हूँ।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, पुलिंग, बहु बचन',
                'example': 'हम [फैलेंगे] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, एक बचन',
                'example': 'मैं [फैलूँगी] हूँ।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, बहु बचन',
                'example': 'हम [फैलेंगी] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, एक बचन',
                'example': 'तू [फैलेगा] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, बहु बचन',
                'example': 'तुम [फैलोगे] हो।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, एक बचन',
                'example': 'तू [फैलेगी] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, बहु बचन',
                'example': 'तुम [फैलोगी] हो।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, एक बचन',
                'example': 'वह [फैलेगा] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, बहु बचन',
                'example': 'वे [फैलेंगे] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, एक बचन',
                'example': 'वह [फैलेगी] है।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, बहु बचन',
                'example': 'वे [फैलेंगी] हैं।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'आम अमर, एक बचन',
                'example': 'तू [फैल]।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'आम अमर, बहु बचन',
                'example': 'तुम [फैलो]।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, एक बचन',
                'example': 'तू [फैलियो]।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, बहु बचन',
                'example': 'तुम [फैलिये]।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'पका अमर',
                'example': 'तुम [फैलियेगा]।',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
        'statements': statements(transitivity, intransitive),
    },

    'hindustani-verb-basic-transitive-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी फैल मुतदी',
        'language': language_Hindi,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'इस्म-ए-मस्दर, फाइली',
                'example': 'मुझे चीजें [धारना] पसंद है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'इस्म-ए-मस्दर, मफऊली',
                'example': 'मैं चीजों [धारने] के लिए करता हूँ।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मतऊफ',
                'example': 'हम चीजें [धार] कर सकते हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, मुतलक',
                'example': 'वह चीजें [धारके] रहे हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, तरकीब-ए-मुतलक',
                'example': 'वह चीजें [धारकर] रहे हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'शक्की, पुलिंग, एक बचन',
                'example': 'वह कुत्ते का काम न [धारना] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, पुलिंग, बहु बचन',
                'example': 'वह कुत्तों के काम न [धारने] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, एक बचन',
                'example': 'बिल्ली चीज न [धारनी] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, बहु बचन',
                'example': 'बिल्लियाँ चीजें न [धारनीं] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, एक बचन',
                'example': 'वह कुत्ते का काम [धारता] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, बहु बचन',
                'example': 'वे कुत्तों के काम [धारते] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, एक बचन',
                'example': 'वह बिल्ली चीज [धारती] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, बहु बचन',
                'example': 'वे बिल्लियाँ चीजें [धारतीं] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'बईद, पुलिंग, एक बचन',
                'example': 'वह कुत्ते का काम [धारा] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, पुलिंग, बहु बचन',
                'example': 'वे कुत्तों के काम [धारे] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, एक बचन',
                'example': 'वह बिल्ली चीज [धारी] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, बहु बचन',
                'example': 'वे बिल्लियाँ चीजें [धारीं] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'एहतिमाली, कहने वाला, एक बचन',
                'example': 'मैं वह [धारूँ] हूँ।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, कहने वाला, बहु बचन',
                'example': 'हम वह [धारें] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, एक बचन',
                'example': 'तू वह [धारे] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, बहु बचन',
                'example': 'तुम वह [धारो] हो।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, एक बचन',
                'example': 'वह यह [धारे] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, बहु बचन',
                'example': 'वे यह [धारें] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'मशरूत, कहने वाला, पुलिंग, एक बचन',
                'example': 'मैं वह [धारूँगा] हूँ।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, पुलिंग, बहु बचन',
                'example': 'हम वह [धारेंगे] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, एक बचन',
                'example': 'मैं वह [धारूँगी] हूँ।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, बहु बचन',
                'example': 'हम वह [धारेंगी] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, एक बचन',
                'example': 'तू वह [धारेगा] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, बहु बचन',
                'example': 'तुम वह [धारोगे] हो।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, एक बचन',
                'example': 'तू वह [धारेगी] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, बहु बचन',
                'example': 'तुम वह [धारोगी] हो।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, एक बचन',
                'example': 'कुत्ता वह [धारेगा] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, बहु बचन',
                'example': 'कुत्ते वह [धारेंगे] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, एक बचन',
                'example': 'बिल्ली वह [धारेगी] है।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, बहु बचन',
                'example': 'बिल्लियाँ वह [धारेंगी] हैं।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'आम अमर, एक बचन',
                'example': 'तू यह [धार]।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'आम अमर, बहु बचन',
                'example': 'तुम यह [धारो]।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, एक बचन',
                'example': 'तू यह [धारियो]।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, बहु बचन',
                'example': 'तुम यह [धारिये]।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'पका अमर',
                'example': 'तुम यह [धारियेगा]।',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
        'statements': statements(transitivity, transitive),
    },

    'hindustani-verb-additive-transitive-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी फैल लाजम का तदिया',
        'language': language_Hindi,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'इस्म-ए-मस्दर, फाइली',
                'example': 'मुझे चीजें [फैलाना] पसंद है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'इस्म-ए-मस्दर, मफऊली',
                'example': 'मैं चीजों [फैलाने] के लिए करता हूँ।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मतऊफ',
                'example': 'हम चीजें [फैला] कर सकते हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, मुतलक',
                'example': 'वह चीजें [फैलाके] रहे हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, तरकीब-ए-मुतलक',
                'example': 'वह चीजें [फैलाकर] रहे हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'शक्की, पुलिंग, एक बचन',
                'example': 'वह कुत्ते का काम न [फैलाना] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, पुलिंग, बहु बचन',
                'example': 'वह कुत्तों के काम न [फैलाने] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, एक बचन',
                'example': 'बिल्ली चीज न [फैलानी] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, बहु बचन',
                'example': 'बिल्लियाँ चीजें न [फैलानीं] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, एक बचन',
                'example': 'वह कुत्ते का काम [फैलाता] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, बहु बचन',
                'example': 'वे कुत्तों के काम [फैलाते] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, एक बचन',
                'example': 'वह बिल्ली चीज [फैलाती] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, बहु बचन',
                'example': 'वे बिल्लियाँ चीजें [फैलातीं] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'बईद, पुलिंग, एक बचन',
                'example': 'वह कुत्ते का काम [फैलाया] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, पुलिंग, बहु बचन',
                'example': 'वे कुत्तों के काम [फैलाये] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, एक बचन',
                'example': 'वह बिल्ली चीज [फैलायी] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, बहु बचन',
                'example': 'वे बिल्लियाँ चीजें [फैलायीं] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'एहतिमाली, कहने वाला, एक बचन',
                'example': 'मैं वह [फैलाऊँ] हूँ।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, कहने वाला, बहु बचन',
                'example': 'हम वह [फैलायें] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, एक बचन',
                'example': 'तू वह [फैलाये] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, बहु बचन',
                'example': 'तुम वह [फैलाओ] हो।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, एक बचन',
                'example': 'वह यह [फैलाये] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, बहु बचन',
                'example': 'वे यह [फैलायें] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'मशरूत, कहने वाला, पुलिंग, एक बचन',
                'example': 'मैं वह [फैलाऊँगा] हूँ।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, पुलिंग, बहु बचन',
                'example': 'हम वह [फैलायेंगे] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, एक बचन',
                'example': 'मैं वह [फैलाऊँगी] हूँ।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, बहु बचन',
                'example': 'हम वह [फैलायेंगी] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, एक बचन',
                'example': 'तू वह [फैलायेगा] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, बहु बचन',
                'example': 'तुम वह [फैलाओगे] हो।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, एक बचन',
                'example': 'तू वह [फैलायेगी] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, बहु बचन',
                'example': 'तुम वह [फैलाओगी] हो।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, एक बचन',
                'example': 'कुत्ता वह [फैलायेगा] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, बहु बचन',
                'example': 'कुत्ते वह [फैलायेंगे] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, एक बचन',
                'example': 'बिल्ली वह [फैलायेगी] है।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, बहु बचन',
                'example': 'बिल्लियाँ वह [फैलायेंगी] हैं।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'आम अमर, एक बचन',
                'example': 'तू यह [फैला]।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'आम अमर, बहु बचन',
                'example': 'तुम यह [फैलाओ]।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, एक बचन',
                'example': 'तू यह [फैलायो]।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, बहु बचन',
                'example': 'तुम यह [फैलाये]।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'पका अमर',
                'example': 'तुम यह [फैलायेगा]।',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
    },

    'hindustani-verb-additive-causative-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी फैल मुतदी का तदिया',
        'language': language_Hindi,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'इस्म-ए-मस्दर, फाइली',
                'example': 'मुझे उन्हें रोटी [खिलाना] पसंद है।',
                'grammatical_features_item_ids': [causative_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'इस्म-ए-मस्दर, मफऊली',
                'example': 'मुझे उन रोटी [खिलाने] के लिए करता हूँ।',
                'grammatical_features_item_ids': [causative_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मतऊफ',
                'example': 'उस ने बच्चों को [खिला] कर सकते हैं।',
                'grammatical_features_item_ids': [causative_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, मुतलक',
                'example': 'उस ने बच्चों को [खिलाके] रहे हैं।',
                'grammatical_features_item_ids': [causative_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, तरकीब-ए-मुतलक',
                'example': 'उस ने बच्चों को [खिलाकर] रहे हैं।',
                'grammatical_features_item_ids': [causative_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'शक्की, पुलिंग, एक बचन',
                'example': 'उस ने बच्चों को पकोड़ा न [खिलाना] है।',
                'grammatical_features_item_ids': [causative_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, पुलिंग, बहु बचन',
                'example': 'उस ने बच्चों को पकोड़े न [खिलाने] हैं।',
                'grammatical_features_item_ids': [causative_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, एक बचन',
                'example': 'उस ने बच्चों को रोटी न [खिलानी] है।',
                'grammatical_features_item_ids': [causative_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, बहु बचन',
                'example': 'उस ने बच्चों को रोटियाँ न [खिलानीं] हैं।',
                'grammatical_features_item_ids': [causative_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, एक बचन',
                'example': 'उस ने बच्चों को पकोड़ा न [खिलाता] है।',
                'grammatical_features_item_ids': [causative_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, बहु बचन',
                'example': 'उस ने बच्चों को पकोड़े न [खिलाते] हैं।',
                'grammatical_features_item_ids': [causative_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, एक बचन',
                'example': 'उस ने बच्चों को रोटी न [खिलाती] है।',
                'grammatical_features_item_ids': [causative_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, बहु बचन',
                'example': 'उस ने बच्चों को रोटियाँ न [खिलातीं] हैं।',
                'grammatical_features_item_ids': [causative_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'बईद, पुलिंग, एक बचन',
                'example': 'उस ने बच्चों को पकोड़ा न [खिलाया] है।',
                'grammatical_features_item_ids': [causative_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, पुलिंग, बहु बचन',
                'example': 'उस ने बच्चों को पकोड़े न [खिलाये] हैं।',
                'grammatical_features_item_ids': [causative_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, एक बचन',
                'example': 'उस ने बच्चों को रोटी न [खिलायी] है।',
                'grammatical_features_item_ids': [causative_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, बहु बचन',
                'example': 'उस ने बच्चों को रोटियाँ न [खिलायीं] हैं।',
                'grammatical_features_item_ids': [causative_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'एहतिमाली, कहने वाला, एक बचन',
                'example': 'मैं बच्चों को [खिलाऊँ] हूँ।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, कहने वाला, बहु बचन',
                'example': 'हम बच्चों को [खिलायें] हैं।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, एक बचन',
                'example': 'तू बच्चों को [खिलाये] है।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, बहु बचन',
                'example': 'तुम बच्चों को [खिलाओ] हो।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, एक बचन',
                'example': 'वह बच्चों को [खिलाये] है।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, बहु बचन',
                'example': 'वे बच्चों को [खिलायें] हैं।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'मशरूत, कहने वाला, पुलिंग, एक बचन',
                'example': 'मैं बच्चों को [खिलाऊँगा] हूँ।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, पुलिंग, बहु बचन',
                'example': 'हम बच्चों को [खिलायेंगे] हैं।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, एक बचन',
                'example': 'मैं बच्चों को [खिलाऊँगी] हूँ।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, बहु बचन',
                'example': 'हम बच्चों को [खिलायेंगी] हैं।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, एक बचन',
                'example': 'तू बच्चों को [खिलायेगा] है।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, बहु बचन',
                'example': 'तुम बच्चों को [खिलाओगे] हो।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, एक बचन',
                'example': 'तू बच्चों को [खिलायेगी] है।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, बहु बचन',
                'example': 'तुम बच्चों को [खिलाओगी] हो।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, एक बचन',
                'example': 'मरद बच्चों को [खिलायेगा] है।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, बहु बचन',
                'example': 'मरद बच्चों को [खिलायेंगे] हैं।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, एक बचन',
                'example': 'औरत बच्चों को [खिलायेगी] है।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, बहु बचन',
                'example': 'औरतें बच्चों को [खिलायेंगी] हैं।',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'आम अमर, एक बचन',
                'example': 'तू बच्चों को [खिला]।',
                'grammatical_features_item_ids': [causative_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'आम अमर, बहु बचन',
                'example': 'तुम बच्चों को [खिलाओ]।',
                'grammatical_features_item_ids': [causative_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, एक बचन',
                'example': 'तू बच्चों को [खिलायो]।',
                'grammatical_features_item_ids': [causative_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, बहु बचन',
                'example': 'तुम बच्चों को [खिलाये]।',
                'grammatical_features_item_ids': [causative_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'पका अमर',
                'example': 'तुम बच्चों को [खिलायेगा]।',
                'grammatical_features_item_ids': [causative_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
    },

    'hindustani-verb-additive-causative-double-hi': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'हिंदुस्तानी फैल मुतदी का दूसरा तदिया',
        'language': language_Hindi,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'इस्म-ए-मस्दर, फाइली',
                'example': 'उन्हें हमारा रोटी [खिलवाना] अच्छा लगता है।',
                'grammatical_features_item_ids': [double_causative_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'इस्म-ए-मस्दर, मफऊली',
                'example': 'उन्हें हमारे रोटी [खिलवाने] के लिए करता हूँ।',
                'grammatical_features_item_ids': [double_causative_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मतऊफ',
                'example': 'उस ने नौकरानी से बच्चों को [खिलवा] कर सकते हैं।',
                'grammatical_features_item_ids': [double_causative_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, मुतलक',
                'example': 'उस ने नौकरानी से बच्चों को [खिलवाके] रहे हैं।',
                'grammatical_features_item_ids': [double_causative_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'मतऊफ, तरकीब-ए-मुतलक',
                'example': 'उस ने नौकरानी से बच्चों को [खिलवाकर] रहे हैं।',
                'grammatical_features_item_ids': [double_causative_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'शक्की, पुलिंग, एक बचन',
                'example': 'उस ने नौकरानी से बच्चों को पकोड़ा न [खिलवाना] है।',
                'grammatical_features_item_ids': [double_causative_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, पुलिंग, बहु बचन',
                'example': 'उस ने नौकरानी से बच्चों को पकोड़े न [खिलवाने] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, एक बचन',
                'example': 'उस ने नौकरानी से बच्चों को रोटी न [खिलवानी] है।',
                'grammatical_features_item_ids': [double_causative_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'शक्की, इसतरी लिंग, बहु बचन',
                'example': 'उस ने नौकरानी से बच्चों को रोटियाँ न [खिलवानीं] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, एक बचन',
                'example': 'उस ने नौकरानी से बच्चों को पकोड़ा न [खिलवाता] है।',
                'grammatical_features_item_ids': [double_causative_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, पुलिंग, बहु बचन',
                'example': 'उस ने नौकरानी से बच्चों को पकोड़े न [खिलवाते] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, एक बचन',
                'example': 'उस ने नौकरानी से बच्चों को रोटी न [खिलवाती] है।',
                'grammatical_features_item_ids': [double_causative_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'इस्तिमरारी, इसतरी लिंग, बहु बचन',
                'example': 'उस ने नौकरानी से बच्चों को रोटियाँ न [खिलवातीं] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'बईद, पुलिंग, एक बचन',
                'example': 'उस ने नौकरानी से बच्चों को पकोड़ा न [खिलवाया] है।',
                'grammatical_features_item_ids': [double_causative_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, पुलिंग, बहु बचन',
                'example': 'उस ने नौकरानी से बच्चों को पकोड़े न [खिलवाये] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, एक बचन',
                'example': 'उस ने नौकरानी से बच्चों को रोटी न [खिलवायी] है।',
                'grammatical_features_item_ids': [double_causative_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'बईद, इसतरी लिंग, बहु बचन',
                'example': 'उस ने नौकरानी से बच्चों को रोटियाँ न [खिलवायीं] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'एहतिमाली, कहने वाला, एक बचन',
                'example': 'मैं ने नौकरानी से बच्चों को [खिलवाऊँ] हूँ।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, कहने वाला, बहु बचन',
                'example': 'हम ने नौकरानी से बच्चों को [खिलवायें] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, एक बचन',
                'example': 'तू ने नौकरानी से बच्चों को [खिलवाये] है।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, सुनने वाला, बहु बचन',
                'example': 'तुम ने नौकरानी से बच्चों को [खिलवाओ] हो।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, एक बचन',
                'example': 'उस ने नौकरानी से बच्चों को [खिलवाये] है।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'एहतिमाली, अन्य, बहु बचन',
                'example': 'उन्हें नौकरानी से बच्चों को [खिलवायें] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'मशरूत, कहने वाला, पुलिंग, एक बचन',
                'example': 'मैं ने नौकरानी से बच्चों को [खिलवाऊँगा] हूँ।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, पुलिंग, बहु बचन',
                'example': 'हम ने नौकरानी से बच्चों को [खिलवायेंगे] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, एक बचन',
                'example': 'मैं ने नौकरानी से बच्चों को [खिलवाऊँगी] हूँ।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, कहने वाला, इसतरी लिंग, बहु बचन',
                'example': 'हम ने नौकरानी से बच्चों को [खिलवायेंगी] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, एक बचन',
                'example': 'तू ने नौकरानी से बच्चों को [खिलवायेगा] है।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, पुलिंग, बहु बचन',
                'example': 'तुम ने नौकरानी से बच्चों को [खिलवाओगे] हो।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, एक बचन',
                'example': 'तू ने नौकरानी से बच्चों को [खिलवायेगी] है।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, सुनने वाला, इसतरी लिंग, बहु बचन',
                'example': 'तुम ने नौकरानी से बच्चों को [खिलवाओगी] हो।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, एक बचन',
                'example': 'मरद ने नौकरानी से बच्चों को [खिलवायेगा] है।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, पुलिंग, बहु बचन',
                'example': 'मरदों ने नौकरानी से बच्चों को [खिलवायेंगे] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, एक बचन',
                'example': 'औरत ने नौकरानी से बच्चों को [खिलवायेगी] है।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'मशरूत, अन्य, इसतरी लिंग, बहु बचन',
                'example': 'औरतों ने नौकरानी से बच्चों को [खिलवायेंगी] हैं।',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'आम अमर, एक बचन',
                'example': 'तू नौकरानी से बच्चों को [खिलवा]।',
                'grammatical_features_item_ids': [double_causative_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'आम अमर, बहु बचन',
                'example': 'तुम नौकरानी से बच्चों को [खिलवाओ]।',
                'grammatical_features_item_ids': [double_causative_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, एक बचन',
                'example': 'तू नौकरानी से बच्चों को [खिलवायो]।',
                'grammatical_features_item_ids': [double_causative_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'तजवीज का अमर, बहु बचन',
                'example': 'तुम नौकरानी से बच्चों को [खिलवाये]।',
                'grammatical_features_item_ids': [double_causative_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'पका अमर',
                'example': 'तुम नौकरानी से बच्चों को [खिलवायेगा]।',
                'grammatical_features_item_ids': [double_causative_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
    },

    'hindustani-noun-masculine-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی ناؤں مذکر',
        'language': language_Urdu,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'واحد، فاعلی',
                'example': 'وہ [پرِندہ] خوبصورت تھا۔',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
                'grammatical_features_item_ids_optional': set([masculine]),
            },
            {
                'label': 'جمع، فاعلی',
                'example': 'وہ [پرِندے] خوبصورت تھے۔',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
                'grammatical_features_item_ids_optional': set([masculine]),
            },
            {
                'label': 'واحد، مفعولی',
                'example': 'اس [پرِندے] نے کیا۔',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
                'grammatical_features_item_ids_optional': set([masculine]),
            },
            {
                'label': 'جمع، مفعولی',
                'example': 'ان [پرِندوں] نے کیا۔',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
                'grammatical_features_item_ids_optional': set([masculine]),
            },
            {
                'section_break': True,
                'label': 'واحد، پکانے',
                'example': 'اے، یہاں آو میرے [پرِندے]!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, singular],
                'grammatical_features_item_ids_optional': set([masculine]),
                'optional': True,
            },
            {
                'label': 'جمع، پکانے',
                'example': 'اے، یہاں آو میرے [پرِندو]!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, plural],
                'grammatical_features_item_ids_optional': set([masculine]),
                'optional': True,
            }
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'hindustani-noun-feminine-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی ناؤں مؤنث',
        'language': language_Urdu,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'واحد، فاعلی',
                'example': 'وہ [بِلّی] خوبصورت تھی۔',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
                'grammatical_features_item_ids_optional': set([feminine]),
            },
            {
                'label': 'جمع، فاعلی',
                'example': 'وہ [بِلّیاں] خوبصورت تھیں۔',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
                'grammatical_features_item_ids_optional': set([feminine]),
            },
            {
                'label': 'واحد، مفعولی',
                'example': 'یہ اس [بِلّی] سے آیا ہے۔',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
                'grammatical_features_item_ids_optional': set([feminine]),
            },
            {
                'label': 'جمع، مفعولی',
                'example': 'یہ ان [بِلّیوں] سے آیا ہے۔',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
                'grammatical_features_item_ids_optional': set([feminine]),
            },
            {
                'section_break': True,
                'label': 'واحد، پکانے',
                'example': 'اے، یہاں آو میری [بِلّی]!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, singular],
                'grammatical_features_item_ids_optional': set([feminine]),
                'optional': True,
            },
            {
                'label': 'جمع، پکانے',
                'example': 'اے، یہاں آو میری [بِلّیو]!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, plural],
                'grammatical_features_item_ids_optional': set([feminine]),
                'optional': True,
            }
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'hindustani-adjective-red-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی لال گن ناؤں',
        'language': language_Urdu,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'مفرد',
                'example': 'میرے [لال] پرندوں کو دیکھو۔',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, indeclinable_adjective)],
            paradigm_class: [statement(paradigm_class, lāl_adjective)],
        },
    },

    'hindustani-adjective-black-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی کالا گن ناؤں',
        'language': language_Urdu,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'مذکر، واحد، فاعلی',
                'example': 'میرا [کالا] پرندہ ہے۔',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'مذکر، جمع، فاعلی',
                'example': 'میرے [کالے] پرندے ہیں۔',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'مذکر، واحد، مفعولی',
                'example': 'میرے [کالے] پرندے کو دیکھو۔',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'مذکر، جمع، مفعولی',
                'example': 'میرے [کالے] پرندوں کو دیکھو۔',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'label': 'مذکر، واحد، پکانے',
                'example': 'اے، یہاں آو میرے [کالے] پرندے!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'مذکر، جمع، پکانے',
                'example': 'اے، یہاں آو میرے [کالے] پرندو!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'مؤنث واحد، فاعلی',
                'example': 'میری [کالی] بلی ہے۔',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'مؤنث، جمع، فاعلی',
                'example': 'میری [کالی] بلیاں ہیں۔',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'مؤنث، واحد، مفعولی',
                'example': 'میری [کالی] بلی کو دیکھو۔',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'مؤنث، جمع، مفعولی',
                'example': 'میری [کالی] بلیاں کو دیکھو۔',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
            {
                'label': 'مؤنث، واحد، پکانے',
                'example': 'اے، یہاں آو میری [کالی] پبلی!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'مؤنث، جمع، پکانے',
                'example': 'اے، یہاں آو میری [کالی] پبلیو!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, plural],
                'optional': True,
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, declinable_adjective)],
            paradigm_class: [statement(paradigm_class, kālā_adjective)],
        },
    },

    'hindustani-adjective-handsomest-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی گن ناؤں تفضیل',
        'language': language_Urdu,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'نفسی',
                'example': 'یہ پرندہ [خُوب] ہے۔',
                'grammatical_features_item_ids': [positive],
            },
            {
                'label': 'بعض',
                'example': 'یہ پرندہ بھی [خُوب تر] ہے۔',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'کُل',
                'example': 'لیکن میرا پرندہ [خُوب ترِین] ہے۔',
                'grammatical_features_item_ids': [superlative],
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, comparable_adjective)],
            paradigm_class: [statement(paradigm_class, isam_ē_tafazīl)],
        },
    },

    'hindustani-adverb-indeclinable-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی عام گن فعل',
        'language': language_Urdu,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'مفرد',
                'example': 'وے [ہَولے ہَولے] چلتے ہیں۔',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements(instance_of, indeclinable_adverb),
    },

    'hindustani-adverb-declinable-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی ایسا بدل کرتا گن فعل',
        'language': language_Urdu,
        'lexical_category_item_id': adverb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'مذکر، واحد، فاعلی',
                'example': 'پکوڑا [اَیسا] پکا کھایا نہ گیا۔',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'مذکر، جمع، فاعلی',
                'example': 'پکوڑے [اَیسے] پکے کھائے نہ گئے۔',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'مذکر، واحد، مفعولی',
                'example': 'پکوڑے [اَیسے] پکے کے کھانے لئے اچھا ہے۔',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'مذکر، جمع، مفعولی',
                'example': 'پکوڑوں [اَیسے] پکے کے کھانے لئے اچھا ہے۔',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'section_break': True,
                'label': 'مؤنث، واحد، فاعلی',
                'example': 'روٹی [اَیسی] پکی کھائی نہ گئی۔',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'مؤنث، جمع، فاعلی',
                'example': 'روٹیاں [اَیسی] پکی کھائیں نہ گئیں۔',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'مؤنث، واحد، مفعولی',
                'example': 'روٹی [اَیسی] پکی کے کھانے لئے اچھا ہے۔',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'مؤنث، جمع، مفعولی',
                'example': 'روٹیاں [اَیسی] پکی کے کھانے لئے اچھا ہے۔',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
        ],
        'statements': statements(instance_of, declinable_adverb),
    },

    'hindustani-verb-basic-intransitive-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی فعل لازمی',
        'language': language_Urdu,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'اسمِ مصدر، فاعلی',
                'example': 'مجھے [پھَیلنا] پسند ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'اسمِ مصدر، مفعولی',
                'example': 'میں [پھَیلنے] کے لیے کرتا ہوں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'معطوف',
                'example': 'ہم [پھَیل] سکتے ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، متعلق',
                'example': 'وہ [پھَیل کے] رہے ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، ترکیبِ متعلق',
                'example': 'وہ [پھَیل کر] رہے ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'شکی، مذکر، واحد',
                'example': 'کتا نہ [پھَیلنا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مذکر، جمع',
                'example': 'کتے نہ [پھَیلنے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، واحد',
                'example': 'بلی نہ [پھَیلنی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، جمع',
                'example': 'بلیاں نہ [پھَیلنِیں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'استمراری، مذکر، واحد',
                'example': 'وہ کتا [پھَیلتا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مذکر، جمع',
                'example': 'وے کتے [پھَیلتے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، واحد',
                'example': 'وہ بلی [پھَیلتی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، جمع',
                'example': 'وے بلیاں [پھَیلتِیں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'بعید، مذکر، واحد',
                'example': 'وہ کتا [پھَیلا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مذکر، جمع',
                'example': 'وے کتے [پھَیلے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، واحد',
                'example': 'وہ بلی [پھَیلی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، جمع',
                'example': 'وے بلیاں [پھَیلِیں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'احتمالی، کہنے والا، واحد',
                'example': 'میں [پھَیلُوں] ہوں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، کہنے والا، جمع',
                'example': 'ہم [پھَیلیں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، واحد',
                'example': 'تو [پھَیلے] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، جمع',
                'example': 'تم [پھَیلو] ہو۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، واحد',
                'example': 'وہ [پھَیلے] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، جمع',
                'example': 'وے [پھَیلیں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'مشروط، کہنے والا، مذکر، واحد',
                'example': 'میں [پھَیلُوں‌گا] ہوں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مذکر، جمع',
                'example': 'ہم [پھَیلیں‌گے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، واحد',
                'example': 'میں [پھَیلُوں‌گی] ہوں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، جمع',
                'example': 'ہم [پھَیلیں‌گی] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، واحد',
                'example': 'تو [پھَیلےگا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، جمع',
                'example': 'تم [پھَیلوگے] ہو۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، واحد',
                'example': 'تو [پھَیلےگی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، جمع',
                'example': 'تم [پھَیلوگی] ہو۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، واحد',
                'example': 'وہ [پھَیلےگا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، جمع',
                'example': 'وے [پھَیلیں‌گے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، واحد',
                'example': 'وہ [پھَیلےگی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، جمع',
                'example': 'وے [پھَیلیں‌گی] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'عام امر، واحد',
                'example': 'تو [پھَیل]۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'عام امر، جمع',
                'example': 'تم [پھَیلو]۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، واحد',
                'example': 'تو [پھَیلیو]۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، جمع',
                'example': 'تم [پھَیلیئے]۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'پکا امر',
                'example': 'تم [پھَیلیئےگا]۔',
                'grammatical_features_item_ids': [basic_phase, intransitive_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, intransitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
        'statements': statements(transitivity, intransitive),
    },

    'hindustani-verb-basic-transitive-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی فعل متعدی',
        'language': language_Urdu,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'اسمِ مصدر، فاعلی',
                'example': 'مجھے چیزیں [دھارنا] پسند ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'اسمِ مصدر، مفعولی',
                'example': 'میں چیزوں [دھارنے] کے لیے کرتا ہوں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'معطوف',
                'example': 'ہم چیزیں [دھار] سکتے ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، متعلق',
                'example': 'وہ چیزیں [دھار کے] رہے ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، ترکیبِ متعلق',
                'example': 'وہ چیزیں [دھار کر] رہے ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'شکی، مذکر، واحد',
                'example': 'وہ کتے کا کام نہ [دھارنا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مذکر، جمع',
                'example': 'وہ کتوں کے کام نہ [دھارنے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، واحد',
                'example': 'بلی چیز نہ [دھارنی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، جمع',
                'example': 'بلیاں چیزیں نہ [دھارنِیں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'استمراری، مذکر، واحد',
                'example': 'وہ کتے کا کام [دھارتا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مذکر، جمع',
                'example': 'وے کتوں کے کام [دھارتے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، واحد',
                'example': 'وہ بلی چیز [دھارتی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، جمع',
                'example': 'وے بلیاں چیزیں [دھارتِیں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'بعید، مذکر، واحد',
                'example': 'وہ کتے کا کام [دھارا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مذکر، جمع',
                'example': 'وے کتوں کے کام [دھارے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، واحد',
                'example': 'وہ بلی چیز [دھاری] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، جمع',
                'example': 'وے بلیاں چیزیں [دھارِیں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'احتمالی، کہنے والا، واحد',
                'example': 'میں وہ [دھارُوں] ہوں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، کہنے والا، جمع',
                'example': 'ہم وہ [دھاریں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، واحد',
                'example': 'تو وہ [دھارے] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، جمع',
                'example': 'تم وہ [دھارو] ہو۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، واحد',
                'example': 'وہ یہ [دھارے] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، جمع',
                'example': 'وے یہ [دھاریں] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'مشروط، کہنے والا، مذکر، واحد',
                'example': 'میں وہ [دھارُوں‌گا] ہوں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مذکر، جمع',
                'example': 'ہم وہ [دھاریں‌گے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، واحد',
                'example': 'میں وہ [دھارُوں‌گی] ہوں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، جمع',
                'example': 'ہم وہ [دھاریں‌گی] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، واحد',
                'example': 'تو وہ [دھارےگا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، جمع',
                'example': 'تم وہ [دھاروگے] ہو۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، واحد',
                'example': 'تو وہ [دھارےگی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، جمع',
                'example': 'تم وہ [دھاروگی] ہو۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، واحد',
                'example': 'کتا وہ [دھارےگا] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، جمع',
                'example': 'کتے وہ [دھاریں‌گے] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، واحد',
                'example': 'بلی وہ [دھارےگی] ہے۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، جمع',
                'example': 'بلیاں وہ [دھاریں‌گی] ہیں۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'عام امر، واحد',
                'example': 'تو یہ [دھار]۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'عام امر، جمع',
                'example': 'تم یہ [دھارو]۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، واحد',
                'example': 'تو یہ [دھاریو]۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، جمع',
                'example': 'تم یہ [دھاریئے]۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'پکا امر',
                'example': 'تم یہ [دھاریئےگا]۔',
                'grammatical_features_item_ids': [basic_phase, transitive_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([basic_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
        'statements': statements(transitivity, transitive),
    },

    'hindustani-verb-additive-transitive-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی فعل لازم کا تعدیہ',
        'language': language_Urdu,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'اسمِ مصدر، فاعلی',
                'example': 'مجھے چیزیں [پھَیلانا] پسند ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'اسمِ مصدر، مفعولی',
                'example': 'میں چیزوں [پھَیلانے] کے لیے کرتا ہوں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'معطوف',
                'example': 'ہم چیزیں [پھَیلا] سکتے ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، متعلق',
                'example': 'وہ چیزیں [پھَیلا کے] رہے ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، ترکیبِ متعلق',
                'example': 'وہ چیزیں [پھَیلا کر] رہے ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'شکی، مذکر، واحد',
                'example': 'وہ کتے کا کام نہ [پھَیلانا] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مذکر، جمع',
                'example': 'وہ کتوں کے کام نہ [پھَیلانے] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، واحد',
                'example': 'بلی چیز نہ [پھَیلانی] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، جمع',
                'example': 'بلیاں چیزیں نہ [پھَیلانِیں] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'استمراری، مذکر، واحد',
                'example': 'وہ کتے کا کام [پھَیلاتا] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مذکر، جمع',
                'example': 'وے کتوں کے کام [پھَیلاتے] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، واحد',
                'example': 'وہ بلی چیز [پھَیلاتی] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، جمع',
                'example': 'وے بلیاں چیزیں [پھَیلاتِیں] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'بعید، مذکر، واحد',
                'example': 'وہ کتے کا کام [پھَیلایا] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مذکر، جمع',
                'example': 'وے کتوں کے کام [پھَیلائے] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، واحد',
                'example': 'وہ بلی چیز [پھَیلائی] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، جمع',
                'example': 'وے بلیاں چیزیں [پھَیلائِیں] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'احتمالی، کہنے والا، واحد',
                'example': 'میں وہ [پھَیلاؤں] ہوں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، کہنے والا، جمع',
                'example': 'ہم وہ [پھَیلائیں] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، واحد',
                'example': 'تو وہ [پھَیلائے] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، جمع',
                'example': 'تم وہ [پھَیلاؤ] ہو۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، واحد',
                'example': 'وہ یہ [پھَیلائے] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، جمع',
                'example': 'وے یہ [پھَیلائیں] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'مشروط، کہنے والا، مذکر، واحد',
                'example': 'میں وہ [پھَیلاؤں‌گا] ہوں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مذکر، جمع',
                'example': 'ہم وہ [پھَیلائیں‌گے] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، واحد',
                'example': 'میں وہ [پھَیلاؤں‌گی] ہوں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، جمع',
                'example': 'ہم وہ [پھَیلائیں‌گی] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، واحد',
                'example': 'تو وہ [پھَیلائےگا] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، جمع',
                'example': 'تم وہ [پھَئلاؤگے] ہو۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، واحد',
                'example': 'تو وہ [پھَیلائےگی] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، جمع',
                'example': 'تم وہ [پھَیلاؤگی] ہو۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، واحد',
                'example': 'کتا وہ [پھَیلائےگا] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، جمع',
                'example': 'کتے وہ [پھَیلائیں‌گے] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، واحد',
                'example': 'بلی وہ [پھَیلائےگی] ہے۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، جمع',
                'example': 'بلیاں وہ [پھَیلائیں‌گی] ہیں۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'عام امر، واحد',
                'example': 'تو یہ [پھَیلا]۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'عام امر، جمع',
                'example': 'تم یہ [پھَیلاؤ]۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، واحد',
                'example': 'تو یہ [پھَیلایو]۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، جمع',
                'example': 'تم یہ [پھَیلائیے]۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'پکا امر',
                'example': 'تم یہ [پھَیلائیےگا]۔',
                'grammatical_features_item_ids': [additive_phase, transitive_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([additive_phase, transitive_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
    },

    'hindustani-verb-additive-causative-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی فعل متعدی کا تعدیہ',
        'language': language_Urdu,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'اسمِ مصدر، فاعلی',
                'example': 'مجھے انہیں روٹی [کھِلانا] پسند ہے۔',
                'grammatical_features_item_ids': [causative_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'اسمِ مصدر، مفعولی',
                'example': 'مجھے ان روٹی [کھِلانے] کے لیے کرتا ہوں۔',
                'grammatical_features_item_ids': [causative_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'معطوف',
                'example': 'ہم بچوں کو [کھِلا] سکتے ہیں۔',
                'grammatical_features_item_ids': [causative_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، متعلق',
                'example': 'اس نے بچوں کو [کھِلا کے] رہے ہیں۔',
                'grammatical_features_item_ids': [causative_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، ترکیبِ متعلق',
                'example': 'اس نے بچوں کو [کھِلا کر] رہے ہیں۔',
                'grammatical_features_item_ids': [causative_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'شکی، مذکر، واحد',
                'example': 'اس نے بچے کو پکوڑا نہ [کھِلانا] ہے۔',
                'grammatical_features_item_ids': [causative_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مذکر، جمع',
                'example': 'اس نے بچوں کو پکوڑے نہ [کھِلانے] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، واحد',
                'example': 'اس نے بچے کو روٹی نہ [کھِلانی] ہے۔',
                'grammatical_features_item_ids': [causative_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، جمع',
                'example': 'اس نے بچوں کو روٹیاں نہ [کھِلانِیں] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'استمراری، مذکر، واحد',
                'example': 'اس نے بچے کو پکوڑا نہ [کھِلاتا] ہے۔',
                'grammatical_features_item_ids': [causative_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مذکر، جمع',
                'example': 'اس نے بچوں کو پکوڑے نہ [کھِلاتے] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، واحد',
                'example': 'اس نے بچے کو روٹی نہ [کھِلاتی] ہے۔',
                'grammatical_features_item_ids': [causative_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، جمع',
                'example': 'اس نے بچوں کو روٹیاں نہ [کھِلاتِیں] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'بعید، مذکر، واحد',
                'example': 'اس نے بچے کو پکوڑا نہ [کھِلایا] ہے۔',
                'grammatical_features_item_ids': [causative_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مذکر، جمع',
                'example': 'اس نے بچوں کو پکوڑے نہ [کھِلائے] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، واحد',
                'example': 'اس نے بچے کو روٹی نہ [کھِلائی] ہے۔',
                'grammatical_features_item_ids': [causative_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، جمع',
                'example': 'اس نے بچوں کو روٹیاں نہ [کھِلائِیں] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'احتمالی، کہنے والا، واحد',
                'example': 'میں بچوں کو [کھِلاؤں] ہوں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، کہنے والا، جمع',
                'example': 'ہم بچوں کو [کھِلائیں] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، واحد',
                'example': 'تو بچوں کو [کھِلائے] ہے۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، جمع',
                'example': 'تم بچوں کو [کھِلاؤ] ہو۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، واحد',
                'example': 'وہ بچوں کو [کھِلائے] ہے۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، جمع',
                'example': 'وے بچوں کو [کھِلائیں] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'مشروط، کہنے والا، مذکر، واحد',
                'example': 'میں بچوں کو [کھِلاؤں‌گا] ہوں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مذکر، جمع',
                'example': 'ہم بچوں کو [کھِلائیں‌گے] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، واحد',
                'example': 'میں بچوں کو [کھِلاؤں‌گی] ہوں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، جمع',
                'example': 'ہم بچوں کو [کھِلائیں‌گی] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، واحد',
                'example': 'تو بچوں کو [کھِلائےگا] ہے۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، جمع',
                'example': 'تم بچوں کو [کھِلاؤگے] ہو۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، واحد',
                'example': 'تو بچوں کو [کھِلائےگی] ہے۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، جمع',
                'example': 'تم بچوں کو [کھِلاؤگی] ہو۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، واحد',
                'example': 'مرد بچوں کو [کھِلائےگا] ہے۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، جمع',
                'example': 'مرد بچوں کو [کھِلائیں‌گے] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، واحد',
                'example': 'عورت بچوں کو [کھِلائےگی] ہے۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، جمع',
                'example': 'عورتیں بچوں کو [کھِلائیں‌گی] ہیں۔',
                'grammatical_features_item_ids': [causative_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'عام امر، واحد',
                'example': 'تو بچوں کو [کھِلا]۔',
                'grammatical_features_item_ids': [causative_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'عام امر، جمع',
                'example': 'تم بچوں کو [کھِلاؤ]۔',
                'grammatical_features_item_ids': [causative_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، واحد',
                'example': 'تو بچوں کو [کھِلایو]۔',
                'grammatical_features_item_ids': [causative_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، جمع',
                'example': 'تم بچوں کو [کھِلائیے]۔',
                'grammatical_features_item_ids': [causative_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'پکا امر',
                'example': 'تم بچوں کو [کھِلائیےگا]۔',
                'grammatical_features_item_ids': [causative_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
    },

    'hindustani-verb-additive-causative-double-ur': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindustani'},
        'label': 'ہندوستانی فعل متعدی کا دوسرا تعدیہ',
        'language': language_Urdu,
        'lexical_category_item_id': verb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'اسمِ مصدر، فاعلی',
                'example': 'انہیں ہمارا روٹی [کھِلوانا] اچھا لگتا ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, gerund, direct_case],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'اسمِ مصدر، مفعولی',
                'example': 'انہیں ہمارے روٹی [کھِلوانے] کے لیے کرتا ہوں۔',
                'grammatical_features_item_ids': [double_causative_phase, gerund, oblique_case],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'معطوف',
                'example': 'اس نے نوکرانی سے بچوں کو [کھِلوا] سکتے ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, conjunctive_participle],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، متعلق',
                'example': 'اس نے نوکرانی سے بچوں کو [کھِلوا کے] رہے ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, conjunctive_participle, adverbial],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'label': 'معطوف، ترکیبِ متعلق',
                'example': 'اس نے نوکرانی سے بچوں کو [کھِلوا کر] رہے ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, conjunctive_participle, adverbial, absolute_construction],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, continuative),
            },
            {
                'section_break': True,
                'label': 'شکی، مذکر، واحد',
                'example': 'اس نے نوکرانی سے بچے کو پکوڑا نہ [کھِلوانا] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, potential_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مذکر، جمع',
                'example': 'اس نے نوکرانی سے بچوں کو پکوڑے نہ [کھِلوانے] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, potential_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، واحد',
                'example': 'اس نے نوکرانی سے بچے کو روٹی نہ [کھِلوانی] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, potential_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'شکی، مؤنث، جمع',
                'example': 'اس نے نوکرانی سے بچوں کو روٹیاں نہ [کھِلوانِیں] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, potential_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, prospective),
            },
            {
                'label': 'استمراری، مذکر، واحد',
                'example': 'اس نے نوکرانی سے بچے کو پکوڑا نہ [کھِلواتا] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, imperfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مذکر، جمع',
                'example': 'اس نے نوکرانی سے بچوں کو پکوڑے نہ [کھِلواتے] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, imperfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، واحد',
                'example': 'اس نے نوکرانی سے بچے کو روٹی نہ [کھِلواتی] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, imperfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'استمراری، مؤنث، جمع',
                'example': 'اس نے نوکرانی سے بچوں کو روٹیاں نہ [کھِلواتِیں] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, imperfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, habitual),
            },
            {
                'label': 'بعید، مذکر، واحد',
                'example': 'اس نے نوکرانی سے بچے کو پکوڑا نہ [کھِلوایا] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, perfect_participle, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مذکر، جمع',
                'example': 'اس نے نوکرانی سے بچوں کو پکوڑے نہ [کھِلوائے] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, perfect_participle, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، واحد',
                'example': 'اس نے نوکرانی سے بچے کو روٹی نہ [کھِلوائی] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, perfect_participle, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'label': 'بعید، مؤنث، جمع',
                'example': 'اس نے نوکرانی سے بچوں کو روٹیاں نہ [کھِلوائِیں] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, perfect_participle, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, retrospective),
            },
            {
                'section_break': True,
                'label': 'احتمالی، کہنے والا، واحد',
                'example': 'میں نے نوکرانی سے بچوں کو [کھِلواؤں] ہوں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, first_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، کہنے والا، جمع',
                'example': 'ہم نے نوکرانی سے بچوں کو [کھِلوائیں] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, first_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، واحد',
                'example': 'تو نے نوکرانی سے بچوں کو [کھِلوائے] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, second_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، سننے والا، جمع',
                'example': 'تم نے نوکرانی سے بچوں کو [کھِلواؤ] ہو۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, second_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، واحد',
                'example': 'اس نے نوکرانی سے بچوں کو [کھِلوائے] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, third_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'احتمالی، انیہ، جمع',
                'example': 'انہیں نوکارنی سے بچوں کو [کھِلوائیں] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, third_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'مشروط، کہنے والا، مذکر، واحد',
                'example': 'میں نے نوکرانی سے بچوں کو [کھِلواؤں‌گا] ہوں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, first_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مذکر، جمع',
                'example': 'ہم نے نوکرانی سے بچوں کو [کھِلوائیں‌گے] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, first_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، واحد',
                'example': 'میں نے نوکرانی سے بچوں کو [کھِلواؤں‌گی] ہوں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, first_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، کہنے والا، مؤنث، جمع',
                'example': 'ہم نے نوکرانی سے بچوں کو [کھِلوائیں‌گی] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, first_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، واحد',
                'example': 'تو نے نوکرانی سے بچوں کو [کھِلوائےگا] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, second_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مذکر، جمع',
                'example': 'تم نے نوکرانی سے بچوں کو [کھِلواؤگے] ہو۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, second_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، واحد',
                'example': 'تو نے نوکرانی سے بچوں کو [کھِلائےگی] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, second_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، سننے والا، مؤنث، جمع',
                'example': 'تم نے نوکرانی سے بچوں کو [کھِلواؤگی] ہو۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, second_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، واحد',
                'example': 'مرد نے نوکرانی سے بچوں کو [کھِلوائےگا] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, third_person, masculine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مذکر، جمع',
                'example': 'مردوں نے نوکرانی سے بچوں کو [کھِلوائیں‌گے] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, third_person, masculine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، واحد',
                'example': 'عورت نے نوکرانی سے بچوں کو [کھِلوائےگی] ہے۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, third_person, feminine, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'مشروط، انیہ، مؤنث، جمع',
                'example': 'عورتوں نے نوکرانی سے بچوں کو [کھِلوائیں‌گی] ہیں۔',
                'grammatical_features_item_ids': [double_causative_phase, subjunctive, definite, third_person, feminine, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'section_break': True,
                'label': 'عام امر، واحد',
                'example': 'تو نوکرانی سے بچوں کو [کھِلوا]۔',
                'grammatical_features_item_ids': [double_causative_phase, imperative, second_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'عام امر، جمع',
                'example': 'تم نوکرانی سے بچوں کو [کھِلواؤ]۔',
                'grammatical_features_item_ids': [double_causative_phase, imperative, second_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، واحد',
                'example': 'تو نوکرانی سے بچوں کو [کھِلوایو]۔',
                'grammatical_features_item_ids': [double_causative_phase, imperative, suggestive, second_person, singular],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'تجویز کا امر، جمع',
                'example': 'تم نوکرانی سے بچوں کو [کھِلوائیے]۔',
                'grammatical_features_item_ids': [double_causative_phase, imperative, suggestive, second_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
            {
                'label': 'پکا امر',
                'example': 'تم نوکرانی سے بچوں کو [کھِلوائیےگا]۔',
                'grammatical_features_item_ids': [double_causative_phase, imperative, definite, second_person, plural],
                'grammatical_features_item_ids_optional': set([double_causative_phase]),
                'statements': statements(grammatical_aspect, 'novalue'),
            },
        ],
    },

    'hindko-noun-masculine': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindko'},
        'label': 'ہندکو اِسم مذکر',
        'language': language_Hindko,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'واحد، فاعلی',
                'example': 'ایہہ [بٹّہ] اے۔',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'جمع، فاعلی',
                'example': 'ایہہ [بٹّے] نیں۔',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'واحد، مفعولی',
                'example': 'میں [بٹّے] آں ویکھیا۔',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'جمع، مفعولی',
                'example': 'میں [بٹّیاں] آں ویکھے۔',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'hindko-noun-feminine': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Hindko'},
        'label': 'ہندکو اِسم مونث',
        'language': language_Hindko,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'واحد، فاعلی',
                'example': 'او اساں دی [تحصِیل] اے۔',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'جمع، فاعلی',
                'example': 'اوہ اساں دیاں [تحصِیلاں] نیں۔',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'واحد، مفعولی',
                'example': 'اِس [تحصِیلی] کول او گیا اے۔',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'جمع، مفعولی',
                'example': 'انہاں [تحصِیلاں] کول اوہ گئے نیں۔',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'croatian-noun-masculine': {
        '@attribution': {'users': ['Ivi104'], 'title': 'Wikidata:Wikidata Lexeme Forms/Croatian'},
        'label': 'hrvatske imenice (muški rod)',
        'language': language_Croatian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'nominativ jednine',
                'example': 'Ovo je [miš].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'genitiv jednine',
                'example': 'Nema [miša].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'dativ jednine',
                'example': 'Prilazim [mišu].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'akuzativ jednine',
                'example': 'Vidim [miša].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'vokativ jednine',
                'example': 'Zar i ti, [mišu]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'lokativ jednine',
                'example': 'Govorim o [mišu].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': 'instrumental jednine',
                'example': 'Vozim se s(a) [mišem].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'nominativ množine',
                'example': 'Ovo su [miševi].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'genitiv množine',
                'example': 'Nema [miševa].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'dativ množine',
                'example': 'Prilazim [miševima].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'akuzativ množine',
                'example': 'Vidim [miševe].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'vokativ množine',
                'example': 'Zar i vi, [miševi]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
            {
                'label': 'lokativ množine',
                'example': 'Govorim o [miševima].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': 'instrumental množine',
                'example': 'Vozim se s(a) [miševima].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'croatian-noun-feminine': {
        '@attribution': {'users': ['Ivi104'], 'title': 'Wikidata:Wikidata Lexeme Forms/Croatian'},
        'label': 'hrvatske imenice (ženski rod)',
        'language': language_Croatian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'nominativ jednine',
                'example': 'Ovo je [žirafa].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'genitiv jednine',
                'example': 'Nema [žirafe].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'dativ jednine',
                'example': 'Prilazim [žirafi].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'akuzativ jednine',
                'example': 'Vidim [žirafu].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'vokativ jednine',
                'example': 'Zar i ti, [žirafo]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'lokativ jednine',
                'example': 'Govorim o [žirafi].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': 'instrumental jednine',
                'example': 'Vozim se s(a) [žirafom].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'nominativ množine',
                'example': 'Ovo su [žirafe].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'genitiv množine',
                'example': 'Nema [žirafa].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'dativ množine',
                'example': 'Prilazim [žirafama].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'akuzativ množine',
                'example': 'Vidim [žirafe].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'vokativ množine',
                'example': 'Zar i vi, [žirafe]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
            {
                'label': 'lokativ množine',
                'example': 'Govorim o [žirafama].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': 'instrumental množine',
                'example': 'Vozim se s(a) [žirafama].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'croatian-noun-neuter': {
        '@attribution': {'users': ['Ivi104'], 'title': 'Wikidata:Wikidata Lexeme Forms/Croatian'},
        'label': 'hrvatske imenice (srednji rod)',
        'language': language_Croatian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'nominativ jednine',
                'example': 'Ovo je [staklo].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'genitiv jednine',
                'example': 'Nema [stakla].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'dativ jednine',
                'example': 'Prilazim [staklu].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'akuzativ jednine',
                'example': 'Vidim [staklo].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'vokativ jednine',
                'example': 'Zar i ti, [staklo]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'lokativ jednine',
                'example': 'Govorim o [staklu].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': 'instrumental jednine',
                'example': 'Vozim se s(a) [staklom].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'nominativ množine',
                'example': 'Ovo su [stakla].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'genitiv množine',
                'example': 'Nema [stakala].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'dativ množine',
                'example': 'Prilazim [staklima].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'akuzativ množine',
                'example': 'Vidim [stakla].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'vokativ množine',
                'example': 'Zar i vi, [stakla]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
            {
                'label': 'lokativ množine',
                'example': 'Govorim o [staklima].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': 'instrumental množine',
                'example': 'Vozim se s(a) [staklima].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'armenian-noun': {
        '@attribution': {'users': ['Emptyfear'], 'title': 'Wikidata:Wikidata Lexeme Forms/Armenian'},
        'label': 'հայերեն գոյական',
        'language': language_Armenian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'եզ․ թիվ, ուղղ․ հոլով',
                'example': 'սա [փողոց] է',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'եզ․ թիվ, սեռ․ հոլով',
                'example': '[փողոցի] նշանակությունը',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'եզ․ թիվ, տր․ հոլով',
                'example': '[փողոցին] նայել',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'եզ․ թիվ, հայց․ հոլով',
                'example': 'տեսնում եմ [փողոց]։',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'եզ․ թիվ, գործ․ հոլով',
                'example': '[փողոցով] գնալ',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'եզ․ թիվ, բաց․ հոլով',
                'example': '[փողոցից] հեռանալ',
                'grammatical_features_item_ids': [ablative_case, singular],
            },
            {
                'label': 'եզ․ թիվ, ներգ․ հոլով',
                'example': '[փողոցում] ապրել',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': 'հոգ․ թիվ, ուղղ․ հոլով',
                'example': 'սրանք [փողոցներ] են',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'հոգ․ թիվ, սեռ․ հոլով',
                'example': 'բազմաթիվ [փողոցների] նշանակությունը',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'հոգ․ թիվ, տր․ հոլով',
                'example': '[փողոցներին] նայել',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'հոգ․ թիվ, հայց․ հոլով',
                'example': 'տեսնում եմ շատ [փողոցներ]',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'հոգ․ թիվ, գործ․ հոլով',
                'example': 'բոլոր [փողոցներով] գնալ',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
            {
                'label': 'հոգ․ թիվ, բաց․ հոլով',
                'example': 'բոլոր [փողոցներից] հեռանալ',
                'grammatical_features_item_ids': [ablative_case, plural],
            },
            {
                'label': 'հոգ․ թիվ, ներգ․ հոլով',
                'example': 'տարբեր [փողոցներում] ապրել',
                'grammatical_features_item_ids': [locative_case, plural],
            },
        ],
    },

    'armenian-noun-singulare-tantum': {
        '@attribution': {'users': ['Emptyfear'], 'title': 'Wikidata:Wikidata Lexeme Forms/Armenian'},
        'label': 'հայերեն հավաքական անհոգնական եզակի գոյական',
        'language': language_Armenian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'եզ․ թիվ, ուղղ․ հոլով',
                'example': 'սա [կաթ] է',
                'grammatical_features_item_ids': [nominative_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'եզ․ թիվ, սեռ․ հոլով',
                'example': '[կաթի] նշանակությունը',
                'grammatical_features_item_ids': [genitive_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'եզ․ թիվ, տր․ հոլով',
                'example': '[կաթին] ավելացնել',
                'grammatical_features_item_ids': [dative_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'եզ․ թիվ, հայց․ հոլով',
                'example': 'ռեսնում եմ [կաթ]',
                'grammatical_features_item_ids': [accusative_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'եզ․ թիվ, գործ․ հոլով',
                'example': '[կաթով] պատրաստել',
                'grammatical_features_item_ids': [instrumental_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'եզ․ թիվ, բաց․ հոլով',
                'example': '[կաթից] առանձնացնել',
                'grammatical_features_item_ids': [ablative_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
            {
                'label': 'եզ․ թիվ, ներգ․ հոլով',
                'example': '[կաթում] լողալ',
                'grammatical_features_item_ids': [locative_case, singular],
                'grammatical_features_item_ids_optional': set([singular]),
            },
        ],
        'statements': statements(instance_of, singulare_tantum),
    },

    'igbo-noun': {
        '@attribution': {'users': ['EnaldoSS', 'Tochiprecious'], 'title': 'Wikidata:Wikidata Lexeme Forms/Igbo'},
        'label': 'Aha n\'Igbo',
        'language': language_Igbo,
        'lexical_category_item_id': noun,
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
        'language': language_Igbo,
        'lexical_category_item_id': verb,
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
        'language': language_Igbo,
        'lexical_category_item_id': pronoun,
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
        'language': language_Igbo,
        'lexical_category_item_id': adjective,
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
        'language': language_Italian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singolare',
                'example': 'Questa è una [rosa].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'plurale',
                'example': 'Queste sono delle [rose].',
                'grammatical_features_item_ids': [plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'italian-noun-masculine': {
        '@attribution': {'users': ['Sannita'], 'title': 'Wikidata:Wikidata Lexeme Forms/Italian'},
        'label': 'sostantivo maschile italiano',
        'language': language_Italian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'singolare',
                'example': 'Questo è un [cane].',
                'grammatical_features_item_ids': [singular],
            },
            {
                'label': 'plurale',
                'example': 'Questi sono dei [cani].',
                'grammatical_features_item_ids': [plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'italian-adjective': {
        '@attribution': {'users': ['Sannita'], 'title': 'Wikidata:Wikidata Lexeme Forms/Italian'},
        'label': 'aggettivo qualificativo italiano',
        'language': language_Italian,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'maschile singolare',
                'example': 'Il panino è [buono].',
                'grammatical_features_item_ids': [masculine, singular],
            },
            {
                'label': 'maschile plurale',
                'example': 'I panini sono [buoni].',
                'grammatical_features_item_ids': [masculine, plural],
            },
            {
                'label': 'femminile singolare',
                'example': 'La maestra è [buona].',
                'grammatical_features_item_ids': [feminine, singular],
            },
            {
                'label': 'femminile plurale',
                'example': 'Le maestre sono [buone].',
                'grammatical_features_item_ids': [feminine, plural],
            },
        ],
    },

    'kurmanji-noun-feminine': {
        '@attribution': {'users': ['Şêr'], 'title': 'Wikidata:Wikidata Lexeme Forms/Kurdish (Kurmancî)'},
        'label': 'navdêra kurdî (mê)',
        'language': language_Kurmanji,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Rewşa navkî ya yekjimar a binavkirî',
                'example': 'Ev [pisîk] e.',
                'grammatical_features_item_ids': [direct_case, singular, definite],
            },
            {
                'label': 'Rewşa navkî ya pirjimar a binavkirî',
                'example': 'Ev [pisîk] in.',
                'grammatical_features_item_ids': [direct_case, plural, definite],
            },
            {
                'section_break': True,
                'label': 'Rewşa çemandî ya yekjimar a binavkirî',
                'example': 'Ez [pisîkê] dibînim.',
                'grammatical_features_item_ids': [oblique_case, singular, definite],
            },
            {
                'label': 'Rewşa çemandî ya pirjimar ya binavkirî',
                'example': 'Ez [pisîkan] dibînim.',
                'grammatical_features_item_ids': [oblique_case, plural, definite],
            },
            {
                'section_break': True,
                'label': 'Rewşa îzafe ya yekjimar a binavkirî',
                'example': 'Ev [pisîka] nû ye.',
                'grammatical_features_item_ids': [ezāfe, singular, definite],
            },
            {
                'label': 'Rewşa îzafe ya pirjimar a binavkirî',
                'example': 'Ev [pisîkên] nû ne.',
                'grammatical_features_item_ids': [ezāfe, plural, definite],
            },
            {
                'section_break': True,
                'label': 'Rewşa navkî ya yekjimar a nebinavkirî',
                'example': 'Ev [pisîkek] e.',
                'grammatical_features_item_ids': [direct_case, singular, indefinite],
            },
            {
                'label': 'Rewşa navkî ya pirjimar a nebinavkirî',
                'example': 'Ev [pisîkin] in.',
                'grammatical_features_item_ids': [direct_case, plural, indefinite],
            },
            {
                'section_break': True,
                'label': 'Rewşa çemandî ya yekjimar ya nebinavkirî',
                'example': 'Ez [pisîkekê] dibînim.',
                'grammatical_features_item_ids': [oblique_case, singular, indefinite],
            },
            {
                'label': 'Rewşa çemandî ya pirjimar ya nebinavkirî',
                'example': 'Ez [pisîkinan] dibînim.',
                'grammatical_features_item_ids': [oblique_case, plural, indefinite],
            },
            {
                'section_break': True,
                'label': 'Rewşa îzafe ya yekjimar a nebinavkirî',
                'example': 'Ev [pisîkeke] nû ye.',
                'grammatical_features_item_ids': [ezāfe, singular, indefinite],
            },
            {
                'label': 'Rewşa îzafe ya pirjimar a nebinavkirî',
                'example': 'Ez [pisîkine] nû dibînim.',
                'grammatical_features_item_ids': [ezāfe, plural, indefinite],
            },
            {
                'section_break': True,
                'label': 'Rewşa gazîkirinê ya yekjimar',
                'example': 'Silav [pisîkê]!',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'Rewşa gazîkirinê ya pirjimar',
                'example': 'Silav [pisîkino]!',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'kurmanji-noun-masculine': {
        '@attribution': {'users': ['Şêr'], 'title': 'Wikidata:Wikidata Lexeme Forms/Kurdish (Kurmancî)'},
        'label': 'navdêra kurdî (nêr)',
        'language': language_Kurmanji,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Rewşa navkî ya yekjimar a binavkirî',
                'example': 'Ev [gund] e.',
                'grammatical_features_item_ids': [direct_case, singular, definite],
            },
            {
                'label': 'Rewşa navkî ya pirjimar a binavkirî',
                'example': 'Ev [gund] in.',
                'grammatical_features_item_ids': [direct_case, plural, definite],
            },
            {
                'section_break': True,
                'label': 'Rewşa çemandî ya yekjimar a binavkirî',
                'example': 'Ez [gundî] dibînim.',
                'grammatical_features_item_ids': [oblique_case, singular, definite],
            },
            {
                'label': 'Rewşa çemandî ya pirjimar ya binavkirî',
                'example': 'Ez [gundan] dibînim.',
                'grammatical_features_item_ids': [oblique_case, plural, definite],
            },
            {
                'section_break': True,
                'label': 'Rewşa îzafe ya yekjimar a binavkirî',
                'example': 'Ev [gundê] kevn e.',
                'grammatical_features_item_ids': [ezāfe, singular, definite],
            },
            {
                'label': 'Rewşa îzafe ya pirjimar a binavkirî',
                'example': 'Ev [gundên] nû kevn in.',
                'grammatical_features_item_ids': [ezāfe, plural, definite],
            },
            {
                'section_break': True,
                'label': 'Rewşa navkî ya yekjimar a nebinavkirî',
                'example': 'Ev [gundek] e.',
                'grammatical_features_item_ids': [direct_case, singular, indefinite],
            },
            {
                'label': 'Rewşa navkî ya pirjimar a nebinavkirî',
                'example': 'Ev [gundin] in.',
                'grammatical_features_item_ids': [direct_case, plural, indefinite],
            },
            {
                'section_break': True,
                'label': 'Rewşa çemandî ya yekjimar ya nebinavkirî',
                'example': 'Ez [gundekî] dibînim.',
                'grammatical_features_item_ids': [oblique_case, singular, indefinite],
            },
            {
                'label': 'Rewşa çemandî ya pirjimar ya nebinavkirî',
                'example': 'Ez [gundinan] dibînim.',
                'grammatical_features_item_ids': [oblique_case, plural, indefinite],
            },
            {
                'section_break': True,
                'label': 'Rewşa îzafe ya yekjimar a nebinavkirî',
                'example': 'Ev [gundekî] nû ye.',
                'grammatical_features_item_ids': [ezāfe, singular, indefinite],
            },
            {
                'label': 'Rewşa îzafe ya pirjimar a nebinavkirî',
                'example': 'Ez [gundine] nû dibînim.',
                'grammatical_features_item_ids': [ezāfe, plural, indefinite],
            },
            {
                'section_break': True,
                'label': 'Rewşa gazîkirinê ya yekjimar',
                'example': 'Silav [bavo]!',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'Rewşa gazîkirinê ya pirjimar',
                'example': 'Silav [bavino]!',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'latin-noun-masculine': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
        'label': 'nomen Latinum (masculinum)',
        'language': language_Latin,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [puer].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [pueri].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'dativus singularis',
                'example': 'Pater [puero] favet.',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puella ad [puerum] adit.',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puella cum [puero] ludet.',
                'grammatical_features_item_ids': [ablative_case, singular],
            },
            {
                'label': 'vocativus singularis',
                'example': 'Et tu, [puer]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [pueri].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [puerorum].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Pater [pueris] favet.',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puella ad [pueros] adit.',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puella cum [pueris] ludet.',
                'grammatical_features_item_ids': [ablative_case, plural],
            },
            {
                'label': 'vocativus pluralis',
                'example': 'Et vos, [pueri]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'latin-noun-feminine': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
        'label': 'nomen Latinum (femininum)',
        'language': language_Latin,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [puella].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [puellae].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'dativus singularis',
                'example': 'Mater [puellae] favet.',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puer ad [puellam] adit.',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puer cum [puella] ludet.',
                'grammatical_features_item_ids': [ablative_case, singular],
            },
            {
                'label': 'vocativus singularis',
                'example': 'Et tu, [puella]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [puellae].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [puellarum].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Mater [puellis] favet.',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puer ad [puellas] adit.',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puer cum [puellis] ludet.',
                'grammatical_features_item_ids': [ablative_case, plural],
            },
            {
                'label': 'vocativus pluralis',
                'example': 'Et vos, [puellae]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'latin-noun-neuter': {
        '@attribution': {'users': ['Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latin'},
        'label': 'nomen Latinum (neutrum)',
        'language': language_Latin,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'nominativus singularis',
                'example': 'Id est [forum].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'genitivus singularis',
                'example': 'Proprietas [fori].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'dativus singularis',
                'example': 'Pater [foro] favet.',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'accusativus singularis',
                'example': 'Puer ad [forum] adit.',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'ablativus singularis',
                'example': 'Puer cum [foro] ludet.',
                'grammatical_features_item_ids': [ablative_case, singular],
            },
            {
                'label': 'vocativus singularis',
                'example': 'Et tu, [forum]?',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'nominativus pluralis',
                'example': 'Id sunt [fora].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'genitivus pluralis',
                'example': 'Proprietas [fororum].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'dativus pluralis',
                'example': 'Pater [foris] favet.',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'accusativus pluralis',
                'example': 'Puer ad [fora] adit.',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'ablativus pluralis',
                'example': 'Puer cum [foris] ludet.',
                'grammatical_features_item_ids': [ablative_case, plural],
            },
            {
                'label': 'vocativus pluralis',
                'example': 'Et vos, [fora]?',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'latvian-noun-masculine': {
        '@attribution': {'users': ['Papuass', 'Lucas Werkmeister', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latvian'},
        'label': 'latviešu valodas vīriešu dzimtes lietvārds',
        'language': language_Latvian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'vienskaitļa nominatīvs',
                'example': 'Šis ir [suns].',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'daudzskaitļa nominatīvs',
                'example': 'Šie ir [suņi].',
                'grammatical_features_item_ids': [plural, nominative_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa ģenitīvs',
                'example': 'Šī ir [suņa] aste.',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'daudzskaitļa ģenitīvs',
                'example': 'Šīs ir [suņu] astes.',
                'grammatical_features_item_ids': [plural, genitive_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa datīvs',
                'example': 'Manam [sunim] ir aste.',
                'grammatical_features_item_ids': [singular, dative_case],
            },
            {
                'label': 'daudzskaitļa datīvs',
                'example': 'Maniem [suņiem] ir aste.',
                'grammatical_features_item_ids': [plural, dative_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa akuzatīvs',
                'example': 'Aste luncina [suni].',
                'grammatical_features_item_ids': [singular, accusative_case],
            },
            {
                'label': 'daudzskaitļa akuzatīvs',
                'example': 'Aste luncina [suņus].',
                'grammatical_features_item_ids': [plural, accusative_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa instrumentālis',
                'example': 'Vislabāk ir [ar suni].',
                'grammatical_features_item_ids': [singular, instrumental_case],
            },
            {
                'label': 'daudzskaitļa instrumentālis',
                'example': 'Vislabāk ir [ar suņiem].',
                'grammatical_features_item_ids': [plural, instrumental_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa lokatīvs',
                'example': 'Katrā [sunī] blusu nav.',
                'grammatical_features_item_ids': [singular, locative_case],
            },
            {
                'label': 'daudzskaitļa lokatīvs',
                'example': 'Visos [suņos] blusu nav.',
                'grammatical_features_item_ids': [plural, locative_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa vokatīvs',
                'example': 'Hei, [suni]!',
                'grammatical_features_item_ids': [singular, vocative_case],
            },
            {
                'label': 'daudzskaitļa vokatīvs',
                'example': 'Hei, [suņi]!',
                'grammatical_features_item_ids': [plural, vocative_case],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'latvian-noun-feminine': {
        '@attribution': {'users': ['Papuass', 'Lucas Werkmeister', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Latvian'},
        'label': 'latviešu valodas sieviešu dzimtes lietvārds',
        'language': language_Latvian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'vienskaitļa nominatīvs',
                'example': 'Šī ir [roka].',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'daudzskaitļa nominatīvs',
                'example': 'Šīs ir [rokas].',
                'grammatical_features_item_ids': [plural, nominative_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa ģenitīvs',
                'example': 'Šie ir kreisās [rokas] pirksti.',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'daudzskaitļa ģenitīvs',
                'example': 'Šis ir [roku] krēms.',
                'grammatical_features_item_ids': [plural, genitive_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa datīvs',
                'example': 'Vienai [rokai] ir pieci pirksti.',
                'grammatical_features_item_ids': [singular, dative_case],
            },
            {
                'label': 'daudzskaitļa datīvs',
                'example': 'Abām [rokām] kopā ir desmit pirksti.',
                'grammatical_features_item_ids': [plural, dative_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa akuzatīvs',
                'example': 'Viņa paspieda [roku].',
                'grammatical_features_item_ids': [singular, accusative_case],
            },
            {
                'label': 'daudzskaitļa akuzatīvs',
                'example': 'Mazgā [rokas] ar ziepēm.',
                'grammatical_features_item_ids': [plural, accusative_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa instrumentālis',
                'example': 'Viņa pamāja [ar roku].',
                'grammatical_features_item_ids': [singular, instrumental_case],
            },
            {
                'label': 'daudzskaitļa instrumentālis',
                'example': 'Šo kreklu ir jāmazgā [ar rokām].',
                'grammatical_features_item_ids': [plural, instrumental_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa lokatīvs',
                'example': 'Karogs [rokā] un uz priekšu.',
                'grammatical_features_item_ids': [singular, locative_case],
            },
            {
                'label': 'daudzskaitļa lokatīvs',
                'example': 'Abās [rokās] ir cimdi.',
                'grammatical_features_item_ids': [plural, locative_case],
            },
            {
                'section_break': True,
                'label': 'vienskaitļa vokatīvs',
                'example': 'Hei, [roka]!',
                'grammatical_features_item_ids': [singular, vocative_case],
            },
            {
                'label': 'daudzskaitļa vokatīvs',
                'example': 'Hei, [rokas]!',
                'grammatical_features_item_ids': [plural, vocative_case],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'malayalam-noun': {
        '@attribution': {'users': ['Jsamwrites', 'Vis M', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Malayalam'},
        'label': 'മലയാളത്തിലെ സാധാരണ നാമം',
        'language': language_Malayalam,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'ഏകവചനം',
                'example': 'ഒരു [പശു].',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'ഏകവചനം പ്രതിഗ്രാഹിക',
                'example': 'ഞാൻ [പശുവിനെ] മെയ്ച്ചു',
                'grammatical_features_item_ids': [singular, accusative_case],
            },
            {
                'label': 'ഏകവചനം ഉദ്ദേശിക',
                'example': 'ഞാൻ [പശുവിന്] പുല്ലു കൊടുത്തു',
                'grammatical_features_item_ids': [singular, dative_case],
            },
            {
                'label': 'ഏകവചനം ആധാരിക',
                'example': '[പുഴയിൽ] കുളിച്ചു',
                'grammatical_features_item_ids': [singular, locative_case],
            },
            {
                'label': 'ഏകവചനം സംയോജിക',
                'example': '[അമ്മയോട്] സംസാരിച്ചു',
                'grammatical_features_item_ids': [singular, sociative_case],
            },
            {
                'label': 'ഏകവചനം പ്രയോജിക',
                'example': 'ചെടികൾ [പശുവാൽ] തിന്നപ്പെട്ടു',
                'grammatical_features_item_ids': [singular, instrumental_case],
            },
            {
                'label': 'ഏകവചനം സംബന്ധിക',
                'example': '[അമ്മയുടെ] സ്നേഹം',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'ഏകവചനം സംബോധിക',
                'example': '[അമ്മേ]!, നോക്കൂ.',
                'grammatical_features_item_ids': [singular, vocative_case],
                'optional': True,
            },
            {
                'label': 'ബഹുവചനം',
                'example': 'അനേകം [പശുക്കൾ].',
                'grammatical_features_item_ids': [plural, nominative_case],
            },
            {
                'label': 'ബഹുവചനം പ്രതിഗ്രാഹിക',
                'example': 'ഞാൻ [പശുക്കളെ] മെയ്ച്ചു',
                'grammatical_features_item_ids': [plural, accusative_case],
            },
            {
                'label': 'ബഹുവചനം ഉദ്ദേശിക',
                'example': 'ഞാൻ [പശുക്കൾക്ക്] പുല്ലു കൊടുത്തു',
                'grammatical_features_item_ids': [plural, dative_case],
            },
            {
                'label': 'ബഹുവചനം ആധാരിക',
                'example': 'പല [വയലുകളിൽ] കളിച്ചു',
                'grammatical_features_item_ids': [plural, locative_case],
            },
            {
                'label': 'ബഹുവചനം സംയോജിക',
                'example': '[കുട്ടികളോട്] പറഞ്ഞു',
                'grammatical_features_item_ids': [plural, sociative_case],
            },
            {
                'label': 'ബഹുവചനം പ്രയോജിക',
                'example': 'ചെടികൾ [പശുക്കളാൽ] തിന്നപ്പെട്ടു',
                'grammatical_features_item_ids': [plural, instrumental_case],
            },
            {
                'label': 'ബഹുവചനം സംബന്ധിക',
                'example': '[കുട്ടികളുടെ] പ്രവർത്തി',
                'grammatical_features_item_ids': [plural, genitive_case],
            },
            {
                'label': 'ബഹുവചനം സംബോധിക',
                'example': '[കുട്ടികളേ]!, അവിടെ പോകരുത്.',
                'grammatical_features_item_ids': [plural, vocative_case],
                'optional': True,
            },
        ],
    },

    'malayalam-noun-proper': {
        '@attribution': {'users': ['Vis M'], 'title': 'Wikidata:Wikidata Lexeme Forms/Malayalam'},
        'label': 'മലയാളം സംജ്ഞാനാമം (proper noun)',
        'language': language_Malayalam,
        'lexical_category_item_id': proper_noun,
        'forms': [
            {
                'label': 'ഏകവചനം',
                'example': '[സീത] പഠിക്കുന്നു.',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'ഏകവചനം പ്രതിഗ്രാഹിക',
                'example': 'ഞാൻ [സീതയെ] സഹായിച്ചു',
                'grammatical_features_item_ids': [singular, accusative_case],
            },
            {
                'label': 'ഏകവചനം ഉദ്ദേശിക',
                'example': 'ഞാൻ [സീതയ്ക്ക്] പണം അയച്ചു',
                'grammatical_features_item_ids': [singular, dative_case],
            },
            {
                'label': 'ഏകവചനം ആധാരിക',
                'example': 'ഞാൻ [കേരളത്തിൽ] എത്തി',
                'grammatical_features_item_ids': [singular, locative_case],
            },
            {
                'label': 'ഏകവചനം സംയോജിക',
                'example': 'ഞാൻ [സീതയോട്] വിവരം പറഞ്ഞു',
                'grammatical_features_item_ids': [singular, sociative_case],
            },
            {
                'label': 'ഏകവചനം പ്രയോജിക',
                'example': 'വാഹനം [സീതയാൽ] ഓടിക്കപ്പെട്ടു',
                'grammatical_features_item_ids': [singular, instrumental_case],
            },
            {
                'label': 'ഏകവചനം സംബന്ധിക',
                'example': '[സീതയുടെ] പണം',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'ഏകവചനം സംബോധിക',
                'example': '[സീതേ]!, നോക്കൂ.',
                'grammatical_features_item_ids': [singular, vocative_case],
                'optional': True,
            },
        ],
    },

    'malayalam-verb': {
        '@attribution': {'users': ['Vis M', 'Nikki'], 'title': 'Wikidata:Wikidata Lexeme Forms/Malayalam'},
        'label': 'മലയാളം ക്രിയ',
        'language': language_Malayalam,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'ഇൻഫിനിറ്റീവ്',
                'example': 'അവൾ [എഴുതുക] ആണ്',
                'grammatical_features_item_ids': [present_infinitive],
            },
            {
                'label': 'സാമാന്യ വർത്തമാനകാലം',
                'example': 'അവൾ [എഴുതുന്നു]',
                'grammatical_features_item_ids': [simple_present],
            },
            {
                'label': 'സാമാന്യ ഭൂതകാലം',
                'example': 'അവൾ [എഴുതി]',
                'grammatical_features_item_ids': [simple_past],
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
        'language': language_Bokmål,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'ubestemt entall',
                'example': 'Dette er en [båt].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bestemt entall',
                'example': 'Dette er [båten].',
                'grammatical_features_item_ids': [singular, definite],
            },
            {
                'label': 'ubestemt flertall',
                'example': 'Dette er noen [båter].',
                'grammatical_features_item_ids': [plural, indefinite],
            },
            {
                'label': 'bestemt flertall',
                'example': 'Dette er [båtene].',
                'grammatical_features_item_ids': [plural, definite],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'bokmål-noun-feminine': {
        '@attribution': {'users': ['Danmichaelo', 'Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål hunkjønnssubstantiv',
        'language': language_Bokmål,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'ubestemt entall',
                'example': 'Dette er ei [liste].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bestemt entall hunkjønn',
                'example': 'Dette er [lista].',
                'grammatical_features_item_ids': [singular, definite, feminine],
            },
            {
                'label': 'bestemt entall hankjønn',
                'example': 'Dette er [listen].',
                'grammatical_features_item_ids': [singular, definite, masculine],
            },
            {
                'label': 'ubestemt flertall',
                'example': 'Dette er noen [lister].',
                'grammatical_features_item_ids': [plural, indefinite],
            },
            {
                'label': 'bestemt flertall',
                'example': 'Dette er [listene].',
                'grammatical_features_item_ids': [plural, definite],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'bokmål-noun-neuter': {
        '@attribution': {'users': ['Danmichaelo'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål intetkjønnssubstantiv',
        'language': language_Bokmål,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'ubestemt entall',
                'example': 'Dette er et [hus].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bestemt entall',
                'example': 'Dette er [huset].',
                'grammatical_features_item_ids': [singular, definite],
            },
            {
                'label': 'ubestemt flertall',
                'example': 'Dette er noen [hus].',
                'grammatical_features_item_ids': [plural, indefinite],
            },
            {
                'label': 'bestemt flertall',
                'example': 'Dette er [husa].',
                'grammatical_features_item_ids': [plural, definite],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'bokmål-noun-masculine-neuter': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål han- og intetkjønnssubstantiv',
        'language': language_Bokmål,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'ubestemt entall',
                'example': 'Nå kommer en/et [rap].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bestemt entall, hankjønn',
                'example': 'Den [rapen] var ekkel.',
                'grammatical_features_item_ids': [singular, definite, masculine],
            },
            {
                'label': 'bestemt entall, intetkjønn',
                'example': 'Det [rapet] var ekkelt.',
                'grammatical_features_item_ids': [singular, definite, neuter],
            },
            {
                'label': 'ubestemt flertall, hankjønn',
                'example': 'Flere [raper] på rad.',
                'grammatical_features_item_ids': [plural, indefinite, masculine],
            },
            {
                # note: the part in parenetheses here is more usage instructions than label, could maybe be split into a different field later
                'label': 'ubestemt flertall, intetkjønn (utelat denne formen hvis den er identisk med den forrige, og fjern «hankjønn» fra forrige etter at leksemet er opprettet)',
                'example': 'Flere [rap] på rad.',
                'grammatical_features_item_ids': [plural, indefinite, neuter],
                'optional': True,
            },
            {
                'label': 'bestemt flertall, han- og intetkjønn',
                'example': 'Alle de illeluktende [rapene].',
                'grammatical_features_item_ids': [plural, definite, masculine, neuter],
            },
            {
                'label': 'bestemt flertall, intetkjønn',
                'example': 'Alle de illeluktende [rapa].',
                'grammatical_features_item_ids': [plural, definite, neuter],
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, masculine),
                statement(grammatical_gender, neuter),
            ],
        },
    },

    'bokmål-adjective': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål adjektiv',
        'language': language_Bokmål,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'ubestemt hankjønn og hunkjønn',
                'example': 'En [flink] person.',
                'grammatical_features_item_ids': [singular, indefinite, masculine, feminine],
            },
            {
                'label': 'ubestemt intetkjønn',
                'example': 'Et [flinkt] barn.',
                'grammatical_features_item_ids': [singular, indefinite, neuter],
            },
            {
                'label': 'bestemt entall',
                'example': 'Det [flinke] barnet.',
                'grammatical_features_item_ids': [singular, definite],
            },
            {
                'label': 'flertall',
                'example': 'Alle de [flinke] barna.',
                'grammatical_features_item_ids': [plural],
            },
            {
                'label': 'komparativ',
                'example': 'Barnet er [flinkere] enn meg.',
                'grammatical_features_item_ids': [comparative],
                'optional': True,
            },
            {
                'label': 'superlativ',
                'example': 'Barnet var aller [flinkest].',
                'grammatical_features_item_ids': [superlative],
                'optional': True,
            },
            {
                'label': 'superlativ, bestemt form',
                'example': 'Det aller [flinkeste] barnet.',
                'grammatical_features_item_ids': [superlative, definite],
                'optional': True,
            },
        ],
    },

    'bokmål-verb': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål verb',
        'language': language_Bokmål,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'infinitiv',
                'example': 'Å [hilse].',
                'grammatical_features_item_ids': [infinitive, active],
            },
            {
                'label': 'presens',
                'example': 'Jeg [hilser].',
                'grammatical_features_item_ids': [present_tense, active],
            },
            {
                'label': 'preteritum',
                'example': 'Jeg [hilste].',
                'grammatical_features_item_ids': [preterite],
            },
            {
                'label': 'presens perfektum',
                'example': 'Jeg har [hilst].',
                'grammatical_features_item_ids': [present_perfect],
            },
            {
                'label': 'imperativ',
                'example': 'Vennligst [hils] nå!',
                'grammatical_features_item_ids': [imperative],
            },
            {
                'label': 'perfektum partisipp, hankjønn og hunkjønn',
                'example': 'En [hilst] person.',
                'grammatical_features_item_ids': [past_participle, singular, indefinite, masculine, feminine],
            },
            {
                'label': 'perfektum partisipp, intetkjønn',
                'example': 'Et [hilst] barn.',
                'grammatical_features_item_ids': [past_participle, singular, indefinite, neuter],
            },
            {
                'label': 'perfektum partisipp, bestemt form',
                'example': 'Den [hilste] personen.',
                'grammatical_features_item_ids': [past_participle, singular, definite],
            },
            {
                'label': 'perfektum partisipp, flertall',
                'example': 'Mange [hilste] personer.',
                'grammatical_features_item_ids': [past_participle, plural],
            },
            {
                'label': 'presens partisipp',
                'example': 'En [hilsende] person.',
                'grammatical_features_item_ids': [present_participle],
            },
            {
                'label': 'passiv infinitiv',
                'example': 'X må ikke [hilses].',
                'grammatical_features_item_ids': [infinitive, passive],
            },
            {
                'label': 'passiv presens',
                'example': 'X [hilses] av meg.',
                'grammatical_features_item_ids': [present_tense, passive],
            },
        ],
    },

    'bokmål-verb-passive': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål s-verb',
        'language': language_Bokmål,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'infinitiv',
                'example': 'Det er bra å [trives].',
                'grammatical_features_item_ids': [infinitive, passive],
            },
            {
                'label': 'presens',
                'example': 'Jeg [trives] på skolen.',
                'grammatical_features_item_ids': [present_tense, passive],
            },
            {
                'label': 'preteritum',
                'example': 'Jeg [trivdes] med det.',
                'grammatical_features_item_ids': [preterite, passive],
            },
            {
                'label': 'presens perfektum',
                'example': 'Jeg har [trivdes] med å være der…',
                'grammatical_features_item_ids': [present_perfect, passive],
            },
            {
                'label': 'imperativ',
                'example': 'Vennligst [trives] nå!',
                'grammatical_features_item_ids': [imperative, passive],
            },
        ],
        'statements': statements(instance_of, passive_verb),
    },

    'bokmål-interjection': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål interjeksjon',
        'language': language_Bokmål,
        'lexical_category_item_id': interjection,
        'forms': [
            {
                'label': 'interjeksjon',
                'example': 'Kvinna sa [hei].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'bokmål-adverb': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Bokmål'},
        'label': 'bokmål adverb',
        'language': language_Bokmål,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'adverb',
                'example': 'Gutten snakket [mye].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'dutch-neuter-noun': 'dutch-noun-neuter',
    'dutch-noun-neuter': {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands onzijdig zelfstandig naamwoord',
        'language': language_Dutch,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'enkelvoud',
                'example': 'Dit is het [huis].',
                'grammatical_features_item_ids': [singular, neuter],
            },
            {
                'label': 'meervoud',
                'example': 'Dit zijn de [huizen].',
                'grammatical_features_item_ids': [plural],
            },
            {
                'label': 'verkleinwoord, enkelvoud',
                'example': 'Dit is het kleine [huisje].',
                'grammatical_features_item_ids': [diminutive, singular, neuter],
            },
            {
                'label': 'verkleinwoord, meervoud',
                'example': 'Dit zijn de kleine [huisjes].',
                'grammatical_features_item_ids': [diminutive, plural],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'dutch-masculine-noun': 'dutch-noun-masculine',
    'dutch-noun-masculine': {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands strikt mannelijk zelfstandig naamwoord',
        'language': language_Dutch,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'enkelvoud',
                'example': 'Dit is de [man].',
                'grammatical_features_item_ids': [singular, masculine],
            },
            {
                'label': 'meervoud',
                'example': 'Dit zijn de [mannen].',
                'grammatical_features_item_ids': [plural],
            },
            {
                'label': 'verkleinwoord, enkelvoud',
                'example': 'Dit is het kleine [mannetje].',
                'grammatical_features_item_ids': [diminutive, singular, neuter],
            },
            {
                'label': 'verkleinwoord, meervoud',
                'example': 'Dit zijn de kleine [mannetjes].',
                'grammatical_features_item_ids': [diminutive, plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'dutch-feminine-noun': 'dutch-noun-feminine',
    'dutch-noun-feminine': {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands strikt vrouwelijk zelfstandig naamwoord',
        'language': language_Dutch,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'enkelvoud',
                'example': 'Dit is de [vrouw].',
                'grammatical_features_item_ids': [singular, feminine],
            },
            {
                'label': 'meervoud',
                'example': 'Dit zijn de [vrouwen].',
                'grammatical_features_item_ids': [plural],
            },
            {
                'label': 'verkleinwoord, enkelvoud',
                'example': 'Dit is het kleine [vrouwtje].',
                'grammatical_features_item_ids': [diminutive, singular, neuter],
            },
            {
                'label': 'verkleinwoord, meervoud',
                'example': 'Dit zijn de kleine [vrouwtjes].',
                'grammatical_features_item_ids': [diminutive, plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'dutch-fem2masc-noun': 'dutch-noun-fem2masc',
    'dutch-noun-fem2masc': {
        '@attribution': {'users': ['MarcoSwart'], 'title': 'Wikidata:Wikidata Lexeme Forms/Dutch'},
        'label': 'Nederlands v/m zelfstandig naamwoord',
        'language': language_Dutch,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'enkelvoud',
                'example': 'Dit is de [tafel].',
                'grammatical_features_item_ids': [singular, f_m],
            },
            {
                'label': 'meervoud',
                'example': 'Dit zijn de [tafels].',
                'grammatical_features_item_ids': [plural],
            },
            {
                'label': 'verkleinwoord, enkelvoud',
                'example': 'Dit is het kleine [tafeltje].',
                'grammatical_features_item_ids': [diminutive, singular, neuter],
            },
            {
                'label': 'verkleinwoord, meervoud',
                'example': 'Dit zijn de kleine [tafeltjes].',
                'grammatical_features_item_ids': [diminutive, plural],
            },
        ],
        'statements': statements(grammatical_gender, f_m),
    },

    'nynorsk-noun-feminine': {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk hokjønnssubstantiv',
        'language': language_Nynorsk,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Dette er ei [liste].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bunde eintal',
                'example': 'Dette er [lista].',
                'grammatical_features_item_ids': [singular, definite],
            },
            {
                'label': 'ubunde fleirtal',
                'example': 'Dette er nokre [lister].',
                'grammatical_features_item_ids': [plural, indefinite],
            },
            {
                'label': 'bunde fleirtal',
                'example': 'Dette er [listene].',
                'grammatical_features_item_ids': [plural, definite],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'nynorsk-noun-masculine': {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk hankjønnssubstantiv',
        'language': language_Nynorsk,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Dette er ein [båt].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bunde eintal',
                'example': 'Dette er [båten].',
                'grammatical_features_item_ids': [singular, definite],
            },
            {
                'label': 'ubunde fleirtal',
                'example': 'Dette er nokre [båtar].',
                'grammatical_features_item_ids': [plural, indefinite],
            },
            {
                'label': 'bunde fleirtal',
                'example': 'Dette er [båtane].',
                'grammatical_features_item_ids': [plural, definite],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'nynorsk-noun-neuter': {
        '@attribution': {'users': ['Njardarlogar'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk inkjekjønnssubstantiv',
        'language': language_Nynorsk,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Dette er eit [hus].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bunde eintal',
                'example': 'Dette er [huset].',
                'grammatical_features_item_ids': [singular, definite],
            },
            {
                'label': 'ubunde fleirtal',
                'example': 'Dette er nokre [hus].',
                'grammatical_features_item_ids': [plural, indefinite],
            },
            {
                'label': 'bunde fleirtal',
                'example': 'Dette er [husa].',
                'grammatical_features_item_ids': [plural, definite],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'nynorsk-noun-feminine-masculine': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk ho- og hankjønnssubstantiv',
        'language': language_Nynorsk,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Du har ei/ein fin [dialekt].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bunde eintal, hokjønn',
                'example': 'Eg likar [dialekta] di.',
                'grammatical_features_item_ids': [singular, definite, feminine],
            },
            {
                'label': 'bunde eintal, hankjønn',
                'example': 'Eg likar [dialekten] din.',
                'grammatical_features_item_ids': [singular, definite, masculine],
            },
            {
                'label': 'ubunde fleirtal, hokjønn',
                'example': 'Dei har forskjellige [dialekter].',
                'grammatical_features_item_ids': [plural, indefinite, feminine],
            },
            {
                'label': 'ubunde fleirtal, hankjønn',
                'example': 'Dei har forskjellige [dialektar].',
                'grammatical_features_item_ids': [plural, indefinite, masculine],
            },
            {
                'label': 'bunde fleirtal, hokjønn',
                'example': 'Eg forstår ikkje dei [dialektene].',
                'grammatical_features_item_ids': [plural, definite, feminine],
            },
            {
                'label': 'binde fleirtal, hankjønn',
                'example': 'Eg forstår ikkje dei [dialektane].',
                'grammatical_features_item_ids': [plural, definite, masculine],
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, feminine),
                statement(grammatical_gender, masculine),
            ],
        },
    },

    'nynorsk-noun-feminine-neuter': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk ho- og inkjekjønnssubstantiv',
        'language': language_Nynorsk,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Eg såg ei/eit [my].',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bunde eintal, hokjønn',
                'example': 'Slå i hel [mya]!',
                'grammatical_features_item_ids': [singular, definite, feminine],
            },
            {
                'label': 'bunde eintal, inkjekjønn',
                'example': 'Slå i hel [myet]!',
                'grammatical_features_item_ids': [singular, definite, neuter],
            },
            {
                'label': 'ubunde fleirtal, hokjønn',
                'example': 'Det er ikkje mange [myer] her.',
                'grammatical_features_item_ids': [plural, indefinite, feminine],
            },
            {
                'label': 'ubunde fleirtal, inkjekjønn',
                'example': 'Det er ikkje mange [my] her.',
                'grammatical_features_item_ids': [plural, indefinite, neuter],
            },
            {
                'label': 'bunde fleirtal, hokjønn',
                'example': 'Har du drepe [myene]?',
                'grammatical_features_item_ids': [plural, definite, feminine],
            },
            {
                'label': 'binde fleirtal, inkjekjønn',
                'example': 'Har du drepe [mya]?',
                'grammatical_features_item_ids': [plural, definite, neuter],
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, feminine),
                statement(grammatical_gender, neuter),
            ],
        },
    },

    'nynorsk-noun-masculine-neuter': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk han- og inkjekjønnssubstantiv',
        'language': language_Nynorsk,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'ubunde eintal',
                'example': 'Har du ein/eit [sekund]?',
                'grammatical_features_item_ids': [singular, indefinite],
            },
            {
                'label': 'bunde eintal, hankjønn',
                'example': 'Den første [sekunden].',
                'grammatical_features_item_ids': [singular, definite, masculine],
            },
            {
                'label': 'bunde eintal, inkjekjønn',
                'example': 'Det første [sekundet].',
                'grammatical_features_item_ids': [singular, definite, neuter],
            },
            {
                'label': 'ubunde fleirtal, hankjønn',
                'example': 'Kor mange [sekundar] har du?',
                'grammatical_features_item_ids': [plural, indefinite, masculine],
            },
            {
                'label': 'ubunde fleirtal, inkjekjønn',
                'example': 'Kor mange [sekund] har du?',
                'grammatical_features_item_ids': [plural, indefinite, neuter],
            },
            {
                'label': 'bunde fleirtal, hankjønn',
                'example': 'Dei har brukt opp alle [sekundane].',
                'grammatical_features_item_ids': [plural, definite, masculine],
            },
            {
                'label': 'binde fleirtal, inkjekjønn',
                'example': 'Dei har brukt opp alle [sekunda].',
                'grammatical_features_item_ids': [plural, definite, neuter],
            },
        ],
        'statements': {
            grammatical_gender: [
                statement(grammatical_gender, masculine),
                statement(grammatical_gender, neuter),
            ],
        },
    },

    'nynorsk-adjective': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk adjektiv',
        'language': language_Nynorsk,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'ubunde hankjønn og hokjønn',
                'example': 'Ein [flink] person.',
                'grammatical_features_item_ids': [singular, indefinite, masculine, feminine],
            },
            {
                'label': 'ubunde inkjekjønn',
                'example': 'Eit [flinkt] barn.',
                'grammatical_features_item_ids': [singular, indefinite, neuter],
            },
            {
                'label': 'bunde eintall',
                'example': 'Det [flinke] barnet.',
                'grammatical_features_item_ids': [singular, definite],
            },
            {
                'label': 'fleirtall',
                'example': 'Alle dei [flinke] borna.',
                'grammatical_features_item_ids': [plural],
            },
            {
                'label': 'komparativ',
                'example': 'Barnet er [flinkare] enn meg.',
                'grammatical_features_item_ids': [comparative],
                'optional': True,
            },
            {
                'label': 'superlativ',
                'example': 'Barnet mitt var aller [flinkast].',
                'grammatical_features_item_ids': [superlative],
                'optional': True,
            },
            {
                'label': 'superlativ, bestemt form',
                'example': 'Det aller [flinkaste] barnet.',
                'grammatical_features_item_ids': [superlative, definite],
                'optional': True,
            },
        ],
    },

    'nynorsk-verb': {
        '@attribution': {'users': ['Njardarlogar', 'Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk verb',
        'language': language_Nynorsk,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'a-infinitiv',
                'example': 'Å [helsa].',
                'grammatical_features_item_ids': [infinitive, active, a_infinitive],
            },
            {
                'label': 'e-infinitiv',
                'example': 'Å [helse].',
                'grammatical_features_item_ids': [infinitive, active, e_infinitive],
            },
            {
                'label': 'notid',
                'example': 'Eg [helsar/helser].',
                'grammatical_features_item_ids': [present_tense, active],
            },
            {
                'label': 'fortid',
                'example': 'Eg [helsa/helste].',
                'grammatical_features_item_ids': [preterite],
            },
            {
                'label': 'presens og preteritum perfektum',
                'example': 'Eg har/hadde [helsa/helst].',
                'grammatical_features_item_ids': [perfect_tense, preterite, present_tense],
            },
            {
                'label': 'imperativ',
                'example': 'Ikkje [hels] på dei!',
                'grammatical_features_item_ids': [imperative],
            },
            {
                'label': 'perfektum partisipp, hankjønn og hokjønn',
                'example': 'Ein [helsa/helst] person.',
                'grammatical_features_item_ids': [past_participle, singular, indefinite, masculine, feminine],
            },
            {
                'label': 'perfektum partisipp, inkjekjønn',
                'example': 'Eit [helsa/helst] barn.',
                'grammatical_features_item_ids': [past_participle, singular, indefinite, neuter],
            },
            {
                'label': 'perfektum partisipp, bunden form',
                'example': 'Den [helsa/helste] personen.',
                'grammatical_features_item_ids': [past_participle, singular, definite],
            },
            {
                'label': 'perfektum partisipp, fleirtal',
                'example': 'Alle dei [helsa/helste] gjestane.',
                'grammatical_features_item_ids': [past_participle, plural],
            },
            {
                'label': 'presens partisipp',
                'example': 'Ein [helsande] person.',
                'grammatical_features_item_ids': [present_participle],
            },
            {
                'label': 'passiv infinitiv',
                'example': 'Det er triveleg å [helsast].',
                'grammatical_features_item_ids': [infinitive, passive],
            },
            {
                'label': 'passiv presens',
                'example': 'Ho [helsast] av gjesten.',
                'grammatical_features_item_ids': [present_tense, passive],
            },
        ],
    },

    'nynorsk-verb-passive': {
        '@attribution': {'users': ['Njardarlogar', 'Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk st-verb',
        'language': language_Nynorsk,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'infinitiv',
                'example': 'Det er bra å [trivast].',
                'grammatical_features_item_ids': [infinitive, passive],
            },
            {
                'label': 'presens',
                'example': 'Eg [trivst] på skulen.',
                'grammatical_features_item_ids': [present_tense, passive],
            },
            {
                'label': 'preteritum',
                'example': 'Eg [treivst] med det.',
                'grammatical_features_item_ids': [preterite, passive],
            },
            {
                'label': 'presens perfektum',
                'example': 'Eg har [trivest] med å vere der…',
                'grammatical_features_item_ids': [present_perfect, passive],
            },
        ],
        'statements': statements(instance_of, passive_verb),
    },

    'nynorsk-interjection': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk interjeksjon',
        'language': language_Nynorsk,
        'lexical_category_item_id': interjection,
        'forms': [
            {
                'label': 'interjeksjon',
                'example': 'Kvinna sa [hei].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'nynorsk-adverb': {
        '@attribution': {'users': ['Jon Harald Søby'], 'title': 'Wikidata:Wikidata Lexeme Forms/Norwegian Nynorsk'},
        'label': 'nynorsk adverb',
        'language': language_Nynorsk,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'adverb',
                'example': 'Guten snakka [mye].',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'odia-noun-human': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ବ୍ୟକ୍ତିବାଚକ ବିଶେଷ୍ୟ',
        'language': language_Odia,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'କର୍ତ୍ତୃବାଚ୍ଯ/କର୍ତ୍ତାକାରକ',
                'example': '[ଖେଳାଳି] ହକି ଖେଳୁଛନ୍ତି ।',
                'grammatical_features_item_ids': [nominative_case],
            },
            {
                'label': 'କର୍ମ କାରକ',
                'example': 'ସେ [ଖେଳାଳିଙ୍କୁ] ଉତ୍ସାହିତ କଲେ ।',
                'grammatical_features_item_ids': [accusative_case],
            },
            {
                'label': 'କରଣ କାରକ',
                'example': 'ସେ [ଖେଳାଳିଙ୍କଦ୍ୱାରା] ହକିର ପ୍ରସାର ହୋଇଛି ।',
                'grammatical_features_item_ids': [instrumental_case],
            },
            {
                'label': 'ସମ୍ପ୍ରଦାନ କାରକ',
                'example': 'ସେ [ଖେଳାଳିଙ୍କୁ] ପୁରସ୍କାର ଦେଲେ ।',
                'grammatical_features_item_ids': [dative_case],
            },
            {
                'label': 'ଅପାଦାନ କାରକ',
                'example': 'ସେ [ଖେଳାଳିଙ୍କଠାରୁ] ଭଲ ଖେଳାଳି ଏଠି ଆଉ କାହିଁ?',
                'grammatical_features_item_ids': [ablative_case],
            },
            {
                'label': 'ସମ୍ବନ୍ଧ ପଦ',
                'example': 'ଏ [ଖେଳାଳିଙ୍କ] ସ୍ଥାନ ଫରୱାର୍ଡ଼ ।',
                'grammatical_features_item_ids': [genitive_case],
            },
            {
                'label': 'ଅଧିକରଣ କାରକ',
                'example': 'ଏ [ଖେଳାଳିଙ୍କଠାରେ] ଦଳର ଭାରି ବିଶ୍ୱାସ ।',
                'grammatical_features_item_ids': [locative_case],
            },
        ],
    },

    'odia-noun-nonhuman': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ପ୍ରାଣୀବାଚକ ଓ ଅପ୍ରାଣୀବାଚକ ବିଶେଷ୍ୟ',
        'language': language_Odia,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'କର୍ତ୍ତୃବାଚ୍ଯ/କର୍ତ୍ତାକାରକ',
                'example': '[କୁକୁରଟି] ମାଂସ ଖାଉଛି ।',
                'grammatical_features_item_ids': [nominative_case],
            },
            {
                'label': 'କର୍ମ କାରକ',
                'example': 'ସେ [କୁକୁରକୁ] ଖେଳାଉଛନ୍ତି ।',
                'grammatical_features_item_ids': [accusative_case],
            },
            {
                'label': 'କରଣ କାରକ',
                'example': '[କୁକୁରଦ୍ୱାରା] ପୋଲିସ ଅନୁସନ୍ଧାନ କରୁଛି ।',
                'grammatical_features_item_ids': [instrumental_case],
            },
            {
                'label': 'ସମ୍ପ୍ରଦାନ କାରକ',
                'example': '[କୁକୁରକୁ] ଆଉ ଦୁଇଖଣ୍ଡ ମାଂସ ଦିଅ ।',
                'grammatical_features_item_ids': [dative_case],
            },
            {
                'label': 'ଅପାଦାନ କାରକ',
                'example': '[କୁକୁରଠାରୁ] ବଳି ସାଙ୍ଗ କିଏ?',
                'grammatical_features_item_ids': [ablative_case],
            },
            {
                'label': 'ସମ୍ବନ୍ଧ ପଦ',
                'example': 'ଆମ [କୁକୁରର] ଭୁକିବା ଶୁଭୁଛି ।',
                'grammatical_features_item_ids': [genitive_case],
            },
            {
                'label': 'ଅଧିକରଣ କାରକ',
                'example': 'ତାଙ୍କର ଏ [କୁକୁରଠାରେ] ଭାରୀ ଭାବ ।',
                'grammatical_features_item_ids': [locative_case],
            },
            {
                'label': 'ସମ୍ବୋଧକ କାରକ',
                'example': '[କୁକୁରରେ] କୁକୁର! କେଉଁଠି ଅଛୁ?',
                'grammatical_features_item_ids': [vocative_case],
            },
        ],
    },

    'odia-adjective-nongendered': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ଲିଙ୍ଗବିହୀନ ବିଶେଷଣ',
        'language': language_Odia,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'ଅସ୍ତିବାଚକ',
                'example': 'ଏଇଟି ଏକ [କ୍ଷୀପ୍ର] କୁକୁର ।',
                'grammatical_features_item_ids': [positive],
            },
            {
                'label': 'ତୁଳନାତ୍ମକ-ମଧ୍ୟ',
                'example': 'ଏ କୁକରଟି ଆର କୁକୁରଠାରୁ [କ୍ଷୀପ୍ରତର] ।',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'ତୁଳନାତ୍ମକ-ଶ୍ରେଷ୍ଠ',
                'example': 'ଏ କୁକୁର ଦୁନିଆର ସବୁ କୁକୁରଙ୍କ ଭିତରେ [କ୍ଷୀପ୍ରତମ] ।',
                'grammatical_features_item_ids': [superlative],
            },
        ],
    },

    'odia-adjective-gendered': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ଲିଙ୍ଗସୂଚକ ବିଶେଷଣ',
        'language': language_Odia,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'ବିଶେଷଣ-ମହିଳା',
                'example': 'ସେ ଗୋଟିଏ [ଜ୍ଞାନବତୀ] ଝିଅ ।',
                'grammatical_features_item_ids': [feminine],
            },
            {
                'label': 'ବିଶେଷଣ-ପୁରୁଷ',
                'example': 'ସେ ଗୋଟିଏ [ଜ୍ଞାନବାନ] ପିଲା ।',
                'grammatical_features_item_ids': [masculine],
            },
        ],
    },

    'odia-adverb': {
        '@attribution': {'users': ['Psubhashish'], 'title': 'Wikidata:Wikidata Lexeme Forms/Odia'},
        'label': 'ଓଡ଼ିଆ କ୍ରିୟା ବିଶେଷଣ',
        'language': language_Odia,
        'lexical_category_item_id': adverb,
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
        'language': language_Polish,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Liczba pojedyncza, mianownik',
                'example': 'To jest [odkurzacz].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'Liczba pojedyncza, dopełniacz',
                'example': 'Wśród nas nie ma [odkurzacza].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'Liczba pojedyncza, celownik',
                'example': 'Przyglądam się [odkurzaczowi].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'Liczba pojedyncza, biernik',
                'example': 'Widzę [odkurzacz].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'Liczba pojedyncza, narzędnik',
                'example': 'Idę z [odkurzaczem].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'Liczba pojedyncza, miejscownik',
                'example': 'Myślę o [odkurzaczu].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': 'Liczba pojedyncza, wołacz',
                'example': '[odkurzaczu]',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'Liczba mnoga, mianownik',
                'example': 'To są [odkurzacze].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'Liczba mnoga, dopełniacz',
                'example': 'Wśród nas nie ma [odkurzaczy/odkurzaczów].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'Liczba mnoga, celownik',
                'example': 'Przyglądam się [odkurzaczom].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'Liczba mnoga, biernik',
                'example': 'Widzę [odkurzacze].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'Liczba mnoga, narzędnik',
                'example': 'Idę z [odkurzaczami].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
            {
                'label': 'Liczba mnoga, miejscownik',
                'example': 'Myślę o [odkurzaczach].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': 'Liczba mnoga, wołacz',
                'example': '[odkurzacze]',
                'grammatical_features_item_ids': [vocative_case, plural],
            },
        ],
    },

    'polish-noun-masculine-personal-with-depreciative-forms': {
        '@attribution': {'users': ['KaMan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Polish'},
        'label': 'polski rzeczownik, rodzaj męskoosobowy z formami ndepr. i depr. w M. i W. lm',
        'language': language_Polish,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'mianownik, liczba pojedyncza',
                'example': 'To jest [robotnik].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'dopełniacz, liczba pojedyncza',
                'example': 'Wśród nas nie ma [robotnika].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'celownik, liczba pojedyncza',
                'example': 'Przyglądam się [robotnikowi].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'biernik, liczba pojedyncza',
                'example': 'Widzę [robotnika].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'narzędnik, liczba pojedyncza',
                'example': 'Idę z [robotnikiem].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'miejscownik, liczba pojedyncza',
                'example': 'Myślę o [robotniku].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': 'wołacz, liczba pojedyncza',
                'example': '[robotniku]',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'mianownik, liczba mnoga, forma niedeprecjatywna',
                'example': 'To są ci [robotnicy].',
                'grammatical_features_item_ids': [nominative_case, plural],
                'statements': statements(instance_of, non_depreciative_form),
            },
            {
                'label': 'mianownik, liczba mnoga, forma deprecjatywna',
                'example': 'To są te [robotniki].',
                'grammatical_features_item_ids': [nominative_case, plural],
                'statements': statements(instance_of, depreciative_form),
            },
            {
                'label': 'dopełniacz, liczba mnoga',
                'example': 'Wśród nas nie ma [robotników].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'celownik, liczba mnoga',
                'example': 'Przyglądam się [robotnikom].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'biernik, liczba mnoga',
                'example': 'Widzę [robotników].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'narzędnik, liczba mnoga',
                'example': 'Idę z [robotnikami].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
            {
                'label': 'miejscownik, liczba mnoga',
                'example': 'Myślę o [robotnikach].',
                'grammatical_features_item_ids': [locative_case, plural],
            },
            {
                'label': 'wołacz, liczba mnoga, forma niedeprecjatywna',
                'example': 'ci [robotnicy]',
                'grammatical_features_item_ids': [vocative_case, plural],
                'statements': statements(instance_of, non_depreciative_form),
            },
            {
                'label': 'wołacz, liczba mnoga, forma deprecjatywna',
                'example': 'te [robotniki]',
                'grammatical_features_item_ids': [vocative_case, plural],
                'statements': statements(instance_of, depreciative_form),
            },
        ],
        'statements': statements(grammatical_gender, masculine_personal),
    },

    'polish-noun-with-potential-plural-forms': {
        '@attribution': {'users': ['KaMan'], 'title': 'Wikidata:Wikidata Lexeme Forms/Polish'},
        'label': 'polski rzeczownik, potencjalna liczba mnoga',
        'language': language_Polish,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'mianownik, liczba pojedyncza',
                'example': 'To jest [językoznawstwo].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'dopełniacz, liczba pojedyncza',
                'example': 'Wśród nas nie ma [językoznawstwa].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'celownik, liczba pojedyncza',
                'example': 'Przyglądam się [językoznawstwu].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'biernik, liczba pojedyncza',
                'example': 'Widzę [językoznawstwo].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'narzędnik, liczba pojedyncza',
                'example': 'Idę z [językoznawstwem].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'miejscownik, liczba pojedyncza',
                'example': 'Myślę o [językoznawstwie].',
                'grammatical_features_item_ids': [locative_case, singular],
            },
            {
                'label': 'wołacz, liczba pojedyncza',
                'example': '[językoznawstwo]',
                'grammatical_features_item_ids': [vocative_case, singular],
            },
            {
                'label': 'mianownik, liczba mnoga, forma potencjalna',
                'example': 'To są [językoznawstwa].',
                'grammatical_features_item_ids': [nominative_case, plural],
                'statements': statements(instance_of, potential_form),
            },
            {
                'label': 'dopełniacz, liczba mnoga, forma potencjalna',
                'example': 'Wśród nas nie ma [językoznawstw].',
                'grammatical_features_item_ids': [genitive_case, plural],
                'statements': statements(instance_of, potential_form),
            },
            {
                'label': 'celownik, liczba mnoga, forma potencjalna',
                'example': 'Przyglądam się [językoznawstwom].',
                'grammatical_features_item_ids': [dative_case, plural],
                'statements': statements(instance_of, potential_form),
            },
            {
                'label': 'biernik, liczba mnoga, forma potencjalna',
                'example': 'Widzę [językoznawstwa].',
                'grammatical_features_item_ids': [accusative_case, plural],
                'statements': statements(instance_of, potential_form),
            },
            {
                'label': 'narzędnik, liczba mnoga, forma potencjalna',
                'example': 'Idę z [językoznawstwami].',
                'grammatical_features_item_ids': [instrumental_case, plural],
                'statements': statements(instance_of, potential_form),
            },
            {
                'label': 'miejscownik, liczba mnoga, forma potencjalna',
                'example': 'Myślę o [językoznawstwach].',
                'grammatical_features_item_ids': [locative_case, plural],
                'statements': statements(instance_of, potential_form),
            },
            {
                'label': 'wołacz, liczba mnoga, forma potencjalna',
                'example': '[językoznawstwa]',
                'grammatical_features_item_ids': [vocative_case, plural],
                'statements': statements(instance_of, potential_form),
            },
        ],
    },

    'polish-adjective-positive': {
        '@attribution': {'users': ['Powerek38'], 'title': 'Wikidata:Wikidata Lexeme Forms/Polish'},
        'label': 'polski przymiotnik, stopień równy',
        'language': language_Polish,
        'lexical_category_item_id': adjective,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'liczba pojedyncza, rodzaj męski nieżywotny, mianownik',
                'example': 'To jest [wysoki] płot.',
                'grammatical_features_item_ids': [singular, masculine_inanimate, nominative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski nieżywotny, dopełniacz',
                'example': 'Nie ma tu [wysokiego] płotu.',
                'grammatical_features_item_ids': [singular, masculine_inanimate, genitive_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski nieżywotny, celownik',
                'example': 'Przyglądam się [wysokiemu] płotowi.',
                'grammatical_features_item_ids': [singular, masculine_inanimate, dative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski nieżywotny, biernik',
                'example': 'Widzę [wysoki] płot.',
                'grammatical_features_item_ids': [singular, masculine_inanimate, accusative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski nieżywotny, narzędnik',
                'example': 'Zderzył się z [wysokim] płotem.',
                'grammatical_features_item_ids': [singular, masculine_inanimate, instrumental_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski nieżywotny, miejscownik',
                'example': 'Myślę o [wysokim] płocie.',
                'grammatical_features_item_ids': [singular, masculine_inanimate, locative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski nieżywotny, wołacz',
                'example': 'Och, mój [wysoki] płocie!',
                'grammatical_features_item_ids': [singular, masculine_inanimate, vocative_case, positive],
            },
            {
                'section_break': True,
                'label': 'liczba pojedyncza, rodzaj męski żywotny, mianownik',
                'example': 'To jest [wysoki] mężczyzna.',
                'grammatical_features_item_ids': [singular, masculine_animate, nominative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski żywotny, dopełniacz',
                'example': 'Nie ma tu [wysokiego] mężczyzny.',
                'grammatical_features_item_ids': [singular, masculine_animate, genitive_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski żywotny, celownik',
                'example': 'Przyglądam się [wysokiemu] mężczyźnie.',
                'grammatical_features_item_ids': [singular, masculine_animate, dative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski żywotny, biernik',
                'example': 'Widzę [wysokiego] mężczyznę.',
                'grammatical_features_item_ids': [singular, masculine_animate, accusative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski żywotny, narzędnik',
                'example': 'Spotkała się z [wysokim] mężczyzną.',
                'grammatical_features_item_ids': [singular, masculine_animate, instrumental_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj rodzaj męski żywotny, miejscownik',
                'example': 'Myślę o [wysokim] mężczyźnie.',
                'grammatical_features_item_ids': [singular, masculine_animate, locative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj męski żywotny, wołacz',
                'example': 'Och, mój [wysoki] mężczyzno!',
                'grammatical_features_item_ids': [singular, masculine_animate, vocative_case, positive],
            },
            {
                'section_break': True,
                'label': 'liczba pojedyncza, rodzaj żeński, mianownik',
                'example': 'To jest [wysoka] kobieta.',
                'grammatical_features_item_ids': [singular, feminine, nominative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj żeński, dopełniacz',
                'example': 'Nie ma tu [wysokiej] kobiety.',
                'grammatical_features_item_ids': [singular, feminine, genitive_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj żeński, celownik',
                'example': 'Przyglądam się [wysokiej] kobiecie.',
                'grammatical_features_item_ids': [singular, feminine, dative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj żeński, biernik',
                'example': 'Widzę [wysoką] kobietę.',
                'grammatical_features_item_ids': [singular, feminine, accusative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj żeński, narzędnik',
                'example': 'Spotkałem się z [wysoką] kobietą.',
                'grammatical_features_item_ids': [singular, feminine, instrumental_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj żeński, miejscownik',
                'example': 'Myślę o [wysokiej] kobiecie.',
                'grammatical_features_item_ids': [singular, feminine, locative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj żeński, wołacz',
                'example': 'Och, moja [wysoka] kobieto!',
                'grammatical_features_item_ids': [singular, feminine, vocative_case, positive],
            },
            {
                'section_break': True,
                'label': 'liczba pojedyncza, rodzaj nijaki, mianownik',
                'example': 'To jest [wysokie] dziecko.',
                'grammatical_features_item_ids': [singular, neuter, nominative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj nijaki, dopełniacz',
                'example': 'Nie ma tu [wysokiego] dziecka.',
                'grammatical_features_item_ids': [singular, neuter, genitive_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj nijaki, celownik',
                'example': 'Przyglądam się [wysokiemu] dziecku.',
                'grammatical_features_item_ids': [singular, neuter, dative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj nijaki, biernik',
                'example': 'Widzę [wysokie] dziecko.',
                'grammatical_features_item_ids': [singular, neuter, accusative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj nijaki, narzędnik',
                'example': 'Spotkałam się z [wysokim] dzieckiem.',
                'grammatical_features_item_ids': [singular, neuter, instrumental_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj nijaki, miejscownik',
                'example': 'Myślę o [wysokim] dziecku.',
                'grammatical_features_item_ids': [singular, neuter, locative_case, positive],
            },
            {
                'label': 'liczba pojedyncza, rodzaj nijaki, wołacz',
                'example': 'Och, moje [wysokie] dziecko!',
                'grammatical_features_item_ids': [singular, neuter, vocative_case, positive],
            },
            {
                'section_break': True,
                'label': 'liczba mnoga, rodzaj męskoosobowy, mianownik',
                'example': 'To są [wysocy] mężczyźni.',
                'grammatical_features_item_ids': [plural, masculine_personal, nominative_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj męskoosobowy, dopełniacz',
                'example': 'Nie ma tu [wysokich] mężczyzn.',
                'grammatical_features_item_ids': [plural, masculine_personal, genitive_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj męskoosobowy, celownik',
                'example': 'Przyglądam się [wysokim] mężczyznom.',
                'grammatical_features_item_ids': [plural, masculine_personal, dative_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj męskoosobowy, biernik',
                'example': 'Widzę [wysokich] mężczyzn.',
                'grammatical_features_item_ids': [plural, masculine_personal, accusative_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj męskoosobowy, narzędnik',
                'example': 'Spotkałem się z [wysokimi] mężczyznami.',
                'grammatical_features_item_ids': [plural, masculine_personal, instrumental_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj męskoosobowy, miejscownik',
                'example': 'Myślę o [wysokich] mężczyznach.',
                'grammatical_features_item_ids': [plural, masculine_personal, locative_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj męskoosobowy, wołacz',
                'example': 'Och, moi [wysocy] mężczyźni!',
                'grammatical_features_item_ids': [plural, masculine_personal, vocative_case, positive],
            },
            {
                'section_break': True,
                'label': 'liczba mnoga, rodzaj niemęskoosobowy, mianownik',
                'example': 'To są [wysokie] kobiety.',
                'grammatical_features_item_ids': [plural, not_masculine_personal, nominative_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj niemęskoosobowy, dopełniacz',
                'example': 'Nie ma tu [wysokich] kobiet.',
                'grammatical_features_item_ids': [plural, not_masculine_personal, genitive_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj niemęskoosobowy, celownik',
                'example': 'Przyglądam się [wysokim] kobietom.',
                'grammatical_features_item_ids': [plural, not_masculine_personal, dative_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj niemęskoosobowy, biernik',
                'example': 'Widzę [wysokie] kobiety.',
                'grammatical_features_item_ids': [plural, not_masculine_personal, accusative_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj niemęskoosobowy, narzędnik',
                'example': 'Spotkałam się z [wysokimi] kobietami.',
                'grammatical_features_item_ids': [plural, not_masculine_personal, instrumental_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj niemęskoosobowy, miejscownik',
                'example': 'Myślę o [wysokich] kobietach.',
                'grammatical_features_item_ids': [plural, not_masculine_personal, locative_case, positive],
            },
            {
                'label': 'liczba mnoga, rodzaj niemęskoosobowy, wołacz',
                'example': 'Och, moje [wysokie] kobiety!',
                'grammatical_features_item_ids': [plural, not_masculine_personal, vocative_case, positive],
            },
        ],
    },

    'punjabi-noun-masculine-shah': {
        '@attribution': {'users': ['Satdeep Gill', 'عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'پنجابی ناؤں مذکر',
        'language': language_Shahmukhi,
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'واحد، فاعلی',
                'example': 'اوہ میرا [ہتھّ] اے۔',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'جمع، فاعلی',
                'example': 'اوہ میرے [ہتھّ] ہن۔',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'واحد، مفعولی',
                'example': 'میرے [ہتھّ] نوں ویکھو۔',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'جمع، مفعولی',
                'example': 'میریاں [ہتھّاں] نوں ویکھو۔',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'section_break': True,
                'label': 'واحد، اپادان',
                'example': 'اوہ [ہتھّوں] بھیجا جا سکدا اے۔؜',
                'grammatical_features_item_ids': [masculine, ablative_case, singular],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'واحد، پکارن',
                'example': 'وے او [ہتھّا]!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'جمع، پکارن',
                'example': 'ہے حسین [ہتھّو]!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'واحد، وسنیک',
                'example': 'میں [ہتھّے] آ گیا۔؜',
                'grammatical_features_item_ids': [masculine, locative_case, singular],
                'optional': True,
            },
            {
                'label': 'جمع، وسنیک',
                'example': 'اسیں [ہتھِّیں] آ گئے۔',
                'grammatical_features_item_ids': [masculine, locative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'دو وچن، کرن',
                'example': 'اوہ [ہتھِّیں] کیتا کم اے۔',
                'grammatical_features_item_ids': [masculine, instrumental_case, dual],
                'optional': True,
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'punjabi-noun-feminine-shah': {
        '@attribution': {'users': ['Satdeep Gill', 'عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'پنجابی ناؤں مونث',
        'language': language_Shahmukhi,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'واحد، فاعلی',
                'example': 'ایہہ [اکھّ] سوہݨی اے۔',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'جمع، فاعلی',
                'example': 'ایہہ [اکھّاں] سوہݨیاں ہن۔',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'واحد، مفعولی',
                'example': 'میری [اکھّ] نوں ویکھو۔',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'جمع، مفعولی',
                'example': 'میریاں [اکھّاں] نوں ویکھو۔',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
            {
                'section_break': True,
                'label': 'واحد، اپادان',
                'example': 'اوہ [اکھّوں] نظرا جاوݨ۔؜',
                'grammatical_features_item_ids': [feminine, ablative_case, singular],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'واحد، پکارن',
                'example': 'وے او [اکھّے]!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'جمع، پکارن',
                'example': 'ہے حسین [اکھّو]!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'واحد، وسنیک',
                'example': 'اوہ [اکھِّیں] جاوݨ۔؜',
                'grammatical_features_item_ids': [feminine, locative_case, singular],
                'optional': True,
            },
            {
                'label': 'جمع، وسنیک',
                'example': 'اوہ [اکھِّیں] گھٹا پاۓگا۔؜',
                'grammatical_features_item_ids': [feminine, locative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'دو وچن، کرن',
                'example': 'اوہ [اکھِّیں] دیکھیا سی۔؜',
                'grammatical_features_item_ids': [feminine, instrumental_case, dual],
                'optional': True,
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'punjabi-adjective-red-shah': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'پنجابی لال گݨ ناں',
        'language': language_Shahmukhi,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'اِکلا',
                'example': 'ہاں جی، میں [ٹھیک] آں۔',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, indeclinable_adjective)],
            paradigm_class: [statement(paradigm_class, lāl_surakh_adjective)],
        },
    },

    'punjabi-adjective-black-shah': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'پنجابی کالا گݨ ناں',
        'language': language_Shahmukhi,
        'lexical_category_item_id': adjective,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'مذکر، واحد، فاعلی',
                'example': 'اوہ [وڈّا] گھوڑا اے۔',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'مذکر، جمع، فاعلی',
                'example': 'اوہ [وڈّے] گھوڑے ہن۔',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'مذکر، واحد، مفعولی',
                'example': 'اوس [وڈّے] گھوڑے نوں ویکھو۔',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'مذکر، جمع، مفعولی',
                'example': 'اوہناں [وڈّیاں] گھوڑیاں نوں ویکھو۔',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'label': 'مذکر، واحد، پکارن',
                'example': 'آہ میریا [وڈّیا] گھوڑیا، آ جاؤ!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'مذکر، جمع، پکارن',
                'example': 'آہ میریو [وڈّیو] گھوڑیو، آ جاؤ!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, plural],
                'optional': True
            },
            {
                'section_break': True,
                'label': 'مونث واحد، فاعلی',
                'example': 'اوہ [وڈّی] گھوڑی اے۔',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'مونث، جمع، فاعلی',
                'example': 'اوہ [وڈِّیاں] گھوڑِیاں ہن۔',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'مونث، واحد، مفعولی',
                'example': 'اوس [وڈّی] گھوڑی نوں ویکھو۔',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'مونث، جمع، مفعولی',
                'example': 'اوہناں [وڈِّیاں] گھوڑِیاں نوں ویکھو۔',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
            {
                'label': 'مونث، واحد، پکارن',
                'example': 'آہ میریئے [وڈّیئے] گھوڑیئے، آ جاؤ!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'مونث، جمع، پکارن',
                'example': 'آہ میرِیو [وڈِّیو] گھوڑِیو، آ جاؤ!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, plural],
                'optional': True,
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, declinable_adjective)],
            paradigm_class: [statement(paradigm_class, kālā_adjective)],
        },
    },

    'punjabi-adjective-longer-shah': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'پنجابی لمیرا گݨ ناں',
        'language': language_Shahmukhi,
        'lexical_category_item_id': adjective,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'نفسی، مذکر، واحد، فاعلی',
                'example': 'اوہ [لمّا] گھوڑا اے۔',
                'grammatical_features_item_ids': [positive, masculine, direct_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'نفسی، مذکر، جمع، فاعلی',
                'example': 'اوہ [لمّے] گھوڑے ہن۔',
                'grammatical_features_item_ids': [positive, masculine, direct_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'نفسی، مذکر، واحد، مفعولی',
                'example': 'اوس [لمّے] گھوڑے نوں ویکھو۔',
                'grammatical_features_item_ids': [positive, masculine, oblique_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'نفسی، مذکر، جمع، مفعولی',
                'example': 'اوہناں [لمّیاں] گھوڑیاں نوں ویکھو۔',
                'grammatical_features_item_ids': [positive, masculine, oblique_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'نفسی، مذکر، واحد، پکارن',
                'example': 'آہ میریا [لمّیا] گھوڑیا، آ جاؤ!؜',
                'grammatical_features_item_ids': [positive, masculine, vocative_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
                'optional': True,
            },
            {
                'label': 'نفسی، مذکر، جمع، پکارن',
                'example': 'آہ میریو [لمّیو] گھوڑیو، آ جاؤ!؜',
                'grammatical_features_item_ids': [positive, masculine, vocative_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'نفسی، مونث واحد، فاعلی',
                'example': 'اوہ [لمّی] گھوڑی اے۔',
                'grammatical_features_item_ids': [positive, feminine, direct_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'نفسی، مونث، جمع، فاعلی',
                'example': 'اوہ [لمِّیاں] گھوڑِیاں ہن۔',
                'grammatical_features_item_ids': [positive, feminine, direct_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'نفسی، مونث، واحد، مفعولی',
                'example': 'اوس [لمّی] گھوڑی نوں ویکھو۔',
                'grammatical_features_item_ids': [positive, feminine, oblique_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'نفسی، مونث، جمع، مفعولی',
                'example': 'اوہناں [لمِّیاں] گھوڑِیاں نوں ویکھو۔',
                'grammatical_features_item_ids': [positive, feminine, oblique_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'نفسی، مونث، واحد، پکارن',
                'example': 'آہ میریئے [لمّیئے] گھوڑیئے، آ جاؤ!؜',
                'grammatical_features_item_ids': [positive, feminine, vocative_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
                'optional': True,
            },
            {
                'label': 'نفسی، مونث، جمع، پکارن',
                'example': 'آہ میرِیو [لمِّیو] گھوڑِیو، آ جاؤ!؜',
                'grammatical_features_item_ids': [positive, feminine, vocative_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'تشبیہہ، مذکر، واحد، فاعلی',
                'example': 'اوہ [لمیرا] گھوڑا اے۔',
                'grammatical_features_item_ids': [comparative, masculine, direct_case, singular],
            },
            {
                'label': 'تشبیہہ، مذکر، جمع، فاعلی',
                'example': 'اوہ [لمیرے] گھوڑے ہن۔',
                'grammatical_features_item_ids': [comparative, masculine, direct_case, plural],
            },
            {
                'label': 'تشبیہہ، مذکر، واحد، مفعولی',
                'example': 'اوس [لمیرے] گھوڑے نوں ویکھو۔',
                'grammatical_features_item_ids': [comparative, masculine, oblique_case, singular],
            },
            {
                'label': 'تشبیہہ، مذکر، جمع، مفعولی',
                'example': 'اوہناں [لمیریاں] گھوڑیاں نوں ویکھو۔',
                'grammatical_features_item_ids': [comparative, masculine, oblique_case, plural],
            },
            {
                'label': 'تشبیہہ، مذکر، واحد، پکارن',
                'example': 'آہ میریا [لمیریا] گھوڑیا، آ جاؤ!؜',
                'grammatical_features_item_ids': [comparative, masculine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'تشبیہہ، مذکر، جمع، پکارن',
                'example': 'آہ میریو [لمیریو] گھوڑیو، آ جاؤ!؜',
                'grammatical_features_item_ids': [comparative, masculine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'تشبیہہ، مونث واحد، فاعلی',
                'example': 'اوہ [لمیری] گھوڑی اے۔',
                'grammatical_features_item_ids': [comparative, feminine, direct_case, singular],
            },
            {
                'label': 'تشبیہہ، مونث، جمع، فاعلی',
                'example': 'اوہ [لمیرِیاں] گھوڑِیاں ہن۔',
                'grammatical_features_item_ids': [comparative, feminine, direct_case, plural],
            },
            {
                'label': 'تشبیہہ، مونث، واحد، مفعولی',
                'example': 'اوس [لمیری] گھوڑی نوں ویکھو۔',
                'grammatical_features_item_ids': [comparative, feminine, oblique_case, singular],
            },
            {
                'label': 'تشبیہہ، مونث، جمع، مفعولی',
                'example': 'اوہناں [لمیرِیاں] گھوڑِیاں نوں ویکھو۔',
                'grammatical_features_item_ids': [comparative, feminine, oblique_case, plural],
            },
            {
                'label': 'تشبیہہ، مونث، واحد، پکارن',
                'example': 'آہ میریئے [لمیریئے] گھوڑیئے، آ جاؤ!؜',
                'grammatical_features_item_ids': [comparative, feminine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'تشبیہہ، مونث، جمع، پکارن',
                'example': 'آہ میرِیو [لمیرِیو] گھوڑِیو، آ جاؤ!؜',
                'grammatical_features_item_ids': [comparative, feminine, vocative_case, plural],
                'optional': True,
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, comparable_adjective)],
            paradigm_class: [statement(paradigm_class, lamera_adjective)],
        },
    },

    'punjabi-adverb-indeclinable-shah': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'پنجابی عام گݨ فعل',
        'language': language_Shahmukhi,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'اِکلا',
                'example': 'تسیں [اجّ] کیہہ کیتا؟',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements(instance_of, indeclinable_adverb),
    },

    'punjabi-adverb-declinable-shah': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'پنجابی ایسا بدل کردا گݨ فعل',
        'language': language_Shahmukhi,
        'lexical_category_item_id': adverb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'مذکر، واحد، فاعلی',
                'example': 'گھوڑا [بڑا] سوہݨا تردا۔',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'مذکر، جمع، فاعلی',
                'example': 'گھوڑے [بڑے] سوہݨے تردے۔',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'مذکر، واحد، مفعولی',
                'example': 'گھوڑے [بڑے] سوہݨے ترن لئی اوہ زور لوڑدا۔',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'مذکر، جمع، مفعولی',
                'example': 'گھوڑیاں [بڑیاں] سوہݨیاں ترن لئی اوہ زور لوڑدا۔',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'section_break': True,
                'label': 'مونث، واحد، فاعلی',
                'example': 'گھوڑی [بڑی] سوہݨی تردی۔',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'مونث، جمع، فاعلی',
                'example': 'گھوڑیاں [بڑِیاں] سوہݨیاں تردیاں۔',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'مونث، واحد، مفعولی',
                'example': 'گھوڑی [بڑی] سوہݨی ترن لئی اوہ زور لوڑدا۔',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'مونث، جمع، مفعولی',
                'example': 'گھوڑیاں [بڑِیاں] سوہݨیاں ترن لئی اوہ زور لوڑدا۔',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
        ],
        'statements': statements(instance_of, declinable_adverb),
    },

    'punjabi-adverb-comparable-shah': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'پنجابی گݨ فعل تفضیل',
        'language': language_Shahmukhi,
        'lexical_category_item_id': adverb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'نفسی، فاعلی',
                'example': 'میں پھیر مونہہ [پرے] کردیاں چلیا۔',
                'grammatical_features_item_ids': [positive, direct_case],
            },
            {
                'label': 'نفسی، مفعولی',
                'example': 'پاݨی نوں [پرے] کرن لئی آسا لاوندا اے۔',
                'grammatical_features_item_ids': [positive, oblique_case],
            },
            {
                'label': 'نفسی، اپادان',
                'example': 'چوک توں [پریوں] ای میں اندازہ اے۔',
                'grammatical_features_item_ids': [positive, ablative_case],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'تشبیہہ، فاعلی',
                'example': 'پیار ول [پریرے] جاندے ہن۔',
                'grammatical_features_item_ids': [comparative, direct_case],
            },
            {
                'label': 'تشبیہہ، مفعولی',
                'example': 'پیار ول [پریرے] جاݨ دی آس بجھدی اے۔',
                'grammatical_features_item_ids': [comparative, oblique_case],
            },
            {
                'label': 'تشبیہہ، اپادان',
                'example': 'میں پنج گز [پریریوں] جا کے پھل لیاوندا آں۔',
                'grammatical_features_item_ids': [comparative, ablative_case],
            },
        ],
        'statements': statements(instance_of, comparable_adverb),
    },

    'punjabi-noun-masculine-guru': {
        '@attribution': {'users': ['Satdeep Gill', 'عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'ਪੰਜਾਬੀ ਨਾਂਵ ਪੁਲਿੰਗ',
        'language': language_Gurmukhi,
        'lexical_category_item_id': 'Q1084',
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ ਮੇਰਾ [ਹੱਥ] ਏ।',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ ਮੇਰੇ [ਹੱਥ] ਹਨ।',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਮੇਰੇ [ਹੱਥ] ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਮੇਰਿਆਂ [ਹੱਥਾਂ] ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'section_break': True,
                'label': 'ਇੱਕ ਵਚਨ, ਅਪਾਦਾਨ',
                'example': 'ਉਹ [ਹੱਥੋਂ] ਭੇਜਾ ਜਾ ਸਕਦਾ ਏ।؜',
                'grammatical_features_item_ids': [masculine, ablative_case, singular],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਇੱਕ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਵੇ ਓ [ਹੱਥਾ]!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'ਬਹੁ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਹੇ ਹਸੀਨ [ਹੱਥੋ]!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਇੱਕ ਵਚਨ, ਵਸਨੀਕ',
                'example': 'ਮੈਂ [ਹੱਥੇ] ਆ ਗਿਆ।؜',
                'grammatical_features_item_ids': [masculine, locative_case, singular],
                'optional': True,
            },
            {
                'label': 'ਬਹੁ ਵਚਨ, ਵਸਨੀਕ',
                'example': 'ਅਸੀਂ [ਹੱਥੀਂ] ਆ ਗਏ।',
                'grammatical_features_item_ids': [masculine, locative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਦੋ ਵਚਨ, ਕਰਨ',
                'example': 'ਉਹ [ਹੱਥੀਂ] ਕੀਤਾ ਕੰਮ ਏ।',
                'grammatical_features_item_ids': [masculine, instrumental_case, dual],
                'optional': True,
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'punjabi-noun-feminine-guru': {
        '@attribution': {'users': ['Satdeep Gill', 'عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'ਪੰਜਾਬੀ ਨਾਂਵ ਇਸਤਰੀ ਲਿੰਗ',
        'language': language_Gurmukhi,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਇਹ [ਅੱਖ] ਸੋਹਣੀ ਏ।',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਇਹ [ਅੱਖੀਆਂ] ਸੋਹਣੀਆਂ ਹਨ।',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਮੇਰੀ [ਅੱਖ] ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਮੇਰੀਆਂ [ਅੱਖੀਆਂ] ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
            {
                'section_break': True,
                'label': 'ਇੱਕ ਵਚਨ, ਅਪਾਦਾਨ',
                'example': 'ਉਹ [ਅੱਖਿਓਂ] ਨਜ਼ਰਾ ਜਾਵਣ।؜',
                'grammatical_features_item_ids': [feminine, ablative_case, singular],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਇੱਕ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਵੇ ਓ [ਅੱਖੇ]!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'ਬਹੁ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਹੇ ਹਸੀਨ [ਅੱਖੋ]!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਇੱਕ ਵਚਨ, ਵਸਨੀਕ',
                'example': 'ਉਹ [ਅੱਖੀਂ] ਜਾਵਣ।',
                'grammatical_features_item_ids': [feminine, locative_case, singular],
                'optional': True,
            },
            {
                'label': 'ਬਹੁ ਵਚਨ, ਵਸਨੀਕ',
                'example': 'ਉਹ [ਅੱਖੀਂ] ਘੱਟਾ ਪਾਏਗਾ।؜',
                'grammatical_features_item_ids': [feminine, locative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਦੋ ਵਚਨ, ਕਰਨ',
                'example': 'ਉਹ [ਅੱਖੀਂ] ਦੇਖਿਆ ਸੀ।؜',
                'grammatical_features_item_ids': [feminine, instrumental_case, dual],
                'optional': True,
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'punjabi-adjective-red-guru': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'ਪੰਜਾਬੀ ਲਾਲ ਗੁਣ ਨਾਂ',
        'language': language_Gurmukhi,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'ਇਕੱਲਾ',
                'example': 'ਹਾਂ ਜੀ, ਮੈਂ [ਠੀਕ] ਆਂ।',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, indeclinable_adjective)],
            paradigm_class: [statement(paradigm_class, lāl_surakh_adjective)],
        },
    },

    'punjabi-adjective-black-guru': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'ਪੰਜਾਬੀ ਕਾਲਾ ਗੁਣ ਨਾਂ',
        'language': language_Gurmukhi,
        'lexical_category_item_id': adjective,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਵੱਡਾ] ਘੋੜਾ ਏ।',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਵੱਡੇ] ਘੋੜੇ ਹਨ।',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਵੱਡੇ] ਘੋੜੇ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਵੱਡਿਆਂ] ਘੋੜਿਆਂ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'label': 'ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰਿਆ [ਵੱਡਿਆ] ਘੋੜਿਆ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰਿਓ [ਵੱਡਿਓ] ਘੋੜਿਓ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [masculine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਵੱਡੀ] ਘੋੜੀ ਏ।',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਵੱਡੀਆਂ] ਘੋੜੀਆਂ ਏ।',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਵੱਡੀ] ਘੋੜੀ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਵੱਡੀਆਂ] ਘੋੜੀਆਂ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
            {
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰੀਏ [ਵੱਡੀਏ] ਘੋੜੀਏ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰੀਓ [ਵੱਡੀਓ] ਘੋੜੀਓ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [feminine, vocative_case, plural],
                'optional': True,
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, declinable_adjective)],
            paradigm_class: [statement(paradigm_class, kālā_adjective)],
        },
    },

    'punjabi-adjective-longer-guru': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'ਪੰਜਾਬੀ ਲਮੇਰਾ ਗੁਣ ਨਾਂ',
        'language': language_Gurmukhi,
        'lexical_category_item_id': adjective,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'ਨਫ਼ਸੀ, ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਲੰਮਾ] ਘੋੜਾ ਏ।',
                'grammatical_features_item_ids': [positive, masculine, direct_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਲੰਮੇ] ਘੋੜੇ ਹਨ।',
                'grammatical_features_item_ids': [positive, masculine, direct_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਲੰਮੇ] ਘੋੜੇ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [positive, masculine, oblique_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਲੰਮਿਆਂ] ਘੋੜਿਆਂ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [positive, masculine, oblique_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰਿਆ [ਲੰਮਿਆ] ਘੋੜਿਆ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [positive, masculine, vocative_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
                'optional': True,
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰਿਓ [ਲੰਮਿਓ] ਘੋੜਿਓ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [positive, masculine, vocative_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਨਫ਼ਸੀ, ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਲੰਮੀ] ਘੋੜੀ ਏ।',
                'grammatical_features_item_ids': [positive, feminine, direct_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਲੰਮੀਆਂ] ਘੋੜੀਆਂ ਏ।',
                'grammatical_features_item_ids': [positive, feminine, direct_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਲੰਮੀ] ਘੋੜੀ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [positive, feminine, oblique_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਲੰਮੀਆਂ] ਘੋੜੀਆਂ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [positive, feminine, oblique_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰੀਏ [ਲੰਮੀਏ] ਘੋੜੀਏ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [positive, feminine, vocative_case, singular],
                'grammatical_features_item_ids_optional': set([positive]),
                'optional': True,
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰੀਓ [ਲੰਮੀਓ] ਘੋੜੀਓ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [positive, feminine, vocative_case, plural],
                'grammatical_features_item_ids_optional': set([positive]),
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਤਸ਼ਬੀਹ, ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਲਮੇਰਾ] ਘੋੜਾ ਏ।',
                'grammatical_features_item_ids': [comparative, masculine, direct_case, singular],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਲਮੇਰੇ] ਘੋੜੇ ਹਨ।',
                'grammatical_features_item_ids': [comparative, masculine, direct_case, plural],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਲਮੇਰੇ] ਘੋੜੇ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [comparative, masculine, oblique_case, singular],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਲਮੇਰਿਆਂ] ਘੋੜਿਆਂ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [comparative, masculine, oblique_case, plural],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰਿਆ [ਲਮੇਰਿਆ] ਘੋੜਿਆ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [comparative, masculine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰਿਓ [ਲਮੇਰਿਓ] ਘੋੜਿਓ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [comparative, masculine, vocative_case, plural],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਤਸ਼ਬੀਹ, ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਲਮੇਰੀ] ਘੋੜੀ ਏ।',
                'grammatical_features_item_ids': [comparative, feminine, direct_case, singular],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਉਹ [ਲਮੇਰੀਆਂ] ਘੋੜੀਆਂ ਏ।',
                'grammatical_features_item_ids': [comparative, feminine, direct_case, plural],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਲਮੇਰੀ] ਘੋੜੀ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [comparative, feminine, oblique_case, singular],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਉਸ [ਲਮੇਰੀਆਂ] ਘੋੜੀਆਂ ਨੂੰ ਵੇਖੋ।',
                'grammatical_features_item_ids': [comparative, feminine, oblique_case, plural],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰੀਏ [ਲਮੇਰੀਏ] ਘੋੜੀਏ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [comparative, feminine, vocative_case, singular],
                'optional': True,
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਪਕਾਰਨ',
                'example': 'ਆਹ ਮੇਰੀਓ [ਲਮੇਰੀਓ] ਘੋੜੀਓ, ਆ ਜਾਓ!؜',
                'grammatical_features_item_ids': [comparative, feminine, vocative_case, plural],
                'optional': True,
            },
        ],
        'statements': {
            instance_of: [statement(instance_of, comparable_adjective)],
            paradigm_class: [statement(paradigm_class, lamera_adjective)],
        },
    },

    'punjabi-adverb-indeclinable-guru': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'ਪੰਜਾਬੀ ਆਮ ਗੁਣ ਫ਼ੇਅਲ',
        'language': language_Gurmukhi,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'ਇਕੱਲਾ',
                'example': 'ਤੁਸੀਂ [ਅੱਜ] ਕੀਹ ਕੀਤਾ?',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements(instance_of, indeclinable_adverb),
    },

    'punjabi-adverb-declinable-guru': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'ਪੰਜਾਬੀ ਐਸਾ ਬਦਲ ਕਰਦਾ ਗੁਣ ਫ਼ੇਅਲ',
        'language': language_Gurmukhi,
        'lexical_category_item_id': adverb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਘੋੜਾ [ਬੜਾ] ਸੋਹਣਾ ਤੁਰਦਾ।',
                'grammatical_features_item_ids': [masculine, direct_case, singular],
            },
            {
                'label': 'ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਘੋੜੇ [ਬੜੇ] ਸੋਹਣੇ ਤੁਰਦੇ।',
                'grammatical_features_item_ids': [masculine, direct_case, plural],
            },
            {
                'label': 'ਪੁਲਿੰਗ, ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਘੋੜੇ [ਬੜੇ] ਸੋਹਣੇ ਤੁਰਨ ਲਈ ਉਹ ਜ਼ੋਰ ਲੋੜਦਾ।',
                'grammatical_features_item_ids': [masculine, oblique_case, singular],
            },
            {
                'label': 'ਪੁਲਿੰਗ, ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਘੋੜਿਆਂ [ਬੜਿਆਂ] ਸੋਹਣਿਆਂ ਤੁਰਨ ਲਈ ਉਹ ਜ਼ੋਰ ਲੋੜਦਾ।',
                'grammatical_features_item_ids': [masculine, oblique_case, plural],
            },
            {
                'section_break': True,
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਘੋੜੀ [ਬੜੀ] ਸੋਹਣੀ ਤੁਰਦੀ।',
                'grammatical_features_item_ids': [feminine, direct_case, singular],
            },
            {
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਫਾਇਲੀ',
                'example': 'ਘੋੜੀਆਂ [ਬੜੀਆਂ] ਸੋਹਣੀਆਂ ਤੁਰਦੀਆਂ।',
                'grammatical_features_item_ids': [feminine, direct_case, plural],
            },
            {
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਇੱਕ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਘੋੜੀ [ਬੜੀ] ਸੋਹਣੀ ਤੁਰਨ ਲਈ ਉਹ ਜ਼ੋਰ ਲੋੜਦਾ।',
                'grammatical_features_item_ids': [feminine, oblique_case, singular],
            },
            {
                'label': 'ਇਸਤਰੀ ਲਿੰਗ, ਬਹੁ ਵਚਨ, ਮਫਊਲੀ',
                'example': 'ਘੋੜੀਆਂ [ਬੜੀਆਂ] ਸੋਹਣੀਆਂ ਤੁਰਨ ਲਈ ਉਹ ਜ਼ੋਰ ਲੋੜਦਾ।',
                'grammatical_features_item_ids': [feminine, oblique_case, plural],
            },
        ],
        'statements': statements(instance_of, declinable_adverb),
    },

    'punjabi-adverb-comparable-guru': {
        '@attribution': {'users': ['عُثمان'], 'title': 'Wikidata:Wikidata Lexeme Forms/Punjabi'},
        'label': 'ਪੰਜਾਬੀ ਗੁਣ ਫ਼ੇਅਲ ਤਫ਼ਜ਼ੀਲ',
        'language': language_Gurmukhi,
        'lexical_category_item_id': adverb,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'ਨਫ਼ਸੀ, ਫ਼ਾਇਲੀ',
                'example': 'ਮੈਂ ਫੇਰ ਮੂੰਹ [ਪਰੇ] ਕਰਦਿਆਂ ਚਲਿਆ।',
                'grammatical_features_item_ids': [positive, direct_case],
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਮਫ਼ਊਲੀ',
                'example': 'ਪਾਣੀ ਨੂੰ [ਪਰੇ] ਕਰਨ ਲਈ ਆਸਾ ਲਾਉਂਦਾ ਏ।',
                'grammatical_features_item_ids': [positive, oblique_case],
            },
            {
                'label': 'ਨਫ਼ਸੀ, ਅਪਾਦਾਨ',
                'example': 'ਚੌਕ ਤੋਂ [ਪਰਿਓਂ] ਈ ਮੈਂ ਅੰਦਾਜ਼ਾ ਏ।',
                'grammatical_features_item_ids': [positive, ablative_case],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'ਤਸ਼ਬੀਹ, ਫ਼ਾਇਲੀ',
                'example': 'ਪਿਆਰ ਵਲ [ਪਰੇਰੇ] ਜਾਂਦੇ ਹਨ।',
                'grammatical_features_item_ids': [comparative, direct_case],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਮਫ਼ਊਲੀ',
                'example': 'ਪਿਆਰ ਵਲ [ਪਰੇਰੇ] ਜਾਣ ਦੀ ਆਸ ਬੱਝਦੀ ਏ।',
                'grammatical_features_item_ids': [comparative, oblique_case],
            },
            {
                'label': 'ਤਸ਼ਬੀਹ, ਅਪਾਦਾਨ',
                'example': 'ਮੈਂ ਪੰਜ ਗੁਜ਼ [ਪਰੇਰਿਓਂ] ਜਾ ਕੇ ਫਲ ਲਿਆਉਂਦਾ ਆਂ।',
                'grammatical_features_item_ids': [comparative, ablative_case],
            },
        ],
        'statements': statements(instance_of, comparable_adverb),
    },

    'portuguese-noun-biform': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'substantivo biforme em português',
        'language': language_Portuguese,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'masculino singular normal',
                'example': 'Eu vi um [amigo] seu.',
                'grammatical_features_item_ids': [masculine, singular, positive],
            },
            {
                'label': 'masculino plural normal',
                'example': 'Eu vi uns [amigos] seus.',
                'grammatical_features_item_ids': [masculine, plural, positive],
            },
            {
                'label': 'feminino singular normal',
                'example': 'Eu vi uma [amiga] sua.',
                'grammatical_features_item_ids': [feminine, singular, positive],
            },
            {
                'label': 'feminino plural normal',
                'example': 'Eu vi umas [amigas] suas.',
                'grammatical_features_item_ids': [feminine, plural, positive],
            },
            {
                'section_break': True,
                'label': 'masculino singular diminutivo',
                'example': 'Eu vi um [amiguinho] seu.',
                'grammatical_features_item_ids': [masculine, singular, diminutive],
                'optional': True,
            },
            {
                'label': 'masculino plural diminutivo',
                'example': 'Eu vi uns [amiguinhos] seus.',
                'grammatical_features_item_ids': [masculine, plural, diminutive],
                'optional': True,
            },
            {
                'label': 'feminino singular diminutivo',
                'example': 'Eu vi uma [amiguinha] sua.',
                'grammatical_features_item_ids': [feminine, singular, diminutive],
                'optional': True,
            },
            {
                'label': 'feminino plural diminutivo',
                'example': 'Eu vi umas [amiguinhas] suas.',
                'grammatical_features_item_ids': [feminine, plural, diminutive],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'masculino singular aumentativo',
                'example': 'Eu vi um [amigão] seu.',
                'grammatical_features_item_ids': [masculine, singular, augmentative],
                'optional': True,
            },
            {
                'label': 'masculino plural aumentativo',
                'example': 'Eu vi uns [amigões] seus.',
                'grammatical_features_item_ids': [masculine, plural, augmentative],
                'optional': True,
            },
            {
                'label': 'feminino singular aumentativo',
                'example': 'Eu vi uma [amigona] sua.',
                'grammatical_features_item_ids': [feminine, singular, augmentative],
                'optional': True,
            },
            {
                'label': 'feminino plural aumentativo',
                'example': 'Eu vi umas [amigonas] suas.',
                'grammatical_features_item_ids': [feminine, plural, augmentative],
                'optional': True,
            },
        ],
    },

    'portuguese-noun-masculine': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'substantivo masculino em português',
        'language': language_Portuguese,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'singular normal',
                'example': 'Ele tem um [nariz].',
                'grammatical_features_item_ids': [singular, positive],
            },
            {
                'label': 'plural normal',
                'example': 'Eles têm uns [narizes].',
                'grammatical_features_item_ids': [plural, positive],
            },
            {
                'section_break': True,
                'label': 'singular diminutivo',
                'example': 'Ele tem um [narizinho/narizito].',
                'grammatical_features_item_ids': [singular, diminutive],
                'optional': True,
            },
            {
                'label': 'plural diminutivo',
                'example': 'Eles têm uns [narizinhos/narizitos].',
                'grammatical_features_item_ids': [plural, diminutive],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular aumentativo',
                'example': 'Ele tem um [narigão/narizão].',
                'grammatical_features_item_ids': [singular, augmentative],
                'optional': True,
            },
            {
                'label': 'plural aumentativo',
                'example': 'Eles têm uns [narigões/narizões].',
                'grammatical_features_item_ids': [plural, augmentative],
                'optional': True,
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'portuguese-noun-feminine': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'substantivo feminino em português',
        'language': language_Portuguese,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'singular feminino normal',
                'example': 'Ela tem uma [boca].',
                'grammatical_features_item_ids': [singular, positive],
            },
            {
                'label': 'plural feminino normal',
                'example': 'Elas têm umas [bocas].',
                'grammatical_features_item_ids': [plural, positive],
            },
            {
                'section_break': True,
                'label': 'singular feminino diminutivo',
                'example': 'Ela tem uma [boquinha/boquita].',
                'grammatical_features_item_ids': [singular, diminutive],
                'optional': True,
            },
            {
                'label': 'plural feminino diminutivo',
                'example': 'Elas têm umas [boquinhas/boquitas].',
                'grammatical_features_item_ids': [plural, diminutive],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular feminino aumentativo',
                'example': 'Ela tem uma [bocona/bocarra].',
                'grammatical_features_item_ids': [singular, augmentative],
                'optional': True,
            },
            {
                'label': 'plural feminino aumentativo',
                'example': 'Elas têm umas [boconas/bocarras].',
                'grammatical_features_item_ids': [plural, augmentative],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular masculino aumentativo',
                'example': 'Ela tem um [bocão].',
                'grammatical_features_item_ids': [masculine, singular, augmentative],
                'optional': True,
            },
            {
                'label': 'plural masculino aumentativo',
                'example': 'Elas têm uns [bocões].',
                'grammatical_features_item_ids': [masculine, plural, augmentative],
                'optional': True,
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'portuguese-noun-uniform': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'substantivo uniforme em português',
        'language': language_Portuguese,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'uniforme singular normal',
                'example': 'Nós temos que encontrar aquele(a) [motorista] hoje mesmo.',
                'grammatical_features_item_ids': [singular, positive],
            },
            {
                'label': 'uniforme plural normal',
                'example': 'Nós temos que encontrar aqueles(as) [motoristas] hoje mesmo.',
                'grammatical_features_item_ids': [plural, positive],
            },
        ],
        'statements': statements(grammatical_gender, common_of_two_genders),
    },

    'portuguese-verb': {
        '@attribution': {'users': ['Carybe', 'EnaldoSS', 'Joalpe', 'Waldir'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'verbo em português',
        'language': language_Portuguese,
        'lexical_category_item_id': verb,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'Infinitivo Impessoal',
                'example': 'O [cantar] dos golfinhos é belo.',
                'grammatical_features_item_ids': [impersonal_infinitive],
            },
            {
                'label': 'Gerúndio',
                'example': 'Ele estava [cantando] no chuveiro.',
                'grammatical_features_item_ids': [gerund],
            },
            {
                'label': 'Particípio',
                'example': 'Estava sem voz, pois havia [cantado] mais cedo.',
                'grammatical_features_item_ids': [participle],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Presente do Modo Indicativo',
                'example': 'Eu [canto] às segundas-feiras.',
                'grammatical_features_item_ids': [first_person, singular, present_tense, indicative],
            },
            {
                'label': 'Segunda Pessoa do Singular do Presente do Modo Indicativo',
                'example': 'Tu [cantas] às terças-feiras.',
                'grammatical_features_item_ids': [second_person, singular, present_tense, indicative],
            },
            {
                'label': 'Terceira Pessoa do Singular do Presente do Modo Indicativo',
                'example': 'Ele [canta] às quartas-feiras.',
                'grammatical_features_item_ids': [third_person, singular, present_tense, indicative],
            },
            {
                'label': 'Primeira Pessoa do Plural do Presente do Modo Indicativo',
                'example': 'Nós [cantamos] às quintas-feiras.',
                'grammatical_features_item_ids': [first_person, plural, present_tense, indicative],
            },
            {
                'label': 'Segunda Pessoa do Plural do Presente do Modo Indicativo',
                'example': 'Vós [cantais] às sextas-feiras.',
                'grammatical_features_item_ids': [second_person, plural, present_tense, indicative],
            },
            {
                'label': 'Terceira Pessoa do Plural do Presente do Modo Indicativo',
                'example': 'Eles [cantam] aos sábados.',
                'grammatical_features_item_ids': [third_person, plural, present_tense, indicative],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Eu [cantei] ontem no palco.',
                'grammatical_features_item_ids': [first_person, singular, 'Q64005357', indicative],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Tu [cantaste] ontem no palco.',
                'grammatical_features_item_ids': [second_person, singular, 'Q64005357', indicative],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Perfeito do Modo Indicativo',
                'example': 'Ele [cantou] ontem no palco.',
                'grammatical_features_item_ids': [third_person, singular, 'Q64005357', indicative],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Nós [cantamos] ontem no palco.',
                'grammatical_features_item_ids': [first_person, plural, 'Q64005357', indicative],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Vós [cantastes] ontem no palco.',
                'grammatical_features_item_ids': [second_person, plural, 'Q64005357', indicative],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Perfeito do Modo Indicativo',
                'example': 'Eles [cantaram] ontem no palco.',
                'grammatical_features_item_ids': [third_person, plural, 'Q64005357', indicative],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Eu [cantava] no coral quando acabou a luz.',
                'grammatical_features_item_ids': [first_person, singular, past_imperfect, indicative],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Tu [cantavas] no coral quando acabou a luz.',
                'grammatical_features_item_ids': [second_person, singular, past_imperfect, indicative],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Ele [cantava] no coral quando acabou a luz.',
                'grammatical_features_item_ids': [third_person, singular, past_imperfect, indicative],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Nós [cantávamos] no coral quando acabou a luz.',
                'grammatical_features_item_ids': [first_person, plural, past_imperfect, indicative],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Vós [cantáveis] no coral quando acabou a luz.',
                'grammatical_features_item_ids': [second_person, plural, past_imperfect, indicative],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Imperfeito do Modo Indicativo',
                'example': 'Eles [cantavam] no coral quando acabou a luz.',
                'grammatical_features_item_ids': [third_person, plural, past_imperfect, indicative],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que eu [cantara] antigamente.',
                'grammatical_features_item_ids': [first_person, singular, pluperfect, indicative],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que tu [cantaras] antigamente.',
                'grammatical_features_item_ids': [second_person, singular, pluperfect, indicative],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que ele [cantara] antigamente.',
                'grammatical_features_item_ids': [third_person, singular, pluperfect, indicative],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que nós [cantáramos] antigamente.',
                'grammatical_features_item_ids': [first_person, plural, pluperfect, indicative],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que ele vós [cantáreis] antigamente.',
                'grammatical_features_item_ids': [second_person, plural, pluperfect, indicative],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Mais-que-perfeito do Modo Indicativo',
                'example': 'Esse é o grupo em que ele eles [cantaram] antigamente.',
                'grammatical_features_item_ids': [third_person, plural, pluperfect, indicative],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Futuro do Presente do Modo Indicativo',
                'example': 'Eu [cantarei] amanhã no teatro municipal.',
                'grammatical_features_item_ids': [first_person, singular, 'Q63997439', indicative],
            },
            {
                'label': 'Segunda Pessoa do Singular do Futuro do Presente do Modo Indicativo',
                'example': 'Tu [cantarás] amanhã no teatro municipal.',
                'grammatical_features_item_ids': [second_person, singular, 'Q63997439', indicative],
            },
            {
                'label': 'Terceira Pessoa do Singular do Futuro do Presente do Modo Indicativo',
                'example': 'Ele [cantará] amanhã no teatro municipal.',
                'grammatical_features_item_ids': [third_person, singular, 'Q63997439', indicative],
            },
            {
                'label': 'Primeira Pessoa do Plural do Futuro do Presente do Modo Indicativo',
                'example': 'Nós [cantaremos] amanhã no teatro municipal.',
                'grammatical_features_item_ids': [first_person, plural, 'Q63997439', indicative],
            },
            {
                'label': 'Segunda Pessoa do Plural do Futuro do Presente do Modo Indicativo',
                'example': 'Vós [cantareis] amanhã no teatro municipal.',
                'grammatical_features_item_ids': [second_person, plural, 'Q63997439', indicative],
            },
            {
                'label': 'Terceira Pessoa do Plural do Futuro do Presente do Modo Indicativo',
                'example': 'Eles [cantarão] amanhã no teatro municipal.',
                'grammatical_features_item_ids': [third_person, plural, 'Q63997439', indicative],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Futuro do Pretérito do Modo Indicativo',
                'example': 'Eu [cantaria] se fosse possível.',
                'grammatical_features_item_ids': [first_person, singular, 'Q63997520', indicative],
            },
            {
                'label': 'Segunda Pessoa do Singular do Futuro do Pretérito do Modo Indicativo',
                'example': 'Tu [cantarias] se fosse possível.',
                'grammatical_features_item_ids': [second_person, singular, 'Q63997520', indicative],
            },
            {
                'label': 'Terceira Pessoa do Singular do Futuro do Pretérito do Modo Indicativo',
                'example': 'Ele [cantaria] se fosse possível.',
                'grammatical_features_item_ids': [third_person, singular, 'Q63997520', indicative],
            },
            {
                'label': 'Primeira Pessoa do Plural do Futuro do Pretérito do Modo Indicativo',
                'example': 'Nós [cantaríamos] se fosse possível.',
                'grammatical_features_item_ids': [first_person, plural, 'Q63997520', indicative],
            },
            {
                'label': 'Segunda Pessoa do Plural do Futuro do Pretérito do Modo Indicativo',
                'example': 'Vós [cantaríeis] se fosse possível.',
                'grammatical_features_item_ids': [second_person, plural, 'Q63997520', indicative],
            },
            {
                'label': 'Terceira Pessoa do Plural do Futuro do Pretérito do Modo Indicativo',
                'example': 'Eles [cantariam] se fosse possível.',
                'grammatical_features_item_ids': [third_person, plural, 'Q63997520', indicative],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Presente do Modo Subjuntivo',
                'example': 'Espero que eu [cante] logo.',
                'grammatical_features_item_ids': [first_person, singular, present_tense, subjunctive],
            },
            {
                'label': 'Segunda Pessoa do Singular do Presente do Modo Subjuntivo',
                'example': 'Espero que tu [cantes] logo.',
                'grammatical_features_item_ids': [second_person, singular, present_tense, subjunctive],
            },
            {
                'label': 'Terceira Pessoa do Singular do Presente do Modo Subjuntivo',
                'example': 'Espero que ele [cante] logo.',
                'grammatical_features_item_ids': [third_person, singular, present_tense, subjunctive],
            },
            {
                'label': 'Primeira Pessoa do Plural do Presente do Modo Subjuntivo',
                'example': 'Espero que nós [cantemos] logo.',
                'grammatical_features_item_ids': [first_person, plural, present_tense, subjunctive],
            },
            {
                'label': 'Segunda Pessoa do Plural do Presente do Modo Subjuntivo',
                'example': 'Espero que vós [canteis] logo.',
                'grammatical_features_item_ids': [second_person, plural, present_tense, subjunctive],
            },
            {
                'label': 'Terceira Pessoa do Plural do Presente do Modo Subjuntivo',
                'example': 'Espero que eles [cantem] logo.',
                'grammatical_features_item_ids': [third_person, plural, present_tense, subjunctive],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se eu [cantasse] mais alto, seria melhor.',
                'grammatical_features_item_ids': [first_person, singular, past_imperfect, subjunctive],
            },
            {
                'label': 'Segunda Pessoa do Singular do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se tu [cantasses] mais alto, seria melhor.',
                'grammatical_features_item_ids': [second_person, singular, past_imperfect, subjunctive],
            },
            {
                'label': 'Terceira Pessoa do Singular do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se ele [cantasse] mais alto, seria melhor.',
                'grammatical_features_item_ids': [third_person, singular, past_imperfect, subjunctive],
            },
            {
                'label': 'Primeira Pessoa do Plural do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se nós [cantássemos] mais alto, seria melhor.',
                'grammatical_features_item_ids': [first_person, plural, past_imperfect, subjunctive],
            },
            {
                'label': 'Segunda Pessoa do Plural do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se vós [cantásseis] mais alto, seria melhor.',
                'grammatical_features_item_ids': [second_person, plural, past_imperfect, subjunctive],
            },
            {
                'label': 'Terceira Pessoa do Plural do Pretérito Imperfeito do Modo Subjuntivo',
                'example': 'Se eles [cantassem] mais alto, seria melhor.',
                'grammatical_features_item_ids': [third_person, plural, past_imperfect, subjunctive],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Futuro do Modo Subjuntivo',
                'example': 'Quando eu [cantar] os outros ouvirão.',
                'grammatical_features_item_ids': [first_person, singular, future_tense, subjunctive],
            },
            {
                'label': 'Segunda Pessoa do Singular do Futuro do Modo Subjuntivo',
                'example': 'Quando tu [cantares] os outros ouvirão.',
                'grammatical_features_item_ids': [second_person, singular, future_tense, subjunctive],
            },
            {
                'label': 'Terceira Pessoa do Singular do Futuro do Modo Subjuntivo',
                'example': 'Quando ele [cantar] os outros ouvirão.',
                'grammatical_features_item_ids': [third_person, singular, future_tense, subjunctive],
            },
            {
                'label': 'Primeira Pessoa do Plural do Futuro do Modo Subjuntivo',
                'example': 'Quando nós [cantarmos] os outros ouvirão.',
                'grammatical_features_item_ids': [first_person, plural, future_tense, subjunctive],
            },
            {
                'label': 'Segunda Pessoa do Plural do Futuro do Modo Subjuntivo',
                'example': 'Quando vós [cantardes] os outros ouvirão.',
                'grammatical_features_item_ids': [second_person, plural, future_tense, subjunctive],
            },
            {
                'label': 'Terceira Pessoa do Plural do Futuro do Modo Subjuntivo',
                'example': 'Quando eles [cantarem] os outros ouvirão.',
                'grammatical_features_item_ids': [third_person, plural, future_tense, subjunctive],
            },
            {
                'section_break': True,
                'label': 'Segunda Pessoa do Singular do Modo Imperativo Afirmativo',
                'example': '[canta] tu agora que há tempo.',
                'grammatical_features_item_ids': [second_person, singular, imperative_affirmative],
            },
            {
                'label': 'Terceira Pessoa do Singular do Modo Imperativo Afirmativo',
                'example': '[canta] você agora que há tempo.',
                'grammatical_features_item_ids': [third_person, singular, imperative_affirmative],
            },
            {
                'label': 'Primeira Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[cantemos] nós agora que há tempo.',
                'grammatical_features_item_ids': [first_person, plural, imperative_affirmative],
            },
            {
                'label': 'Segunda Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[cantai] vós agora que há tempo.',
                'grammatical_features_item_ids': [second_person, plural, imperative_affirmative],
            },
            {
                'label': 'Terceira Pessoa do Plural do Modo Imperativo Afirmativo',
                'example': '[cantem] vocês agora que há tempo.',
                'grammatical_features_item_ids': [third_person, plural, imperative_affirmative],
            },
            {
                'section_break': True,
                'label': 'Segunda Pessoa do Singular do Modo Imperativo Negativo',
                'example': 'Não [cantes] tu, ainda não está na hora.',
                'grammatical_features_item_ids': [second_person, singular, negative_imperative],
            },
            {
                'label': 'Terceira Pessoa do Singular do Modo Imperativo Negativo',
                'example': 'Não [cante] você, ainda não está na hora.',
                'grammatical_features_item_ids': [third_person, singular, negative_imperative],
            },
            {
                'label': 'Primeira Pessoa do Plural do Modo Imperativo Negativo',
                'example': 'Não [cantemos] nós, ainda não está na hora.',
                'grammatical_features_item_ids': [first_person, plural, negative_imperative],
            },
            {
                'label': 'Segunda Pessoa do Plural do Modo Imperativo Negativo',
                'example': 'Não [canteis] vós, ainda não está na hora.',
                'grammatical_features_item_ids': [second_person, plural, negative_imperative],
            },
            {
                'label': 'Terceira Pessoa do Plural do Modo Imperativo Negativo',
                'example': 'Não [cantem] vocês, ainda não está na hora.',
                'grammatical_features_item_ids': [third_person, plural, negative_imperative],
            },
            {
                'section_break': True,
                'label': 'Primeira Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantar] eu ganhei vários prêmios.',
                'grammatical_features_item_ids': [first_person, singular, personal_infinitive],
            },
            {
                'label': 'Segunda Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantares] tu ganhaste vários prêmios.',
                'grammatical_features_item_ids': [second_person, singular, personal_infinitive],
            },
            {
                'label': 'Terceira Pessoa do Singular do Infinitivo Pessoal',
                'example': 'Por [cantar] ele ganhou vários prêmios.',
                'grammatical_features_item_ids': [third_person, singular, personal_infinitive],
            },
            {
                'label': 'Primeira Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantarmos] nós ganhamos vários prêmios.',
                'grammatical_features_item_ids': [first_person, plural, personal_infinitive],
            },
            {
                'label': 'Segunda Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantardes] vós ganhastes vários prêmios.',
                'grammatical_features_item_ids': [second_person, plural, personal_infinitive],
            },
            {
                'label': 'Terceira Pessoa do Plural do Infinitivo Pessoal',
                'example': 'Por [cantarem] eles ganharam vários prêmios.',
                'grammatical_features_item_ids': [third_person, plural, personal_infinitive],
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
        'language': language_Portuguese,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'singular masculino normal',
                'example': 'Eu vi um homem [alto].',
                'grammatical_features_item_ids': [masculine, singular, positive],
            },
            {
                'label': 'plural masculino normal',
                'example': 'Eu vi uns homens [altos].',
                'grammatical_features_item_ids': [masculine, plural, positive],
            },
            {
                'label': 'singular feminino normal',
                'example': 'Eu vi uma mulher [alta].',
                'grammatical_features_item_ids': [feminine, singular, positive],
            },
            {
                'label': 'plural feminino normal',
                'example': 'Eu vi umas mulheres [altas].',
                'grammatical_features_item_ids': [feminine, plural, positive],
            },
            {
                'section_break': True,
                'label': 'singular masculino superlativo',
                'example': 'Eu vi um homem [altíssimo].',
                'grammatical_features_item_ids': [masculine, singular, superlative],
                'optional': True,
            },
            {
                'label': 'plural masculino superlativo',
                'example': 'Eu vi uns homens [altíssimos].',
                'grammatical_features_item_ids': [masculine, plural, superlative],
                'optional': True,
            },
            {
                'label': 'singular feminino superlativo',
                'example': 'Eu vi uma mulher [altíssima].',
                'grammatical_features_item_ids': [feminine, singular, superlative],
                'optional': True,
            },
            {
                'label': 'plural feminino superlativo',
                'example': 'Eu vi umas mulheres [altíssimas].',
                'grammatical_features_item_ids': [feminine, plural, superlative],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular masculino diminutivo',
                'example': 'Eu vi um homem [altinho].',
                'grammatical_features_item_ids': [masculine, singular, diminutive],
                'optional': True,
            },
            {
                'label': 'plural masculino diminutivo',
                'example': 'Eu vi uns homens [altinhos].',
                'grammatical_features_item_ids': [masculine, plural, diminutive],
                'optional': True,
            },
            {
                'label': 'singular feminino diminutivo',
                'example': 'Eu vi uma mulher [altinha].',
                'grammatical_features_item_ids': [feminine, singular, diminutive],
                'optional': True,
            },
            {
                'label': 'plural feminino diminutivo',
                'example': 'Eu vi umas mulheres [altinhas].',
                'grammatical_features_item_ids': [feminine, plural, diminutive],
                'optional': True,
            },
            {
                'section_break': True,
                'label': 'singular masculino aumentativo',
                'example': 'Eu vi um homem [altão].',
                'grammatical_features_item_ids': [masculine, singular, augmentative],
                'optional': True,
            },
            {
                'label': 'plural masculino aumentativo',
                'example': 'Eu vi uns homens [altões].',
                'grammatical_features_item_ids': [masculine, plural, augmentative],
                'optional': True,
            },
            {
                'label': 'singular feminino aumentativo',
                'example': 'Eu vi uma mulher [altona].',
                'grammatical_features_item_ids': [feminine, singular, augmentative],
                'optional': True,
            },
            {
                'label': 'plural feminino aumentativo',
                'example': 'Eu vi umas mulheres [altonas].',
                'grammatical_features_item_ids': [feminine, plural, augmentative],
                'optional': True,
            },
        ],
    },

    'portuguese-adjective-uniform': {
        '@attribution': {'users': ['EnaldoSS', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'adjetivo uniforme em português',
        'language': language_Portuguese,
        'lexical_category_item_id': adjective,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'uniforme singular normal',
                'example': 'Acho sim que ele(a) é um(a) bom(a) [artista].',
                'grammatical_features_item_ids': [singular, positive],
            },
            {
                'label': 'uniforme plural normal',
                'example': 'Acho sim que eles(as) são bons(as) [artistas].',
                'grammatical_features_item_ids': [plural, positive],
            },
        ],
        'statements': statements(grammatical_gender, common_of_two_genders),
    },

    'portuguese-adverb-modal': {
        '@attribution': {'users': ['EnaldoSS'], 'title': 'Wikidata:Wikidata Lexeme Forms/Portuguese'},
        'label': 'advérbio de modo em português',
        'language': language_Portuguese,
        'lexical_category_item_id': adverb,
        'forms': [
            {
                'label': 'Advérbio de modo',
                'example': 'A prova estava [extremamente] difícil.',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements(instance_of, modal_adverb),
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
        'language': language_Portuguese,
        'lexical_category_item_id': noun_phrase,
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
        'language': language_Portuguese,
        'lexical_category_item_id': verb_phrase,
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
        'language': language_Portuguese,
        'lexical_category_item_id': adjectival_phrase,
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
        'language': language_Portuguese,
        'lexical_category_item_id': adverbial_phrase,
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
        'language': language_Portuguese,
        'lexical_category_item_id': proverb,
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
        'language': language_Russian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ед.ч. им.п.',
                'example': 'Это [дом].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'ед.ч. род.п.',
                'example': 'Нет [дома].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'ед.ч. дат.п.',
                'example': 'Дать [дому].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'ед.ч. вин.п.',
                'example': 'Вижу [дом].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'ед.ч. твор.п.',
                'example': 'Руковожу [домом].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'ед.ч. предл.п.',
                'example': 'Говорить о [доме].',
                'grammatical_features_item_ids': [prepositional_case, singular],
            },
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это разные [дома].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет разных [домов].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать разным [домам].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу разные (разных) [дома].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу разными [домами].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о разных [домах].',
                'grammatical_features_item_ids': [prepositional_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'russian-noun-feminine': {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
        'label': 'русское существительное, женский род',
        'language': language_Russian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ед.ч. им.п.',
                'example': 'Это [собака].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'ед.ч. род.п.',
                'example': 'Нет [собаки].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'ед.ч. дат.п.',
                'example': 'Дать [собаке].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'ед.ч. вин.п.',
                'example': 'Вижу [собаку].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'ед.ч. твор.п.',
                'example': 'Руковожу [собакой].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'ед.ч. предл.п.',
                'example': 'Говорить о [собаке].',
                'grammatical_features_item_ids': [prepositional_case, singular],
            },
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это разные [собаки].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет разных [собак].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать разным [собакам].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу разных (разные) [собак].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу разными [собаками].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о разных [собаках].',
                'grammatical_features_item_ids': [prepositional_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'russian-noun-neuter': {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
        'label': 'русское существительное, средний род',
        'language': language_Russian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'ед.ч. им.п.',
                'example': 'Это [облако].',
                'grammatical_features_item_ids': [nominative_case, singular],
            },
            {
                'label': 'ед.ч. род.п.',
                'example': 'Нет [облака].',
                'grammatical_features_item_ids': [genitive_case, singular],
            },
            {
                'label': 'ед.ч. дат.п.',
                'example': 'Дать [облаку].',
                'grammatical_features_item_ids': [dative_case, singular],
            },
            {
                'label': 'ед.ч. вин.п.',
                'example': 'Вижу [облако].',
                'grammatical_features_item_ids': [accusative_case, singular],
            },
            {
                'label': 'ед.ч. твор.п.',
                'example': 'Руковожу [облаком].',
                'grammatical_features_item_ids': [instrumental_case, singular],
            },
            {
                'label': 'ед.ч. предл.п.',
                'example': 'Говорить о(б) [облаке].',
                'grammatical_features_item_ids': [prepositional_case, singular],
            },
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это разные [облака].',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет разных [облаков].',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать разным [облакам].',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу разные (разных) [облака].',
                'grammatical_features_item_ids': [accusative_case, plural],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу разными [облаками].',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о(б) [облаках].',
                'grammatical_features_item_ids': [prepositional_case, plural],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'russian-noun-pluraletantum': {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
        'label': 'имя существительное (Pluralia tantum, без рода)',
        'language': language_Russian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это [ножницы].',
                'grammatical_features_item_ids': [nominative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет [ножниц].',
                'grammatical_features_item_ids': [genitive_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать [ножницам].',
                'grammatical_features_item_ids': [dative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'мн.ч. вин.п.',
                'example': 'Вижу [ножницы].',
                'grammatical_features_item_ids': [accusative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу [ножницами].',
                'grammatical_features_item_ids': [instrumental_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о [ножницах].',
                'grammatical_features_item_ids': [prepositional_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
        ],
        'statements': statements(instance_of, plurale_tantum),
    },

    'russian-adjective': {
        '@attribution': {'users': ['Infovarius'], 'title': 'Wikidata:Wikidata Lexeme Forms/Russian'},
        'label': 'русское прилагательное',
        'language': language_Russian,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'ед.ч. м.р. им.п.',
                'example': 'Это [хороший] дом.',
                'grammatical_features_item_ids': [nominative_case, masculine, singular],
            },
            {
                'label': 'ед.ч. м.р. род.п.',
                'example': 'Нет [хорошего] дома.',
                'grammatical_features_item_ids': [genitive_case, masculine, singular],
            },
            {
                'label': 'ед.ч. м.р. дат.п.',
                'example': 'Дать [хорошему] дому.',
                'grammatical_features_item_ids': [dative_case, masculine, singular],
            },
            {
                'label': 'ед.ч. м.р. неодушевл. вин.п.',
                'example': 'Вижу [хороший] дом.',
                'grammatical_features_item_ids': [accusative_case, masculine, inanimate, masculine_inanimate, singular],
            },
            {
                'label': 'ед.ч. м.р. одушевл. вин.п.',
                'example': 'Вижу [хорошего] человека.',
                'grammatical_features_item_ids': [accusative_case, masculine, animate, masculine_animate, singular],
            },
            {
                'label': 'ед.ч. м.р. твор.п.',
                'example': 'Руковожу [хорошим] домом.',
                'grammatical_features_item_ids': [instrumental_case, masculine, singular],
            },
            {
                'label': 'ед.ч. м.р. предл.п.',
                'example': 'Говорить о [хорошем] доме.',
                'grammatical_features_item_ids': [prepositional_case, masculine, singular],
            },
            {
                'label': 'ед.ч. ж.р. им.п.',
                'example': 'Это [хорошая] еда.',
                'grammatical_features_item_ids': [nominative_case, feminine, singular],
            },
            {
                'label': 'ед.ч. ж.р. род.п.',
                'example': 'Нет [хорошей] еды.',
                'grammatical_features_item_ids': [genitive_case, feminine, singular],
            },
            {
                'label': 'ед.ч. ж.р. дат.п.',
                'example': 'Дать [хорошей] еде.',
                'grammatical_features_item_ids': [dative_case, feminine, singular],
            },
            {
                'label': 'ед.ч. ж.р. вин.п.',
                'example': 'Вижу [хорошую] еду.',
                'grammatical_features_item_ids': [accusative_case, feminine, singular],
            },
            {
                'label': 'ед.ч. ж.р. твор.п.',
                'example': 'Восхищаюсь [хорошей] едой.',
                'grammatical_features_item_ids': [instrumental_case, feminine, singular],
            },
            {
                'label': 'ед.ч. ж.р. предл.п.',
                'example': 'Говорить о [хорошей] еде.',
                'grammatical_features_item_ids': [prepositional_case, feminine, singular],
            },
            {
                'label': 'ед.ч. ср.р. им.п.',
                'example': 'Это [хорошее] облако.',
                'grammatical_features_item_ids': [nominative_case, neuter, singular],
            },
            {
                'label': 'ед.ч. ср.р. род.п.',
                'example': 'Нет [хорошего] облака.',
                'grammatical_features_item_ids': [genitive_case, neuter, singular],
            },
            {
                'label': 'ед.ч. ср.р. дат.п.',
                'example': 'Дать [хорошему] облаку.',
                'grammatical_features_item_ids': [dative_case, neuter, singular],
            },
            {
                'label': 'ед.ч. ср.р. вин.п.',
                'example': 'Вижу [хорошее] облако.',
                'grammatical_features_item_ids': [accusative_case, neuter, singular],
            },
            {
                'label': 'ед.ч. ср.р. твор.п.',
                'example': 'Руковожу [хорошим] облаком.',
                'grammatical_features_item_ids': [instrumental_case, neuter, singular],
            },
            {
                'label': 'ед.ч. ср.р. предл.п.',
                'example': 'Говорить о [хорошем] облаке.',
                'grammatical_features_item_ids': [prepositional_case, neuter, singular],
            },
            {
                'label': 'мн.ч. им.п.',
                'example': 'Это [хорошие] дома/девочки/облака.',
                'grammatical_features_item_ids': [nominative_case, plural],
            },
            {
                'label': 'мн.ч. род.п.',
                'example': 'Нет [хороших] домов/девочек/облаков.',
                'grammatical_features_item_ids': [genitive_case, plural],
            },
            {
                'label': 'мн.ч. дат.п.',
                'example': 'Дать [хорошим] домам/девочкам/облакам.',
                'grammatical_features_item_ids': [dative_case, plural],
            },
            {
                'label': 'мн.ч. одушевл. вин.п.',
                'example': 'Вижу [хороших] людей/девочек.',
                'grammatical_features_item_ids': [accusative_case, animate, plural],
            },
            {
                'label': 'мн.ч. неодушевл. вин.п.',
                'example': 'Вижу [хорошие] дома/жизни/облака.',
                'grammatical_features_item_ids': [accusative_case, inanimate, plural],
            },
            {
                'label': 'мн.ч. твор.п.',
                'example': 'Руковожу [хорошими] домами/девочками/облаками.',
                'grammatical_features_item_ids': [instrumental_case, plural],
            },
            {
                'label': 'мн.ч. предл.п.',
                'example': 'Говорить о [хороших] домах/девочках/облаках.',
                'grammatical_features_item_ids': [prepositional_case, plural],
            },
        ],
    },

    'swedish-noun-common': {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt substantiv (utrum)',
        'language': language_Swedish,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'nominativ singular, obestämd',
                'example': 'Det här är en [bil].',
                'grammatical_features_item_ids': [nominative_case, singular, indefinite],
            },
            {
                'label': 'nominativ singular, bestämd',
                'example': 'Den nya [bilen].',
                'grammatical_features_item_ids': [nominative_case, singular, definite],
            },
            {
                'label': 'nominativ plural, obestämd',
                'example': 'Jag ser flera [bilar].',
                'grammatical_features_item_ids': [nominative_case, plural, indefinite],
            },
            {
                'label': 'nominativ plural, bestämd',
                'example': 'De nya [bilarna].',
                'grammatical_features_item_ids': [nominative_case, plural, definite],
            },
            {
                'section_break': True,
                'label': 'genitiv singular, obestämd',
                'example': 'En [bils] utseende.',
                'grammatical_features_item_ids': [genitive_case, singular, indefinite],
            },
            {
                'label': 'genitiv singular, bestämd',
                'example': 'Den här [bilens] utseende.',
                'grammatical_features_item_ids': [genitive_case, singular, definite],
            },
            {
                'label': 'genitiv plural, obestämd',
                'example': 'Många [bilars] utseende.',
                'grammatical_features_item_ids': [genitive_case, plural, indefinite],
            },
            {
                'label': 'genitiv plural, bestämd',
                'example': 'De här [bilarnas] utseende.',
                'grammatical_features_item_ids': [genitive_case, plural, definite],
            },
        ],
        'statements': statements(grammatical_gender, common),
    },

    'swedish-noun-neuter': {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt substantiv (neutrum)',
        'language': language_Swedish,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'nominativ singular, obestämd',
                'example': 'Det här är ett [bord].',
                'grammatical_features_item_ids': [nominative_case, singular, indefinite],
            },
            {
                'label': 'nominativ singular, bestämd',
                'example': 'Det nya [bordet].',
                'grammatical_features_item_ids': [nominative_case, singular, definite],
            },
            {
                'label': 'nominativ plural, obestämd',
                'example': 'Jag ser flera [bord].',
                'grammatical_features_item_ids': [nominative_case, plural, indefinite],
            },
            {
                'label': 'nominativ plural, bestämd',
                'example': 'De nya [borden].',
                'grammatical_features_item_ids': [nominative_case, plural, definite],
            },
            {
                'section_break': True,
                'label': 'genitiv singular, obestämd',
                'example': 'Ett [bords] utseende.',
                'grammatical_features_item_ids': [genitive_case, singular, indefinite],
            },
            {
                'label': 'genitiv singular, bestämd',
                'example': 'Det här [bordets] utseende.',
                'grammatical_features_item_ids': [genitive_case, singular, definite],
            },
            {
                'label': 'genitiv plural, obestämd',
                'example': 'Många [bords] utseende.',
                'grammatical_features_item_ids': [genitive_case, plural, indefinite],
            },
            {
                'label': 'genitiv plural, bestämd',
                'example': 'De här [bordens] utseende.',
                'grammatical_features_item_ids': [genitive_case, plural, definite],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'swedish-noun-proper': {
        '@attribution': {'users': ['LA2'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt egennamn',
        'language': language_Swedish,
        'lexical_category_item_id': proper_noun,
        'forms': [
            {
                'label': 'nominativ',
                'example': 'Jag ser [Sara].',
                'grammatical_features_item_ids': [nominative_case],
            },
            {
                'label': 'genitiv',
                'example': 'Jag imponeras av [Saras] utseende.',
                'grammatical_features_item_ids': [genitive_case],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'swedish-verb': {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt verb',
        'language': language_Swedish,
        'lexical_category_item_id': verb,
        'forms': [
            {
                'label': 'infinitiv aktiv',
                'example': 'Att [läsa] är bra.',
                'grammatical_features_item_ids': [infinitive, active],
            },
            {
                'label': 'presens aktiv',
                'example': 'Hen [läser] varje dag.',
                'grammatical_features_item_ids': [present_tense, active],
            },
            {
                'label': 'preteritum aktiv',
                'example': 'Hen [läste] igår.',
                'grammatical_features_item_ids': [preterite, active],
            },
            {
                'label': 'supinum aktiv',
                'example': 'Hen har [läst] hela dagen.',
                'grammatical_features_item_ids': [supine, active],
            },
            {
                'label': 'imperativ',
                'example': '[läs] nu!',
                'grammatical_features_item_ids': [imperative],
            },
            {
                'label': 'infinitiv passiv',
                'example': 'Det ska [läsas].',
                'grammatical_features_item_ids': [infinitive, passive],
            },
            {
                'label': 'presens passiv',
                'example': 'Det [läses] varje dag.',
                'grammatical_features_item_ids': [present_tense, passive],
            },
            {
                'label': 'preteritum passiv',
                'example': 'Det [lästes] igår.',
                'grammatical_features_item_ids': [preterite, passive],
            },
            {
                'label': 'supinum passiv',
                'example': 'Det har [lästs] hela dagen.',
                'grammatical_features_item_ids': [supine, passive],
            },
        ],
    },

    'swedish-absolute-adjective': 'swedish-adjective-absolute',
    'swedish-adjective-absolute': {
        '@attribution': {'users': ['Vesihiisi'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt adjektiv (utan komparativ)',
        'language': language_Swedish,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'obestämd singular, utrum',
                'example': 'en [tolvårig] pojke',
                'grammatical_features_item_ids': [indefinite, singular, common, positive],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'obestämd singular, neutrum',
                'example': 'ett [tolvårigt] barn',
                'grammatical_features_item_ids': [indefinite, singular, neuter, positive],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'bestämd singular, maskulinum',
                'example': 'den [tolvårige] pojken',
                'grammatical_features_item_ids': [definite, singular, masculine, positive],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'bestämd singular, utrum/neutrum',
                'example': 'det [tolvåriga] barnet',
                'grammatical_features_item_ids': [definite, singular, positive],
                'grammatical_features_item_ids_optional': set([positive]),
            },
            {
                'label': 'bestämd plural',
                'example': 'de [tolvåriga] barnen',
                'grammatical_features_item_ids': [definite, plural, positive],
                'grammatical_features_item_ids_optional': set([positive]),
            },
        ],
        'statements': statements(instance_of, absolute_adjective),
    },

    'swedish-adjective': {
        '@attribution': {'users': ['Belteshassar', 'Ainali'], 'title': 'Wikidata:Wikidata Lexeme Forms/Swedish'},
        'label': 'svenskt adjektiv (med komparativ)',
        'language': language_Swedish,
        'lexical_category_item_id': adjective,
        'two_column_sections': False,
        'forms': [
            {
                'label': 'positiv obestämd singular, utrum',
                'example': 'en [ung] pojke',
                'grammatical_features_item_ids': [indefinite, singular, common, positive],
            },
            {
                'label': 'positiv obestämd singular, neutrum',
                'example': 'ett [ungt] barn',
                'grammatical_features_item_ids': [indefinite, singular, neuter, positive],
            },
            {
                'label': 'positiv bestämd singular, maskulinum',
                'example': 'den [unge] pojken',
                'grammatical_features_item_ids': [definite, singular, masculine, positive],
            },
            {
                'label': 'positiv bestämd singular, utrum/neutrum',
                'example': 'det [unga] barnet',
                'grammatical_features_item_ids': [definite, singular, positive],
            },
            {
                'label': 'positiv plural',
                'example': 'de [unga] barnen',
                'grammatical_features_item_ids': [plural, positive],
            },
            {
                'section_break': True,
                'label': 'komparativ (kongruensböjs inte)',
                'example': 'pojken är [yngre] än flickan',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'section_break': True,
                'label': 'superlativ predikativ',
                'example': 'pojken är [yngst] av alla barnen',
                'grammatical_features_item_ids': [superlative, predicative],
            },
            {
                'label': 'superlativ singular attributiv bestämd maskulinum',
                'example': 'den [yngste] pojken i klassen',
                'grammatical_features_item_ids': [superlative, singular, definite, masculine, attributive],
            },
            {
                'label': 'superlativ singular attributiv bestämd',
                'example': 'det [yngsta] barnet i klassen',
                'grammatical_features_item_ids': [superlative, singular, definite, attributive],
            },
            {
                'label': 'superlativ plural attributiv',
                'example': 'de [yngsta] pojkarna i klassen',
                'grammatical_features_item_ids': [superlative, plural, attributive],
            },
        ],
    },

    'ukrainian-noun-masculine': {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, чоловічий рід',
        'language': language_Ukrainian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'однина, називний відмінок',
                'example': 'Це [будинок].',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'однина, родовий відмінок',
                'example': 'Це відноситься до [будинка].',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'однина, давальний відмінок',
                'example': 'Це належить [будинку].',
                'grammatical_features_item_ids': [singular, dative_case],
            },
            {
                'label': 'однина, знахідний відмінок',
                'example': 'Я бачу [будинок].',
                'grammatical_features_item_ids': [singular, accusative_case],
            },
            {
                'label': 'однина, орудний відмінок',
                'example': 'Я керую цим [будинком].',
                'grammatical_features_item_ids': [singular, instrumental_case],
            },
            {
                'label': 'однина, місцевий відмінок',
                'example': 'Воно знаходиться в [будинку].',
                'grammatical_features_item_ids': [singular, locative_case],
            },
            {
                'label': 'однина, кличний відмінок',
                'example': 'Привіт, [будинку].',
                'grammatical_features_item_ids': [singular, vocative_case],
            },
            {
                'label': 'множина, називний відмінок',
                'example': 'Це [будинки].',
                'grammatical_features_item_ids': [plural, nominative_case],
            },
            {
                'label': 'множина, родовий відмінок',
                'example': 'Це відноситься до [будинків].',
                'grammatical_features_item_ids': [plural, genitive_case],
            },
            {
                'label': 'множина, давальний відмінок',
                'example': 'Це належить [будинкам].',
                'grammatical_features_item_ids': [plural, dative_case],
            },
            {
                'label': 'множина, знахідний відмінок',
                'example': 'Я бачу [будинки].',
                'grammatical_features_item_ids': [plural, accusative_case],
            },
            {
                'label': 'множина, орудний відмінок',
                'example': 'Я керую цими [будинками].',
                'grammatical_features_item_ids': [plural, instrumental_case],
            },
            {
                'label': 'множина, місцевий відмінок',
                'example': 'Вони знаходиться в [будинках].',
                'grammatical_features_item_ids': [plural, locative_case],
            },
            {
                'label': 'множина, кличний відмінок',
                'example': 'Привіт, [будинки].',
                'grammatical_features_item_ids': [plural, vocative_case],
            },
        ],
        'statements': statements(grammatical_gender, masculine),
    },

    'ukrainian-noun-feminine': {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, жіночий рід',
        'language': language_Ukrainian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'однина, називний відмінок',
                'example': 'Це [будівля].',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'однина, родовий відмінок',
                'example': 'Це відноситься до [будівлі].',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'однина, давальний відмінок',
                'example': 'Це належить [будівлі].',
                'grammatical_features_item_ids': [singular, dative_case],
            },
            {
                'label': 'однина, знахідний відмінок',
                'example': 'Я бачу [будівлю].',
                'grammatical_features_item_ids': [singular, accusative_case],
            },
            {
                'label': 'однина, орудний відмінок',
                'example': 'Я керую цією [будівлею].',
                'grammatical_features_item_ids': [singular, instrumental_case],
            },
            {
                'label': 'однина, місцевий відмінок',
                'example': 'Воно знаходиться в [будівлі].',
                'grammatical_features_item_ids': [singular, locative_case],
            },
            {
                'label': 'однина, кличний відмінок',
                'example': 'Привіт, [будівле].',
                'grammatical_features_item_ids': [singular, vocative_case],
            },
            {
                'label': 'множина, називний відмінок',
                'example': 'Це [будівлі].',
                'grammatical_features_item_ids': [plural, nominative_case],
            },
            {
                'label': 'множина, родовий відмінок',
                'example': 'Це відноситься до [будівель].',
                'grammatical_features_item_ids': [plural, genitive_case],
            },
            {
                'label': 'множина, давальний відмінок',
                'example': 'Це належить [будівлям].',
                'grammatical_features_item_ids': [plural, dative_case],
            },
            {
                'label': 'множина, знахідний відмінок',
                'example': 'Я бачу [будівлі].',
                'grammatical_features_item_ids': [plural, accusative_case],
            },
            {
                'label': 'множина, орудний відмінок',
                'example': 'Я керую цими [будівлями].',
                'grammatical_features_item_ids': [plural, instrumental_case],
            },
            {
                'label': 'множина, місцевий відмінок',
                'example': 'Вони знаходиться в [будівлях].',
                'grammatical_features_item_ids': [plural, locative_case],
            },
            {
                'label': 'множина, кличний відмінок',
                'example': 'Привіт, [будівлі].',
                'grammatical_features_item_ids': [plural, vocative_case],
            },
        ],
        'statements': statements(grammatical_gender, feminine),
    },

    'ukrainian-noun-neuter': {
        '@attribution': {'users': ['Tohaomg'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, середній рід',
        'language': language_Ukrainian,
        'lexical_category_item_id': noun,
        'two_column_sections': True,
        'forms': [
            {
                'label': 'однина, називний відмінок',
                'example': 'Це [серце].',
                'grammatical_features_item_ids': [singular, nominative_case],
            },
            {
                'label': 'однина, родовий відмінок',
                'example': 'Це відноситься до [серця].',
                'grammatical_features_item_ids': [singular, genitive_case],
            },
            {
                'label': 'однина, давальний відмінок',
                'example': 'Це належить [серцю].',
                'grammatical_features_item_ids': [singular, dative_case],
            },
            {
                'label': 'однина, знахідний відмінок',
                'example': 'Я бачу [серце].',
                'grammatical_features_item_ids': [singular, accusative_case],
            },
            {
                'label': 'однина, орудний відмінок',
                'example': 'Я живу із цим [серцем].',
                'grammatical_features_item_ids': [singular, instrumental_case],
            },
            {
                'label': 'однина, місцевий відмінок',
                'example': 'Воно знаходиться в [серці].',
                'grammatical_features_item_ids': [singular, locative_case],
            },
            {
                'label': 'однина, кличний відмінок',
                'example': 'Привіт, [серцю].',
                'grammatical_features_item_ids': [singular, vocative_case],
            },
            {
                'label': 'множина, називний відмінок',
                'example': 'Це [серця].',
                'grammatical_features_item_ids': [plural, nominative_case],
            },
            {
                'label': 'множина, родовий відмінок',
                'example': 'Це відноситься до [сердець].',
                'grammatical_features_item_ids': [plural, genitive_case],
            },
            {
                'label': 'множина, давальний відмінок',
                'example': 'Це належить [серцям].',
                'grammatical_features_item_ids': [plural, dative_case],
            },
            {
                'label': 'множина, знахідний відмінок',
                'example': 'Я бачу [серця].',
                'grammatical_features_item_ids': [plural, accusative_case],
            },
            {
                'label': 'множина, орудний відмінок',
                'example': 'Кохання між цими [серцями].',
                'grammatical_features_item_ids': [plural, instrumental_case],
            },
            {
                'label': 'множина, місцевий відмінок',
                'example': 'Вони знаходиться в [серцях].',
                'grammatical_features_item_ids': [plural, locative_case],
            },
            {
                'label': 'множина, кличний відмінок',
                'example': 'Привіт, [серця].',
                'grammatical_features_item_ids': [plural, vocative_case],
            },
        ],
        'statements': statements(grammatical_gender, neuter),
    },

    'ukrainian-noun-pluraletantum': {
        '@attribution': {'users': ['Tohaomg', 'Lucas Werkmeister'], 'title': 'Wikidata:Wikidata Lexeme Forms/Ukrainian'},
        'label': 'український іменник, тільки множина (pluralia tantum)',
        'language': language_Ukrainian,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'називний відмінок',
                'example': 'Це [ножиці].',
                'grammatical_features_item_ids': [nominative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'родовий відмінок',
                'example': 'Ніде нема [ножиць].',
                'grammatical_features_item_ids': [genitive_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'давальний відмінок',
                'example': 'Віддати це [ножицям].',
                'grammatical_features_item_ids': [dative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'знахідний відмінок',
                'example': 'Я бачу [ножиці].',
                'grammatical_features_item_ids': [accusative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'орудний відмінок',
                'example': 'Я користуюсь цими [ножицями].',
                'grammatical_features_item_ids': [instrumental_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'місцевий відмінок',
                'example': 'Папір застряг в [ножицях].',
                'grammatical_features_item_ids': [locative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
            {
                'label': 'кличний відмінок',
                'example': 'Привіт, [ножиці].',
                'grammatical_features_item_ids': [vocative_case, plural],
                'grammatical_features_item_ids_optional': set([plural]),
            },
        ],
        'statements': statements(instance_of, plurale_tantum),
    },

    # note: Urdu (ur) templates are under hindustani-*, grouping Hindi (hi) and Urdu (ur) together

    'yoruba-noun': {
        '@attribution': {'users': ['T Cells'], 'title': 'Wikidata:Wikidata Lexeme Forms/Yoruba'},
        'label': 'Orúkọ Yorùbá',
        'language': language_Yoruba,
        'lexical_category_item_id': noun,
        'forms': [
            {
                'label': 'kan',
                'example': 'mo tẹ̀lé ọkunrin [kan] lọ oko.',
                'grammatical_features_item_ids': [],
            },
        ],
    },

    'yoruba-adjective': {
        '@attribution': {'users': ['T Cells'], 'title': 'Wikidata:Wikidata Lexeme Forms/Yoruba'},
        'label': 'Ọ̀rọ̀ àpọ́nlé Yorùbá',
        'language': language_Yoruba,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': 'ga',
                'example': 'ọmọ mi [ga]',
                'grammatical_features_item_ids': [positive],
            },
            {
                'label': 'jù',
                'example': 'ọmọ mi [ga ju tì ẹ] .',
                'grammatical_features_item_ids': [comparative],
            },
            {
                'label': 'jùlọ',
                'example': 'ọmọ mi [ga jùlọ].',
                'grammatical_features_item_ids': [superlative],
            },
        ],
    },

    'mandarin-noun': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語名詞',
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': noun,
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
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': pronoun,
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
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': verb,
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
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': adjective,
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
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': adjective,
        'forms': [
            {
                'label': '形音一',
                'example': '這東西是[雄]的。',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements(has_quality, non_predicative_adjective),
    },

    'mandarin-adverb': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語副詞',
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': adverb,
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
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': interjection,
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
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': preposition,
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
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': classifier,
        'forms': [
            {
                'label': '形音一',
                'example': '這是一[件]什麽東西來著？',
                'grammatical_features_item_ids': [],
            },
        ],
        'statements': statements(has_quality, Chinese_classifier),
    },

    'mandarin-numeral': {
        '@attribution': {'users': ['白布飘扬'], 'title': 'Wikidata:Wikidata Lexeme Forms/Mandarin'},
        'label': '漢語數詞',
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': numeral,
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
        'language': language_Standard_Mandarin,
        'lexical_category_item_id': particle,
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
        'language': {
            'language_item_id': 'Q348',
            'language_code': 'de',
        },
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


# rewrite _internal_templates ('language' as one dict entry with a dict value)
# into templates ('language_item_id' and 'language_code' as separate dict entries)
# (using **language_English directly doesn’t work yet, python/mypy#9408)
templates: Dict[str, Union[str, list[str], Template]] = {}
for _template_name, _internal_template in _internal_templates.items():
    if not isinstance(_internal_template, dict):
        templates[_template_name] = _internal_template
        continue
    _template: Template = {
        'label': _internal_template['label'],
        'language_item_id': _internal_template['language']['language_item_id'],
        'language_code': _internal_template['language']['language_code'],
        'lexical_category_item_id': _internal_template['lexical_category_item_id'],
        'forms': _internal_template['forms'],
    }
    if '@attribution' in _internal_template:
        _template['@attribution'] = _internal_template['@attribution']
    if 'test' in _internal_template:
        _template['test'] = _internal_template['test']
    if 'two_column_sections' in _internal_template:
        _template['two_column_sections'] = _internal_template['two_column_sections']
    if 'statements' in _internal_template:
        _template['statements'] = _internal_template['statements']
    templates[_template_name] = _template


templates_without_redirects = {
    template_name: template
    for template_name, template in templates.items()
    if isinstance(template, dict)
}


for template_name, template in templates_without_redirects.items():
    template['@template_name'] = template_name
