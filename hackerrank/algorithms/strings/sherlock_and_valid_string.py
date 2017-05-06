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
    print(is_valid(input()))

def is_valid(string):
    """Output YES if string can be converted to a "valid" string
    by removing less than or equal to one character.
    Else, output NO.
    "Valid" string consists of equal number of each character

    >>> print(is_valid("aabbcd"))
    NO
    >>> print(is_valid("aabb"))
    YES
    >>> print(is_valid("abbac"))
    YES
    >>> print(is_valid("aa"))
    YES
    >>> print(is_valid("abcd"))
    YES
    >>> print(is_valid("aaad"))
    YES
    """
    from collections import Counter
    chr_count = Counter(string)
    unique_chrs = len(set(string))
    max_count = max(chr_count.values())
    max_chrs, second_max = 0, 0
    for key, value in chr_count.items():
        if value == max_count:
            max_chrs += 1
        elif value == max_count - 1:
            second_max += 1
    return ('YES' if (max_chrs == unique_chrs
            or (max_chrs == 1 and second_max == unique_chrs - 1)
            or (max_chrs == unique_chrs - 1 and second_max == 1)
            or (max_chrs == unique_chrs - 1 and 1 in chr_count.values()))
            else 'NO')

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

