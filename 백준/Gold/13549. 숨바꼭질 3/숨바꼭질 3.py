# 다익스트라 = heapq + distances[]
import heapq

n, k = map(int, input().split())
answer = 0
if n > k:
    answer = n - k
elif n == k:
    answer = 0
else:
    q = []
    heapq.heappush(q, (0, n))
    distances = [float('inf') for _ in range(2*k)]
    distances[n] = 0
    if n < k:
        while q:
            dist, node = heapq.heappop(q)

            if dist > distances[node]:
                continue
            if 2*node < len(distances) and dist < distances[2*node]:
                distances[2*node] = dist
                heapq.heappush(q, (dist, 2*node))

            if node - 1 >= 0 and dist + 1 < distances[node - 1]:
                distances[node - 1] = dist + 1
                heapq.heappush(q, (dist + 1, node - 1))
            if node + 1 < len(distances) and dist + 1 < distances[node + 1]:
                distances[node + 1] = dist + 1
                heapq.heappush(q, (dist + 1, node + 1))
        
        answer = distances[k]
print(answer)