#!/usr/bin/env python3

import time

import mwapi
import toolforge

user_agent = toolforge.set_user_agent('lexeme-forms', email='mail@lucaswerkmeister.de')
session = mwapi.Session(
    host='https://www.wikidata.org',
    user_agent=user_agent
)
session.session.cookies['PHP_ENGINE'] = 'php7' # TODO remove this once PHP7 is the default

for result in session.post(
        action='purge',
        generator='allpages',
        gapnamespace=146, # Lexeme
        gaplimit=30, # rate limit permits 30 purges per 60 seconds
        forcelinkupdate=True,
        continuation=True
    ):
    pages = result['purge']
    first_id = pages[0]['title'][len('Lexeme:'):]
    last_id = pages[-1]['title'][len('Lexeme:'):]
    print('Purged {:>6} ... {:>6}'.format(first_id, last_id), flush=True)
    time.sleep(75) # rate limit permits 30 purges per 60 seconds, +15s for some buffer

print('Done.')
