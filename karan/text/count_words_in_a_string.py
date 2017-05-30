#!/usr/bin/env python3
"""Count Words in a String

Counts the number of individual words in a string. For added complexity read
these strings in from a text file and generate a summary.
"""

import sys
import getopt

def count_words(string):
    """Counts and returns number of individual words in a string.

    string      str input

    returns     int of number of words

    >>> count_words('the quick brown fox')
    4
    >>> count_words('1 2 3 4 5 6')
    6
    """
    return len(string.split())

def read_file(filename):
    """Opens and reads file into string.

    filename    str input of filename to read

    returns     str output of contents of filename
    """
    string = []
    with open(filename, 'r') as file:
        for line in file:
            string.append(line.strip())
    return ' '.join(string)

def main(argv):
    """Main function"""

    help_text = """
Count Words in a String v1.0

Usage:
  python count_words_in_a_string.py [options] [filename]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(argv, "hts", ["help", "test", "stress"])
    except getopt.GetoptError:
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
    if args:
        try:
            print("Word Count: {}".format(count_words(read_file(args[0]))))
        except FileNotFoundError as err:
            print("Error: Cannot open {}.".format(args[0]))
            print(err)
    else:
        print(count_words(input("Enter a string to count words: ")))

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

