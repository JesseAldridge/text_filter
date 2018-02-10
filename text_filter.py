#!/usr/bin/python
import sys, importlib, os, glob

import clipboard

def main():
  filters_path = os.path.expanduser('~/Dropbox/text_filter/filters')
  sys.path.append(filters_path)

  if len(sys.argv) == 1:
    print 'filters:'
    for path in glob.glob(filters_path + '/*.py'):
      filename = os.path.basename(path).rsplit('.py')[0]
      if filename == '__init__':
        continue
      print '  ' + filename
    return

  testing = 'test' in sys.argv
  filter_name = 'normal_words' if testing else sys.argv[1]
  module = importlib.import_module(filter_name)
  filter_ = getattr(module, filter_name)

  def each_line(text, filter_):
    in_lines = text.splitlines()
    clean_lines = []
    for line in in_lines:
      clean_lines.append(filter_(line))
    return '\n'.join([line for line in clean_lines if line.strip()])

  if testing:
    with open('test.txt') as f:
      text = f.read()
  else:
    text = clipboard.paste()

  print each_line(text, filter_)

if __name__ == '__main__':
  main()
