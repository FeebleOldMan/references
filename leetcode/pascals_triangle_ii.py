#!/usr/bin/env python3
"""Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1, 3, 3, 1].

Note: Could you optimize your algorithm to use only O(k) extra space?
"""

import sys
import getopt

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
    print(pascal_row(int(input())))

def pascal_row(row):
    """Returns row of Pascal's triangle.

    >>> pascal_row(0)
    [1]
    >>> pascal_row(1)
    [1, 1]
    >>> pascal_row(2)
    [1, 2, 1]
    >>> pascal_row(3)
    [1, 3, 3, 1]
    """
    result = [1]
    for i in range(row):
        result.append(result[-1]*(row-i)//(i+1))
    return result

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

