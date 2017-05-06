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
    num_int, difference = map(int, input().strip().split())
    numbers = list(map(int, input().strip().split()))
    print(count_pairs(num_int, difference, numbers))

### v1.1 using sets
def count_pairs(num_int, difference, numbers):
    numbers = set(numbers)
    numbers_with_difference = set([number + difference for number in numbers])
    return len(numbers & numbers_with_difference)

### v1.0 correct!
#def count_pairs(num_int, difference, numbers):
#    numbers.sort(reverse = True)
#    numbers_dict = {number: 1 for number in numbers}
#    # make dict and use get?
#    pairs = 0
#    for i in range(num_int):
#        if numbers[i] < difference: break
#        target = numbers[i] - difference
#        pairs += numbers_dict.get(target, 0)
#    return pairs

### v0.3 too slow
#def count_pairs(num_int, difference, numbers):
#    numbers.sort(reverse = True)
#    pairs = 0
#    for i in range(num_int):
#        if numbers[i] < difference: break
#        target = numbers[i] - difference
#        if target in numbers[i:i + difference + 1]:
#            pairs += 1
#    return pairs

### v0.2 too slow
#def count_pairs(num_int, difference, numbers):
#    numbers.sort()
#    pairs = 0
#    while numbers:
#        number = numbers.pop()
#        if number < difference: break
#        target = number - difference
#        if target in numbers:
#            pairs += 1
#    return pairs

### v0.1 too slow
#def count_pairs(num_int, difference, numbers):
#    numbers.sort(reverse = True)
#    pairs = 0
#    for number in numbers:
#        if number < difference: break
#        target = number - difference
#        if target in numbers:
#            pairs += 1
#    return pairs

def test():
    from random import randrange
    from time import time
    print("TEST01:", "pass" if count_pairs(5, 2, [1, 5, 3, 4, 2]) == 3 else "**FAIL**")
    print("TEST02:", "pass" if count_pairs(5, 2, [1, 2, 3, 7, 9]) == 2 else "**FAIL**")
    print("Long test")
    n = 100000
    k = randrange(1000000000)
    a = [randrange(2147483647 - k) for _ in range(n)]
    start = time()
    print(count_pairs(n, k, a))
    print(time() - start)

if __name__ == '__main__':
    main(sys.argv[1:])

