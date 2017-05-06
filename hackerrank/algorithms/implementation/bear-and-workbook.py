#!/usr/bin/env python

def count(chapters, prob_per_page, probs):
    page = 0
    count = 0
    for chapter in range(chapters):
        for prob in range(1, probs[chapter]+1):
            if (prob % prob_per_page == 1) or prob_per_page == 1:
                page += 1
            if prob == page:
                count += 1
    return count

def main():
    chapters, prob_per_page = map(int, raw_input().strip().split())
    probs = map(int, raw_input().strip().split())
    print count(chapters, prob_per_page, probs)

def test():
    print count(5, 3, [4, 2, 6, 1, 10])
    print count(5, 1, [2, 3, 4, 5, 6])

main()
#test()
