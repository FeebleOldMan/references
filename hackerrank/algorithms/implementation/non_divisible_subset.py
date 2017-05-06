#!/usr/bin/env python3

DEBUG = False

#from itertools import combinations
#from collections import Counter

def main():
    set_len, divisor = map(int, input().strip().split())
    set_num = list(map(int, input().strip().split()))
    print(largest_subset(set_len, divisor, set_num))

def largest_subset(set_len, divisor, set_num):
    remainder_dict = {x: [] for x in range(0, divisor)}
    for num in set_num:
        remainder = num % divisor
        remainder_dict[remainder].append(num)
    max_len = 0
    if len(remainder_dict[0]) > 0:
        max_len += 1
    if divisor % 2 == 0 and len(remainder_dict[divisor/2]) > 0:
        max_len += 1
    for remainder in range(1, (divisor-1)//2 + 1):
        max_len += max(len(remainder_dict[remainder]), len(remainder_dict[divisor - remainder]))
    if DEBUG: print(max_len)
    return max_len

### v0.6 TOO SLOW, bug. add numbers to list, avoid nums that can be divided
#def largest_subset(set_len, divisor, set_num):
#    result = [set_num.pop()]
#    while set_num:
#        num = set_num.pop()
#        valid = True
#        for x in result:
#            if (num + x) % divisor == 0:
#                valid = False
#                break
#        if valid:
#            result.append(num)
#    if len(result) == 1 and result[0] % divisor == 0:
#        result = []
#    if DEBUG: print("RESULT:", len(result))
#    if DEBUG: print("COMBIS LEFT:", len(list(filter(lambda x: (x[0] + x[1]) % divisor == 0, combinations(set_num, 2)))))
#    return len(result)

### v0.5 combinations uses too much memory and crashes
#def largest_subset(set_len, divisor, set_num):
#    combis = list(filter(lambda x: (x[0] + x[1]) % divisor == 0, combinations(set_num, 2)))
#    if combis:
#        counter = Counter(num for combo in combis for num in combo)
#        while max(counter.values()) > 0:
#            max_num = counter.most_common(1)[0][0]
#            set_len -= 1
#            set_num.remove(max_num)
#            del counter[max_num]
#            working_combis = combis[:]
#            for combo in combis:
#                if max_num in combo:
#                    num_left = list(combo)
#                    num_left.remove(max_num)
#                    counter[num_left[0]] -= 1
#                    working_combis.remove(combo)
#            combis = working_combis[:]
#    if set_len == 1 and set_num[0] % divisor == 0:
#        set_len = 0
#    if DEBUG: print("RESULT:", set_len)
#    if DEBUG: print("COMBIS LEFT:", len(list(filter(lambda x: (x[0] + x[1]) % divisor == 0, combinations(set_num, 2)))))
#    return set_len

### v0.4 bug, but fast
#def largest_subset(set_len, divisor, set_num):
#    combis = list(filter(lambda x: (x[0] + x[1]) % divisor == 0, list(combinations(set_num, 2))))
#    if DEBUG:
#        print(set_num, divisor)
#        print(combis)
#    if combis:
#        counter = Counter(num for combo in combis for num in combo)
#        if DEBUG: print(counter)
#        count_list = sorted(counter.values())
#        pop_sum = 0
#        while count_list:
#            #if DEBUG: print(count_list)
#            max_num = count_list.pop()
#            pop_sum += max_num
#            set_len -= 1
#            if pop_sum == sum(count_list):
#                break
#    if set_len == 2 and count_list[0] == count_list[1]:
#        for num in set_num:
#            if num % divisor != 0:
#                set_len = 1
#                break
#            set_len = 0
#    ### introduces bugs for legit unedited sets
#    elif set_len == 1 and set_num[0] % divisor == 0:
#        set_len = 0
#    if DEBUG: print('RESULT:', set_len)
#    return set_len


### v0.3 some sort of bug
#def largest_subset(set_len, divisor, set_num):
#    combis = list(filter(lambda x: (x[0] + x[1]) % divisor == 0, list(combinations(set_num, 2))))
#    if combis:
#        counter = Counter(num for combo in combis for num in combo)
#        while max(counter.values()) > 0:
#            if DEBUG: print(combis)
#            max_num = counter.most_common(1)[0][0]
#            if DEBUG: print(set_num)
#            set_len -= 1
#            del counter[max_num]
#            working_combis = combis[:]
#            for combo in combis:
#                if max_num in combo:
#                    num_left = list(combo)
#                    num_left.remove(max_num)
#                    counter[num_left[0]] -= 1
#                    working_combis.remove(combo)
#            combis = working_combis[:]
#        largest_subset = set_len
#        if largest_subset == 1:
#            for num in set_num:
#                if num % divisor != 0:
#                    break
#                largest_subset = 0
#    else:
#        largest_subset = set_len
#    if DEBUG: print("RESULT:", largest_subset)
#    return largest_subset

### v0.2 too slow and some bug
#from collections import Counter
#def largest_subset(set_len, divisor, set_num):
#    counter_val = {num: [] for num in set_num}
#    if DEBUG: print(counter_val)
#    for i in range(set_len):
#        for j in range(i, set_len):
#            if (set_num[i] + set_num[j]) % divisor == 0:
#                counter_val[set_num[i]].append(set_num[j])
#                counter_val[set_num[j]].append(set_num[i])
#    counter_len = Counter({num: len(counter_val[num]) for num in counter_val})
#    while max(counter_len.values()) > 0:
#        max_num = counter_len.most_common(1)[0][0]
#        if DEBUG: print(max_num)
#        del counter_len[max_num]
#        del counter_val[max_num]
#        for num, values in counter_val.items():
#            if max_num in values:
#                counter_len[num] -= 1
#                counter_val[num].pop(counter_val[num].index(max_num))
#            if DEBUG: print(counter_len)
#    return len(counter_len)

### v0.1 doesn't make sense because it removes count from all values
#def largest_subset(set_len, divisor, set_num):
#    counter = Counter({num: 0 for num in set_num})
#    for i in range(set_len):
#        for j in range(i, set_len):
#            if (set_num[i] + set_num[j]) % divisor == 0:
#                counter[set_num[i]] += 1
#                counter[set_num[j]] += 1
#    if DEBUG: print(counter)
#    while max(counter.values()) > 0:
#        max_num = counter.most_common(1)
#        if DEBUG: print(max_num)
#        del counter[max_num[0][0]]
#        for num in counter:
#            counter[num] -= 1
#            if DEBUG: print(counter)
#    return len(counter)

def test():
    print("TEST01: 3", "pass" if largest_subset(4, 3, [1, 7, 2, 4]) == 3 else "**FAIL**")
    print("TEST02: 0", "pass" if largest_subset(4, 1, [1, 2, 3, 4]) == 0 else "**FAIL**")
    print("TEST03: 4", "pass" if largest_subset(4, 9, [1, 3, 5, 7]) == 4 else "**FAIL**")
    print("TEST04: 1", "pass" if largest_subset(4, 2, [1, 3, 5, 7]) == 1 else "**FAIL**")
    print("TEST05: 4", "pass" if largest_subset(5, 3, [1, 3, 5, 7, 4]) == 4 else "**FAIL**")
    print("TEST06: 4", "pass" if largest_subset(6, 3, [1, 3, 5, 7, 4, 9]) == 4 else "**FAIL**")
    print("TEST07: 0", "pass" if largest_subset(1, 1, [1]) == 0 else "**FAIL**")
    print("TEST08: 1", "pass" if largest_subset(1, 2, [1]) == 1 else "**FAIL**")
#    print("TEST09: random", random_test())

def random_test():
    import random
    n = 100000
    k = random.randint(1, 100)
    a = list(range(1, 100000))
    random.shuffle(a)
    largest_subset(n, k, a)

test() if DEBUG else main()
