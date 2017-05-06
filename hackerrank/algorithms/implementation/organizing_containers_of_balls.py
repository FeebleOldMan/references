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
        containers = int(input())
        container_matrix = []
        for _ in range(containers):
            container_matrix.append(list(map(int, input().strip().split())))
        print(check_possibility(container_matrix))

def check_possibility(container_matrix):
    """Returns 'Possible' if balls can be sorted else 'Impossible'

    >>> check_possibility([[1, 1], [1, 1]])
    'Possible'
    >>> check_possibility([[0, 2], [1, 1]])
    'Impossible'
    """
    row_sum = set([sum(row) for row in container_matrix])
    container_matrix = zip(*container_matrix)
    col_sum = set([sum(row) for row in container_matrix])
    return 'Possible' if (
        row_sum == col_sum and len(row_sum) == len(col_sum)
        ) else 'Impossible'

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

