from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = defaultdict(set)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)

q = deque()
visited = set()
answer = 0

q.append((a, 0))
visited.add(a)

while q:
    now, chon = q.popleft()
    if now == b:
        answer = chon
        break

    for neighbor in graph[now]:
        if neighbor not in visited:
            q.append((neighbor, chon+1))
            visited.add(neighbor)

if answer == 0:
    answer = -1
print(answer)