#!/usr/bin/env python3

n, sticks = int(input()), sorted(map(int, input().strip().split()))

found = False
for i in range(len(sticks)-3, -1, -1):
    if sticks[i] + sticks[i+1] > sticks[i+2]:
        print(*sticks[i:i+3], sep=' ')
        found = True
        break
if not found: print(-1)

### v0.1 buggy. misses out [1, 1, 1, 9]
#print(-1 if sticks[-3] + sticks[-2] <= sticks[-1] else ' '.join(map(str, sticks[-3:])))

