#!/usr/bin/env python3

DEBUG = True

def main():
    arr_len, divisor = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    print(find_pairs(arr_len, divisor, arr))

def find_pairs(arr_len, divisor, arr):
    pairs = 0
    for i in range(arr_len):
        for j in range(i+1, arr_len):
            if (arr[i] + arr[j]) % divisor == 0:
                pairs += 1
    return pairs

def test():
    print('TEST01:', 'pass' if find_pairs(6, 3, [1, 3, 2, 6, 1, 2]) == 5 else '**FAIL**')

test() if DEBUG else main()
