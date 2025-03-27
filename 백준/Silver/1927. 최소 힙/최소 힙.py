import heapq
import sys
input = sys.stdin.readline

arr = []
n = int(input())

for i in range(n):
    order = int(input())
    if order == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, order)