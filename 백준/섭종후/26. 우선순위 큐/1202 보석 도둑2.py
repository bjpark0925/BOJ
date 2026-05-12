import heapq

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

# 둘 다 무게 기준 오름차순
jewels.sort()
bags.sort()

heap = [] # 최대힙(현재 가방에 넣을 수 있는 보석)
total = 0
jewel_idx = 0

for bag in bags:
  while jewel_idx < n and jewels[jewel_idx][0] <= bag:
    heapq.heappush(heap, -jewels[jewel_idx][1])
    jewel_idx += 1
  if heap:
    total += -heapq.heappop(heap)

print(total)
