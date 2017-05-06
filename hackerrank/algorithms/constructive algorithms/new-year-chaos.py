#!/usr/bin/env python2

TEST_MODE = False 

def main():
  for _ in range(int(raw_input().strip())):
    n = int(raw_input().strip())
    queue = map(int, raw_input().strip().split())
    print bribe(n, queue)
  return

def bribe(n, queue):
  #bubble sort backwards but keep tabs on not exceeding 2 steps
  steps = 0
  bribes_left = {x: 2 for x in range(1, n+1)}
  sorted_queue = [x for x in range(1, n+1)]
  loop_count = n-1
  while queue != sorted_queue:
    for i in range(loop_count):
      if queue[i] > queue[i+1]:
        queue[i], queue[i+1] = queue[i+1], queue[i]
        steps += 1
        if bribes_left[queue[i+1]] > 0:
          bribes_left[queue[i+1]] -= 1
        else:
          return "Too chaotic"
    loop_count -= 1
  return steps

def test():
  print bribe(5, [2, 1, 5, 3, 4])
  print bribe(5, [2, 5, 1, 3, 4])
  return

test() if TEST_MODE else main()
