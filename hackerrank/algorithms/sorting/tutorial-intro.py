#!/usr/bin/env python2

TEST_MODE = False

def main():
  value = int(raw_input().strip())
  size = int(raw_input().strip())
  array = map(int, raw_input().strip().split())
#  print find(int(raw_input().strip()), int(raw_input().strip()), map(int, raw_input.strip().split()))
  print find(value, size, array)

def find(value, size, array):
  return array.index(value)

def test():
  print "TEST01:", "pass" if find(4, 6, [1, 4, 5, 7, 9, 12]) == 1 else "**FAIL**"

test() if TEST_MODE else main()
