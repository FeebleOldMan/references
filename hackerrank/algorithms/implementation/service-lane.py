#!/usr/bin/env python

def main():
    length, cases = map(int, raw_input().strip().split())
    width_arr = map(int, raw_input().strip().split())
    for _ in range(cases):
        enter, exit = map(int, raw_input().strip().split())
        print min(width_arr[enter:exit+1])

main()
