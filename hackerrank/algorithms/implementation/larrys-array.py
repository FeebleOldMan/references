#!/usr/bin/env python

TEST_MODE = True

def main():
  for _ in range(int(raw_input().strip())):
    a_size = int(raw_input().strip())
    array = map(int, raw_input().strip().split())
    print sort_check(array)
  return

def sort_check(array):
  for i in range(len(array) - 2):
    min_num = min(array[i:])
    while min_num != array[i]:
      loc_min = max(array.index(min_num) - 2, i) # find 2 spaces before min num in order to shift it there
      counter = 0
      while ((array[loc_min] > array[loc_min + 1]) or (array[loc_min] > array[loc_min + 2])) and counter < 3:
        array[loc_min], array[loc_min + 1], array[loc_min + 2] = rotate(array[loc_min], array[loc_min + 1], array[loc_min+2])
        counter += 1
      if counter == 3:
        return 'NO'
  if array[-2] > array[-1]: return 'NO'
  return 'YES'

def rotate(a, b, c):
  return b, c, a

def test():
  print "TEST 01:", "pass" if sort_check([3, 1, 2]) == 'YES' else "**FAIL**"
  print "TEST 02:", "pass" if sort_check([1, 3, 4, 2]) == 'YES' else "**FAIL**"
  print "TEST 03:", "pass" if sort_check([1, 2, 3, 5, 4]) == 'NO' else "**FAIL**"
  print "TEST 04:", "pass" if sort_check([17, 21, 2, 1, 16, 9, 12, 11, 6, 18, 20, 7, 14, 8, 19, 10, 3, 4, 13, 5, 15]) == 'YES' else "**FAIL**"
  return

test() if TEST_MODE else main()

### v0.1 doesn't sort smallest numbers all the way to front of array
#def sort_check(array):
#  for i in range(len(array) - 2):
#    counter = 0
#    print array
#    while ((array[i] > array[i+1]) or (array[i] > array[i+2])) and counter < 3:
#      array[i], array[i+1], array[i+2] = rotate(array[i], array[i+1], array[i+2])
#      counter += 1
#      print array
#    if counter == 3:
#      return 'NO'
#  if array[-2] > array[-1]: return 'NO'
#  return 'YES'

