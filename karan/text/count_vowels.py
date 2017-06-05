#!/usr/bin/env python3
"""Count Vowels

Counts the number of vowels in a text string.
Prints the sum of each vowel found.
"""

import sys
import getopt

def count_vowels(text):
    """Counts number of vowels in string text. Prints a summary of vowels.

    text        string of input text

    >>> count_vowels('')
    Vowel Counts
    ------------
    No vowels found
    >>> count_vowels('a cat in a bag')
    Vowel Counts
    ------------
    a: 4
    i: 1
    """
    VOWELS = ('a', 'e', 'i', 'o', 'u',)
    vowel_count = {}

    for letter in list(text.lower()):
        if letter in VOWELS:
            vowel_count[letter] = vowel_count.get(letter, 0) + 1

    print("Vowel Counts")
    print("------------")
    if vowel_count:
        for letter, value in vowel_count.items():
            print("{}: {}".format(letter, str(value)))
    else:
        print("No vowels found")


def main(argv):
    """Main function"""

    help_text = """
Count Vowels v1.0

Usage:
  python CODE.py [options]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, _ = getopt.getopt(argv, "hts", ["help", "test", "stress"])
    except getopt.GetoptError as error:
        print("Invalid option: {}".format(error))
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
    count_vowels(input("Enter a string: "))

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

