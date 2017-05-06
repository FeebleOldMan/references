#!/usr/bin/env python2

TEST_MODE = False

def main():
  for _ in range(int(raw_input().strip())):
    print shrinkify(raw_input().strip())

  return

def shrinkify(line):
  cursor = None
  deletions = 0
  for char in line:
    if char == cursor:
      deletions += 1
    cursor = char
  return deletions

def test():
  print "TEST01:", "pass" if shrinkify("AAAA") == 3 else "**FAIL**"
  print "TEST02:", "pass" if shrinkify("BBBBB") == 4 else "**FAIL**"
  print "TEST03:", "pass" if shrinkify("ABABABAB") == 0 else "**FAIL**"
  print "TEST04:", "pass" if shrinkify("BABABA") == 0 else "**FAIL**"
  print "TEST05:", "pass" if shrinkify("AAABBB") == 4 else "**FAIL**"
  return

test() if TEST_MODE else main()
