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
    clouds, distance = map(int, input().strip().split())
    cloud_map = list(map(int, input().strip().split()))
    print(fuel_left(clouds, distance, cloud_map))

def fuel_left(clouds, distance, cloud_map):
    pos = 0
    energy = 100
    while True:
        pos = (pos + distance) % clouds
        energy -= 1 + (2 * cloud_map[pos])
        if pos == 0:
            return energy

def test():
    print("TEST01:", "pass" if fuel_left(8, 2, [0, 0, 1, 0, 0, 1, 1, 0])
            == 92 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

