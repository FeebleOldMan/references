#!/usr/bin/env python2

TEST_MODE = False

def main():
  size = input()
  sortable(map(int, raw_input().strip().split()))

def sortable(array):
  left, right = None, None
  for i in range(len(array)-1):
    if array[i] > array[i+1]:
      left = i
      break
  if left == None: return 'yes'
  for j in range(len(array)-1, 0, -1):
    if array[j] < array[j-1]:
      right = j
      break
  swap_array = array[:]
  swap_array[left], swap_array[right] = swap_array[right], swap_array[left]
  if is_sorted(swap_array):
    print 'yes'
    print 'swap', left+1, right+1
    return
  reverse_array = array[:]
  reverse_array[left:right+1] = list(reversed(reverse_array[left:right+1]))
  if is_sorted(reverse_array):
    print 'yes'
    print 'reverse', left+1, right+1
    return
  print 'no'

def is_sorted(array):
  for i in range(len(array)-1):
    if array[i] > array[i+1]:
      return False
  return True

def test():
  return

test() if TEST_MODE else main()
