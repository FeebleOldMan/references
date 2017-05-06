#!/usr/bin/env python3

A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
A_score, B_score = 0, 0
for i in range(len(A)):
    if A[i] < B[i]:
        B_score += 1
    elif A[i] > B[i]:
        A_score += 1
print(A_score, B_score)

