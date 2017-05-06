#!/usr/bin/env python2

TEST_MODE = True

def main():
  length = int(raw_input().strip())
  array = []
  for _ in range(length):
    entry = raw_input().strip().split()
    entry[0] = int(entry[0])
    array.append(entry)
  print countSort(array)

def countSort(array):
  numdict = {i: 0 for i in range(100)}
  for i in array:
    numdict[i[0]] += 1
  total = 0
  output = []
  for key in range(100):
    total += numdict[key]
    output.append(str(total))
  return ' '.join(output)

def test():
  print "TEST01:", "pass" if countSort([[4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']]) == '1 3 5 6 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10' else "**FAIL**"
  print countSort([[4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']])

test() if TEST_MODE else main()
