#!/usr/bin/env python3
"""Fizz Buzz

Prints numbers from 1 to 100, but print "Fizz" instead for multiples of three
and "Buzz" instead for multiples of five. For numbres which are multiples of
both three and five print "FizzBuzz".
"""

for n in range(1, 101):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
