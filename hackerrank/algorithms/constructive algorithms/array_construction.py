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
    for _ in rannge(int(input())):
        len_arr, sum_arr, sum_diff = map(int, input().strip().split())
        print(make_arr(len_arr, sum_arr, sum_diff))

def make_arr(len_arr, sum_arr, sum_diff):
    from itertools import combinations
    # start with equally distributed array
    results = [sum_arr // len_arr for _ in range(len_arr)]
    results[-1] += sum_arr % len_arr
    arr_diff = (sum_arr % len_arr) * (len_arr - 1)
    # adjust front downwards and back upwards until fit requirements
    # TODO: figure out stop trigger. abs diff between diffs increase instead of
    # decrease?
    while arr_diff != sum_diff:
        for i, num in enumerate(results):
            if num:
                results[i] -= 1
                # TODO: where to put removed value?
                # position will affect how much diff
                results[-1] += 1 # this is wrong
                break
        arr_combinations = combinations(results, 2)
        arr_diff = sum([abs(combi[0] - combi[1]) for combi in arr_combinations])
    # make results into string
    results = ' '.join(map(str, results))
    print(arr_diff, '|', results)  # debug
    return results

def test():
    print("TEST01:", "pass" if make_arr(3, 3, 4) == '0 1 2'  else "**FAIL**")
    print("TEST02:", "pass" if make_arr(3, 5, 4) == '1 1 3'  else "**FAIL**")
    print("TEST03:", "pass" if make_arr(3, 0, 0) == '0 0 0'  else "**FAIL**")
    print("TEST04:", "pass" if make_arr(3, 0, 1) == '-1'  else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

