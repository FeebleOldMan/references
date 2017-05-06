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
    print(min_dist(len_array, array))

def min_dist(len_array, array):
    min_dist = float('inf')
    for i, n in enumerate(array):
        try:
            dist = array[i+1:].index(n) + 1
            if dist < min_dist:
                min_dist = dist
        except:
            pass
    return min_dist if min_dist < float('inf') else -1

def test():
    print("TEST01:", "pass" if min_dist(6, [7, 1, 3, 4, 1, 7]) == 3 else "**FAIL**")
    print("TEST02:", "pass" if min_dist(6, [7, 1, 3, 4, 5, 6]) == -1 else "**FAIL**")
    print("TEST03:", "pass" if min_dist(6, [7, 1, 3, 4, 5, 7]) == 5 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

