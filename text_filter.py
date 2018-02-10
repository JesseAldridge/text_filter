#!/usr/bin/python
import sys, importlib, os, glob

import clipboard

def main():
  filters_path = os.path.expanduser('~/Dropbox/text_filter/filters')
  sys.path.append(filters_path)

  if len(sys.argv) == 1:
    print 'mutators:'
    for path in glob.glob(filters_path + '/*.py'):
      filename = os.path.basename(path).rsplit('.py')[0]
      if filename == '__init__':
        continue
      print '  ' + filename
    return

  testing = 'test' in sys.argv
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

if __name__ == '__main__':
  main()
