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
    print(decipher(input()))

def decipher(string):
    #count = 0
    #for i in range(len(string)):
    #    if string[i] != 'SOS'[i % 3]:
    #        count += 1
    #return count
    return [l != 'SOS' [i % 3] for i, l in enumerate(string)].count(True)

def test():
    print("TEST01:", "pass" if decipher('SOSSPSSQSSOR') == 3 else "**FAIL**")
    print("TEST02:", "pass" if decipher('SOSSOT') == 1 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

