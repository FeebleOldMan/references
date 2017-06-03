#!/usr/bin/env python3
"""Two Sum
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.
"""

# pylint: disable=too-few-public-methods, invalid-name, missing-docstring
# pylint: disable=no-self-use

import getopt
import sys

class Solution:

    def twoSum(self, nums, target):
        """
        Returns indices of two numbers from nums that add up to target.

        nums        list of integers
        target      int
        return      list of integers

        >>> s = Solution(); s.twoSum([2, 7, 11, 5], 9)
        [0, 1]
        >>> s = Solution(); s.twoSum([-2, -7, -11, 5], -9)
        [0, 1]
        >>> s = Solution(); s.twoSum([-5, 10, 3, -6, -2], 4)
        [1, 3]
        """
        for idx_0, value in enumerate(nums):
            try:
                idx_1 = nums[idx_0+1:].index(target - value)
                return [idx_0, idx_0 + idx_1 + 1]
            except ValueError:
                pass

def main(argv):
    """Main function"""

    help_text = """
CODE v1.0

Usage:
  python CODE.py [options] [filename]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, _ = getopt.getopt(argv, "hts", ["help", "test", "stress"])
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
    s = Solution()
    nums = list(map(
        int,
        input("Enter a list of numbers separated by space: ").strip().split())
               )
    target = int(input("Enter a target number: "))
    print(s.twoSum(nums, target))

def test():
    """Runs doctest on functions."""

    import doctest
    print(doctest.testmod())

def stress():
    """Runs stress test on functions."""

    print("STRESS TEST")
    import timeit
    setup = """
from __main__ import Solution;
import random
s = Solution();
nums = [int(1000*random.random()) for _ in range(1000000)];
target = int(1500*random.random());
"""
    print(timeit.timeit(
        # edit stress test function here
        's.twoSum(nums, target)',
        number=10,
        setup=setup,
        )
         )

if __name__ == '__main__':
    main(sys.argv[1:])

