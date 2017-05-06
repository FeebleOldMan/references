#!/usr/bin/env python2

TEST_MODE = False 

def main():
  for _ in range(int(raw_input().strip())):
    print mirror(raw_input().strip())
  return

def mirror(line):
  line = list(line)
  operations = 0
  for i in range(len(line)/2 + 1):
    while ord(line[i]) != ord(line[-(i+1)]):
      if ord(line[i]) > ord(line[-(i+1)]):
        line[i] = chr(ord(line[i])-1)
      else:
        line[-(i+1)] = chr(ord(line[-(i+1)])-1)
      operations += 1
  return operations

def test():
  print "TEST01:", "pass" if mirror("abc") == 2 else "**FAIL**"
  print "TEST02:", "pass" if mirror("abcba") == 0 else "**FAIL**"
  print "TEST03:", "pass" if mirror("abcd") == 4 else "**FAIL**"
  print "TEST04:", "pass" if mirror("cba") == 2 else "**FAIL**"
  return

test() if TEST_MODE else main()
