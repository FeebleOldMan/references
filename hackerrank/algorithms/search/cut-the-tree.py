#!/usr/bin/env python2

TEST_MODE = False

def main():
  vertices = input()
  values = map(int, raw_input().strip().split())
  edges = [map(int, raw_input().strip().split()) for _ in range(vertices-1)]
  print min_diff(vertices, values, edges)


# find total
# div/2
# add branch until nearest to 2. start from smallest value

def min_diff(vertices, values, edges):
  tree = {}
  values = dict(zip(range(1, len(values)+1), values))
  for parent, child in edges:
    tree.setdefault(parent, set([])).add(child)
    tree.setdefault(child, set([])).add(parent)
  tree_sum = sum_tree(tree, values, edges[0][0], -1)
  small_root = values.values().index(min(values.values())) + 1  # find node of smallest value
  target_val = tree_sum / 2  # get as close to this as possible
  curr_val = 0
  min_val = float('inf')
  next_min_val = target_val
  visited, stack = set([]), [small_root]
  while next_min_val < min_val:
    min_val = next_min_val
    vertex = stack.pop()
    if vertex not in visited:
      visited.add(vertex)
      curr_val += values[vertex]
      next_min_val = abs(target_val - curr_val)
      stack.extend(tree[vertex] - visited)
  return min_val*2  # x 2 because min_val measures one sided distance from middle of tree

def sum_tree(tree, values, start, prune):
  """
  start   int input of root node of branch
  prune   int input of removed vertice of branch
  """
  sum_branch = 0
  visited, stack = set([prune]), [start]
  while stack:
    vertex = stack.pop()
    if vertex not in visited:
      visited.add(vertex)
      sum_branch += values[vertex]
      stack.extend(tree[vertex] - visited)
  return sum_branch

### v0.1 too slow
#def min_diff(vertices, values, edges):
#  tree = {}
#  values = dict(zip(range(1, len(values)+1), values))
#  min_value = float('inf')
#  for parent, child in edges:
#    tree.setdefault(parent, set([])).add(child)
#    tree.setdefault(child, set([])).add(parent)
#  for edge in edges:
#    # set the root of new trees as vertices of removed edge
#    # ignore when reach removed edge
#    branch1 = sum_tree(tree, values, edge[0], edge[1])
#    branch2 = sum_tree(tree, values, edge[1], edge[0])
#    if abs(branch1 - branch2) < min_value:
#      min_value = abs(branch1 - branch2)
#  return min_value

def test():
  return

test() if TEST_MODE else main()
