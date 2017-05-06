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
    num_items, item_idx = map(int, input().strip().split())
    costs = list(map(int, input().strip().split()))
    charge = int(input())
    print(check_please(num_items, item_idx, costs, charge))

def check_please(num_items, item_idx, costs, charge):
    actual_charge = (sum(costs) - costs[item_idx])//2
    return("Bon Appetit" if charge == actual_charge
            else (charge - actual_charge))

def test():
    print("TEST01:", "pass" if check_please(4, 1, [3, 10, 2, 9], 12) == 5
            else "**FAIL**")
    print("TEST02:", "pass" 
            if check_please(4, 1, [3, 10, 2, 9], 7) == "Bon Appetit" 
            else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

