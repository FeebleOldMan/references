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
    for _ in range(int(input())):
        quad_size = int(input())
        matrix = [list(map(int, input().strip().split())) for _ in range(2
            * quad_size)]
        print(optimize_quad(quad_size, matrix))

def optimize_quad(quad_size, matrix):
    score = 0
    for i in range(quad_size):
        for j in range(quad_size):
            score += max(matrix[i][j], matrix[i][-j-1], matrix[-i-1][-j-1],
                    matrix[-i-1][j])
    return score

### v0.1 bug. wrong algorithm
#def optimize_quad(quad_size, matrix):
#    # compare halves of each col and flip high to top
#    matrix = list(zip(*matrix))       # transpose matrix
#    print(matrix)
#    for i, col in enumerate(matrix):
#        if sum(col[:quad_size]) < sum(col[quad_size:]): # top < btm
#            matrix[i] = matrix[i][::-1]                 # flip
#    # compare halves of each row and flip high to left
#    matrix = list(zip(*matrix))       # untranspose matrix
#    print(matrix)
#    for i, row in enumerate(matrix[:quad_size]):
#        if sum(row[:quad_size]) < sum(row[quad_size:]):
#            matrix[i] = matrix[i][::-1]
#    score = sum(sum(row[:quad_size]) for row in matrix[:quad_size])
#    print(matrix)
#    print(score)
#    return score

def test():
    print("TEST01:", "pass" if optimize_quad(2, 
        [[112, 42, 83, 119],
         [56, 125, 56, 49],
         [15, 78, 101, 43],
         [62, 98, 114, 108]]) == 414 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

