#!/usr/bin/env python

TEST_MODE = True

def main():
  low = int(raw_input().strip())
  high = int(raw_input().strip())
  print kaprekar(low, high)
  return

def kaprekar(low, high):
  output = []
  for num in range(low, high+1):
    square = str(num * num)
    midpoint = len(square)/2
    left = int(square[:midpoint]) if square[:midpoint] != '' else 0
    right = int(square[midpoint:]) if square[midpoint:] != '' else 0
    if left + right == num:
      output.append(str(num))
  if len(output) == 0:
    return 'INVALID RANGE'
  return ' '.join(output)

def test():
  print "TEST 01:", "pass" if kaprekar(1, 100) == '1 9 45 55 99' else "**FAIL**: " + kaprekar(1,100)
  return

test() if TEST_MODE else main()
