"""
DFS implementation using loops
"""

d = { 
    'e': [],
    'c': ['e'],
    'b': ['d'],
    'd': ['f'],
    'f': [],
    'a': ['c', 'b'],
    }

def dfs_loop(d):
    visited = []
    stack = []
    for node, neighbours in d.items():
        while len(visited) != len(d):
            if node in visited:
                break
            print(node)
            visited.append(node)
            stack += d[node]
            if not stack:
                break
            node = stack.pop()


dfs_loop(d)
