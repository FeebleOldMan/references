#!/usr/bin/env python3
"""Python module template"""

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
    int(input())  # num_players
    scoreboard = list(map(int, input().strip().split()))
    int(input())    # level_ups
    player_scores = list(map(int, input().strip().split()))
    track_rank(scoreboard, player_scores)

def track_rank(scoreboard, player_scores):
    """Tracks ranking of player. Returns player rank for each completed level.

    >>> track_rank([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
    6
    4
    2
    1
    """
    rankboard = sorted(set(scoreboard))
    rank_count = len(rankboard)
    pos = 0
    for score in player_scores:
        while pos < rank_count and score >= rankboard[pos]:
            pos += 1
        print(rank_count + 1 - pos)

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

