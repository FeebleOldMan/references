#!/usr/bin/env python2

TEST_MODE = True

def main():
  print make_anagram(raw_input().strip(), raw_input().strip())
  return

def make_anagram(s1, s2):
  s1_count, s2_count = {}, {}
  s1_len, s2_len = len(s1), len(s2)
  for l in s1:
    s1_count[l] = s1_count.get(l, 0) + 1
  for l in s2:
    s2_count[l] = s2_count.get(l, 0) + 1
  steps = 0
  while s1_count != s2_count:
    if s1_len > s2_len:

  return steps

def test():
  print "TEST01:", "pass" if make_anagram("cde", "adc") == 4 else "**FAIL**"
  return

test() if TEST_MODE else main()
