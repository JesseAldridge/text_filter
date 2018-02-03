#!/usr/bin/python
import sys, importlib, os

import clipboard

filters_path = '/Users/jesse_aldridge/Dropbox/text_filter/filters'
sys.path.append(filters_path)

testing = (len(sys.argv) == 1 or 'test' in sys.argv)
mutator_name = 'normal_words' if testing else sys.argv[1]
module = importlib.import_module(mutator_name)
mutator = getattr(module, mutator_name)

def each_line(text, mutator):
  in_lines = text.splitlines()
  clean_lines = []
  for line in in_lines:
    clean_lines.append(mutator(line))
  return '\n'.join([line for line in clean_lines if line.strip()])

if testing:
  with open('test.txt') as f:
    text = f.read()
else:
  text = clipboard.paste()

print each_line(text, mutator)
