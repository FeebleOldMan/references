#!/usr/bin/env python

def main():
    for _ in range(int(raw_input().strip())):
        N = int(raw_input().strip())
        arr = map(int, raw_input().strip().split())
        arr = map_sum(map_array(arr))
        print max_contig(arr), max_noncontig(arr)

def map_array(arr):
    """
    Split input array into positive and negative subarray blocks
    """
    array_map = []
    array_block = []
    sign_check = arr[0] > 0 # track if current num is +/-
    for num in arr:
        if (num > 0) == sign_check: # current num matches sign of previous num
            array_block.append(num)
        else:
            sign_check = num > 0 # flip sign_check
            array_map.append(array_block)
            array_block = [num] # restart array block
    array_map.append(array_block) # at end of input array, append remaining of array block
    return array_map

def map_sum(arr):
    """
    Sum each subarray block
    """
    if len(arr) == 1 and sum(arr[0]) < 0:
        return arr[0]
    return [sum(sub_array) for sub_array in arr]

### Kadane's Algorithm
def max_contig(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

### v0.5 :(
#def max_contig(arr):
#    """
#    Find maximum sum of contiguous sequence
#    """
#    arr_proc = arr[:]
#    while arr_proc[0] <= 0:
#        arr_proc = arr_proc[1:]
#        if len(arr_proc) == 0:
#            return max(arr)
#    while arr_proc[-1] <= 0:
#        arr_proc = arr_proc[:-1]
#    arr_after = []
#    has_merge = False
#    max_val = max(arr_proc)
#    while True:
#        for i in range(len(arr_proc)):
#            if has_merge:
#                has_merge = False
#                continue
#            if (i == len(arr_proc)-1):
#                if (arr_proc[i] > 0):
#                    arr_after.append(arr_proc[i])
#            elif (arr_proc[i] + arr_proc[i+1]) > 0:
#                arr_after.append(arr_proc[i] + arr_proc[i+1])
#                has_merge = True
#            else:
#                arr_after.append(arr_proc[i])
#        if arr_proc == arr_after:
#            break
#        else:
#            arr_proc = map_sum(map_array(arr_after))
#            if (max(arr_proc) > max_val):
#                max_val = max(arr_proc)
#            arr_after = []
#    return max_val

def max_noncontig(arr):
    """
    Find maximum sum of non-contiguous sequence
    """
    positive_sum = sum([num for num in arr if num > 0])
    return positive_sum if positive_sum != 0 else max(arr)

#def test():
#    import test_cases
#    print "map_array():", "pass" if (map_array([1, 2, 3, -4, -5, 6, 7, -8])) == [[1, 2, 3], [-4, -5], [6, 7], [-8]] else "***FAIL***"
#    print "map_sum():", "pass" if (map_sum([[2, 3, 4], [-1, -2, -3], [5, 6, 10]])) == [9, -6, 21] else "***FAIL***"
#    print "max_noncontig() normal:", "pass" if max_noncontig([1, 2, 3, -4, -5, 6, 7, -8]) == 19 else "***FAIL***"
#    print "max_noncontig() negative:", "pass" if max_noncontig([-1, -2, -3, -4, -5, -6, -7, -8]) == -1 else "***FAIL***"
#    print "max_contig():", "pass" if max_contig([2, -1, 2, 3, 4, -5]) == 10 else "***FAIL***"
#    print "max_contig([3, -1, 2, -5, 4, -1, 3]) alternate:", "pass" if max_contig([3, -1, 2, -5, 4, -1, 3]) == 6 else "***FAIL***"
#    print "map_array([2, -1, 2, 3, 4, -5])", "pass" if (map_array([2, -1, 2, 3, 4, -5])) == [[2], [-1], [2, 3, 4], [-5]] else "***FAIL***"
#    print "map_sum([[2], [-1], [2, 3, 4], [-5]]):", "pass" if (map_sum([[2], [-1], [2, 3, 4], [-5]])) == [2, -1, 9, -5] else "***FAIL***"
#    print "max_contig([2, -1, 9, -5]):", "pass" if (max_contig([2, -1, 9, -5])) == 10 else ("***FAIL***", max_contig([2, -1, 9, -5]))
#    print "max_noncontig([-1, -2, -3, -4, -5, -6]):", "pass" if max_noncontig([-1, -2, -3, -4, -5, -6]) == -1 else "***FAIL***"
#    print "max_noncontig([-1, -2, -3, -4, -5, -6]):", "pass" if max_noncontig([-1, -2, -3, -4, -5, -6]) == -1 else "***FAIL***"
#    print "max_contig([1, -1, -1, -1, -1, 5]):", "pass" if max_contig([1, -1, -1, -1, -1, 5]) == 5 else "***FAIL***"
#    print "main([1, -1, -1, -1, -1, 5]):", "pass" if max_contig(map_sum(map_array([1, -1, -1, -1, -1, 5]))) == 5 else "***FAIL***"
#    print "map_sum(map_array([-1, -2, -3, -4, -5, -6])):", "pass" if map_sum(map_array([-1, -2, -3, -4, -5, -6])) == [-1, -2, -3, -4, -5, -6] else "***FAIL***"
#    print "max_contig(test_cases.test1):", "pass" if max_contig(map_sum(map_array(test_cases.test1_arr))) == test_cases.test1_contig else ("***FAIL***", max_contig(map_sum(map_array(test_cases.test1_arr))), test_cases.test1_contig)
#    print "max_noncontig(test_cases.test1):", "pass" if max_noncontig(map_sum(map_array(test_cases.test1_arr))) == test_cases.test1_noncontig else "***FAIL***"
#    print "max_contig(test_cases.test2):", "pass" if max_contig(map_sum(map_array(test_cases.test2_arr))) == test_cases.test2_contig else ("***FAIL***", max_contig(map_sum(map_array(test_cases.test2_arr))), test_cases.test2_contig)
#    print "max_noncontig(test_cases.test2):", "pass" if max_noncontig(map_sum(map_array(test_cases.test2_arr))) == test_cases.test2_noncontig else "***FAIL***"
#    return

main()

#####
#for _ in range(int(raw_input().strip())):
#    N = int(raw_input().strip())
#    arr = map(int, raw_input().strip().split())
#
#### v0.4
#### split array into subarrays of positive stretches and negative stretches
#### if left and right pos stretch more than neg stretch, include neg stretch
#    arr_map = []
#    arr_block = []
#    sign_check = arr[0] > 0
#    for num in arr:
#        if (num > 0) == sign_check:
#            arr_block.append(num)
#        else:
#            sign_check = num > 0
#            arr_map.append(arr_block)
#            arr_block = [num]
#    if len(arr_block) > 0:
#        arr_map.append(arr_block)
#### sum each array block in array map
#    arr_map_sum = []
#    max_noncontig = 0
#    for sub_arr in arr_map:
#        arr_sum = sum(sub_arr)
#        arr_map_sum.append(arr_sum)
#        if arr_sum > 0:
#            max_noncontig += arr_sum
#### iter through all combi of sums for highest val
#    max_contig = max(arr_map_sum)
#    for i in range(len(arr_map_sum)-1):
#        if arr[i] > 0:
#            for j in range(i+1, len(arr_map_sum)+1):
#                if arr[j-1] > 0:
#                    sum_slice = sum(arr_map_sum[i:j])
#                    if sum_slice > max_contig:
#                        max_contig = sum_slice
#    print max_contig, max_noncontig
#


### v0.3
### bug: stops if interrupted by negative number along the way
#    # start from max value and extend left and right if value increases
#    max_val = max(arr)
#    start_pos = min(max(arr.index(max_val), 0), len(arr)) # ensure index within bounds
#    i, j = start_pos-1, start_pos+2
#    # search left
#    for i in range(start_pos-1, -1, -1):
#        cur_val = sum(arr[i:start_pos+1])
#        if cur_val < max_val:
#            i += 1
#            break
#        else:
#            max_val = cur_val
#    for j in range(start_pos+2, len(arr)):
#       cur_val = sum(arr[start_pos:j])
#       if cur_val < max_val:
#           j -= 1
#           break
#       else:
#            max_val = cur_val
#    i, j = max(i, 0), min(j, len(arr))
# v0.2
    # start from both ends and move towards middle.
    # if value starts to decrease stop before that point.
### bug: does not account for big negative number in middle
### bug: cannot handle all negative numbers
#    i, j = 0, len(arr)
#    prev_val = sum(arr)
#    for i in range(1, len(arr)-1):
#        curr_val = sum(arr[i:j])
#        if curr_val < prev_val:
#            i -= 1
#            break
#        else:
#            prev_val = curr_val
#    for j in range(len(arr)-1, 0, -1):
#        curr_val = sum(arr[i:j])
#        if curr_val < prev_val:
#            j += 1
#            break
#        else:
#            prev_val = curr_val
#    max_val = sum(arr[i:j])
#    max_pos = sum(pos for pos in arr if pos > 0)
#    if max_pos == 0:
#        max_pos = max(arr)
#    print max_val, max_pos
