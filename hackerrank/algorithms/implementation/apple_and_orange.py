#!/usr/bin/env python3

import sys, getopt

def main(argv):
    help = """Apple and Orange v1.0

Usage:
  python apple_and_orange.py [options]

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
    # get inputs
    house = list(map(int, input().strip().split()))
    apple_tree, orange_tree = map(int, input().strip().split())
    apple_num, orange_num = map(int, input().strip().split())
    apple_dist = list(map(int, input().strip().split()))
    orange_dist = list(map(int, input().strip().split()))
    # call function
    print(house_fruits(house, apple_tree, orange_tree,
                       apple_dist, orange_dist))

def house_fruits(house, apple_tree, orange_tree, apple_dist, orange_dist): 
    apple_hits = [(apple + apple_tree >= house[0]
            and apple + apple_tree <= house[1])
            for apple in apple_dist].count(True)
    orange_hits = [(orange + orange_tree <= house[1]
            and orange + orange_tree >= house[0])
            for orange in orange_dist].count(True)
    return "{}\n{}".format(apple_hits, orange_hits)

def test():
    print('TEST01:', 'pass' 
          if house_fruits([7, 11], 5, 15, [-2, 2, 1], [5, -6]) == "1\n1"
          else '**FAIL**')

if __name__ == '__main__':
    main(sys.argv[1:])


