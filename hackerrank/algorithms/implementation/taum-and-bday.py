#!/usr/bin/env python

TEST_MODE = True

def main():
  for _ in range(int(raw_input().strip())):
    black, white = map(int, raw_input().strip().split())
    cost_black, cost_white, cost_conv = map(int, raw_input().strip().split())
    print buy_gifts(black, white, cost_black, cost_white, cost_conv)

def buy_gifts(black, white, cost_black, cost_white, cost_conv):
  # check if any cost is more expensive than buying opposite + converting
  if (cost_black) > (cost_white + cost_conv):
    cost_black = cost_white + cost_conv
  if (cost_white) > (cost_black + cost_conv):
    cost_white = cost_black + cost_conv
  return (black * cost_black + white * cost_white)

def test():
  print "Test 01:", "pass" if buy_gifts(10, 10, 1, 1, 1) == 20 else "FAIL"
  print "Test 02:", "pass" if buy_gifts(5, 9, 2, 3, 4) == 37 else "FAIL"
  print "Test 03:", "pass" if buy_gifts(3, 6, 9, 1, 1) == 12 else "FAIL"
  print "Test 04:", "pass" if buy_gifts(7, 7, 4, 2, 1) == 35 else "FAIL"
  print "Test 05:", "pass" if buy_gifts(3, 3, 1, 9, 2) == 12 else "FAIL"
  return

test() if TEST_MODE else main()
