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
    num = int(input())
    breads = list(map(int, input().strip().split()))
    print(distribute(num, breads))

def distribute(num, breads):
    count = 0
    for i in range(num - 1):
        if breads[i] % 2 != 0:
            breads[i] += 1
            breads[i+1] += 1
            count += 2
    if breads[-1] % 2:
        count = 'NO'
    return count

def test():
    print("TEST01:", "pass" if distribute(5, [2, 3, 4, 5, 6]) == 4 else "**FAIL**")
    print("TEST02:", "pass" if distribute(2, [1, 2]) == 'NO' else "**FAIL**")
    print("TEST03:", "pass" if distribute(5, [1, 2, 3, 4, 5]) == 'NO' else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

