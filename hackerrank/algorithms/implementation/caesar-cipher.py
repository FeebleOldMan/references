#!/usr/bin/env python

TEST_MODE = True

def main():
    length = int(raw_input().strip())
    input_string = raw_input().strip()
    enc_key = int(raw_input().strip())
    print encrypt(input_string, enc_key)

def encrypt(input_string, enc_key):
    input_arr = list(input_string)
    for i, letter in enumerate(input_arr):
        if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            input_arr[i] = chr((((ord(letter) - 65) + enc_key) % 26) + 65)
        elif ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            input_arr[i] = chr((((ord(letter) - 97) + enc_key) % 26) + 97)
    return ''.join(input_arr)

def test():
    print 'test1:', 'pass' if encrypt('middle-Outz', 2) == 'okffng-Qwvb' else "**FAIL**"
    print encrypt('middle-Outz', 2)
    return

test() if TEST_MODE else main()
