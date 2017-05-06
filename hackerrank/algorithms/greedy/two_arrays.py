#!/usr/bin/env python3

for _ in range(int(input())):
    arr_size, min_val = map(int, input().strip().split())
    arr_A = sorted(map(int, input().strip().split()))
    arr_B = sorted(map(int, input().strip().split()), reverse=True)
    is_valid = 'YES'
    for i in range(arr_size):
        if arr_A[i] + arr_B[i] < min_val:
            is_valid = 'NO'
            break
    print(is_valid)

