#!/usr/bin/env python3
"""Finds π to the nth digit."""
# pylint: disable=invalid-name

import sys
import getopt
from decimal import Decimal, getcontext

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
    except getopt.GetoptError as error:
        print("Invalid option: {}".format(error))
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
    n = int(input("π to decimal places: "))
    print(pi_gauss_legendre(n))
    # TODO
    #print(pi_bbp(n))

def pi_bbp(n):
    """Returns π to nth decimal place using the Bailey-Borwein-Plouffe
    formula:
    https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula

    n       int >= 0 desired decimal places of π

    return  str value of π to nth decimal place

    >>> pi_bbp(0)
    '3'
    >>> pi_bbp(6)
    '3.141593'
    """
    # TODO implement bbp
    pi = '3'
    if n > 0:
        pi += '.'
    for _ in range(n):
        digit = '0'
        pi += digit
    return pi

def pi_gauss_legendre(n):
    """Returns π to nth decimal place using the Guess-Legendre iterative
    algorithm:
    https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    n       int >= 0 desired decimal places of π

    return  str value of π to nth decimal place

    >>> pi_gauss_legendre(0)
    '3'
    >>> pi_gauss_legendre(6)
    '3.141593'
    >>> pi_gauss_legendre(75)
    '3.141592653589793238462643383279502884197169399375105820974944592307816406286'
    """
    # TODO fix precision bug
    # initialization
    getcontext().prec = 1000000
    ax = Decimal(1.0)
    bx = Decimal(1/(2**0.5))
    tx = Decimal(0.25)
    px = Decimal(1.0)
    ITERATIONS = 25     # 25 iterations produce 45 million digits

    # iteration
    for _ in range(ITERATIONS):
        ay = (ax + bx)/Decimal(2.0)
        by = (ax * bx)**Decimal(0.5)
        ty = tx - px * (ax - ay)**Decimal(2.0)
        py = Decimal(2.0)*px
        ax, bx, tx, px = ay, by, ty, py
    pi = (ay + by)**Decimal(2.0) / (Decimal(4.0) * ty)
    return "{:.{n}f}".format(pi, n=n)
    #return "{}".format(pi)

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

