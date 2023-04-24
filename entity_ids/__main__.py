#!/usr/bin/env python3
import os
import subprocess
import sys

dir = os.path.dirname(os.path.realpath(__file__))
files = [
    'property_ids.py',
    'language_item_ids.py',
    'lexical_category_item_ids.py',
    'other_item_ids.py',
]
for file in files:
    subprocess.run([sys.executable, file], cwd=dir, check=True)

missing_files = set()
for entry in os.listdir(dir):
    if entry.startswith('_'):
        continue
    if entry not in files:
        missing_files.add(entry)
if missing_files:
    sys.exit(f'You forgot to add these file(s) to entity_ids/__main__.py: {missing_files}')

identifiers = set()
ambiguous = set()
for file in files:
    with open(f'{dir}/{file}', 'r') as f:
        while line := f.readline():
            identifier, eq, value = line.partition(' = ')
            if not identifier.isidentifier():
                continue
            if identifier in identifiers:
                ambiguous.add(identifier)
            else:
                identifiers.add(identifier)
if ambiguous:
    sys.exit(f'The following variables are ambiguous: {ambiguous}')
