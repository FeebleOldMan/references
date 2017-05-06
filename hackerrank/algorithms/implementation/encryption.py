#!/usr/bin/env python

TEST_MODE = True

import math

def main():
  message = raw_input().strip()
  print encrypt(message)
  return

def encrypt(message):
  length = len(message)
  rows = int(math.floor(math.sqrt(length)))
  cols = int(math.ceil(math.sqrt(length)))
  if rows * cols < length:
    rows += 1
  initial_arr = []
  for i in range(0, length, cols):
    initial_arr.append(list(message[i:i+cols]))
  while len(initial_arr[-1]) < len(initial_arr[0]):
    initial_arr[-1].append('')
  output = [[] for col in range(cols)]
  for col in range(cols):
    for row in range(rows):
      output[col].append(initial_arr[row][col])
  output = ' '.join([''.join(word) for word in output])
  return output

def test():
  print "TEST 01:", "pass" if encrypt("haveaniceday") == "hae and via ecy" else "**FAIL**: " + encrypt("haveaniceday")
  print "TEST 02:", "pass" if encrypt("feedthedog") == "fto ehg ee dd" else "**FAIL**: " + encrypt("feedthedog")
  print "TEST 03:", "pass" if encrypt("chillout") == "clu hlt io" else "**FAIL**: " + encrypt("chillout")
  return

test() if TEST_MODE else main()
