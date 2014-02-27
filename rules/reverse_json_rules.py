"""
reverserules.py - reverse a transliteration scheme
"""
import json
import sys

rules = json.load(open(sys.argv[1]))

new_rules = []

for before, after in rules:
  new_rules.append([after, before])

print json.dumps(new_rules, indent=2)
