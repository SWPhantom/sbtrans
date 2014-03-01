"""
reverse_json_rules.py - reverse a transliteration scheme

You need to run this file with python taking two arguemnts.

1. the first list of json rules
2. the second list of json rules you want to create

* Make sure you remember to type the full path to the location where you want
your out file to end up ! 

"""
import json
import sys

rules = json.load(open(sys.argv[1]))
outfile_name = sys.argv[2]

new_rules = []

for before, after in rules:
  new_rules.append([after, before])

outfile = open(outfile_name, "w")
outfile.write(json.dumps(new_rules, indent=2))
outfile.close()

