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
    low, high, divisor = map(int, input().strip().split())
    print(beautiful_days(low, high, divisor))

def beautiful_days(low, high, divisor):
    count = 0
    for day in range(low, high + 1):
        if abs(day - int(''.join(list(str(day))[::-1]))) % divisor == 0:
            count += 1
    return count

def test():
    print("TEST01:", "pass" if beautiful_days(20, 23, 6) == 2 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

