#!/usr/bin/env python2

TEST_MODE = False

def main():
  length = input()
  counter = [0] * 100
  words = [[] for _ in xrange(100)]

  for i in xrange(length):
    index, word = raw_input().strip().split()
    index = int(index)
    counter[index] += 1
    words[index].append('-') if i < length/2 else words[index].append(word)

  for j in xrange(100):
    for k in xrange(counter[j]):
      print words[j][k],

### v0.3 too slow
#def main():
#  length = int(raw_input().strip())
#  num_array, word_array = [], []
#  for n in range(length):
#    entry = raw_input().strip().split()
#    num_array.append(int(entry[0]))
#    if n < length/2:
#      word_array.append('-')
#    else:
#      word_array.append(entry[1])
#  print countSort(num_array, word_array)
#
#def countSort(num_array, word_array):
#  output = []
#  for key in range(100):
#    while True:
#      try:
#        output.append(word_array.pop(num_array.index(key)))
#        num_array.remove(key)
#      except ValueError:
#        break
#  return ' '.join(output)

### v0.2 too slow
#def countSort(num_array, word_array):
#  numdict = {i: 0 for i in range(100)}
#  for i in num_array:
#    numdict[i] += 1
#  output = []
#  for key in range(100):
#    for _count in range(numdict[key]):
#      output.append(word_array.pop(num_array.index(key)))
#      num_array.remove(key)
#  return ' '.join(output)

### v0.1 too slow
#def main():
#  length = int(raw_input().strip())
#  array = []
#  for n in range(length):
#    entry = raw_input().strip().split()
#    entry[0] = int(entry[0])
#    array.append(entry)
#  print countSort(array)
#
#def countSort(array):
#  for n in range(len(array)/2):
#    array[n][1] = '-'
#  num_array, word_array = [], []
#  for item in array:
#    num_array.append(item[0])
#    word_array.append(item[1])
#  numdict = {i: 0 for i in range(100)}
#  for i in array:
#    numdict[i[0]] += 1
#  output = []
#  for key in range(100):
#    for _count in range(numdict[key]):
#      output.append(word_array.pop(num_array.index(key)))
#      num_array.remove(key)
#  return ' '.join(output)

def test():
  print "TEST01:", "pass" if countSort([[0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [0, 'ij'], [4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']]) == '- - - - - to be or not to be - that is the question - - - -' else "**FAIL**"
  print countSort([[0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [0, 'ij'], [4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']])

test() if TEST_MODE else main()
