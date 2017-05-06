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
    print(max_xor(int(input()), int(input())))

def max_xor(left, right):
    """Returns maximum xor value of ints within range left and right
    
    >>> print(max_xor(10, 15))
    7
    """
### v1.1 editorial answer
# i have no idea how or why this works
# apparently this shifts the binary leftwards and rightwards
    P = left^right
    ret = 1
    while (P):  # takes (m+1) = O(logR) steps
        ret <<= 1
        P >>= 1
    return (ret - 1)
### v1.0
#    from itertools import combinations
#    max_xor = 0
#    combos = combinations(range(left, right + 1), 2)
#    for combo in combos:
#        if combo[0] ^ combo[1] > max_xor:
#            max_xor = combo[0] ^ combo[1] 
#    return max_xor

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

