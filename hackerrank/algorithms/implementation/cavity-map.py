#!/usr/bin/env python

TEST_MODE = True 

def main():
    map_grid = []
    for _ in range(int(raw_input().strip())):
        map_grid.append(map(int, list(raw_input().strip())))
    find_cavities(map_grid)

def find_cavities(map_grid):
    map_out = map_grid[:]
    for i, row in enumerate(map_grid[1:-1], start=1):
        for j, col in enumerate(map_grid[i][1:-1], start=1):
            if (map_grid[i-1][j] < col and
               map_grid[i][j-1] < col and
               map_grid[i][j+1] < col and
               map_grid[i+1][j] < col):
               map_out[i][j] = 'X'
    map_out = [[str(col) for col in row] for row in map_out]
    #map_out = map('\n'.join, (map(''.join, (row for row in map_out))))
    for row in map_out:
        print ''.join(row)
    return

def test():
    map_grid = [[1,1,1,2],[1,9,1,2],[1,8,9,2],[1,2,3,4]]
    find_cavities(map_grid)

test() if TEST_MODE else main()
