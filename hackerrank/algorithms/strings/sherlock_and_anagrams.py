#!/usr/bin/env python3

import sys, getopt
from itertools import combinations, combinations_with_replacement
from collections import Counter

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
    for _ in range(int(input())):
        print(count_pairs(input()))

def count_pairs(string):
    count = 0
    pos_pairs = list(combinations_with_replacement(range(len(string)), 2))
    counter_list = []
    for x, y in pos_pairs:
        counter_list.append(Counter(string[x:y+1]))
    for n, i in enumerate(counter_list):
        for j in counter_list[n+1:]:
            if i == j:
                count += 1
    return count

### v0.4 works, but too slow
#def count_pairs(string):
#    count = 0
#    pos_pairs = list(combinations_with_replacement(range(len(string)), 2))
#    for n, i in enumerate(pos_pairs):
#        for j in pos_pairs[n+1:]:
#            if (i[1] - i[0]) == (j[1] - j[0]):
#                is_valid = True
#                str1, str2 = list(string[i[0]:i[1]+1]), list(string[j[0]:j[1]+1])
#                for l in str1:
#                    try:
#                        str2.remove(l)
#                    except:
#                        is_valid = False
#                        break
#                if is_valid:
#                    count += 1
#    return count

### The indexes indicate range of letters across string, not a pair
### v0.3 slow
#def count_pairs(string):
#    count = 0
#    pos_pairs = combinations_with_replacement(range(len(string)), 2)
#    pairs_of_pairs = combinations(pos_pairs, 2)
#    for i, j in pairs_of_pairs:
#        if Counter(string[i[0]:i[1]+1]) == Counter(string[j[0]:j[1]+1]):
#            count += 1
#    return count

### v0.2 bug. this is double counting
#def count_pairs(string):
#    string = list(string)
#    count = 0
#    # pop item out from string before doing second combi
#    first_pairs = combinations_with_replacement(range(len(string)), 2)
#    for pair in first_pairs:
#        leftovers = string[:]
#        pair = sorted(set(pair), reverse = True)
#        for i in pair:
#            leftovers.pop(i)
#        second_pairs = combinations_with_replacement(leftovers, 2)
#        for second_pair in second_pairs:
#            if set([string[pair[0]], string[pair[-1]]]) == set(second_pair):
#                count += 1
#    return count

### v0.1 bug
#def count_pairs(string):
#    count = 0
#    pos_pairs = combinations_with_replacement(range(len(string)), 2)
#    pairs_of_pairs = combinations(pos_pairs, 2)
#    for pair in pairs_of_pairs:
#        # check unique
#        if pair[0][0] not in pair[1] and pair[0][1] not in pair[1]:  
#            if (set([string[pair[0][0]], string[pair[0][1]]]) ==
#                    set([string[pair[1][0]], string[pair[1][1]]])):
#                count += 1
#    print(count)
#    return count

def test():
    print("TEST01:", "pass" if count_pairs('abba') == 4 else "**FAIL**")
    print("TEST02:", "pass" if count_pairs('abcd') == 0 else "**FAIL**")
    print("TEST03:", "pass" if count_pairs('ifailuhkqq') == 3 else "**FAIL**")
    print("TEST04:", "pass" if count_pairs('hucpoltgty') == 2 else "**FAIL**")
    print("TEST05:", "pass" if count_pairs('ovarjsnrbf') == 2 else "**FAIL**")
    print("TEST06:", "pass" if count_pairs('pvmupwjjjf') == 6 else "**FAIL**")
    print("TEST07:", "pass" if count_pairs("iwwhrlkpek") == 3 else "**FAIL**")
    random_text()

def random_text():
    from random import choice 
    from string import ascii_lowercase
    test_list = [''.join(choice(ascii_lowercase) for _ in range(100))
            for _ in range(10)]
    for test in test_list:
        print(test, count_pairs(test))

if __name__ == '__main__':
    main(sys.argv[1:])


##!/usr/bin/env python2
#
#TEST_MODE = True
#
#def main():
#  for _ in range(int(raw_input().strip())):
#    print sub_count(string)
#
#def sub_count(string):
#  count = 0
#  for i in range(len(string)):
#    for j in range(i, len(string)+1):
#
#  return count
#
#def test():
#  print "TEST01:", "pass" if sub_count('abba') == 4 else "**FAIL**"
#  print "TEST02:", "pass" if sub_count('abcd') == 0 else "**FAIL**"
#  print "TEST03:", "pass" if sub_count('ifailuhkqq') == 3 else "**FAIL**"
#  print "TEST04:", "pass" if sub_count('hucpoltgty') == 2 else "**FAIL**"
#  print "TEST05:", "pass" if sub_count('ovarjsnrbf') == 2 else "**FAIL**"
#  print "TEST06:", "pass" if sub_count('pvmupwjjjf') == 6 else "**FAIL**"
#  print "TEST07:", "pass" if sub_count('iwwhrlkpek') == 3 else "**FAIL**"
#
#test() if TEST_MODE else main()
