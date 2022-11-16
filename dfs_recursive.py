"""
DFS implementation using recursion
"""
d = { 
    'e': [],
    'c': ['e'],
    'b': ['d'],
    'd': ['f'],
    'f': [],
    'a': ['c', 'b'],
    }

def dfs_recursive(d, node, stack, visited):
    for node in d:
        if node in visited:
            continue
        visited.append(node)
        print(node)
        stack += d[node]
        if stack:
            dfs_recursive(d, stack.pop(), stack, visited)
        else:
            continue

dfs_recursive(d, 'e', stack=[], visited=[])

