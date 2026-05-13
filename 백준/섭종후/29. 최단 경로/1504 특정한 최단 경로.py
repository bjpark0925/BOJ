from collections import defaultdict
import heapq

def dijk(start):
  q = [] # (거리, 정점) 저장
  heapq.heappush(q, (0, start))

  distances = [1e9] * (n+1)
  distances[start] = 0

  while q:
    dist, node = heapq.heappop(q)
    if dist > distances[node]:
      continue
    for neighbor, weight in graph[node]:
      if dist + weight < distances[neighbor]:
        distances[neighbor] = dist + weight
        heapq.heappush(q, (dist+weight, neighbor))

  return distances

# 다익스트라 = 힙큐, distances 필요
n, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
  u, v, c = map(int, input().split())
  graph[u].append((v,c))
  graph[v].append((u,c))
v1, v2 = map(int, input().split())
# 1-v1-v2-N 또는 1-v2-v1-N 중 최단경로 길이 리턴
# 경우1에서 1-v1는 1-N 다익스트라 후 확인, v1-v2는 v1-N 다익스트라 후 확인, v2-N은 v2-N 다익스트라 후 확인

arr_1 = dijk(1)
arr_v1 = dijk(v1)
arr_v2 = dijk(v2)
answer = min(arr_1[v1] + arr_v1[v2] + arr_v2[n], arr_1[v2] + arr_v2[v1] + arr_v1[n])

if answer >= 1e9:
  print(-1)
else:
  print(answer)
