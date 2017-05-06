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
    print(strange_count(int(input())))

def strange_count(time):
    t = 1
    cycle = 0
    value = 3
    while t < time:
        t += 2**(cycle) * 3
        cycle += 1
    if t == time:
        value = 2**(cycle) * 3
    elif t > time:
        value = 2**(cycle-1) * 3 - (time - (t - 2**(cycle-1) * 3))
    return value

def test():
    print("TEST01:", "pass" if strange_count(4) == 6 else "**FAIL**")
    print("TEST02:", "pass" if strange_count(1) == 3 else "**FAIL**")
    print("TEST03:", "pass" if strange_count(8) == 2 else "**FAIL**")
    print("TEST04:", "pass" if strange_count(3) == 1 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

