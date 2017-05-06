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
    board_size, num_obstacles = map(int, input().strip().split())
    queen_pos = list(map(int, input().strip().split()))
    obs_pos = [list(map(int, input().strip().split())) for _ in
               range(num_obstacles)]
    print(count_squares(board_size, queen_pos, obs_pos))

def count_squares(board_size, queen_pos, obs_pos):
    """Given the queen's position and the locations of all the obstacles, find
    and print the number of squares the queen can attack from her position.

    >>> count_squares(4, [4, 4], [])
    9
    >>> count_squares(5, [4, 3], [[5,5], [4,2], [2,3]])
    10
    >>> count_squares(1, [1, 1], [])
    0
    >>> count_squares(2, [1, 1], [])
    3
    >>> count_squares(3, [1, 1], [[1,2], [2,2], [2,1]])
    0
    >>> count_squares(3, [2, 2], [])
    8
    >>> count_squares(3, [1, 1], [[1,2], [2,1]])
    2
    >>> count_squares(3, [1, 1], [[1,2], [2,1], [3,3], [2,2]])
    0
    >>> count_squares(3, [1, 1], [[1,2], [2,1], [3,3]])
    1
    """
    end_points = {(-1.0, 0.0): None,
                  (-1.0, 1.0): None,
                  (0.0, 1.0): None,
                  (1.0, 1.0): None,
                  (1.0, 0.0): None,
                  (1.0, -1.0): None,
                  (0.0, -1.0): None,
                  (-1.0, -1.0): None,
                 }
    # set full end points
    for direction in end_points.keys():
        end_point = queen_pos[:]
        max_steps = [board_size, board_size]
        for i, j in enumerate(direction):
            if j == 1.0:
                max_steps[i] = board_size - queen_pos[i]
            elif j == -1.0:
                max_steps[i] = queen_pos[i] - 1
        max_steps = min(max_steps)
        for i, j in enumerate(direction):
            if j == 1.0:
                end_point[i] += max_steps
            elif j == -1.0:
                end_point[i] -= max_steps
        end_points[direction] = end_point
    # replace end points with obstacles
    for obs in obs_pos:
        vector_list = [obs[0] - queen_pos[0], obs[1] - queen_pos[1]]
        max_vector = max([abs(obs[0] - queen_pos[0]),
                          abs(obs[1] - queen_pos[1])])
        vector = tuple([x / max_vector for x in vector_list])
        if vector in end_points.keys():
            # check if obs is closer to queen_pos
            obs_dist = max(abs(obs[0] - queen_pos[0]),
                           abs(obs[1] - queen_pos[1])
                          ) - 1
            end_point_dist = max(abs(end_points[vector][0] - queen_pos[0]),
                                 abs(end_points[vector][1] - queen_pos[1]),
                                )
            if obs_dist < end_point_dist:
                end_points[vector] = [obs[0] - vector[0],
                                      obs[1] - vector[1]
                                     ]
    count = 0
    for direction in end_points.values():
        count += int(max(abs(direction[0] - queen_pos[0]),
                         abs(direction[1] - queen_pos[1])))
    return count

'''
    ### v0.1 bug. obstacles in same vector will not be counted
    # clockwise from up
    directions = [[-1.0, 0.0],
                  [-1.0, 1.0],
                  [0.0, 1.0],
                  [1.0, 1.0],
                  [1.0, 0.0],
                  [1.0, -1.0],
                  [0.0, -1.0],
                  [-1.0, -1.0],
                 ]
    valid_directions = []
    to_pop = set()
    for obs in obs_pos:
        vector = [obs[0] - queen_pos[0], obs[1] - queen_pos[1]]
        max_vector = max([abs(obs[0] - queen_pos[0]),
                          abs(obs[1] - queen_pos[1])])
        vector = [x / max_vector for x in vector]
        if vector in directions:
            to_pop.add(vector)
            valid_directions.append(obs)
    for vector in to_pop:
        directions.pop(directions.index(vector))
    count = 0 - len(valid_directions)
    for direction in directions:
        valid_direction = queen_pos[:]
        max_steps = [board_size, board_size]
        for i, j in enumerate(direction):
            if j == 1.0:
                max_steps[i] = board_size - valid_direction[i]
            elif j == -1.0:
                max_steps[i] = valid_direction[i] - 1
        max_steps = min(max_steps)
        for i, j in enumerate(direction):
            if j == 1.0:
                valid_direction[i] += max_steps
            elif j == -1.0:
                valid_direction[i] -= max_steps
        valid_directions.append(valid_direction)
    for direction in valid_directions:
        count += max(abs(direction[0] - queen_pos[0]),
                     abs(direction[1] - queen_pos[1]))
    return count
'''

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

