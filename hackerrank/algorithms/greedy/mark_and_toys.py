#!/usr/bin/env python3

num_toys, budget = map(int, input().strip().split())
pricelist = sorted(list(map(int, input().strip().split())))

total, number = 0, 0
while total < budget:
    total += pricelist[number]
    number += 1
print(max(number - 1, 0))

