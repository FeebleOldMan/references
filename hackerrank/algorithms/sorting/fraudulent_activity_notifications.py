#!/usr/bin/env python3

import sys, getopt
#import bisect
import heapq

def main(argv):
    help = """CODE! v1.0

Usage:
  python CODE.py [options]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(argv, "ht", ["help", "test",])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
    num_days, median_days = map(int, input().strip().split())
    expenditure = list(map(int, input().strip().split()))
    print(count_frauds(num_days, median_days, expenditure))

def count_frauds(num_days, median_days, expenditure):
    """Counts number of fraud warnings

    >>> print(count_frauds(9, 5, 
    ...     [2, 3, 4, 2, 3, 6, 8, 4, 5]))
    2
    >>> print(count_frauds(5, 4, 
    ...     [1, 2, 3, 4, 4]))
    0
    """
    ### v0.7 heapq
    notifications = 0
    median_list = sorted(expenditure[:median_days])
    if median_days > 2:
        is_equal = not bool(median_days % 2)
        # negate values for max heap
        max_heap = [n * -1 for n in median_list[:median_days // 2]]
        min_heap = median_list[median_days // 2:]
        heapq.heapify(max_heap)
        for day in range(median_days, num_days):
            amount = expenditure[day]
            if amount >= 2 * get_median(max_heap, min_heap, is_equal):
                notifications += 1
            # remove tail expenditure from heaps
            tail = expenditure[day - median_days] 
            if tail >= min_heap[0]:
                min_heap[min_heap.index(tail)] = min_heap[0]
                heapq.heappop(min_heap)
            else:
                max_heap[max_heap.index(tail * -1)] = max_heap[0]
                heapq.heappop(max_heap)
            # add expenditure to heaps
            if amount >= min_heap[0]:
                heapq.heappush(min_heap, amount)
            else:
                heapq.heappush(max_heap, (amount * -1))
            # balance heaps
            while len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
            while len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, heapq.heappop(max_heap) * -1) 
    else:
        for day in range(median_days, num_days):
            amount = expenditure[day]
            if median_days == 2:
                if amount >= sum(median_list):
                    notifications += 1
            else:
                if amount >= 2 * median_list[0]:
                    notifications += 1
    return notifications

def get_median(max_heap, min_heap, is_equal):
    return ((max_heap[0] * -1) + min_heap[0]) / 2 if is_equal else min_heap[0]

#    ### v0.6 proper heap implementation?
#    notifications = 0
#
#class Heap:
#    """Base implementation of heap array"""
#
#    def __init__(self):
#        self.heap = []
#
#    def left(self, i):
#        return 2 * i + 1
#
#    def right(self, i):
#        return 2 * (i + 1)
#
#    def parent(self, i):
#        return (i - 1) / 2
#
#    def top(self):
#        """Returns largest element in heap"""
#        return max(self.heap)
#
#    def count(self):
#        """Returns number of elements in heap"""
#        return len(self.heap)
#
#    def heapify(self, i):
#        """Heapifies array towards root"""
#        parent = self.parent(i)
#        # differentiate max and minheap to percolate up
#        if (parent >= 0 and self.heap[i] < self.heap[parent]):
#            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
#            heapify(parent)
#
#    def deleteTop(self):
#        """Deletes root of heap"""
#        deleted_value = self.heap.pop(0)
#        self.heap[-1] = deleted_value
#        heapify(self.parent(self.count()))
#        return deleted_value
#
#    def insertHelper(self, key):
#        self.heap.append(key)
#        heapify(self.count())
#
#class MaxHeap(Heap):
#    """Subclasses Heap to provide MaxHeap functions"""
#    # I have no idea what I'm doing.

### v0.5 heap in and out. too slow. need to get rid of the head tail thing
#    notifications = 0
#    # create max_heap and min_heap
#    median_list = sorted(expenditure[:median_days])
#    if median_days > 2:
#        max_heap = median_list[:median_days // 2]
#        min_heap = median_list[median_days // 2:]
#        equal_heaps = median_days % 2 == 0
#        # stream days
#        for day in range(median_days, num_days):
#            amount = expenditure[day]
#            # check for notification
#            if amount >= 2 * median_heaps(max_heap, min_heap, equal_heaps):
#                notifications += 1
#            # update heaps
#            max_heap, min_heap = remove_insert_heap(max_heap, min_heap,
#                    amount, expenditure[day - median_days], equal_heaps)
#    else:
#        for day in range(median_days, num_days):
#            amount = expenditure[day]
#            if median_days == 2:
#                if amount >= sum(median_list):
#                    notifications += 1
#            else:
#                if amount >= 2 * median_list[0]:
#                    notifications += 1
#    return notifications
#
#
#
#def remove_insert_heap(max_heap, min_heap, number, tail, equal_heaps):
#    """Removes tail from heaps, then inserts number into heap before sorting
#    head or tail of respective heaps.
#
#    >>> remove_insert_heap([4, 2, 5], [6, 9, 7], 1, 9, True)
#    ([1, 2, 4], [5, 6, 7])
#    """
#    if equal_heaps:
#        # remove tail
#        if tail <= max_heap[-1]:
#            max_heap.remove(tail)
#        else:
#            min_heap.remove(tail)
#            min_heap.insert(0, max_heap.pop())
#        # arrange max_heap
#        max_heap.append(max_heap.pop(max_heap.index(max(max_heap))))
#        # add number
#        if number < max_heap[-1]:
#            max_heap.insert(0, number)
#        elif number < min_heap[0]:
#            max_heap.append(number)
#        else:
#            min_heap.append(number)
#            max_heap.append(min_heap.pop(0))
#            min_heap.insert(0, min_heap.pop(min_heap.index(min(min_heap))))
#    else:
#        if tail <= max_heap[-1]:
#            max_heap.remove(tail)
#            max_heap.append(min_heap.pop(0))
#        else:
#            min_heap.remove(tail)
#        min_heap.insert(0, min_heap.pop(min_heap.index(min(min_heap))))
#        if number < max_heap[-1]:
#            max_heap.insert(0, number)
#            min_heap.insert(0, max_heap.pop())
#            max_heap.append(max_heap.pop(max_heap.index(max(max_heap))))
#        elif number < min_heap[0]:
#            min_heap.insert(0, number)
#        else:
#            min_heap.append(number)
#    return max_heap, min_heap


