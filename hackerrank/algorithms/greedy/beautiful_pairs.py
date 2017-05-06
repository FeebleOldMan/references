#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

max_pairs = 0
switch = False

for num in A:
    if num in B:
        B.remove(num)
        max_pairs += 1
    else:
        switch = True

if B and switch:
    max_pairs += 1
elif not switch:
    max_pairs -= 1

print(max_pairs)
