# return list of all nodes in the graph
from collections import defaultdict


def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited, path)
    return path


v, e = map(int, input().split())
graph = defaultdict(list)
for i in range(e):
    u, x = input().split()
    graph[u].append(x)
    graph[x].append(u)

path = []
start = 'A'
visited = defaultdict(bool)
traverse = dfs(graph, start, visited, path)
print(traverse)
