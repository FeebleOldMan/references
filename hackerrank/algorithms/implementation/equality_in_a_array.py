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
    len_array = int(input())
    array = list(map(int, input().strip().split()))
    print(min_deletions(len_array, array))

def min_deletions(len_array, array):
    from collections import Counter
    count = Counter(array)
    return sum(count.values()) - max(count.values())

def test():
    print("TEST01:", "pass" if min_deletions(5, [3, 3, 2, 1, 3]) == 2 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

