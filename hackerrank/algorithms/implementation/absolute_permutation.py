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
    for _ in range(int(input())):
        print(smallest_abs(*map(int, input().strip().split())))

def smallest_abs(num, abs_diff):
    perm = []
    idx = {n: n for n in range(1, num + 1)}
    for pos in range(1, num + 1):
        small = pos - abs_diff
        big = pos + abs_diff
        if small >=1 and small <= num and idx.get(small, 0):
            perm.append(str(small))
            idx[small] = 0
        elif big >=1 and big <= num and idx.get(big, 0):
            perm.append(str(big))
            idx[big] = 0
        else:
            return '-1'
    return ' '.join(perm)

### v0.1 slow and buggy
#def smallest_abs(num, abs_diff):
#    # take abs_diff to add / subtract to position to figure out
#    # possible values, then pick smallest perm first
#    permute, permutation = [], []
#    for pos in range(1, num+1):
#        permute.append([])
#        small = pos - abs_diff
#        if small >= 1 and small <= num:
#            permute[-1].append(small)
#        big = pos + abs_diff
#        if big >= 1 and big <= num:
#            permute[-1].append(big)
#        if permute[-1] == []:
#            return '-1'
#    for pos in permute:
#        is_invalid = True
#        for i in pos:
#            if i not in permutation:
#                permutation.append(str(i))
#                is_invalid = False
#                break
#        if is_invalid:
#            return '-1'
#    return ' '.join(permutation)

def test():
    print("TEST01:", "pass" if smallest_abs(2, 1) == '2 1' else "**FAIL**")
    print("TEST02:", "pass" if smallest_abs(3, 0) == '1 2 3' else "**FAIL**")
    print("TEST03:", "pass" if smallest_abs(3, 2) == '-1' else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