### v0.4 heaps. bug heaps get unsorted over time
#    notifications = 0
#    # create max_heap and min_heap
#    median_list = sorted(expenditure[:median_days + 1])
#    max_heap = median_list[:median_days // 2]
#    min_heap = median_list[median_days // 2:]
#    equal_heaps = median_days % 2 == 0
#    # stream days
#    for day in range(median_days, num_days):
#        amount = expenditure[day]
#        # check for notification
#        if amount >= 2 * median_heaps(max_heap, min_heap, equal_heaps):
#            notifications += 1
#        # remove tail amount from heaps
#        max_heap, min_heap = remove_from_heap(max_heap, min_heap,
#                expenditure[day - median_days], equal_heaps)
#        # put amount in heaps
#        max_heap, min_heap = insert_into_heap(max_heap, min_heap,
#                amount, equal_heaps)
#    return notifications
#
#
#def insert_into_heap(max_heap, min_heap, number, equal_heaps):
#    """
#    equal_heaps will be opposite after removing tail
#
#    >>> insert_into_heap([1,2], [3,4,5], 1, True)
#    ([1, 1, 2], [3, 4, 5])
#    >>> insert_into_heap([1,2], [3,4,5], 2, True)
#    ([1, 2, 2], [3, 4, 5])
#    >>> insert_into_heap([1,2], [3,4,5], 3, True)
#    ([1, 2, 3], [3, 4, 5])
#    >>> insert_into_heap([1,2], [3,4,5], 4, True)
#    ([1, 2, 3], [4, 4, 5])
#    >>> insert_into_heap([1,2], [3,4,5], 5, True)
#    ([1, 2, 3], [4, 5, 5])
#    >>> insert_into_heap([1,2], [3,4], 2, False)
#    ([1, 2], [2, 3, 4])
#    >>> insert_into_heap([1,2], [3,4], 4, False)
#    ([1, 2], [3, 4, 4])
#    >>> insert_into_heap([1,2], [4,5], 3, False)
#    ([1, 2], [3, 4, 5])
#    """
#    if equal_heaps:
#        if number < max_heap[-1]:
#            max_heap.insert(0, number)
#        elif number > min_heap[0]:
#            max_heap.append(min_heap.pop(0))
#            if number > min_heap[-1]:
#                min_heap.append(number)
#            else:
#                for i, heap_num in enumerate(min_heap):
#                    if number <= heap_num:
#                        min_heap.insert(i, number)
#                        break
#        else:
#            max_heap.append(number)
#    else:
#        if number < max_heap[-1]:
#            max_heap.insert(0, number)
#            min_heap.insert(0, max_heap.pop())
#        elif number > min_heap[0]:
#            min_heap.append(number)
#        else:
#            min_heap.insert(0, number)
#    return max_heap, min_heap
#
#def remove_from_heap(max_heap, min_heap, number, equal_heaps):
#    """
#    >>> remove_from_heap([1,2], [3,4,5], 1, False)
#    ([2, 3], [4, 5])
#    >>> remove_from_heap([1,2], [3,4,5], 2, False)
#    ([1, 3], [4, 5])
#    >>> remove_from_heap([1,2], [3,4,5], 3, False)
#    ([1, 2], [4, 5])
#    >>> remove_from_heap([1,2], [3,4,5], 4, False)
#    ([1, 2], [3, 5])
#    >>> remove_from_heap([1,2], [3,4,5], 5, False)
#    ([1, 2], [3, 4])
#    >>> remove_from_heap([1,2], [3, 4], 2, True)
#    ([1], [3, 4])
#    >>> remove_from_heap([1,2], [3, 4], 3, True)
#    ([1], [2, 4])
#    >>> remove_from_heap([1,2], [3, 4], 1, True)
#    ([2], [3, 4])
#    """
#    if equal_heaps:
#        if number <= max_heap[-1]:
#            max_heap.remove(number)
#        else:
#            min_heap.remove(number)
#            min_heap.insert(0, max_heap.pop())
#    else:
#        if number <= max_heap[-1]:
#            max_heap.remove(number)
#            max_heap.append(min_heap.pop(0))
#        else:
#            min_heap.remove(number)
#            min_heap.insert(0, min_heap.pop(min_heap.index(min(min_heap))))
#    return max_heap, min_heap

