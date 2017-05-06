n = int(raw_input()) #size of array
ar = map(int, (raw_input().strip().split(' ')))
ar.sort()
if (n%2 == 0):
    # even length, take average of median
    mid_idx = n/2
    print str((ar[mid_idx-1] + ar[mid_idx]) / 2.0)
else:
    print ar[n/2]
