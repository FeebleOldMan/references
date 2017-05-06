#!/usr/bin/env python2

TEST_MODE = True

def main():
  len_a = input()
  arr_a = map(int, raw_input().strip().split())
  len_b = input()
  arr_b = map(int, raw_input().strip().split())
  print find_missing(arr_a, arr_b)

def find_missing(arr_a, arr_b):
  arr_out = [0]*100
  start = min(arr_b)
  for i in arr_a:
    arr_out[i-start] -= 1
  for j in arr_b:
    arr_out[j-start] += 1
  output = []
  for i in range(100):
    if arr_out[i] > 0:
      output.append(str(i+start))
  return ' '.join(output)

### v0.1 too slow
#def find_missing(arr_a, arr_b):
#  for num in arr_a:
#    arr_b.remove(num)
#  return ' '.join(map(str, sorted(list(set(arr_b)))))

def test():
  print "TEST01:", "pass" if find_missing([203,204,205,206,207,208,203,204,205,206], [203,204,204,205,206,207,205,208,203,206,205,206,204]) == '204 205 206' else "**FAIL**"

test() if TEST_MODE else main()
