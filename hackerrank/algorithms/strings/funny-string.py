#!/usr/bin/env python2

TEST_MODE = False

def main():
  for _ in range(int(raw_input().strip())):
    print funny(raw_input().strip())
  return

def funny(line):
  reverse = line[len(line)::-1]
  for i in range(1, len(line)):
    if abs(ord(line[i]) - ord(line[i-1])) != abs(ord(reverse[i]) - ord(reverse[i-1])):
      return "Not Funny"
  return "Funny"

def test():
  print funny('acxz')
  print funny('bcxz')
  return

test() if TEST_MODE else main()
