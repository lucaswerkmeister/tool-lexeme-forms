#!/usr/bin/env python3
import entity_ids.language_item_ids

with open('templates.py', 'r', encoding='utf8') as f:
    templates = f.read()

for var in dir(entity_ids.language_item_ids):
    if var.startswith('_'):
        continue
    val = getattr(entity_ids.language_item_ids, var)
    templates = templates.replace(f'{val!r}', var)

with open('templates.py', 'w', encoding='utf8') as f:
    f.write(templates)
