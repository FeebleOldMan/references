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
    len_str = int(input())
    string = input()
    print(two_chars(len_str, string))

def two_chars(len_str, string):
    from itertools import combinations
    string = list(string)
    letters = list(set(string))
    max_length = 0
    letter_combos = combinations(letters, 2)
    for combo in letter_combos:
        test_str = [l for l in string if l in combo]
        len_test = len(test_str)
        is_valid = True
        for l in range(len_test - 1):
            if test_str[l] == test_str[l+1]:
                is_valid = False
        if is_valid and len_test > max_length:
            max_length = len_test
    return max_length

def test():
    print("TEST01:", "pass" if two_chars(10, 'beabeefeab') == 5 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

