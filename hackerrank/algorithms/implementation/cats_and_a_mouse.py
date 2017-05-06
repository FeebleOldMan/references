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
    for _ in range(int(input())):
        print(which_cat(*map(int, input().strip().split())))

def which_cat(cat_a, cat_b, mouse_c):
    """Returns 'Cat A', 'Cat B', or 'Mouse C' depending on which cat is closest
    to the mouse.

    >>> print(which_cat(1, 2, 3))
    Cat B
    >>> print(which_cat(1, 3, 2))
    Mouse C
    >>> print(which_cat(2, 1, 3))
    Cat A
    """
    dist_a = abs(mouse_c - cat_a)
    dist_b = abs(mouse_c - cat_b)
    if dist_a == dist_b:
        return 'Mouse C'
    else:
        return 'Cat A' if dist_a < dist_b else 'Cat B'

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

