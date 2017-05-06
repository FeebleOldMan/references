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
    input()
    print(min_swaps(input().strip().split()))

def min_swaps(array):
    """Counts minimum pair swaps to make array sorted (in either order).

    >>> min_swaps([2, 5, 3, 1])
    2
    >>> min_swaps([3, 5, 1, 2])
    2
    >>> min_swaps([3, 1, 5, 2])
    3
    >>> min_swaps([1, 2, 3, 4])
    0
    >>> min_swaps([4, 3, 2, 1])
    0
    >>> min_swaps([4, 2, 3, 1])
    1
    >>> min_swaps([3, 4, 2, 1, 5])
    3
    """
    array = list(map(int, array))
    up_sort = sorted(array)
    down_sort = up_sort[::-1]
    count = [0, 0]
    for i, sorted_arr in enumerate((up_sort, down_sort)):
        arr = array[:]
        arr_dict = {value: index for index, value in enumerate(array)}
        for j, value in enumerate(sorted_arr):
            if arr_dict[value] != j:
                # get position of target value
                target_pos = arr_dict[value]
                # swap current position value to target position value
                arr_dict[arr[j]], arr_dict[value] = arr_dict[value], arr_dict[arr[j]]
                arr[j], arr[target_pos] = arr[target_pos], arr[j]
                count[i] += 1
    return min(count)
    """
    ### v0.2 correct but too slow
    array = list(map(int, array))
    up_sort = sorted(array)
    down_sort = up_sort[::-1]
    count = [0, 0]
    for j, main_list in enumerate((up_sort, down_sort)):
        arr = array[:]
        for i, value in enumerate(arr):
            current_min = main_list[i]
            if current_min != value:
                min_idx = arr[i:].index(current_min) + i
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                count[j] += 1
    return min(count)

    """
    """
    ### v0.1 is not optimal and incorrect
    array = list(map(int, array))
    count = 0
    for i, value in enumerate(array):
        current_min = min(array[i:])
        if current_min != value:
            min_idx = array.index(current_min)
            array[i], array[min_idx] = array[min_idx], array[i]
            count += 1
    print(array)
    return count
    """

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

