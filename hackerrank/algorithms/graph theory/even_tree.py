#!/usr/bin/env python3

import sys, getopt

def main(argv):
    help = """CODE! v1.0

Usage:
  python CODE.py [options]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(argv, "ht", ["help", "test",])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
    vertices, edges = map(int, input().strip().split())
    edge_map = [tuple(map(int, input().strip().split())) for _ in range(edges)]
    print(even_tree(vertices, edges, edge_map))

def even_tree(vertices, edges, edge_map):
    """Given a tree with N nodes number 1 to N rooted at 1, returns
    the maximum number of edges to remove from tree to get a forest
    such that each connect component of the forest contains an even
    number of vertices.

    >>> even_tree(10, 9,
    ...     [(2,1),(3,1),(4,3),(5,2),(6,1),(7,2),(8,6),(9,8),(10,8)])
    2
    """
    nodes = list(range(1, vertices + 1))
    tree_map = {node: [] for node in nodes}
    for edge in edge_map:
        tree_map[edge[0]].append(edge[1])
        tree_map[edge[1]].append(edge[0])
    forest_map = {}
    # create this using breadth/depth traversal. root is smallest number
    for node in range(1, vertices + 1):
        if node in nodes:
            nodes.delete(node)


    return tree_map

def test():
    import doctest
    print(doctest.testmod())

if __name__ == '__main__':
    main(sys.argv[1:])

