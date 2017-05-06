#!/usr/bin/env python

def decent(N):
    for fives in range(N, -1, -1):
        if ((fives % 3 == 0) and ((N-fives) % 5 == 0)):
            return ('5'*fives + '3'*(N-fives))
    return -1

for _ in range(int(raw_input().strip())):
    print decent(int(raw_input().strip()))
