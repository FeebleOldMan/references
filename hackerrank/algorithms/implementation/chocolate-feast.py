#!/usr/bin/env python

for _ in range(int(raw_input().strip())):
    money, price, rate = map(int, raw_input().strip().split())
    total = wrappers = money / price
    while True:
        exchange = wrappers/rate
        total += exchange
        wrappers = (wrappers % rate) + exchange
        if (wrappers / rate) == 0: break
    print total
