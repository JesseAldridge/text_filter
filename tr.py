import re

def tr(line):
  if re.search('^[a-zA-Z]', line):
    return ''

  tokens = line.split()

  start_re = '[a-zA-Z\-]{3,}'
  stop_re = '[^a-zA-Z\-0-9]'

  for left in range(len(tokens)):
    if re.match(start_re, tokens[left]):
      break

  right = -1
  for right in range(left + 1, len(tokens)):
    if re.match(stop_re, tokens[right]):
      break

  return ' '.join(tokens[left:right])

if __name__ == '__main__':
  for line, expect in [
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
    actual = tr(line)
    if expect != actual:
      print 'line:', line
      print 'expect:', expect
      print 'actual:', actual
      break
  else:
    print 'all good'
