from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

V, E = map(int,input().split()) # 총 vertex, edge 수
K = int(input()) # 시작점
graph = defaultdict(list)
for i in range(E):
    u, v, w = map(int,input().split()) # u -> v의 edge 가중치가 w
    graph[u].append((v,w))
'''
graph = {5:[(1,1)],
1:[(2,2),(3,3)],
2:[(3,4),(4,5)],
3:[(4,6)]}
'''

queue = []
heapq.heappush(queue, (0,K))
distances = [float('inf') for _ in range(V+1)]
distances[K] = 0
while queue:
    dist, node = heapq.heappop(queue)
    if dist <= distances[node]:
        for neighbor, weight in graph[node]:
            if dist+weight < distances[neighbor]:
                distances[neighbor] = dist+weight
                heapq.heappush(queue, (dist+weight, neighbor))

for i in range(1, V+1):
    if distances[i] == float('inf'):
        print("INF")
    else:
        print(distances[i])