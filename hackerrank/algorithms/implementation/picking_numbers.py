#!/usr/bin/env python3
"""Python module template"""

import sys
import getopt
from collections import Counter

def main(argv):
    """Main function"""

    help_text = """CODE! v1.0

Usage:
  python CODE.py [options]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(argv, "hts", ["help", "test", "stress"])
    except getopt.GetoptError:
        print(args)
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg)
            print(help)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
        elif opt in ("-s", "--stress"):
            stress()
            sys.exit()
    input()
    print(largest_set(list(map(int, input().strip().split()))))

def largest_set(numbers):
    """Given an array of integers, find and print the maximum number of
    integers you can select from the array such that the absolute difference
    between any two of the chosen integers is <= 1.

    >>> largest_set([4, 6, 5, 3, 3, 1])
    3
    >>> largest_set([1, 2, 2, 3, 1, 2])
    5
    >>> largest_set([1, 1, 2, 2, 5, 5, 5])
    4
    """
    count = Counter(numbers)
    largest_count = 0
    for number in set(numbers):
        low_count = count[number-1] + count[number]
        high_count = count[number] + count[number+1]
        largest_count = max(low_count, high_count, largest_count)
    return largest_count

def test():
    """Runs doctest on functions."""

    import doctest
    print(doctest.testmod())

def stress():
    """Runs stress test on functions."""

    print("STRESS TEST")
    import timeit
    print(timeit.timeit(
        # edit stress test function here
        'FUNCTION()',
        number=1,
        setup="from __main__ import FUNCTION",
        )
         )

if __name__ == '__main__':
    main(sys.argv[1:])

