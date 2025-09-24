import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#print(arr)
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    prev = i + arr[i][0]
    if prev > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(arr[i][1] + dp[prev], dp[i+1])

print(dp[0])