#!/usr/bin/env python3

import sys, getopt

def main(argv):
    help = """Jumping on the Clouds v1.0

Usage:
  python jumping_on_the_clouds.py [option]

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
    # main code here
    total = int(input())
    clouds = list(map(int, input().strip().split()))
    print(count_jumps(total, clouds))

def count_jumps(total, clouds):
    jump_count, pos = 0, 0
    clouds.append(0)
    while pos < total-1:
        if not clouds[pos+2]:
            pos += 2
        else:
            pos += 1
        jump_count += 1
    return jump_count

def test():
    print('TEST01:', 'pass' if count_jumps(7, [0, 0, 1, 0, 0, 1, 0])
          == 4 else '**FAIL**')
    print('TEST02:', 'pass' if count_jumps(6, [0, 0, 0, 0, 1, 0])
          == 3 else '**FAIL**')
    print('TEST03:', 'pass' if count_jumps(4, [0, 0, 0, 0])
          == 2 else '**FAIL**')
if __name__ == '__main__':
    main(sys.argv[1:])

