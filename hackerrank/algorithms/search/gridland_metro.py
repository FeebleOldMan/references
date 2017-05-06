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
    rows, cols, num_tracks = map(int, input().strip().split())
    tracks = []
    for _ in range(num_tracks):
        tracks.append(list(map(int, input().strip().split())))
    print(count_lampposts(rows, cols, num_tracks, tracks))

def count_lampposts(rows, cols, num_tracks, tracks):
    track_map = {}
    for row, start, end in tracks:
        track_map[row] = track_map.setdefault(row, [])
        track_map[row].append([start, end])
    # merge tracks
    for row, values in track_map.items():
        track_map[row] = sorted(values)
    for r in track_map.keys():
        row = track_map[r]
        print("row", row)
        if len(row) > 1:
            changed = True
            while changed:
                changed = False
                updated_row = []
                print(row)
                input()
                for track1, track2 in zip(row[:-1], row[1:]):
                    if track1[0] <= track2[0] <= track1[1]:
                        updated_row.append([track1[0], max(track1[1],
                            track2[1])])
                        changed = True
                    else:
                        # bug here
                        updated_row.append(track1)
                if len(row) > 1 and not row[-2][0] <= row[-1][0] <= row[-2][1]:
                    updated_row.append(row[-1])
                row = updated_row[:]
            track_map[r] = row[:]
    print(track_map)
    #lampposts = rows * cols - sum([len(cells) for cells in track_map.values()])
    #return lampposts

### v0.2 too much memory
#def count_lampposts(rows, cols, num_tracks, tracks):
#    track_map = {}
#    for row, start, end in tracks:
#        track_map[row] = track_map.get(row, set())|set([col for col in
#            range(start-1, end)])
#    lampposts = rows * cols - sum([len(cells) for cells in track_map.values()])
#    return lampposts

### v0.1 too much memory
#def count_lampposts(rows, cols, num_tracks, tracks):
#    grid = [[1 for _ in range(cols)] for _ in range(rows)]
#    for row, start, end in tracks:
#        for i in range(start-1, end):
#            grid[row-1][i] = 0
#    lampposts = sum([sum(row) for row in grid])
#    return lampposts

def test():
    print("TEST01:", "pass" if count_lampposts(4, 4, 3, 
        [[2, 2, 3],
         [3, 1, 4],
         [4, 4, 4]]) == 9 else "**FAIL**")

    print("TEST02:", "pass" if count_lampposts(4, 4, 3, 
        [[2, 2, 3],
         [3, 1, 4],
         [3, 4, 4]]) == 13 else "**FAIL**")

    print("TEST03:", "pass" if count_lampposts(4, 4, 3, 
        [[2, 2, 3],
         [2, 3, 4],
         [3, 4, 4]]) == 12 else "**FAIL**")

    print("TEST04:", "pass" if count_lampposts(5, 5, 3, 
        [[1, 1, 3],
         [1, 2, 4],
         [1, 3, 3]]) == 21 else "**FAIL**")

    print("TEST05:", "pass" if count_lampposts(10, 10, 3, 
        [[1, 1, 5],
         [1, 2, 4],
         [1, 7, 9]]) == 92 else "**FAIL**")


if __name__ == '__main__':
    main(sys.argv[1:])

