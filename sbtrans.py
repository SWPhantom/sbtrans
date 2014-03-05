"""
sbtrans.py - apply a set of transliteration rules to text

Created by ComplingFTW at UCSB
"""
import json

def order_rules(rules):
  """
  Transliteration rules must be ordered by the length of the 
  "before" side of each, to prevent rule bleeding.

  Consider the ruleset:  

  [
    ["n", "N"],   # rule 1
    ["na", "NA"]  # rule 2
  ]

  Consider what happens If this ruleset is applied to the 
  string "nana":

  Apply rule 1:  
  
    "nana" -> "NaNa"

  Now rule 2 is blocked!

  The solution is to reorder the rules such that the longest
  rules with the longest input sides are run first. (In this
  example, rule 2 should precede rule 1.
 
  """
  bylength = sorted([(len(left), left, right) for left, right in rules])
  ordered = [(left, right) for length, left, right in bylength]
  return list(reversed(ordered))
  
def reverse_rules(rules):
  """
    Convert:

    [ 
       ['a', 'A'],
       ['b', 'B'],
       ['c', 'C']
    ]
    
    To: 

    [ 
       ['A', 'a'],
       ['B', 'b'],
       ['C', 'c']
    ]

    @TODO: what if the rules are not reversible? 
  """
  return [(b,a) for a,b in rules] 

def read_rules(filename):
  """
  Read the contents of the json file called filename and return
  the data structure. Contains a structure like (imagine a trivial
  capitalization transliteration scheme):
  
  [
     ['a', 'A'],
     ['b', 'B'],
     ['c', 'C']  
  ]
  
  """
  return json.load(open(filename))

def transliterate(rules, input_text):
  """
  apply the before, after transliteration rules in 
  the list "rules" to input_text

  Returns a Unicode string.
  """
  text = input_text
  for before, after in rules:
    text = text.replace(before, after) 
  return text

def transliterate_file(rules_filename, input_filename, output_filename):
  """
  """
  rules = read_rules(rules_filename)
  input_text = open(input_filename).read().decode('utf-8')
  output_handle = open(output_filename, 'w')
  transliterated_text = transliterate(rules, input_text)
  output_handle.write(transliterated_text.encode('utf-8'))
  output_handle.close()

