#!/usr/bin/env python2

TEST_MODE = True

def main():
  for _ in range(input()):
    size = input()
    print indice_pairs(map(int, raw_input().strip().split()))

def indice_pairs(array):
  num_count = {}
  for num in array:
    num_count[num] = num_count.get(num, 0) + 1
  pair_count = 0
  for count in num_count.values():
    if count > 1:
      pair_count += count * (count - 1)
  return pair_count

### v0.1 factorial too slow
#from math import factorial
#def indice_pairs(array):
#  num_count = {}
#  for num in array:
#    num_count[num] = num_count.get(num, 0) + 1
#  pair_count = 0
#  for count in num_count.values():
#    if count > 1:
#      pair_count += factorial(count)/factorial(count - 2)
#  return pair_count

def test():
  print "TEST01:", "pass" if indice_pairs([1, 2, 3]) == 0 else "**FAIL**", indice_pairs([1,2,3])
  print "TEST02:", "pass" if indice_pairs([1, 1, 3]) == 2 else "**FAIL**", indice_pairs([1,1,3])
  print "TEST03:", "pass" if indice_pairs([1, 1, 1, 1, 3, 3]) == 14 else "**FAIL**", indice_pairs([1,1,1,1,3,3])

test() if TEST_MODE else main()
