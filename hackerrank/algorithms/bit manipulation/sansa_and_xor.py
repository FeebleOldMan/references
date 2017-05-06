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
        print(sub_xor(int(input()), list(map(int, input().strip().split()))))

def sub_xor(len_array, array):
    """XORs contiguous subarrays, then XORs values obtained

    >>> print(sub_xor(3, [1, 2, 3]))
    2
    >>> print(sub_xor(4, [4, 5, 7, 5]))
    0
    >>> print(sub_xor(5, [1, 2, 3, 4, 5]))
    7
    >>> print(sub_xor(6, [1, 2, 3, 4, 5, 6]))
    0
    """
    from functools import reduce
    return reduce(lambda x, y: x ^ y, array[::2]) if len_array % 2 != 0 else 0

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

