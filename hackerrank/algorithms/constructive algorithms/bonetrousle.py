#!/usr/bin/env python3

import sys, getopt
from itertools import combinations

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
    [print(box_combo(*map(int, input().strip().split()))) for _ 
        in range(int(input()))]

def box_combo(sticks, stock, boxes):
    """Determine boxes combo to buy to get sticks amount while limited to
    stock.

    sticks  int total sticks to obtain
    stock   int of 1 to stock boxes
    boxes   int boxes to buy

    >>> print(box_combo(12, 8, 3))
    1 3 8
    >>> print(box_combo(10, 3, 3))
    -1
    >>> print(box_combo(9, 10, 2))
    5 4
    """
    result = []
    # we won't need to access a range higher than sticks
    stock = list(range(1, min(stock + 1, sticks + 1)))
    # find average value needed to buy
    average = sticks / boxes
    if boxes % 2:
        try:
            result.append(stock.pop(stock.index(average * 2)))
        except:
            return -1
        boxes -= 1
    if average % 1:
        counter = 0.5
    else:
        counter = 1
    while boxes:
        try:
            result.append(stock.pop(stock.index(average + counter)))
            result.append(stock.pop(stock.index(average - counter)))
        except:
            return -1
        counter += 1
        boxes -= 2
    return " ".join(map(str, result))
    ### v0.2 correct but too slow and too much memory
#    stock = range(1, min(stock+1, sticks+1))
#    combos = combinations(stock, boxes)
#    for combo in combos:
#        if sum(combo) == sticks:
#            return " ".join(map(str, combo))
#    return -1

    ### v0.1 correct but too slow and too much memory
#    stock = list(range(1, stock+1))
#    combos = combinations(stock, boxes)
#    for combo in combos:
#        if sum(combo) == sticks:
#            return " ".join(map(str, combo))
#    return -1

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

