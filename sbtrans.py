#!/usr/bin/python2.7
"""
sbtrans.py - apply a set of transliteration rules to text

Created by ComplingFTW at UCSB
"""
import json

def read_rules(filename):
  """
  Read the contents of the json file called filename and return
  the data structure. Contains a structure like (imagine a trivial
  capitalization file):
  
  [
     ['a', 'A'],
     ['b', 'B']  
  ]
  
  """
  return json.load(open(filename))

def transliterate(rules, input_text):
  text = input_text
  for before, after in rules:
    text = text.replace(before, after) 
  return text

def process_file(rules_filename, input_filename, output_filename):
  rules = read_rules(rules_filename)
  input_text = open(input_filename).read().decode('utf-8')
  output_handle = open(output_filename, 'w')
  transliterated_text = transliterate(rules, input_text)
  output_handle.write(transliterated_text.encode('utf-8'))
  output_handle.close()

if __name__ == "__main__":
  import sys
  from optparse import OptionParser

  parser = OptionParser(description="sbtrans.py - apply transliteration rules to text")

  parser.add_option("-o", "--output", dest="output_file",
                    help="write transliterated content to OUTPUT_FILE",   metavar="OUTPUT_FILE")
  parser.add_option("-i", "--input", dest="input_file",
                    help="read untransliterated content from INPUT_FILE", metavar="INPUT_FILE")

  (options, args) = parser.parse_args()

  parser.print_help()
  #print options
  #print args


