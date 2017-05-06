#!/usr/bin/env python3

likes, people = 0, 5
for _ in range(int(input())):
    people //= 2
    likes += people
    people *= 3
print(likes)

