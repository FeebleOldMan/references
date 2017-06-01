#!/usr/bin/env python3
"""Coin Flip Simulation

Write some code that simulates flipping a single coin however many times the
user decides. The code should record the outcomes and count the number of
tails and heads.
"""

import getopt
import sys
from random import choice

def flip_coins(flips):
    """Flips `flips` number of coins.

    flips       int of number of coins to flip

    returns     dict of results
    """
    results = {'heads': 0, 'tails': 0}
    for _ in range(flips):
        result = choice(('heads', 'tails'))
        results[result] += 1
    return results

def main(argv):
    """Main function"""

    help_text = """
Flip Coins v1.0

Usage:
  python coin_flip_simulation.py [options] \x1B[3mflips\x1B[0m

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(argv, "hts", ["help", "test", "stress"])
    except getopt.GetoptError:
        print("Invalid option: {}".format(opts))
        print(help_text)
        sys.exit(2)
    for opt, _ in opts:
        if opt in ("-h", "--help"):
            print(help_text)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
        elif opt in ("-s", "--stress"):
            stress()
            sys.exit()
    print()
    print("COIN FLIPPER")
    print("************")
    if args:
        try:
            flips = int(args[0])
        except TypeError as error:
            print("Invalid number of flips")
            print(error)
    else:
        flips = int(input("Number of coin flips: "))
    results = flip_coins(flips)
    for result, value in results.items():
        print("{result}: {value:{pad}d} ({percent:.2f}%)".format(
            result=result.title(),
            value=value,
            percent=(value/flips)*100,
            pad=len(str(flips))
            )
             )
    print("Total: {}".format(flips))
    print()

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

