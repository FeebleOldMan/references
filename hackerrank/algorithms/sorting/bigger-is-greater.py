#!/usr/bin/env python2

TEST_MODE = True

def main():
  for _ in xrange(input()):
    print next_bigger(raw_input())

def next_bigger(letters):
  # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
  letters = list(letters)
  for i in range(len(letters)-1, 0, -1):
    if letters[i-1] < letters[i]:
      for j in range(len(letters)-1, i-1, -1):
        if letters[j] > letters[i-1]:
          letters[j], letters[i-1] = letters[i-1], letters[j]
          letters[i:] = list(reversed(letters[i:]))
          return ''.join(letters)
  return 'no answer'

#from itertools import permutations

### v0.2 doesn't give correct next biggest
#def next_bigger(letters):
#  perms = permutations(list(letters))
#  next_word = ''.join(perms.next())
#  while next_word <= letters:
#    try:
#      next_word = ''.join(perms.next())
#    except StopIteration:
#      return 'no answer'
#  print ''.join(next_word)
#  return ''.join(next_word)

### v0.1 O(N!) too much memory
#def next_bigger(letters):
#  array = [''.join(word) for word in permutations(sorted(list(letters)))]
#  i = array.index(letters) + 1
#  if i > len(array)-1:
#    return 'no answer'
#  elif array[i] == array[i-1]:
#    return 'no answer'
#  return ''.join(array[i])

def test():
  print "TEST01:", "pass" if next_bigger('ab') == 'ba' else "**FAIL**"
  print "TEST02:", "pass" if next_bigger('bb') == 'no answer' else "**FAIL**"
  print "TEST03:", "pass" if next_bigger('hefg') == 'hegf' else "**FAIL**"
  print "TEST04:", "pass" if next_bigger('dhck') == 'dhkc' else "**FAIL**"
  print "TEST05:", "pass" if next_bigger('dkhc') == 'hcdk' else "**FAIL**"
  print "TEST06:", "pass" if next_bigger('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzaz') == 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzza' else "**FAIL**"

test() if TEST_MODE else main()
