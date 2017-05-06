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
    cities, stations = map(int, input().strip().split())
    station_idx = list(map(int, input().strip().split()))
    print(max_dist(cities, stations, station_idx))

### v0.2 use the list of station_idx to figure out max dist
def max_dist(cities, stations, station_idx):
    dist = []
    if stations == 1:
        dist.extend([station_idx[0] - 0,
            cities - 1 - station_idx[0]])
    else:
        station_idx.sort()
        station_a, station_b = None, None
        for station in station_idx:
            if station_a is None:
                station_a = station
                dist.append(station_a)
                continue
            if station_b is None:
                station_b = station
            else:
                station_a, station_b = station_b, station
            dist.append((station_b - station_a) // 2)
        dist.append(cities - 1 - station_b)
    return max(dist) 

### v0.1 slow
#def max_dist(cities, stations, station_idx):
#    station_idx.sort()
#    dist = []
#    for city in range(cities):
#        dist.append(min([abs(city - station) for station in station_idx]))
#    return max(dist)

def test():
    print("TEST01:", "pass" if max_dist(5, 2, [0, 4]) == 2 else "**FAIL**")
    print("TEST02:", "pass" if max_dist(6, 6, [0, 1, 2, 4, 3, 5]) == 0 else "**FAIL**")
    print("TEST03:", "pass" if max_dist(5, 1, [0]) == 4 else "**FAIL**")
    print("TEST04:", "pass" if max_dist(5, 1, [2]) == 2 else "**FAIL**")
    print("TEST05:", "pass" if max_dist(10, 3, [0, 1, 2]) == 7 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

