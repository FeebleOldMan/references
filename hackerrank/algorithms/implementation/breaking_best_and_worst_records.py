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
    int(input())
    scores = list(map(int, input().strip().split()))
    print(count_records(scores))

def count_records(scores):
    """Tracks each score in array.
    Returns number of times record for most and least points scored was
    broken.

    >>> print(count_records([10, 5, 20, 20, 4, 5, 2, 25, 1]))
    2 4
    >>> print(count_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
    4 0
    """
    low_count, high_count = 0, 0
    low_score = high_score = scores.pop(0)
    for score in scores:
        if score < low_score:
            low_count += 1
            low_score = score
        elif score > high_score:
            high_count += 1
            high_score = score
    return ' '.join(map(str, [high_count, low_count]))

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

