#!/usr/bin/env python

for _ in range(int(raw_input().strip())):
    N = int(raw_input().strip())
    count = 0
    for d in str(N):
       if (int(d) != 0) and (N % int(d) == 0): count += 1
    print count
