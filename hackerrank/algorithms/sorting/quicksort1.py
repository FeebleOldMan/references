#!/usr/bin/env python2

TEST_MODE = False

def main():
  length = int(raw_input().strip())
  print quicksort(map(int, raw_input().strip().split()))

def quicksort(array):
  equal, left, right = [array[0]], [], []
  for i in range(1, len(array)):
    if array[i] < equal[0]:
      left.append(array[i])
    elif array[i] > equal[0]:
      right.append(array[i])
    else:
      equal.append(array[i])
  return ' '.join(map(str, left + equal + right))

def test():
  print "TEST01:", "pass" if quicksort([4, 5, 3, 7, 2]) == '3 2 4 5 7' else "**FAIL**"
  print "TEST02:", "pass" if quicksort([2, 10, 3, 7, 9, 4, 6, 12, 8]) == '2 10 3 7 9 4 6 12 8' else "**FAIL**"
  print "TEST03:", "pass" if quicksort([-13, 68, -43, -71, -39, -10, 40, -49, -19, -3, -70, -62, -76, -94, -73, 64, 72, -5, 88, 2, -63, 92, -40, 16, 49, 47, -86, -51, -9, -14, 96, 74, -22, -34, 38, -12, 6, 63, 19, -69, 14, -90, -27, 76, 54, 57, -87, -91, 43, -92]) == '-43 -71 -39 -49 -19 -70 -62 -76 -94 -73 -63 -40 -86 -51 -14 -22 -34 -69 -90 -27 -87 -91 -92 -13 68 -10 40 -3 64 72 -5 88 2 92 16 49 47 -9 96 74 38 -12 6 63 19 14 76 54 57 43' else "**FAIL**"
  print quicksort([-13, 68, -43, -71, -39, -10, 40, -49, -19, -3, -70, -62, -76, -94, -73, 64, 72, -5, 88, 2, -63, 92, -40, 16, 49, 47, -86, -51, -9, -14, 96, 74, -22, -34, 38, -12, 6, 63, 19, -69, 14, -90, -27, 76, 54, 57, -87, -91, 43, -92])
  print quicksort([4, 4, 4, 4, 4])
  print quicksort([3, 4, 5, 6, 7])
  print quicksort([7, 6, 5, 4, 3])
  print quicksort([-7, 6, -8, 4, 5])
  print quicksort([-7, 6, -8, -8, 5])
  print quicksort([-7, -7, -7, -7, -7])
  print quicksort([0, -3, 6, 4, -10, 8, -5, 2, -7])
  print quicksort([9, 0, -3, 6, 4, -10, 8, -5, 2, -7])

test() if TEST_MODE else main()