#def median_heaps(max_heap, min_heap, equal_heaps):
#    """
#    >>> median_heaps([1,2], [3, 4, 5], False)
#    3
#    >>> median_heaps([1,2], [3, 4], True)
#    2.5
#    """
#    return (max_heap[-1] + min_heap[0]) / 2 if equal_heaps else min_heap[0]
        
    
### v0.3 too slow
#    notifications = 0
#    # fixed length list = median_days
#    median_list = sorted(expenditure[:median_days + 1])
#    median_pos = get_median_pos(median_days)
#    for day in range(median_days, num_days):
#        # calculate median
#        median = get_median(median_pos, median_list)
#        if expenditure[day] >= 2 * median:
#            notifications += 1
#        # remove last day from median_list
#        median_list.remove(expenditure[day - median_days])
#        # slot in first day in appropriate slot
#        bisect.insort_left(median_list, expenditure[day])
#    return notifications
#
#def binary_insert(amount, median_list):
#    """Inserts int amount into appropriate location in sorted median_list
#    >>> binary_insert(5, [2, 4, 6, 7, 8])
#    [2, 4, 5, 6, 7, 8]
#    >>> binary_insert(1, [2, 4, 6, 7, 8])
#    [1, 2, 4, 6, 7, 8]
#    >>> binary_insert(9, [2, 4, 6, 7, 8])
#    [2, 4, 6, 7, 8, 9]
#    >>> binary_insert(2, [2, 2, 2, 2, 2])
#    [2, 2, 2, 2, 2, 2]
#    """
#    bisect.insort_left(median_list, amount)
#    return median_list
#
#def get_median_pos(median_days):
#    """Calculates tuple median_pos given int median_days
#    >>> get_median_pos(5)
#    (2,)
#    >>> get_median_pos(6)
#    (2, 3)
#    """
#    if median_days % 2 == 0:
#        median_pos = (median_days // 2 - 1, median_days // 2)
#    else:
#        median_pos = ((median_days // 2),)
#    return median_pos 
#
#def get_median(median_pos, median_list):
#    """Find median from given tuple positions in list
#    >>> get_median((1,), [1, 2, 3])
#    2
#    >>> get_median((1, 2), [1, 2, 3, 4])
#    2.5
#    """
#    if len(median_pos) == 1:
#        return median_list[median_pos[0]]
#    else:
#        median = 0
#        for d in median_pos:
#            median += median_list[d]
#        return median / len(median_pos)

### v0.2 too slow
#def count_frauds(num_days, median_days, expenditure):
#    from statistics import median
#    notifications = 0
#    for day in range(median_days, num_days):
#        med = median(expenditure[day - median_days:day])
#        if expenditure[day] >= 2 * med:
#            notifications += 1
#    return notifications

### v0.1 too slow
#def count_frauds(num_days, median_days, expenditure):
#    notifications = 0
#    for day in range(median_days, num_days):
#        median = sorted(expenditure[day - median_days:day])
#        if median_days  % 2 == 0:
#            median = sum(median[median_days // 2 - 1:median_days // 2 + 1]) / 2
#        else:
#            median = median[len(median)//2]
#        if expenditure[day] >= 2 * median:
#            notifications += 1
#    return notifications

def test():
    import doctest
    print(doctest.testmod())
    import random
    print("STRESS TEST")
    while True:
        number_days = 200000
        #median_days = random.randint(1, number_days) 
        median_days = 100000
        #median_days = 2
        expenditure = [random.randint(0, 200) for _ in range(number_days)]
        print(count_frauds(number_days, median_days, expenditure))

#def test():
#    print("TEST01:", "pass" if count_frauds(9, 5, 
#        [2, 3, 4, 2, 3, 6, 8, 4, 5]) == 2 else "**FAIL**")
#    print("TEST02:", "pass" if count_frauds(5, 4, 
#        [1, 2, 3, 4, 4]) == 0 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])

