#!/usr/bin/env python2

TEST_MODE = False

def main():
  for _ in range(input()):
    target = input()
    num_flavors = input()
    prices = map(int, raw_input().strip().split())
    print optimize(target, num_flavors, prices)

def optimize(target, num_flavors, prices):
  for i in range(num_flavors-1):
    for j in range(i+1, num_flavors):
      if prices[i] + prices[j] == target:
        return str(i+1) + ' ' + str(j+1)

def test():
  print "TEST01:", "pass" if optimize(4, 5, [1, 4, 5, 3, 2]) == '1 4' else "**FAIL**"
  print "TEST01:", "pass" if optimize(4, 4, [2, 2, 4, 3]) == '1 2' else "**FAIL**"

test() if TEST_MODE else main()
