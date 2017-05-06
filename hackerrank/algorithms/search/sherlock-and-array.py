#!/usr/bin/env python2

TEST_MODE = True

def main():
  for _ in range(input()):
    length = input()
    array = map(int, raw_input().strip().split())
    print balance(length, array)

def balance(length, array):
  left, mid, right, prev_mid = 0, length / 2, length-1, -1
  while mid != prev_mid:
    prev_mid = mid
    if sum(array[:mid]) < sum(array[mid+1:]):
      left = mid
      mid = (right + mid)/2
    elif sum(array[:mid]) > sum(array[mid+1:]):
      right = mid
      mid = (mid - left)/2
    else:
      return 'YES'
  return 'NO'

def test():
  print "TEST01:", "pass" if balance(3, [1,2,3]) == 'NO' else "**FAIL**"
  print "TEST01:", "pass" if balance(4, [1,2,3,3]) == 'YES' else "**FAIL**"

test() if TEST_MODE else main()
