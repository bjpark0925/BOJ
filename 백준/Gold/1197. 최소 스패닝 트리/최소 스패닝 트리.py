from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c)) # 무방향
'''
graph = {
1:[(2,1),(3,3)], # (정점,비용)
2:[(1,1),(3,2)]
3:[(1,3),(2,2)]
}
'''
pq = []
heapq.heappush(pq, (0,1)) # (비용,정점) 1번부터 시작
visited = set()
answer = 0
# 프림 알고리즘
while pq and len(visited) < v:        
    current_d, current_v = heapq.heappop(pq)
    if current_v not in visited:
        answer+=current_d
        visited.add(current_v)
        for neighbor_v, neighbor_d in graph[current_v]:
            if neighbor_v not in visited:
                heapq.heappush(pq, (neighbor_d, neighbor_v))

print(answer)