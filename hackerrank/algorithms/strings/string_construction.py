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
    print(*[len(set(input())) for _ in range(int(input()))], sep='\n')
#    for _ in range(int(input())):
#        print(make_string(input()))

def make_string(string):
    return len(set(string))

def test():
    print("TEST01:", "pass" if make_string('abcd') == 4 else "**FAIL**")
    print("TEST02:", "pass" if make_string('abab') == 2 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

