#!/usr/bin/env python3

DEBUG = True

def main():
    num_socks = int(input())
    socks = list(map(int, input().strip().split()))
    print(sock_pairs(num_socks, socks))

def sock_pairs(num_socks, socks):
    pairs = 0
    while socks:
        sock = socks.pop()
        try:
            socks.pop(socks.index(sock))
            pairs += 1
        except:
            pass
    return pairs

def test():
    print("TEST01:", "pass" if sock_pairs(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3 else "**FAIL**")

test() if DEBUG else main()
