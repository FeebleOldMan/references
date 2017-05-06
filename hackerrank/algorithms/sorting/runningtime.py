#!/usr/bin/env python2

TEST_MODE = True

def main():
  size = int(raw_input().strip())
  array = map(int, raw_input().strip().split())
  print insertionSortSteps(array)

def insertionSortSteps(l):
    steps = 0
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           steps += 1
        l[j+1] = key
    return steps

def test():
  print insertionSortSteps([2, 1, 3, 1, 2])
  print insertionSortSteps([1, 4, 3, 5, 6, 2])
  print insertionSortSteps([9, 8, 6, 7, 3, 5, 4, 1, 2])

test() if TEST_MODE else main()
