#!/usr/bin/env python3

Esperanto = 'Q143'
French = 'Q150'
German = 'Q188'
Latin = 'Q397'
Italian = 'Q652'
Polish = 'Q809'
Spanish = 'Q1321'
Finnish = 'Q1412'
English = 'Q1860'
Portuguese = 'Q5146'
Croatian = 'Q6654'
Dutch = 'Q7411'
Russian = 'Q7737'
Basque = 'Q8752'
Armenian = 'Q8785'
Ukrainian = 'Q8798'
Swedish = 'Q9027'
Danish = 'Q9035'
Czech = 'Q9056'
Estonian = 'Q9072'
Latvian = 'Q9078'
Persian = 'Q9168'
Hebrew = 'Q9288'
Bengali = 'Q9610'
Hindustani = 'Q11051'
Breton = 'Q12107'
Nynorsk = 'Q25164'
Bokmål = 'Q25167'
Asturian = 'Q29507'
Igbo = 'Q33578'
Odia = 'Q33810'
Yoruba = 'Q34311'
Kurmanji = 'Q36163'
Malayalam = 'Q36236'
Punjabi = 'Q58635'
Hindko = 'Q382273'
Standard_Mandarin = 'Q727694'
Manbhumi = 'Q6747180'

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
    background: #fee7e6;
}}'''.strip() + '\n')

if __name__ == '__main__':
    _main()
