#!/usr/bin/env python2

def main():
  for _ in range(input()):
    rows, cols = map(int, raw_input().strip().split())
    matrix = []
    for _row in range(rows):
      matrix.append(list(raw_input().strip()))
    guess = input()
    print check_guess(rows, cols, matrix, guess)

def check_guess(rows, cols, matrix, guess):
  start, end = None, None
  directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
  stack = []
  for row, data in enumerate(matrix):
    if start and end:
      break
    else:
      if not start:
        try:
          start = [row, data.index('M')]
        except ValueError:
          pass
      if not end:
        try:
          end = [row, data.index('*')]
        except ValueError:
          pass
  stack.append([start, start]) # next step, parent step
  matrix[start[0]][start[1]] = 0
  while stack:
    curr_step, parent_step = stack.pop()
    if curr_step == end:
      return 'Impressed' if matrix[end[0]][end[1]] == guess else 'Oops!'
    available_dirs = 0
    for move in directions:
      next_step = [curr_step[0] + move[0], curr_step[1] + move[1]]
      if next_step[0] < 0 or next_step[0] == rows or next_step[1] < 0 or next_step[1] == cols or matrix[next_step[0]][next_step[1]] not in ['.', '*']:
        pass
      else:
        available_dirs += 1
        stack.append([next_step, curr_step])
        matrix[next_step[0]][next_step[1]] = matrix[curr_step[0]][curr_step[1]]
    if available_dirs > 1:
      matrix[curr_step[0]][curr_step[1]] += 1
      for i in range(1, available_dirs+1):
        matrix[stack[-i][0][0]][stack[-i][0][1]] = matrix[curr_step[0]][curr_step[1]]
  return 'Impressed' if matrix[end[0]][end[1]] == guess else 'Oops!'

main()
