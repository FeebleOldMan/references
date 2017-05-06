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
    [print(~int(input()) ^ (1 << 32)) for _ in range(int(input()))]
    #[print(int(input()) ^ ((1 << 32) - 1)) for _ in range(int(input()))]
    #[print(int(input()) ^ 0xffffffff) for _ in range(int(input()))]
#   for _ in range(int(input())):
#        print(flip_bits(int(input())))

def flip_bits(num):
    """Flips bits of binary representation of num

    >>> flip_bits(2147483647)
    2147483648
    >>> flip_bits(1)
    4294967294
    >>> flip_bits(0)
    4294967295
    """
    return num ^ 0xffffffff

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

