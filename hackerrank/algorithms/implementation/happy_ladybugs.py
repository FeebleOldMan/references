#!/usr/bin/env python3

import sys, getopt
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
        num_cells = int(input())
        board = input().strip()
        print(happy_ladybugs(num_cells, board))

def happy_ladybugs(num_cells, board):
    bugs = Counter(board)
    are_happy = 'YES'
    if not bugs.pop('_', None) and len(bugs) > 1:
        # yes if board is already in order
        board = list(board)
        cell1, cell2 = board.pop(), None
        chain = 1
        while board:
            cell2, cell1 = cell1, board.pop()
            if cell1 == cell2:
                chain += 1
            else:
                if chain == 1:
                    are_happy = 'NO'
                    break
                else:
                    chain = 1
    else:
        for count in bugs.values():
            if count <= 1:
                are_happy = 'NO'
                break
    return are_happy

def test():
    print("TEST01:", "pass" if happy_ladybugs(7, 'RBY_YBR') == 'YES' else "**FAIL**")
    print("TEST02:", "pass" if happy_ladybugs(6, 'X_Y__X') == 'NO' else "**FAIL**")
    print("TEST03:", "pass" if happy_ladybugs(2, '__') == 'YES' else "**FAIL**")
    print("TEST04:", "pass" if happy_ladybugs(6, 'B_RRBR') == 'YES' else "**FAIL**")
    print("TEST05:", "pass" if happy_ladybugs(6, 'BBRRBR') == 'NO' else "**FAIL**")
    print("TEST06:", "pass" if happy_ladybugs(6, 'BBBBBR') == 'NO' else "**FAIL**")
    print("TEST07:", "pass" if happy_ladybugs(6, 'BBBBBB') == 'YES' else "**FAIL**")
    print("TEST08:", "pass" if happy_ladybugs(2, 'BB') == 'YES' else "**FAIL**")
    print("TEST09:", "pass" if happy_ladybugs(1, 'B') == 'NO' else "**FAIL**")
    print("TEST10:", "pass" if happy_ladybugs(1, '_') == 'YES' else "**FAIL**")
    print("TEST11:", "pass" if happy_ladybugs(5, '_____') == 'YES' else "**FAIL**")
    print("TEST12:", "pass" if happy_ladybugs(5, '__A__') == 'NO' else "**FAIL**")
    print("TEST13:", "pass" if happy_ladybugs(5, 'AAABB') == 'YES' else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

