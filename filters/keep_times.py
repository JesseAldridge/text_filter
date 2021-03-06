import re

import base_filter_

class KeepTimes(base_filter_.BaseFilter):
  def transform_line(self, line):
    match = re.search(' \(?([0-9]+:[0-9]+)', line)
    return match.group(1) if match else ''

  def handle_lines(self, lines):
    return lines

if __name__ == '__main__':
  keep_times = KeepTimes()

  for line, expect in [
    (
      'follow up on stuff ~(00:32)~ (00:20)',
      '00:20'
    ),
    (
      '~/Dropbox/bin/sum_times.py',
      ''
    ),
    (
      'airflow job -- talk to greg about default ruby method (00:21)',
      '00:21'
    ),
    (
      'how to know whether I already updated the time? (00:31)',
      '00:31'
    ),
    (
      'ok now that we have listing ids... (00:23)',
      '00:23'
    ),
    (
      'merge branding protection PR (00:19)',
      '00:19'
    ),
    (
      'more stuff (00:08)',
      '00:08'
    ),
    (
      'ok acceptance rate... upcoming meeting (00:16)',
      '00:16'
    ),
    (
      'ok so we will get a list of listing_ids... (00:23)',
      '00:23'
    ),
    (
      'more info (00:10)',
      '00:10'
    ),
    (
      'ok, so we will generate a json blob of select listing ids... (00:24)',
      '00:24'
    ),
    (
      'ok, airbed3_production_hostings_v01 joined with dim_listing_standards_for_select... test in superset (00:47)',
      '00:47'
    )
  ]:
    actual = keep_times.transform_line(line)
    if expect != actual:
      print 'line:', line
      print 'expect:', expect
      print 'actual:', actual
      break
  else:
    print 'all good'
