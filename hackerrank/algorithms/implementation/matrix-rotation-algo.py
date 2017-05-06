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
    rows, cols, steps = map(int, input().strip().split())
    matrix = [input().strip().split() for _ in range(rows)]
    print(rotate(rows, cols, steps, matrix))

def rotate(rows, cols, steps, matrix):
    # find corners and work way inwards to middle
    layers = min(rows, cols) // 2
    # ul, ur, lr, ll
    corner_directions = ((1, 1), (1, -1), (-1, -1), (-1, 1))
    anchors = [[0, 0], [0, cols-1], [rows-1, cols-1], [rows-1, 0]] 
    clockwise_directions = ((0, 1), (1, 0), (0, -1), (-1, 0)) # r, d, l, u
    rotated = [[None for _ in range(cols)] for _ in range(rows)]
    for layer in range(layers):
        # transform each layer into array and shift steps, then put back 
        inward_steps = [(x*layer, y*layer) for x, y in corner_directions]
        inward_anchors = [[anchor[0]+step[0], anchor[1]+step[1]] for anchor, step 
                in zip(anchors, inward_steps)]
        flattened_layer = []
        for i, anchor in enumerate(inward_anchors):
            cell = anchor[:]
            while cell != inward_anchors[-3+i]:  # check if reached anchor corner
                flattened_layer.append(cell[:])
                cell[0] += clockwise_directions[i][0]  # stepwise clockwise
                cell[1] += clockwise_directions[i][1]
        # rotate flattened layer by steps
        layer_steps = steps % len(flattened_layer)
        rotated_layer = (flattened_layer[layer_steps:]
                + flattened_layer[:layer_steps])
        # place matrix values into rotated for each rotated_layer
        for cell, target in zip(flattened_layer, rotated_layer):
            rotated[cell[0]][cell[1]] = matrix[target[0]][target[1]]
    rotated = '\n'.join([' '.join(row) for row in rotated])
    return rotated

def test():
    print("TEST01:", "pass" if rotate(4, 4, 1, 
        [['1', '2', '3', '4'], 
         ['5', '6', '7', '8'], 
         ['9', '10', '11', '12'],
         ['13', '14', '15', '16']]
        )
        ==
        ('2 3 4 8\n'
         '1 7 11 12\n'
         '5 6 10 16\n'
         '9 13 14 15')
        else "**FAIL**")
    print("TEST02:", "pass" if rotate(4, 4, 2, 
        [['1', '2', '3', '4'], 
         ['5', '6', '7', '8'], 
         ['9', '10', '11', '12'],
         ['13', '14', '15', '16']]
        )
        ==
        ('3 4 8 12\n'
         '2 11 10 16\n'
         '1 7 6 15\n'
         '5 9 13 14')
        else "**FAIL**")
    print("TEST03:", "pass" if rotate(5, 4, 7, 
        [['1', '2', '3', '4'], 
         ['7', '8', '9', '10'], 
         ['13', '14', '15', '16'],
         ['19', '20', '21', '22'],
         ['25', '26', '27', '28']]
        )
        ==
        ('28 27 26 25\n'
         '22 9 15 19\n'
         '16 8 21 13\n'
         '10 14 20 7\n'
         '4 3 2 1')
        else "**FAIL**")
    print("TEST04:", "pass" if rotate(2, 2, 3, 
        [['1', '1'], 
         ['1', '1']]
        )
        ==
        ('1 1\n' 
         '1 1')
        else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

##### OLD PYTHON2 VERSION
##!/usr/bin/env python2
#
#TEST_MODE = False
#
#def main():
#  rows, cols, steps = map(int, raw_input().strip().split())
#  matrix = [raw_input().strip().split() for _row in range(rows)]
#  print rotate(rows, cols, steps, matrix)
#  return
#
#def rotate(rows, cols, steps, matrix):
#  # move by step except for X in matrix
#  # figure out where corners are by taking min of rows and cols
#  rotated = list(matrix)
#  for step in range(steps):
#    before = list(rotated)
#    for row in range(rows):
#      for col in range(cols):
#        if col === row:
#          rotated[row][col+1] = before[row][col]
#        elif 
#  return rotated
#
#def test():
#  return
#
#test() if TEST_MODE else main()
