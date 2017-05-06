#!/usr/bin/env python
import math

for _ in range(int(raw_input().strip())):
    start, end = map(int, raw_input().strip().split());
    start = int(math.ceil(math.pow(start, 0.5)))
    end = int(math.floor(math.pow(end, 0.5)))
    print (end - start + 1)
#    square_list = []
#    for num in range(start, end+1):
#        square_list.append(math.pow(num, 2))
#    return len(square_list)
