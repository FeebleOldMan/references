#!/usr/bin/env python2

TEST_MODE = False

def main():
  length, rot_steps, queries = map(int, raw_input().strip().split())
  array = map(int, raw_input().strip().split())
  array = arr_rotate(rot_steps, array)
  for _ in xrange(queries):
    print array[input()]

def arr_rotate(rot_steps, array):
  for _ in xrange(rot_steps):
    array.insert(0, array.pop())
  return array

def test():
  return

test() if TEST_MODE else main()
