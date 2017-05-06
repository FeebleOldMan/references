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
        print(find_probability(*map(int, input().strip().split())))

def find_probability(num_a, num_b, num_c):
    """Given two numbers A and B and we generate x and y using a random
    number generator with uniform probability density function [0, A]
    and [0, B] respectively, what's the probability that x + y is less than C
    where C is a positive integer.

    Outputs a reduced fraction that indicates probability.

    >>> find_probability(1, 1, 1)
    1/2
    >>> find_probability(1, 1, 2)
    1/1
    >>> find_probability(1, 1, 3)
    1/1
    """
    # sum of 2 uniform pdf is ?
    expected_value = num_a/2 + num_b/2
    max_value = num_a + num_b
    return

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

