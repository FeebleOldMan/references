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
    num_houses, transmit_range = map(int, input().strip().split())
    houses = list(map(int, input().strip().split()))
    print(min_transmitters(num_houses, transmit_range, houses))

### v1.0
def min_transmitters(num_houses, transmit_range, houses):
    count = 1
    houses = sorted(set(houses))
    base_house, candidate_house = houses[0], houses[0]
    for house in houses[1:]:
        if house <= base_house + transmit_range:
            candidate_house = house
        elif house > candidate_house + transmit_range:
            count += 1
            base_house = house
    return count

### v0.5 fast but buggy
#def min_transmitters(num_houses, transmit_range, houses):
#    count = 0
#    houses = sorted(set(houses))
#    base_house, candidate_house = houses[0], houses[0]
#    for house in houses[1:]:
#        if house <= base_house + transmit_range:
#            candidate_house = house
#        elif house > candidate_house + transmit_range:
#            count += 1
#            base_house = house
#    if base_house == houses[-1] or candidate_house == houses[-1]:
#        count += 1
#    return count

### v0.4 correct but too slow
#def min_transmitters(num_houses, transmit_range, houses):
#    count = 0
#    houses = sorted(set(houses))
#    house_map = ''.join(['1' if house in houses else '0'
#        for house in range(houses[0], houses[-1] + 1)])
#    while house_map:
#        try:
#            furthest_house = house_map[:transmit_range + 1].rindex('1')
#            count += 1
#            house_map = house_map[furthest_house + transmit_range + 1:]
#            house_map = house_map[house_map.index('1'):]
#        except:
#            try:
#                house_map = house_map[house_map.index('1'):]
#            except:
#                break
#    return count

# switch to string for rindex?
### v0.3 correct but too slow
#def min_transmitters(num_houses, transmit_range, houses):
#    count = 0
#    houses = sorted(set(houses))
#    house_map = [1 if house in houses else 0 for house in range(houses[0],
#        houses[-1] + 1)]
#    while house_map:
#        try:
#            chunk = house_map[:transmit_range + 1]
#            furthest_house = (len(chunk)
#                - house_map[transmit_range::-1].index(1) - 1)
#            count += 1
#            house_map = house_map[furthest_house + transmit_range + 1:]
#            house_map = house_map[house_map.index(1):]
#        except:
#            try:
#                house_map = house_map[house_map.index(1):]
#            except:
#                break
#    return count

### v0.2 too slow and buggy
#def min_transmitters(num_houses, transmit_range, houses):
#    count = 0
#    chunk = 2 * transmit_range + 1
#    houses = sorted(set(houses))
#    while houses:
#        count += 1
#        starting_house = houses[0]
#        for n in range(chunk):
#            if starting_house + n in houses:
#                houses.remove(starting_house + n)
#    return count

### v0.1 too slow and buggy
#def min_transmitters(num_houses, transmit_range, houses):
#    count = 0
#    chunk = 2 * transmit_range + 1
#    houses.sort()
#    while houses:
#        count += 1
#        starting_house = houses[0]
#        for n in range(chunk):
#            if starting_house + n in houses:
#                houses.remove(starting_house + n)
#    return count

def test():
    print("TEST01:", "pass" if min_transmitters(5, 1, [1, 2, 3, 4, 5])
            == 2 else "**FAIL**")
    print("TEST02:", "pass" if min_transmitters(8, 2, 
        [7, 2, 4, 6, 5, 9, 12, 11]) == 3 else "**FAIL**")
    print("TEST03:", "pass" if min_transmitters(9, 2, 
        [7, 2, 9, 5, 4, 2, 6, 15, 12]) == 4 else "**FAIL**")
    print("TEST04:", "pass" if min_transmitters(8, 2,
        [9, 5, 4, 2, 6, 15, 11, 12]) == 3 else "**FAIL**")
    print("TEST05:", "pass" if min_transmitters(1, 1, [1])
            == 1 else "**FAIL**")
    print("TEST06:", "pass" if min_transmitters(3, 1, [1, 2, 3])
            == 1 else "**FAIL**")
    print("TEST07:", "pass" if min_transmitters(4, 1, [1, 2, 3, 10])
            == 2 else "**FAIL**")
    print("TEST08:", "pass" if min_transmitters(5, 1, 
        [1, 2, 3, 10, 11]) == 2 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

