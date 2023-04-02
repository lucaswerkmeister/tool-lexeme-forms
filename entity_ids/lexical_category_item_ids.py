#!/usr/bin/env python3

noun = 'Q1084'
verb = 'Q24905'
adjective = 'Q34698'
proverb = 'Q35102'
pronoun = 'Q36224'
numeral = 'Q63116'
classifier = 'Q63153'
interjection = 'Q83034'
proper_noun = 'Q147276'
particle = 'Q184943'
adjectival_phrase = 'Q357760'
adverb = 'Q380057'
noun_phrase = 'Q1401131'
verb_phrase = 'Q1778442'
adverbial_phrase = 'Q3734650'
preposition = 'Q4833830'
adverbial_locution = 'Q5978303'
interjectional_locution = 'Q10319520'
prepositional_locution = 'Q10319522'
attributive_locution = 'Q12734432'
nominal_locution = 'Q29888377'

def _main():
    for var, val in globals().items():
        if var.startswith('_'):
            continue
        print(f'''
.rootpage-Wikidata_Wikidata_Lexeme_Forms a[title="{val}"] {{
    font-size: 0;
}}
.rootpage-Wikidata_Wikidata_Lexeme_Forms a[title="{val}"]::after {{
    content: "{var}";
    font-size: 0.875rem;
    font-family: monospace;
    background: #fef6e7;
}}'''.strip() + '\n')

if __name__ == '__main__':
    _main()
