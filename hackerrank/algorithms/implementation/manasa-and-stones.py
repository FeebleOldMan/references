#!/usr/bin/env python

TEST_MODE = True

def main():
    for _ in range(int(raw_input().strip())):
        n = int(raw_input().strip())
        a = int(raw_input().strip())
        b = int(raw_input().strip())
        print stones(n, a, b)

def stones(n, a, b):
    output = []
    for i in range(n):
        output.append(((i*a) + ((n-i-1)*b)))
    return ' '.join(map(str, sorted(list(set(output)))))

def test():
    print stones(3, 1, 2)
    print stones(4, 10, 100)
    return

test() if TEST_MODE else main()
