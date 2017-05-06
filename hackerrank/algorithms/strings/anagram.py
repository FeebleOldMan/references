#!/usr/bin/env python2

TEST_MODE = True

def main():
  for _ in range(int(raw_input().strip())):
    print anagram(raw_input().strip())
  return

def anagram(line):
  # dict count the number of letters in second string and adjust first to match
  if len(line) % 2 != 0: return -1
  s1 = line[:len(line)/2]
  s2 = line[len(line)/2:]
  s1_count, s2_count = {i:0 for i in map(chr, range(ord('a'), ord('z')+1))}, {i:0 for i in map(chr, range(ord('a'), ord('z')+1))}
  step_count = 0
  for i in range(len(s1)):
    s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
    s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
  for letter in s1_count.keys():
    if s1_count[letter] < s2_count[letter]:
      step_count += s2_count[letter] - s1_count[letter]
  return step_count

def test():
  print anagram('abcd')
  print anagram('abba')
  print anagram('aaabbb')
  return

test() if TEST_MODE else main()

