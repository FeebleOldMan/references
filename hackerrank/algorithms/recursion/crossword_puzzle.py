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
    layout = [list(input().strip()) for _ in range(10)]
    words = input().strip().split(';')
    print(fill_puzzle(layout, words))

def fill_puzzle(layout, words):
    """Solves crossword puzzle with words.

    >>> print(fill_puzzle(
    ...     [list('+-++++++++'),
    ...      list('+-++++++++'),
    ...      list('+-++++++++'),
    ...      list('+-----++++'),
    ...      list('+-+++-++++'),
    ...      list('+-+++-++++'),
    ...      list('+++++-++++'),
    ...      list('++------++'),
    ...      list('+++++-++++'),
    ...      list('+++++-++++')
    ...     ],
    ...     ['LONDON', 'DELHI', 'ICELAND', 'ANKARA']
    ...     ))
    +L++++++++
    +O++++++++
    +N++++++++
    +DELHI++++
    +O+++C++++
    +N+++E++++
    +++++L++++
    ++ANKARA++
    +++++N++++
    +++++D++++
    >>> print(fill_puzzle(
    ...      list('+-++++++++'),
    ...      list('+-++++++++'),
    ...      list('+-------++'),
    ...      list('+-++++++++'),
    ...      list('+-++++++++'),
    ...      list('+------+++'),
    ...      list('+-+++-++++'),
    ...      list('+++++-++++'),
    ...      list('+++++-++++'),
    ...      list('++++++++++'),
    ...      ],
    ...      ['AGRA', 'NORWAY', 'ENGLAND', 'GWALIOR']
    ...      ))
    +E++++++++
    +N++++++++
    +GWALIOR++
    +L++++++++
    +A++++++++
    +NORWAY+++
    +D+++G++++
    +++++R++++
    +++++A++++
    ++++++++++
    """
    layout = [[0 if x == '+' else 1 for x in col] for col in layout]
    # change blanks to lines? but how to change back to grid?
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

