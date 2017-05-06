#!/usr/bin/env python2

TEST_MODE = True

def main():
  print can_palindrome(raw_input().strip())
  return

def can_palindrome(line):
  alpha_count = {}
  for l in line:
    alpha_count[l] = alpha_count.get(l, 0) + 1
  has_odd = False
  for v in alpha_count.values():
    if v % 2 != 0 and not has_odd:
      has_odd = True
    elif v % 2 != 0 and has_odd:
      return "NO"
  return "YES"

def test():
  print "TEST01:", "pass" if can_palindrome("aaabbbb") == "YES" else "**FAIL**"
  print "TEST02:", "pass" if can_palindrome("cdefghmnopqrstuvw") == "NO" else "**FAIL**"
  print "TEST03:", "pass" if can_palindrome("cdcdcdcdeeeef") == "YES" else "**FAIL**"
  return

test() if TEST_MODE else main()
