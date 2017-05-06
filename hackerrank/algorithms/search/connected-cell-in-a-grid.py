#!/usr/bin/env python2

TEST_MODE = False

def main():
  rows = input()
  cols = input()
  matrix = []
  for _ in range(rows):
    matrix.append(map(int, raw_input().strip().split()))
  print largest(rows, cols, matrix)

def largest(rows, cols, matrix):
  directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
  high_score, current_score = 0, 0
  visited = []
  for row in range(rows):
    for col in range(cols):
      if matrix[row][col] == 1 and [row, col] not in visited:
        current_score = 1
        stack = [[row, col]]
        visited.append([row, col])
        while len(stack):
          curr_row, curr_col = stack.pop()
          for adj in directions:
            next_row = curr_row + adj[0]
            next_col = curr_col + adj[1]
            if next_row >= 0 and next_row < rows and next_col >= 0 and next_col < cols and [next_row, next_col] not in visited and matrix[next_row][next_col] == 1:
              stack.append([next_row, next_col])
              visited.append([next_row, next_col])
              current_score += 1
        if current_score > high_score:
          high_score = current_score
  return high_score

def test():
  print "TEST01:", "pass" if largest(4, 4, [[1,1,0,0],[0,1,1,0],[0,0,1,0],[1,0,0,0]]) == 5 else "**FAIL**"

test() if TEST_MODE else main()
