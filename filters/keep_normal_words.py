import re

import base_filter_

class KeepNormalWords(base_filter_.BaseFilter):
  def transform_line(self, line):
    # Ignore dates and times
    if re.search('[0-9]+$', line):
      return ''

    tokens = line.split()

    start_re = '[a-zA-Z\-]{3,}'
    stop_re = '[^a-zA-Z\-0-9]'

    for left in range(len(tokens)):
      if re.match(start_re, tokens[left]):
        break

    right = left + 1
    while right < len(tokens):
      if re.match(stop_re, tokens[right]):
        break
      right += 1

    return ' '.join(tokens[left:right])

if __name__ == '__main__':
  keep_normal_words = KeepNormalWords()

  for line, expect in [
    (
      'testing',
      'testing',
    ),
    (
      '01:58 pm #setup collect improvement notes (00:32)',
      'collect improvement notes'
    ),
    (
      '02:31 pm further break down non-work tasks (00:21)',
      'further break down non-work tasks',
    ),
    (
      'December 19th 2017',
      '',
    ),
    (
      '00:39',
      '',
    ),
    (
      '04:54 pm #setup mario copy -- add reasons_group_title (00:22)',
      'mario copy -- add reasons_group_title',
    ),
    (
      '01:33 pm run again with 30 days (00:13)',
      'run again with 30 days',
    ),
    (
      '10:26 am #setup ship PRs and talk to fede about test user (00:27)',
      'ship PRs and talk to fede about test user',
    )
  ]:
    actual = keep_normal_words.transform_line(line)
    if expect != actual:
      print 'line:', line
      print 'expect:', expect
      print 'actual:', actual
      break
  else:
    print 'all good'
