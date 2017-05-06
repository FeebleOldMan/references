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
    initial = input().strip()
    final = input().strip()
    num_ops = int(input())
    print(append_delete(initial, final, num_ops))

def append_delete(initial, final, num_ops):
    """Checks if a string can be converted to another string in exactly
    num_ops steps using only the following operations:

    1. Append a lowercase English alphabetic letter to the end of the string.
    2. Delete the last character in the string.
       Performing this operation on an empty string results in an empty string.

    Returns 'Yes' if possible else 'No'

    >>> print(append_delete('hackerhappy', 'hackerrank', 9))
    Yes
    >>> print(append_delete('hackerrank', 'hackerhappy', 9))
    Yes
    >>> print(append_delete('aba', 'aba', 7))
    Yes
    >>> print(append_delete('aba', 'aba', 0))
    Yes
    >>> print(append_delete('aba', 'aba', 1))
    No
    >>> print(append_delete('aba', 'aba', 2))
    Yes
    >>> print(append_delete('ab', 'aba', 1))
    Yes
    >>> print(append_delete('aba', 'ab', 1))
    Yes
    >>> print(append_delete('hackerhappy', 'hackerrank', 1))
    No
    >>> print(append_delete('hackerhappy', 'hackerrank', 8))
    No
    >>> print(append_delete('abcd', 'abcdert', 10))
    No
    >>> print(append_delete('aaaaaaaaaa', 'aaaaa', 7))
    Yes
    >>> print(append_delete('abcdef', 'fedcba', 15))
    Yes
    """
### v1.1 editorial version
    initial, final = list(initial), list(final)
    len_p, len_i, len_f = 0, len(initial), len(final)
    for i, f in zip(initial, final):
        if i == f:
            len_p += 1
        else:
            break
    min_ops = len_i + len_f - 2 * len_p
    min_ops = len_i + len_f + 1 if min_ops % 2 != num_ops % 2 else min_ops
    return 'Yes' if num_ops >= min_ops else 'No'

### v1.0 works
#    initial = list(initial)
#    final = list(final)
#    working = []
#    for i, f in zip(initial, final):
#        if i == f:
#            working.append(f)
#        else:
#            break
#    to_delete = len(initial) - len(working)
#    to_append = len(final) - len(working)
#    steps_left = num_ops - (to_delete + to_append)
#    return 'Yes' if (steps_left == 0
#            or (steps_left > 1
#                and (steps_left % 2 == 0))
#            or num_ops >= len(initial) + len(final)) else 'No'

### v0.1 buggy
#    initial = list(initial)
#    final = list(final)
#    working = []
#    for i, f in zip(initial, final):
#        if i == f:
#            working.append(f)
#        else:
#            break
#    len_delete = len(initial) - len(working)
#    len_append = len(final) - len(working)
#    if (len_delete == 0 and num_ops == 1
#            and len(initial) == len(final)):
#        return 'No'
#    return 'Yes' if (num_ops - len_append >= len_delete
#            ) else 'No'

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

