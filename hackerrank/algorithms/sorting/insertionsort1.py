#!/usr/bin/env python2

TEST_MODE = False

def main():
  size = int(raw_input().strip())
  array = [int(i) for i in raw_input().strip().split()]
  sort(size, array)

def sort(size, array):
  num = array[-1]
  for i in range(size-2, -1, -1):
    if array[i] > num:
      array[i+1] = array[i]
      print ' '.join(map(str, array))
    elif array[i] < num:
      array[i+1] = num
      print ' '.join(map(str, array))
      return
  array[0] = num
  print ' '.join(map(str, array))
  return

def test():
  print "TEST01:", "sort(5, [2, 4, 6, 8, 3])", sort(5, [2, 4, 6, 8, 3])

test() if TEST_MODE else main()
