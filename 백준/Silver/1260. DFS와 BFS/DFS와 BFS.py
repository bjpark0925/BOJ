import sys
sys.setrecursionlimit(10**6)
from collections import deque

n, m, v = map(int, input().split())
graph = {}
for i in range(m):
    a, b = map(int, input().split())
    if graph.get(a) == None:
        graph[a] = {b}
    else:
        graph[a].add(b)
    if graph.get(b) == None:
        graph[b] = {a}
    else:
        graph[b].add(a)

# dfs
dfs_visited = {}
dfs_answer = []
def dfs(graph, vertex):
    dfs_answer.append(vertex)
    if vertex not in graph or dfs_visited.get(vertex) == True:
        return
    
    dfs_visited[vertex] = True
    linked_vertex = sorted(list(graph[vertex]))
    for vt in linked_vertex:
        if dfs_visited.get(vt) == True:
            continue
        dfs(graph, vt)
    return
dfs(graph, v)
print(*dfs_answer)

# bfs
bfs_visited = {}
bfs_answer = []
bfs_queue = deque()
def bfs(graph, vertex):
    bfs_answer.append(vertex)
    if vertex not in graph:
        return
    
    bfs_visited[vertex] = True
    linked_vt = sorted(list(graph[vertex]))
    for vt in linked_vt:
        if bfs_visited.get(vt) == True:
            continue
        bfs_queue.append(vt)
        bfs_visited[vt] = True
    
    if not bfs_queue:
        return
    bfs(graph, bfs_queue.popleft())
    return
bfs(graph, v)
print(*bfs_answer)