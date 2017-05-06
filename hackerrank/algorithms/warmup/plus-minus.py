#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos, neg, zero = 0.0, 0.0, 0.0

for num in arr:
    if num > 0:
        pos += 1.0
    elif num < 0:
        neg += 1.0
    elif num == 0:
        zero += 1.0

print pos/(pos+neg+zero)
print neg/(pos+neg+zero)
print zero/(pos+neg+zero)
