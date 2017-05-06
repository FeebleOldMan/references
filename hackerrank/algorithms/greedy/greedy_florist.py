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
    num_flowers, num_friends = map(int, input().strip().split())
    costs = list(map(int, input().strip().split()))
    print(min_cost(num_flowers, num_friends, costs))

def min_cost(num_flowers, num_friends, costs):
    """Returns minimum cost of buying flowers
    Each flower bought by a customer costs (n + 1) * cost
    where n is number of flowers already bought

    >>> min_cost(3, 3, [2, 5, 6])
    13
    >>> min_cost(3, 2, [2, 5, 6])
    15
    >>> min_cost(5, 1, [1, 1, 1, 1, 1])
    15
    >>> min_cost(5, 3, [1, 1, 1, 1, 5])
    11
    >>> min_cost(3, 5, [1, 1, 1])
    3
    >>> min_cost(5, 2, [2, 4, 6, 8, 8])
    42
    """
    allowance = {person: 0 for person in range(num_friends)}
    cost = 0
    while costs:
        for person in range(num_friends):
            try:
                cost += (allowance[person] + 1) * costs.pop(costs.index(max(costs)))
                allowance[person] += 1
            except:
                break
    return cost
### v0.1 wrong algorithm. need to spread buying amongst people first rather
### than finish person by person
#    allowance = {person: num_flowers // num_friends for person in
#            range(num_friends)}
#    extras = num_flowers % num_friends
#    for person in range(extras):
#        allowance[person] += 1
#    cost = 0
#    for person in range(num_friends - 1, -1, -1):
#        flowers_bought = 0
#        while flowers_bought < allowance[person]:
#            cost += (flowers_bought + 1) * costs.pop(costs.index(max(costs)))
#            flowers_bought += 1
#    return cost

def test():
    import doctest
    doctest.testmod(verbose = True)

if __name__ == '__main__':
    main(sys.argv[1:])

