#!/usr/bin/env python2

TEST_MODE = False

def main():
  for _tests in range(int(raw_input().strip())): # no. of test cases
    layout = {}
    for _ladders in range(int(raw_input().strip())): # no. of ladders
      start, end = map(int, raw_input().strip().split())
      layout[start] = end
    for _snakes in range(int(raw_input().strip())): # no. of snakes
      start, end = map(int, raw_input().strip().split())
      layout[start] = end
    print optimize_moves(layout)
  return

### v0.4 going to merge the input layout with adjacency list
def optimize_moves(layout):
  board = {x: [x+i for i in range(1, 7)] for x in range(1, 95)}
  for _i in range(95, 101):
    board[_i] = [x for x in range(_i+1, 101)]
  for box in layout:
    board[box] = layout[box]
  # start bfs
  distance = {x: 999 for x in range(1, 101)}
  parent = {x: None for x in range(1, 101)}
  root = 1
  queue = [root]
  distance[root] = 0
  while queue:
    current = queue.pop(0)
    if type(board[current]) is not list:
      distance[board[current]] = distance[current]
      parent[board[current]] = current
      queue.append(board[current])
    else:
      for node in board[current]:
        if distance[node] > (distance[current] + 1):
          distance[node] = distance[current] + 1
          parent[node] = current
          queue.append(node)
  return distance[100] if distance[100] < 999 else -1

def test():
  return


test() if TEST_MODE else main()

### v0.3 class implementation. a bit complex. gonna rewrite simple function
#class Board:
#    def __init__(self):
#        self._layout = {x: [x+i for i in range(1, 7)] for x in range(1, 95)}
#        for _i in range(95, 101):
#          self._layout[_i] = [x for x in range(_i+1, 101)]
#        self._distance = [999]*100
#        self._pos = 1
#        self._move_count = 0
#    def add_layout(self, start, end):
#        self._layout[start] = [end]
#    def get_layout(self):
#        return self._layout
#    def set_distance(self, pos, dist):
#        self._distance[pos-1] = dist
#    def get_distance(self, pos):
#        return self._distance[pos-1]
#    def add_move_count(self):
#        self._move_count += 1
#    def get_move_count(self):
#        return self._move_count
#    def get_pos(self):
#        return self._pos
#    def move(self, roll):
#        pos = get_pos() + roll
#        pos = get_layout()[pos] # move up/down if needed
#        return pos
#    def update_pos(self, pos):
#        self._pos = pos
#### v0.2
#    # generate tree of moves? should not exceed 100 else board is looped
#    def optimize_moves(self):
#      root = 1
#      queue = [root]
#      self.set_distance(root, 0)
#      while queue:
#        current = queue.pop(0)
#        print self.get_layout()[current], queue, self.get_distance(100)
#        if len(self.get_layout()[current]) == 1:
#          queue.append(self.get_layout()[current][0])
#        else:
#          for node in self.get_layout()[current]:
#            if self.get_distance(node) > (self.get_distance(current) + 1):
#              self.set_distance(node, self.get_distance(current) + 1)
#              queue.append(node)
#      return self.get_distance(100)

### v0.1
#class Board:
#    def __init__(self):
#        self._ladders = {}
#        self._snakes = {}
#        self._pos = 1
#        self._move_count = 0
#    def add_ladder(self, start, end):
#        self._ladders[start] = end
#    def get_ladders(self):
#        return self._ladders
#    def add_snake(self, start, end):
#        self._snakes[start] = end
#    def get_snakes(self):
#        return self._snakes
#    def add_move_count(self):
#        self._move_count += 1
#    def get_move_count(self):
#        return self._move_count
#    def get_pos(self):
#        return self._pos
#    def move(self, roll):
#        pos = self._pos + roll
#        pos = self._ladders.get(pos, pos) # move up if needed
#        pos = self._snakes.get(pos, pos) # move down if needed
#        return pos
#    def update_pos(self, pos):
#        self._pos = pos

### doesn't work if player gets 'trapped'
#    def optimize_moves(self):
#        while self.get_pos() != 100:
#            best_pos = self.get_pos()
#            # for best move, start by rolling each number from 6 to 1
#            for roll in range(6, 0, -1):
#            # check each move's ending pos for max
#                move_pos = self.move(roll)
#                if (move_pos > best_pos) and (move_pos <= 100):
#                    best_pos = move_pos
#            # update pos using best_move
#            self.update_pos(best_pos)
#            # increment move count
#            self.add_move_count()
#        return self.get_move_count()
#
#def main():
#    for _tests in range(int(raw_input().strip())): # no. of test cases
#        board = Board()
#        for _ladders in range(int(raw_input().strip())): # no. of ladders
#            start, end = map(int, raw_input().strip().split())
#            board.add_layout(start, end)
#        for _snakes in range(int(raw_input().strip())): # no. of snakes
#            start, end = map(int, raw_input().strip().split())
#            board.add_layout(start, end)
#        print board.optimize_moves()
#
#def test():
#    board = Board()
#    board.add_layout(32, 62)
#    board.add_layout(42, 68)
#    board.add_layout(12, 98)
#    board.add_layout(95, 13)
#    board.add_layout(97, 25)
#    board.add_layout(93, 37)
#    board.add_layout(79, 27)
#    board.add_layout(75, 19)
#    board.add_layout(49, 47)
#    board.add_layout(67, 17)
#    print board.optimize_moves()

