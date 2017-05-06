#!/usr/bin/env python3

x1, v1, x2, v2 = map(int, input().strip().split())

diff = abs((x1-v1) - (x2-v2))
next_diff = abs(x1 - x2)
answer = 'NO'
while next_diff < diff:
    if x1 == x2:
        answer = 'YES'
        break
    diff = next_diff
    x1 += v1
    x2 += v2
    next_diff = abs(x1 - x2)
print(answer)

