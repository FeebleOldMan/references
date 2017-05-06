#!/usr/bin/env python3

TEST_MODE = True

def main():
  for _ in range(int(input().strip())):
    print(has_substring(input().strip(), input().strip()))
  return

def has_substring(word1, word2):
  set1 = set(word1)
  set2 = set(word2)
  for letter in set1:
    if letter in set2:
      return 'YES'
  return 'NO'

### v0.1 generates combinations of all substrings. unnecessary as only 1 letter is required to match
#def has_substring(word1, word2):
#  combo1 = combi(word1)
#  combo2 = combi(word2)
#  for word in combo1:
#    if word in combo2:
#      return "YES"
#  return "NO"
#
#def combi(word):
#  combinations = []
#  for i in range(len(word)):
#    for j in range(i+1, len(word)+1):
#      combinations.append(word[i:j])
#  return combinations

def test():
  print("TEST01:", "pass" if has_substring("hello", "world") == "YES" else "**FAIL**")
  print("TEST02:", "pass" if has_substring("hi", "world") == "NO" else "**FAIL**")
  return

test() if TEST_MODE else main()
