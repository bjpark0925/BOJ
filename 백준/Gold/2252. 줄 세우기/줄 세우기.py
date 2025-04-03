# 위상정렬
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = defaultdict(list)
inDegree = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    inDegree[b]+=1

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)
        
line = []

while q:
    now = q.popleft()
    line.append(now)
    
    for neighbor in graph[now]:
        inDegree[neighbor]-=1
        if inDegree[neighbor] == 0:
            q.append(neighbor)

print(*line)