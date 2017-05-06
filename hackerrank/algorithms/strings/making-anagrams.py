#!/usr/bin/env python2

TEST_MODE = True

def main():
  print make_anagram(raw_input().strip(), raw_input().strip())
  return


def make_anagram(word1, word2):
  count = 0
  letters1, letters2 = {}, {}
  for letter in word1:
    letters1[letter] = letters1.get(letter, 0) + 1
  for letter in word2:
    letters2[letter] = letters2.get(letter, 0) + 1
  for letter in letters1.keys():
    if letter in letters2.keys():
      count += abs(letters1[letter] - letters2[letter])
    if letter not in letters2.keys():
      count += letters1[letter]
  for letter in letters2.keys():
    if letter not in letters1.keys():
      count +=letters2[letter]
  return count

def test():
  print "TEST01:", "pass" if make_anagram("cde", "abc") == 4 else "**FAIL**"
  return

test() if TEST_MODE else main()
