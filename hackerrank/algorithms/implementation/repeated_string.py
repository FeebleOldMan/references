#!/usr/bin/env python3

s = input()
n = int(input())
print(s.count('a')*(n//len(s))+s[:(n%len(s))].count('a'))

#v0.1 too slow
#s = input()
#n = int(input())
#print((s*(n//len(s)+1))[:n].count('a'))
#print(len(list(filter(lambda x: x == 'a', ((s*(n//len(s)+1))[:n])))))
