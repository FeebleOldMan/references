#!/usr/bin/env python2

print 'pangram' if len(set(raw_input().replace(' ', '').lower())) == 26 else 'not pangram'

### v0.1 should work but slower due to testing each letter of alphabet

#TEST_MODE = False

#def main():
#  sentence = set(raw_input().strip().lower())
#  print is_pangram(sentence)
#  return
#
#def is_pangram(sentence):
#  alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
#  for letter in alphabet:
#    if letter not in sentence:
#      return 'not pangram'
#  return 'pangram'
#
#def test():
#  return
#
#test() if TEST_MODE else main()
