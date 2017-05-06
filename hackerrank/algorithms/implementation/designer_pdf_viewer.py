#!/usr/bin/env python3

import sys, getopt

def main(argv):
    help = """CODE! v1.0

Usage:
  python CODE.py [options]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(argv, "ht", ["help", "test",])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
    heights = list(map(int, input().strip().split()))
    word = input()
    print(area(heights, word))

def area(heights, word):
    heights = dict(zip(
        [chr(i) for i in range(ord('a'), ord('z') + 1)],
        heights))
    word = list(word)
    max_height = 0
    for letter in word:
        if heights[letter] > max_height:
            max_height = heights[letter]
    return len(word) * max_height

def test():
    print("TEST01:", "pass" if area(
        [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
        'abc') == 9 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

