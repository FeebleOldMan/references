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
    print(count_sum_xor(int(input())))

def count_sum_xor(n):
    """Count number of x that satisfies n + x == n ^ x

    >>> print(count_sum_xor(0))
    1
    >>> print(count_sum_xor(5))
    2
    >>> print(count_sum_xor(10))
    4
    >>> print(count_sum_xor(1000000000000000))
    1073741824
    """
    ### v0.2
    # count number of 0 bits in n
    # count combinations of 0 bits + 1 for answer
    return 2**list(bin(n)[2:]).count('0') if n else 1

### v0.1 too slow
#    count = 0
#    for i in range(n + 1):
#        if n + i == n ^ i:
#            count += 1
#    return count

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

