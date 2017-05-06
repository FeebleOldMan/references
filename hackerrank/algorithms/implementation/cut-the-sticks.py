#!/usr/bin/env python

def main():
    num_sticks = int(raw_input().strip())
    stick_arr = map(int, raw_input().strip().split())
    while len(stick_arr) != 0:
        print len(stick_arr)
        short_stick = min(stick_arr)
        for idx, stick in enumerate(stick_arr):
            stick_arr[idx] -= short_stick
        stick_arr = filter(lambda stick: stick != 0, stick_arr)

main()
