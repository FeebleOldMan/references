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
    len_seq, diff = map(int, input().strip().split())
    seq = list(map(int, input().strip().split()))
    print(beautiful_triplets(len_seq, diff, seq))

def beautiful_triplets(len_seq, diff, seq):
    count = 0
    for num in seq:
        if (num + diff) in seq and (num + (2 * diff)) in seq:
            count += 1
    return count

def test():
    print("TEST01:", "pass" if beautiful_triplets(7, 3, 
        [1, 2, 4, 5, 7, 8, 10]) == 3 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

