#!/usr/bin/env python3

instance_of = 'P31'
has_quality = 'P1552'
grammatical_gender = 'P5185'
paradigm_class = 'P5911'
language_style = 'P6191'
grammatical_aspect = 'P7486'
transitivity = 'P9295'

def _main():
    for var, val in globals().items():
        if var.startswith('_'):
            continue
        print(f'''
.rootpage-Wikidata_Wikidata_Lexeme_Forms a[title="Property:{val}"] {{
    font-size: 0;
}}
.rootpage-Wikidata_Wikidata_Lexeme_Forms a[title="Property:{val}"]::after {{
    content: "{var}";
    font-size: 0.875rem;
    font-family: monospace;
    background: #d5fdf4;
}}'''.strip() + '\n')

if __name__ == '__main__':
    _main()
