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
    rows, cols = map(int, input().strip().split())
    grid = []
    for row in range(rows):
        grid.append(list(input().strip()))
    print(two_pluses(rows, cols, grid))

### pythonic answer
#from itertools import repeat, chain, combinations
#
## naive solution should work here -- itertools and composition for sanity preservation
#N, M = [int(x) for x in input().strip().split(' ')]
#grid = [[c == 'G' for c in input().strip()] for _ in range(N)]
#
#def all_plusses(i0, j0):
#    # edge coordinates of all plusses radiating from this location
#    # including the 1-square "plus"
#    return chain([[(i0, j0)]],
#                 zip(zip(range(i0+1, N), repeat(j0)), \
#                     zip(reversed(range(0, i0)), repeat(j0)), \
#                     zip(repeat(i0), range(j0+1, M)), \
#                     zip(repeat(i0), reversed(range(0, j0)))))
#
#def valid_plusses(i0, j0):
#    # yields sets of coordinates each describing a valid
#    # plus originating at (i0, j0)
#    coords = set()
#    for edge in all_plusses(i0, j0):
#        if all(grid[i][j] for i, j in edge):
#            coords.update(edge)
#            yield frozenset(coords)
#        else:
#            return
#
## finally generate all possible plusses
#poss_plusses = chain.from_iterable(valid_plusses(i, j) for i in range(N) for j in range(M))
#
## find the non-intersecting pair with the largest area product
## (we only need to remember the largest size)
#max_size = -1
#for p1, p2 in combinations(poss_plusses, 2):
#    if not (p1 & p2):
#        max_size = max(max_size, len(p1) * len(p2))
#        
#print(max_size)

def two_pluses(rows, cols, grid):
    # convert to G=1, B=0, easy to add area
    grid = [[1 if col == 'G' else 0 for col in row] for row in grid]
    pluses = []
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1)) # u, d, l, r
    # find all pluses
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col:
                plus = [(i, j)]
                pluses.append(plus[:])
                is_valid = True
                multiplier = 0
                while is_valid:
                    check_grids = []
                    multiplier += 1
                    for direction in directions:
                        check_box = (i + direction[0]*multiplier,
                                j + direction[1]*multiplier)
                        if (check_box[0] < 0 or check_box[0] >= rows
                                or check_box[1] < 0 or check_box[1] >= cols
                                or not grid[check_box[0]][check_box[1]]):
                            is_valid = False
                            break
                        else:
                            check_grids.append((check_box))
                    if is_valid:
                        plus.extend(check_grids)
                        pluses.append(plus[:])
    # find biggest non-overlapping permutation of products
    max_area = 0
    while pluses:
        current_plus = pluses.pop()
        current_size = len(current_plus)
        for plus in pluses:
            plus_size = len(plus)
            if current_size + plus_size == len(set(current_plus + plus)):
                if max_area < (current_size * plus_size):
                    max_area = current_size * plus_size
    return max_area

def test():
    test_set =  [
                    [5, 6, [
                        list(s) for s in [
                        'GGGGGG',
                        'GBBBGB',
                        'GGGGGG',
                        'GGBBGB',
                        'GGGGGG'
                        ]
                           ]
                    ],
                    [6, 6, [
                        list(s) for s in [
                        'BGBBGB',
                        'GGGGGG',
                        'BGBBGB',
                        'GGGGGG',
                        'BGBBGB',
                        'BGBBGB'
                        ]
                           ]
                    ],
                    [2, 2, [
                        list(s) for s in [
                            'BB',
                            'BB',
                            ]
                        ]
                    ],
                    [2, 2, [
                        list(s) for s in [
                            'GG',
                            'GG',
                            ]
                        ]
                    ],
                    [5, 6, [
                        list(s) for s in [
                        'BBBBBB',
                        'BBBBBB',
                        'BBBBBB',
                        'BBBBBB',
                        'BBBBBB'
                        ]
                           ]
                    ],
                    [3, 3, [
                        list(s) for s in [
                            'GGG',
                            'GGG',
                            'GGG',
                            ]
                        ]
                    ],
                    [5, 6, [
                        list(s) for s in [
                        'GGGGGG',
                        'GGGGGG',
                        'GGGGGG',
                        'GGGGGG',
                        'GGGGGG'
                        ]
                           ]
                    ],
                    [15, 15, [
                        list(s) for s in [
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        'GGGGGGGGGGGGGGG',
                        ]
                           ]
                    ],
                    [15, 15, [
                        list(s) for s in [
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        ]
                           ]
                    ],
                    [15, 15, [
                        list(s) for s in [
                        'BGBBBBBBBBBBBBB',
                        'GGGBBBBBBBBBBBB',
                        'BGBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        'BBBBBBBBBBBBBBB',
                        ]
                           ]
                    ],
                    [12, 12, [
                        list(s) for s in [
                        'GGGGGGGGGGGG',
                        'GBGGBBBBBBBG',
                        'GBGGBBBBBBBG',
                        'GGGGGGGGGGGG',
                        'GGGGGGGGGGGG',
                        'GGGGGGGGGGGG',
                        'GGGGGGGGGGGG',
                        'GBGGBBBBBBBG',
                        'GBGGBBBBBBBG',
                        'GBGGBBBBBBBG',
                        'GGGGGGGGGGGG',
                        'GBGGBBBBBBBG',
                        ]
                            ]
                    ],
                    [12, 12, [
                        list(s) for s in [
                        'GGGGGGGGGGGG',
                        'GBGGBBBBBBBG',
                        'GBGGBBBBBBBG',
                        'GGGGGGGGGGGG',
                        'GGGGGGGGGGGG',
                        'GGGGGGGGGGGG',
                        'GGGGGGGGGGGG',
                        'GBGGBBBBBBBG',
                        'GBGGBBBBBBBG',
                        'GBGGBBBBBBBG',
                        'GGGGGGGGGGGG',
                        'GBGGBBBBBBBG',
                        ]
                            ]
                    ],

                 ]
    test_ans = [5, 25, 0, 1, 0, 5, 25, 377, 0, 1, 81, 81]
    for t in range(len(test_set)):
        print("TEST{:02d}:".format(t), "pass" 
            if two_pluses(*test_set[t]) == test_ans[t] else ("**FAIL**",
                two_pluses(*test_set[t])))

if __name__ == '__main__':
    main(sys.argv[1:])

