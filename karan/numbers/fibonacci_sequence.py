#!/usr/bin/env python3
"""Fibonacci Sequence

Enter a number and have the program generate the Fibonacci sequence to that
number or to the Nth number.
"""

import getopt
import sys

def memoize(function):
    """Memoization helper for fibonacci().
    Stores Fibonacci sequence in a dictionary.

    function        function object (fibonacci())

    return          function object wrapped around function
    """

    sequence = {}

    def memo_wrapper(index):
        """Checks for Fibonnaci number in sequence, adding it in if missing.

        index       int of index of Fibonacci sequence

        return      int of Fibonacci number
        """
        if index not in sequence:
            sequence[index] = function(index)
        return sequence[index]

    return memo_wrapper

@memoize
def fibonacci(index):
    """Generates the Fibonacci number of index.

    index           int of index of Fibonacci sequence

    return          int of Fibonacci number

    >>> fibonacci(5)
    5
    >>> fibonacci(8)
    21
    """
    if index == 0 or index == 1:
        return index
    else:
        return fibonacci(index-1) + fibonacci(index-2)

def fibonacci_sequence(index):
    """Generates the Fibonacci sequence to index.

    index           int of index of Fibonacci sequence

    return          list of Fibonacci sequence to index

    >>> fibonacci_sequence(1)
    [1]
    >>> fibonacci_sequence(2)
    [1, 1]
    >>> fibonacci_sequence(5)
    [1, 1, 2, 3, 5]
    """
    assert index > 0, "Please enter an index greater than 0"

    sequence = [1, 1]

    for i in range(2, index):
        sequence.append(sequence[i-1] + sequence[i-2])

    return sequence[:index]

def main(argv):
    """Main function"""

    help_text = """
Fibonacci Sequence v1.0

Usage:
  python fibonacci_sequence.py [options] [index]

  Running fibonacci_sequence.py without options will return the Fibonacci
  sequence until the index value.

Options:

  -i, --index               Returns value of Fibonacci sequence at index
  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(
            argv,
            "htsi",
            ["help", "test", "stress", "index"]
            )
    except getopt.GetoptError as error:
        print("Invalid option: {}".format(error))
        print(help_text)
        sys.exit(2)
    for opt, _ in opts:
        if opt in ("-h", "--help"):
            print(help_text)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
        elif opt in ("-s", "--stress"):
            stress()
            sys.exit()
        elif opt in ("-i", "--index"):
            print(fibonacci(int(args[0])))
            sys.exit()
    if args:
        print(fibonacci_sequence(int(args[0])))
        sys.exit()
    else:
        index = int(input("Fibonnaci index: "))
        print(fibonacci_sequence(index))

def test():
    """Runs doctest on functions."""

    import doctest
    print(doctest.testmod())

def stress():
    """Runs stress test on functions."""

    print("STRESS TEST")
    import timeit
    print(timeit.timeit(
        # edit stress test function here
        'FUNCTION()',
        number=1,
        setup="from __main__ import FUNCTION",
        )
         )

if __name__ == '__main__':
    main(sys.argv[1:])

