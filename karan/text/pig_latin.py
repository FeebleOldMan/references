#!/usr/bin/env python3
"""Pig Latin

Transposes initial consonant sound to the end of the word and appends 'ay'.
Rules can be seen at:
https://en.wikipedia.org/wiki/Pig_latin
"""

import sys
import getopt

def pig_latinize(sentence):
    """Converts sentence to pig latin.

    All consonants before first vowel of each word is shifted to the end of the
    word. '-ay' is appended to the word.
    If the word starts with a vowel, '-way' is appended to the word.

    sentence        string to pig latinize
    return          string sentence in pig latin

    >>> pig_latinize('a for apple')
    'away orfay appleway'
    >>> pig_latinize('b for banana')
    'bay orfay ananabay'
    """
    VOWELS = ('a', 'e', 'i', 'o', 'u',)

    sentence = sentence.split()
    for i, word in enumerate(sentence):
        if word.startswith(VOWELS):
            word += 'way'
        else:
            for j, letter in enumerate(word):
                if letter in VOWELS:
                    word = word[j:] + word[:j] + 'ay'
                    break
            else:
                word += 'ay'
        sentence[i] = word
    sentence = ' '.join(sentence)
    return sentence

def main(argv):
    """Main function"""

    help_text = """
Pig Latin v1.0

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
    sentence = input("Enter sentence to pig latinize: ")
    print(pig_latinize(sentence))

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

