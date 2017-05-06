#!/usr/bin/env python2

TEST_MODE = True

def main():
  for _ in range(int(raw_input().strip())):
    print palindrome(raw_input().strip())
  return

def palindrome(line):
  for i in range(len(line)/2):
    if line[i] != line[-(i+1)]:
      if is_palindrome(line[:i]+line[i+1:]):
        return i
      else:
        return len(line)-(i+1)
  return -1

### v0.1 too slow
#def palindrome(line):
#  if is_palindrome(line): return -1
#  for i in range(len(line)):
#    shortened = line[:i] + line[i+1:]
#    if is_palindrome(shortened):
#      return i
#  return -1
#
def is_palindrome(line):
  for i in range(len(line)/2):
    if line[i] != line[-(i+1)]:
      return False
  return True

def test():
  print "TEST01:", "pass" if palindrome('aaab') == 3 else "**FAIL**"
  print "TEST02:", "pass" if palindrome('baa') == 0 else "**FAIL**"
  print "TEST03:", "pass" if palindrome('aaa') == -1 else "**FAIL**"
  print "TEST04:", "pass" if palindrome('bcbc') == 0 or palindrome('bcbc') == 3 else "**FAIL**"
  return

test() if TEST_MODE else main()
