#!/usr/bin/env python2

#https://en.wikipedia.org/wiki/Merge_sort
#http://www.geeksforgeeks.org/counting-inversions/

TEST_MODE = True

def main():
  for _ in xrange(input()):
    length = input()
    print count_moves(map(int, raw_input().strip().split()))

def count_moves(array):
  count = 0
  num_dict = {}
  for i in array:
    num_dict[i] = num_dict.get(i, 0) + 1
  idx = 0
  while num_dict.keys():
    min_num = min(num_dict.keys())
    for j in range(num_dict[min_num]):
      count += abs(array.index(min_num) - idx)
      idx += 1
      array[array.index(min_num)] = None
      print array, count
    del num_dict[min_num]
  return count
# find min of dict.keys
# iter range(value) of min
# use a[i:].index(val) and subtract from i to add to count
# del num_dict[min]

def test():
  print "TEST01:", "pass" if count_moves([1,1,1,2,2]) == 0 else "**FAIL**"
  print "TEST02:", "pass" if count_moves([2,1,3,1,2]) == 4 else "**FAIL**"

test() if TEST_MODE else main()
