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
    #print([l.isupper() for l in input()].count(True) + 1)
    print(count_camelcase(input()))

def count_camelcase(s):
    return [l.isupper() for l in s].count(True) + 1

def test():
    print("TEST01:", "pass" if count_camelcase('saveChangesInTheEditor') == 5 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

