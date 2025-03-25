import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefixSum = [0]
tmp = 0

for num in arr:
    tmp += num
    prefixSum.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefixSum[j] - prefixSum[i-1])