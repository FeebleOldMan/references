#!/usr/bin/env python2

TEST_MODE = False

def main():
  rocks = []
  for _ in range(int(raw_input().strip())):
    rocks.append(raw_input().strip())
  print count_elements(rocks)
  return

def count_elements(rocks):
  element_count = 0
  merged_rocks = []
  for rock in rocks:
    merged_rocks += rock
  alphabets = set(merged_rocks)
  for letter in alphabets:
    element = True
    for rock in rocks:
      if letter not in rock:
        element = False
        break
    if element:
      element_count += 1
  return element_count

def test():
  print count_elements(['abcdde', 'baccd', 'eeabg'])
  return

test() if TEST_MODE else main()
