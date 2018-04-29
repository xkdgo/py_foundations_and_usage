#!/usr/bin/python

graph = { 'A':set(['B','C']),
          'B':set(['E','F']),
          'C':set(['G','H']),
          'G':set([]),
          'H':set([]),
          'F':set(['B']),
          'E':set([])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited



print(dfs(graph, 'C'))
print(dfs(graph, 'H'))
print(dfs(graph, 'A'))
