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
    len_arr = int(input())
    array = list(map(int, input().strip().split()))
    print(find_integer(len_arr, array))

def find_integer(len_arr, array):
    """Returns unique element in int array

    >>> print(find_integer(1, [1]))
    1
    >>> print(find_integer(3, [1, 1, 2]))
    2
    >>> print(find_integer(5, [0, 0, 1, 2, 1]))
    2
    """
### v1.1 editorial answer
    result = 0
    for i in array:
        result ^= i
    return result

### v1.0
#    from collections import Counter
#    counter = Counter(array)
#    num, count = list(counter.keys()), list(counter.values())
#    return num[count.index(1)]

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

