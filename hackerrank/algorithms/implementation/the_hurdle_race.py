#!/usr/bin/env python3
"""Python module template"""

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
    initial_height = list(map(int, input().strip().split()))[1]
    hurdles = list(map(int, input().strip().split()))
    print(min_drinks(initial_height, hurdles))

def min_drinks(initial_height, hurdles):
    """Returns minimum number of drinks to clear hurdles.

    >>> min_drinks(4, [1, 6, 3, 5, 2])
    2
    >>> min_drinks(7, [2, 5, 4, 5, 2])
    0
    """
    return max(max(hurdles) - initial_height, 0)

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

