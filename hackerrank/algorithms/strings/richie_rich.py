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
    num_digits, max_changes = map(int, input().strip().split())
    number = list(map(int, list(input())))
    print(largest_palindrome(num_digits, max_changes, number))

def largest_palindrome(num_digits, max_changes, number):
    """Make largest palindromic number by changing up to max_changes digits

    >>> print(largest_palindrome(4, 1, [3, 9, 4, 3]))
    3993
    >>> print(largest_palindrome(6, 3, [0, 9, 2, 2, 8, 2]))
    992299
    >>> print(largest_palindrome(4, 1, [0, 0, 1, 1]))
    -1
    >>> print(largest_palindrome(5, 1, [0, 0, 1, 1, 0]))
    01110
    >>> print(largest_palindrome(5, 1, [9, 9, 1, 9, 9]))
    99999
    """
### v0.2
    original = number[:]
    changes = 0
    # change front and back simultaneously first
    for i in range(num_digits // 2):
        if number[i] != number[-1 - i]:
            if number[i] > number[-1 - i]:
                number[-1 - i] = number[i]
            else:
                number[i] = number[-1 - i]
            changes += 1
        if changes > max_changes: return -1
    # second pass change front and back to 9s if not 9s
    for i in range(num_digits // 2):
        if changes == max_changes: break
        if (number[i] != 9 and number[-1 - i] != 9):
            if (original[i] != number[i]
                    or original[-1 - i] != number[-1 - i]):
                # previously changed
                changes += 1
            else:
                if changes + 2 > max_changes:
                    break
                else:
                    changes += 2
            number[i], number[-1 - i] = 9, 9
    # lastly if num_digits is odd and changes < max_changes, change mid
    if changes < max_changes and num_digits % 2 != 0:
        number[num_digits // 2] = 9
    return "".join(map(str, number))
    # change from front to mid. if have spare changes, change front
    # and back simultaneously to 9 while monitoring changes < max_changes
### v0.1 bug
#    front = number[:num_digits//2]
#    back = number[num_digits:num_digits//2 - 1:-1]
#    # compare front back and count differences to see how much to patch
#    changes = 0
#    for i, j in zip(front, back):
#        if i != j:
#            changes += 1
#    changes_left = max_changes - changes
#    if changes_left < 0:
#        return -1
#    # if have extra even steps start changing front number and back number
#    elif changes_left > 0 and changes_left % 2 == 0:
#        i = 0
#        while changes_left:
#            if front[i] != 9:
#                front[i] = 9
#                changes_left -= 1
#            if back[i] != 9:
#                back[i] = 9
#                changes_left -= 1
#            i += 1
#    for i in range(len(front)):
#        if front[i] != back[i]:
#            if front[i] > back[i]:
#                back[i] = front[i]
#            else:
#                front[i] = back[i]
#    # if odd length change last "back" number last
#    return "".join(map(str, front + back[::-1]))

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

