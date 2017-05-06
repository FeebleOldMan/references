#!/usr/bin/env python2

TEST_MODE = True

def main():
  size = int(raw_input().strip())
  array = map(int, raw_input().strip().split())
  insertionSort(array)

def insertionSort(array):
  for i in range(1, len(array)):
    num = array.pop(i)
    for j in range(i-1, -1, -1):
      if array[0] > num:
        array.insert(0, num)
        print ' '.join(map(str, array))
        break
      if array[j] <= num:
        array = array[:j+1] + [num] + array[j+1:]
        print ' '.join(map(str, array))
        break

def test():
  #insertionSort([1, 4, 3, 5, 6, 2])
  insertionSort([9, 8, 6, 7, 3, 5, 4, 1, 2])

test() if TEST_MODE else main()
