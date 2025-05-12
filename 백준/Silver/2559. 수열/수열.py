import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefixSum = []
prefixSum.append(sum(arr[:k]))
for i in range(n-k):
    prefixSum.append(prefixSum[-1] - arr[i] + arr[i+k])

print(max(prefixSum))