#!/usr/bin/env python2

TEST_MODE = False
quickCount = 0

def main():
  global quickCount
  length = int(raw_input().strip())
  array = map(int, raw_input().strip().split())
  array2 = array[:]
  quicksort(array, 0, len(array)-1)
  print insertionSortSteps(array2) - quickCount

def quicksort(array, low, high):
  global quickCount
  if low < high:
    array, p = partition(array, low, high)
    return quicksort(quicksort(array, low, p - 1), p + 1, high)
  else:
    return array

def partition(array, low, high):
  global quickCount
  pivot = array[high]
  i = low
  for j in range(low, high):
    if array[j] <= pivot:
      array[i], array[j] = array[j], array[i]
      i += 1
      quickCount += 1
  array[i], array[high] = array[high], array[i]
  quickCount += 1
  return array, i

#def quicksort(array, low, high, steps = 0):
#  if low < high:
#    array, p, steps = partition(array, low, high, steps)
#    array = quicksort(quicksort(array, low, p - 1, steps), p + 1, high, steps)
#    return array
#  else:
#    return array
#
#def partition(array, low, high, steps):
#  pivot = array[high]
#  i = low
#  for j in range(low, high):
#    if array[j] <= pivot:
#      array[i], array[j] = array[j], array[i]
#      i += 1
#      steps += 1
#  array[i], array[high] = array[high], array[i]
#  steps += 1
#  print steps
#  return array, i, steps

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
  array = [1, 3, 9, 8, 2, 7, 5]
#  print "TEST01:", "pass" if insertionSortSteps(array) - quicksort(array, 0, len(array)-1) == 1 else "**FAIL**"
  print insertionSortSteps(array)
  array = [1, 3, 9, 8, 2, 7, 5]
  quicksort(array, 0, len(array)-1)
  print quickCount
test() if TEST_MODE else main()
