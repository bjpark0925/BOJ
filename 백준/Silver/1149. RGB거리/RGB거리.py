import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0] = arr[0]
for i in range(1, n):
    # 이전 B,G 비용 중 최솟값 + 현재 R 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0] # R
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1] # G
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2] # B

print(min(dp[n-1]))