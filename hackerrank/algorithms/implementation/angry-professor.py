#!/usr/bin/env python

for _ in range(int(raw_input().strip())):
    num, threshold = map(int, raw_input().strip().split())
    for arrival in map(int, raw_input().strip().split()):
        if arrival <= 0: threshold -= 1
    print ('NO' if threshold <= 0 else 'YES')
