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
    len_a, len_b = map(int, input().strip().split())
    set_a = set(map(int, input().strip().split()))
    set_b = set(map(int, input().strip().split()))
    print(count_between(len_a, len_b, set_a, set_b))

def count_between(len_a, len_b, set_a, set_b):
    count = 0
    for i in range(max(set_a), min(set_b)+1):
        test_a = all([i % n == 0 for n in set_a]) 
        if test_a:
            test_b = all([n % i == 0 for n in set_b])
            if test_b:
                count += 1
    return count

def test():
    print("TEST01:", "pass" if count_between(2, 3, {2, 4}, {16, 32, 96}) == 3 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

