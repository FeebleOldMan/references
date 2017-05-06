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
    #sorted(map(int, input().strip().split()))
    print(mini_max_sum(list(map(int, input().strip().split()))))

def mini_max_sum(arr):
    arr.sort()
    arr = str(sum(arr[:4])) + ' ' + str(sum(arr[-4:]))
    return arr

def test():
    print("TEST01:", "pass" if mini_max_sum([1,2,3,4,5]) == '10 14' else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

