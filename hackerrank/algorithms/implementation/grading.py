#!/usr/bin/env python3
"""Test module"""

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
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg)
            print(help_text)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
        elif opt in ("-s", "--stress"):
            stress()
            sys.exit()
    for _ in range(int(input())):
        print(round_grade(int(input())))

def round_grade(grade):
    """If difference between grade and next multiple of 5 is less than 3, round
    grade up to the next multiple of 5. If grade < 38, no rounding occurs.

    >>> round_grade(73)
    75
    >>> round_grade(67)
    67
    >>> round_grade(38)
    40
    >>> round_grade(33)
    33
    """
    if grade >= 38 and grade % 5 >= 3:
        grade += 5 - (grade % 5)
    return grade

def test():
    """Test function"""

    import doctest
    print(doctest.testmod())

def stress():
    """Stress test function"""

    print("STRESS TEST")
    import timeit
    print(timeit.timeit(
        # edit test here
        'FUNCTION()',
        number=1,
        setup="from __main__ import FUNCTION",
        )
         )

if __name__ == '__main__':
    main(sys.argv[1:])

