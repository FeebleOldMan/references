#!/usr/bin/env python3

import sys, getopt

def main(argv):
    help = """CODE! v1.0

Usage:
  python CODE.py [options]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(argv, "ht", ["help", "test",])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
    num_toys = int(input())
    weights = list(map(int, input().strip().split()))
    print(min_cost(num_toys, weights))

def min_cost(num_toys, weights):
    """Minimum units to buy all toys.
    Each toy costs 1 unit, and if she buys a toy with weight w,
    then she can get all other toys whose weight lies between
    [w, w+4] (both inclusive) free of cost.

    >>> min_cost(5, [1, 2, 3, 17, 10])
    3

    >>> min_cost(10, [1, 2, 2, 2, 2, 3, 3, 17, 17, 10])
    3
    """
    cost = 0
    weights = sorted(set(weights))
    while weights:
        weight = weights.pop(0)
        cost += 1
        for i in range(1, 5):
            if weight + i in weights: weights.remove(weight + i)
    return cost

def test():
    import doctest
    doctest.testmod(verbose = True)

if __name__ == '__main__':
    main(sys.argv[1:])

