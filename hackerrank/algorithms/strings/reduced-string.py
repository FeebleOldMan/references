#!/usr/bin/env python2

TEST_MODE = True

def main():
  print shrink(raw_input().strip())
  return

def shrink(word):
  shrank = True
  while shrank:
    shrank = False
    for i in range(len(word)-1):
      if word[i] == word[i+1]:
        word = word[:i]+word[i+2:]
        shrank = True
        break
  return word if len(word) > 0 else "Empty String"

def test():
  print "TEST01:", "pass" if shrink("aaabccddd") == "abd" else "**FAIL**"
  print "TEST02:", "pass" if shrink("baab") == "Empty String" else "**FAIL**"
  print "TEST03:", "pass" if shrink("aa") == "Empty String" else "**FAIL**"

test() if TEST_MODE else main()
