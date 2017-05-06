#!/usr/bin/env python2

TEST_MODE = True

def main():
  print beautify(int(raw_input().strip()), raw_input().strip())

def beautify(n, binary):
  steps = 0
  binary = list(binary)
  for i in range(n-2):
    if binary[i:i+3] == list('010'):
      binary[i+2] = '1'
      steps += 1
  return steps

def test():
  print "TEST01:", "pass" if beautify(7, '0101010') == 2 else "**FAIL**"
  print "TEST02:", "pass" if beautify(5, '01100') == 0 else "**FAIL**"
  print "TEST03:", "pass" if beautify(10, '0100101010') == 3 else "**FAIL**"

test() if TEST_MODE else main()

