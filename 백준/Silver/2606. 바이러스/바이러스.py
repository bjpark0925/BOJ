from collections import deque, defaultdict
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

graph = defaultdict(set)
for i in range(e):
    vertex, neighbor = map(int, input().split())
    graph[vertex].add(neighbor)
    graph[neighbor].add(vertex)

bfs_queue = deque([1])
visited = {1}
answer = 0
while bfs_queue:
    node = bfs_queue.popleft()
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            bfs_queue.append(neighbor)
            visited.add(neighbor)
            answer+=1

print(answer)
'''
1:2,5
2:1,3,5
3:2
4:7
5:1,2,5
6:5
7:4
'''