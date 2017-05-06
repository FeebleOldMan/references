#!/usr/bin/env python3

import sys, getopt

def main(argv):
    help = """CODE! v1.0

Usage:
  python CODE.py [options]

Options:

  -h, --help                help
  -t, --test                test
  -s, --stress              stress"""

    try:
        opts, args = getopt.getopt(argv, "hts", ["help", "test", "stress"])
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
        elif opt in ("-s", "--stress"):
            stress()
            sys.exit()
    rows, cols, seconds = map(int, input().strip().split())
    grid = []
    for _ in range(rows):
        grid.append(list(input().strip()))
    print(bomberman(rows, cols, seconds, grid))

### v0.2 try to optimize using plant and explode cycles
def bomberman(rows, cols, seconds, grid):
    explosion = ((-1, 0), (1, 0), (0, -1), (0, 1))
    # 3 = fresh bomb, -1 = nothing
    grid = [[3 if i == 'O' else -1 for i in row] for row in grid]
    grid_db = []
    tick = 0
    while tick < seconds:
        tick += 1
        # update grid
        exploded_cells = []
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    exploded_cells.append((i, j))
                    for boom in explosion:
                        cell = (i + boom[0], j + boom[1])
                        if (cell[0] < rows and cell[0] >= 0
                                and cell[1] < cols and cell[1] >= 0):
                            exploded_cells.append((cell[0], cell[1]))
                elif col > 1:
                    grid[i][j] -= 1
        # set bombs in empty cells if tick % 2 == 0
        if tick % 2 == 0:
            grid = [[3 if i == -1 else i for i in row] for row in grid]
        # blow up cells
        for cell in exploded_cells:
            grid[cell[0]][cell[1]] = -1
        grid_copy = tuple(tuple(row) for row in grid)
        if grid_copy not in grid_db:
            grid_db.append(grid_copy)
        else:
            grid_db = grid_db[grid_db.index(grid_copy):]  # trim to pattern
            break
    if seconds == tick:
        grid = grid_db[-1]
    else:
        grid = grid_db[(seconds-tick) % len(grid_db)]
    return grid_it(grid)


### v0.1 works but too slow
#def bomberman(rows, cols, seconds, grid):
#    explosion = ((-1, 0), (1, 0), (0, -1), (0, 1))
#    # 3 = fresh bomb, -1 = nothing
#    grid = [[3 if i == 'O' else -1 for i in row] for row in grid]
#    tick = 0
#    while tick < seconds:
#        tick += 1
#        # update grid
#        exploded_cells = []
#        for i, row in enumerate(grid):
#            for j, col in enumerate(row):
#                if col == 1:
#                    exploded_cells.append((i, j))
#                    for boom in explosion:
#                        cell = (i + boom[0], j + boom[1])
#                        if (cell[0] < rows and cell[0] >= 0
#                                and cell[1] < cols and cell[1] >= 0):
#                            exploded_cells.append((cell[0], cell[1]))
#                elif col > 1:
#                    grid[i][j] -= 1
#        # set bombs in empty cells if tick % 2 == 0
#        if tick % 2 == 0:
#            grid = [[3 if i == -1 else i for i in row] for row in grid]
#        # blow up cells
#        for cell in exploded_cells:
#            grid[cell[0]][cell[1]] = -1
#    return grid_it(grid)

def grid_it(grid):
    #grid = [['{:3d}'.format(i) for i in row] for row in grid]   #debug
    #grid = '\n'.join([(''.join(row)) for row in grid])
    grid = [['.' if i == -1 else 'O' for i in row] for row in grid]
    grid = '\n'.join([(''.join(row)) for row in grid])
    return grid

def test():
    print("TEST01:", "pass" if
        bomberman(6, 7, 3,
            [
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'O', '.', '.', '.'], 
                ['.', '.', '.', '.', 'O', '.', '.'], 
                ['.', '.', '.', '.', '.', '.', '.'], 
                ['O', 'O', '.', '.', '.', '.', '.'], 
                ['O', 'O', '.', '.', '.', '.', '.']
            ])
            ==
            (
                "OOO.OOO\n"
                "OO...OO\n"
                "OOO...O\n"
                "..OO.OO\n"
                "...OOOO\n"
                "...OOOO"
            )
            else "**FAIL**")
    
    print("TEST02:", "pass" if
        bomberman(6, 7, 7,
            [
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'O', '.', '.', '.'], 
                ['.', '.', '.', '.', 'O', '.', '.'], 
                ['.', '.', '.', '.', '.', '.', '.'], 
                ['O', 'O', '.', '.', '.', '.', '.'], 
                ['O', 'O', '.', '.', '.', '.', '.']
            ])
            ==
            (
                "OOO.OOO\n"
                "OO...OO\n"
                "OOO...O\n"
                "..OO.OO\n"
                "...OOOO\n"
                "...OOOO"
            )
            else "**FAIL**")

    print("TEST03:", "pass" if bomberman(1, 1, 11, [['O']]) 
            == (".") else "**FAIL**")

def stress():
    import random
    rows, cols, seconds  = 200, 200, 1000000000
    grid = [[random.choice(['.', 'O']) for col in range(cols)]
            for row in range(rows)]
    print(bomberman(rows, cols, seconds, grid))

if __name__ == '__main__':
    main(sys.argv[1:])

