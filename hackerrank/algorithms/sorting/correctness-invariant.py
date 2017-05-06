#!/usr/bin/env python2

TEST_MODE = True

def main():
  size = int(raw_input().strip())
  array = map(int, raw_input().strip().split())
  array = insertion_sort(array)
  print " ".join(map(str,array))

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
    return l

def insertionSort(array):
  for i in range(1, len(array)):
    num = array.pop(i)
    for j in range(i-1, -1, -1):
      if array[0] > num:
        array.insert(0, num)
        print ' '.join(map(str, array))
        break
      if array[j] < num:
        array = array[:j+1] + [num] + array[j+1:]
        print ' '.join(map(str, array))
        break

def test():
  print insertion_sort([1, 4, 3, 5, 6, 2])
  print insertion_sort([9, 8, 6, 7, 3, 5, 4, 1, 2])

test() if TEST_MODE else main()
