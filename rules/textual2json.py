"""
txt2json.py - convert newline-separated transliteration
  scheme into appropriate JSON scheme
"""
import json
import sys

input_filename = sys.argv[1]

if not input_filename.endswith('txt'):
  print 'must be .txt file'
  exit()

raw = open(input_filename).read().decode('utf-8')

chunks = raw.strip().split('\n\n')

rules = []

for chunk in chunks:
  rules.append(chunk.splitlines()) 

print json.dumps(rules, indent=2)
