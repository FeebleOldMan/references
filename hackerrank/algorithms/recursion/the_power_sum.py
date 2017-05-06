#!/usr/bin/env python3
"""Python module template"""

import sys
import getopt
#from itertools import combinations

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
    print(count_power_sum(int(input()), int(input())))

def count_power_sum(target, exponent, base=1):
    """Returns number of ways target can be expressed as sum of exponents of unique
    natural numbers.

    >>> count_power_sum(10, 2)
    1
    >>> count_power_sum(100, 2)
    3
    >>> count_power_sum(100, 3)
    1
    """
    current_value = base**exponent
    # stop condition
    if current_value > target:
        return 0
    elif current_value == target:
        return 1
    return (
        count_power_sum(target-current_value, exponent, base+1)
        + count_power_sum(target, exponent, base+1)
        )

    """
    ### v0.1 too slow
    # create range of values of power to <= target
    power_arr = []
    power = 1
    base = 1
    while power <= target:
        power_arr.append(power)
        base += 1
        power = base**exponent
    # iterate power_arr to sum to target
    count = 0
    for i in range(1, len(power_arr)+1):
        combos = combinations(power_arr, i)
        for j in combos:
            if sum(j) == target:
                count += 1
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
        'count_power_sum(1000, 2)',
        number=1,
        setup="from __main__ import count_power_sum",
        )
         )

if __name__ == '__main__':
    main(sys.argv[1:])

