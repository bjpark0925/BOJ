import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    op = int(input())
    if op == 0:
        if arr:
            value = heapq.heappop(arr)
            print(value*(-1))
        else:
            print(0)
    else:
        heapq.heappush(arr, op*(-1))
