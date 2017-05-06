#!/usr/bin/env python

for _ in range(int(raw_input().strip())):
    height = 1
    for cycle in range(0, int(raw_input().strip())):
        if cycle % 2 == 0:
            height *= 2
        else:
            height += 1
    print height
