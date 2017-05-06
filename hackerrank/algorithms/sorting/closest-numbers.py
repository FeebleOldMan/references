#!/usr/bin/env python2

TEST_MODE = True

def main():
  length = input()
  print smallest_diff(map(int, raw_input().strip().split()))

def smallest_diff(array):
  array = sorted(array)
  smallest_value = float('inf')
  output = []
  for i in range(len(array) - 1):
    diff = array[i+1] - array[i]
    if diff < smallest_value:
      output = [array[i], array[i+1]]
      smallest_value = diff
    elif diff == smallest_value:
      output.extend([array[i], array[i+1]])
  return ' '.join(map(str, output))

def test():
  print "TEST01:", "pass" if smallest_diff([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]) == "-20 30" else "**FAIL**"
  print "TEST02:", "pass" if smallest_diff([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]) == "-520 -470 -20 30" else "**FAIL**"
  print "TEST03:", "pass" if smallest_diff([5, 4, 3, 2]) == "2 3 3 4 4 5" else "**FAIL**"

test() if TEST_MODE else main()
