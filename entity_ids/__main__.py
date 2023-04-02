#!/usr/bin/env python3
import os
import subprocess
import sys

dir = os.path.dirname(os.path.realpath(__file__))
for entry in os.listdir(dir):
    if entry.startswith('_'):
        continue
    subprocess.run([sys.executable, entry], cwd=dir, check=True)
