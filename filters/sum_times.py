from datetime import timedelta

import keep_times

class SumTimes(keep_times.KeepTimes):
  def handle_lines(self, lines):
    sum_ = timedelta()
    for line in lines:
      ints = [int(x) for x in line.split(':')]
      sum_ += timedelta(minutes=ints[0], seconds=ints[1])

    return '  ' + '\n  '.join(lines[:-1]) + '\n+ ' + lines[-1] + '\n-------\n' + str(sum_)

if __name__ == '__main__':
  print SumTimes().handle_lines(['00:33', '00:10', '00:15', '00:34'])
