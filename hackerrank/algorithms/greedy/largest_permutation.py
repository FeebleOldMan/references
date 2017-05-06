#!/usr/bin/env python3

TEST_MODE = False

def main():
    size, max_swaps = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    print(*largest_perm(size, max_swaps, arr), sep=' ')

### v0.7 use indexing on data entry
def largest_perm(size, max_swaps, arr):
    pos_dict = {val: idx for idx, val in enumerate(arr)}
    presort = sorted(arr, reverse=True)
    skips = 0
    for i in range(size):
        if i == max_swaps + skips: break
        if presort[i] == arr[i]:
            skips += 1
        else:
            arr[pos_dict[presort[i]]], pos_dict[arr[i]] = arr[i], pos_dict[presort[i]]
    return presort[:max_swaps+skips] + arr[max_swaps+skips:]

### v0.6 works but too slow
#def largest_perm(size, max_swaps, arr):
#    presort = sorted(arr, reverse=True)
#    skips = 0
#    for i in range(size):
#        if i == max_swaps + skips: break
#        if presort[i] == arr[i]:
#            skips += 1
#        else:
#            arr[arr[i + 1:].index(presort[i]) + i + 1] = arr[i]
#    return presort[:max_swaps+skips] + arr[max_swaps+skips:]

### just search from back half after max_swaps
### there are no repeats
### v0.5 BUG doesn't work
#def largest_perm(size, max_swaps, arr):
#    presort = sorted(arr, reverse=True)
#    skips = sum([1 for x, y in zip(arr, presort) if x == y])
#    back = arr[max_swaps + skips:]
#    cutoff = presort[max_swaps + skips]
#    for i in range(len(back)):
#        if i == max_swaps + skips: break
#        if back[i] >= cutoff:
#            back[i] = arr[presort.index(back[i])]
#    return presort[:max_swaps + skips] + back

### v0.4 bug and too slow
#def largest_perm(size, max_swaps, arr):
#    presort = sorted(arr, reverse=True)
#    back = list(reversed(arr))
#    skips = 0
#    for i in range(size):
#        if i == max_swaps + skips: break
#        if presort[i] == arr[i]:
#            skips += 1
#        else:
#            back_idx = back[:size-i].index(presort[i])
#            back[back_idx], back[-i-1] = back[-i-1], back[back_idx]
#    return presort[:max_swaps + skips] + list(reversed(back))[max_swaps + skips:]

### v0.3 bug. cannot cut off back list because numbers might come from front
#def largest_perm(size, max_swaps, arr):
#    presort = sorted(arr, reverse=True)
#    back = list(reversed(arr[max_swaps:]))
#    skips = 0
#    for i in range(len(back)):
#        if i == max_swaps + skips: break
#        if presort[i] == arr[i]:
#            skips += 1
#        else:
#            try:
#                back[back[i-skips:].index(presort[i])] = arr[i]
#            except ValueError:
#                pass
#    return presort[:max_swaps + skips] + list(reversed(back))[skips:]

### v0.25 fast, but doesn't sort correctly since it's sorts from 'front'
#def largest_perm(size, max_swaps, arr):
#    presort = sorted(arr, reverse=True)
#    back = arr[max_swaps:]
#    skips = 0
#    for i in range(len(back)):
#        if i == max_swaps + skips: break
#        if presort[i] == arr[i]:
#            skips += 1
#        else:
#            try:
#                back[back[i-skips:].index(presort[i])] = arr[i]
#            except ValueError:
#                pass
#    return presort[:max_swaps + skips] + back[skips:]

### v0.2 slightly too slow
#def largest_perm(size, max_swaps, arr):
#    presort = sorted(arr)
#    idx, arr_len = 0, len(arr)
#    while max_swaps and idx < len(arr):
#        curr_high = presort.pop()
#        if arr[idx] < curr_high:
#            arr[arr[idx:].index(curr_high)+idx], arr[idx] = arr[idx], curr_high
#            max_swaps -= 1
#        idx += 1
#    return(arr)

### v0.1 too slow, bugs
### change to countdown counter and skip if swap doesn't change
#def largest_perm(size, max_swaps, arr):
#    for i in range(min(len(arr), max_swaps)):
#        high_idx = arr.index(max(arr[i:]))
#        arr[i], arr[high_idx] = arr[high_idx], arr[i]
#    return arr

def test():
    print(largest_perm(5, 1, [4, 2, 3, 5, 1]), [5, 2, 3, 4, 1])
    print(largest_perm(3, 1, [2, 1, 3]), [3, 1, 2])
    print(largest_perm(2, 1, [2, 1]), [2, 1])
    print(largest_perm(5, 5, [4, 2, 3, 5, 1]), [5, 4, 3, 2, 1])
    print(largest_perm(5, 3, [1, 2, 3, 5, 1]), [5, 3, 2, 1, 1])
    print(largest_perm(1, 1, [1]), [1])
    print(largest_perm(5, 1, [1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])

test() if TEST_MODE else main()
