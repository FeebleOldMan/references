#!/usr/bin/env python

r_d, r_m, r_y = map(int, raw_input().strip().split(' '))
d_d, d_m, d_y = map(int, raw_input().strip().split(' '))

if r_y > d_y:
    print '10000'
elif r_m > d_m and r_y == d_y:
    print 500*(r_m - d_m)
elif r_d > d_d and r_y == d_y and r_m == d_m:
    print 15*(r_d - d_d)
else:
    print '0'
