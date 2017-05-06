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
    for _ in range(int(input())):
        print(poison(*list(map(int, input().strip().split()))))

def poison(prisoners, sweets, start):
    return ((sweets % prisoners + start - 1) % prisoners or prisoners)

def test():
    print("TEST01:", "pass" if poison(5, 2, 1) == 2 else "**FAIL**")
    print("TEST02:", "pass" if poison(5, 6, 1) == 1 else "**FAIL**")
    print("TEST03:", "pass" if poison(5, 6, 3) == 3 else "**FAIL**")
    print("TEST04:", "pass" if poison(10, 1, 1) == 1 else "**FAIL**")
    print("TEST05:", "pass" if poison(2, 8, 2) == 1 else "**FAIL**")
    print("TEST06:", "pass" if poison(2, 8, 1) == 2 else "**FAIL**")
    print("TEST07:", "pass" if poison(3, 8, 1) == 2 else "**FAIL**")
    print("TEST08:", "pass" if poison(3, 9, 1) == 3 else "**FAIL**")
    print("TEST09:", "pass" if poison(3, 2, 1) == 2 else "**FAIL**")
    print("TEST10:", "pass" if poison(3, 8, 3) == 1 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

