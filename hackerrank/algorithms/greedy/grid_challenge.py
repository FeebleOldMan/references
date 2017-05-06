#!/usr/bin/env python3

for _ in range(int(input())):
    result = "YES"
    grid = [list(col) for col in zip(*[sorted(list(input())) for _ in range(int(input()))])]
    for row in grid:
        if row != sorted(row):
            result = "NO"
            break
    print(result)

### v0.1 no numpy allowed
#import numpy
#
#for _ in range(int(input())):
#    result = "YES"
#    grid = numpy.array([sorted(input().strip().split()) for _ in range(int(input()))])
#    grid.transpose()
#    for row in grid:
#        if row != sorted(row):
#            result = "NO"
#            break
#    print(result)
