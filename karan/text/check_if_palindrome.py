#!/usr/bin/env python3
"""Check if Palindrome

Checks if the string entered by the user is a palindrome. That is that it
reads the same forwards as backwards like “racecar”
"""

import sys
import getopt
import re

def is_palindrome(string):
    """Check if str is palindrome

    Return      True if palindrome else False

    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('A man, a plan, a canal, Panama.')
    True
    >>> is_palindrome('1221')
    True
    >>> is_palindrome('abca')
    False
    >>> is_palindrome('abbbb')
    False
    """
    string = string.lower()
    re_nonalphanumeric = re.compile(r'[\W_]+')
    string = re_nonalphanumeric.sub('', string)
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return False
    return True

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
    string = input("Enter a string to check for palindromicity: ")
    if is_palindrome(str):
        print("{} is a palindrome.".format(string))
    else:
        print("{} is NOT a palindrome.".format(string))

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

