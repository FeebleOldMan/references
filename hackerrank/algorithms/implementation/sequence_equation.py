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
#    numbers = int(input())
#    sequence = {}
#    for i in range(1, numbers+1):
#        sequence[i] = int(input())
    permutate(int(input()), list(map(int, input().strip().split())))

def permutate(length, sequence):
    """For each x where 1 <= x <= length, prints integer such that
    sequence(sequence(y)) == x.

    >>> permutate(3, [2, 3, 1])
    2
    3
    1
    """
    for pos in range(1, length+1):
        print(sequence.index(sequence.index(pos)+1)+1)

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

