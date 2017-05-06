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
    [print(count_strings(*input().strip().split()))
            for _ in range(int(input()))]

def count_strings(regex, length):
    """Count number of possible strings of length given regex, where
    alphabet only consists of 'a' and 'b'

    >>> count_strings("((ab)|(ba))", 2)
    2
    >>> count_strings("((a|b)*)", 5)
    32
    >>> count_strings("((a*)(b(a*)))", 100)
    100
    """
    return

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

