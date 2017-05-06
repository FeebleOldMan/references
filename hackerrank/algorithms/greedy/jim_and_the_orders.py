#!/usr/bin/env python3

print(*(q[0]+1 for q in sorted([(i, sum(map(int, input().strip().split()))) for i in range(int(input()))], key=lambda x: (x[1], x[0]))))

### some other guy
#print(*(lambda s: sorted(range(1, len(s) + 1), key=lambda i: s[i - 1]))(tuple(sum(map(int, input().split())) for _ in range(int(input())))))
