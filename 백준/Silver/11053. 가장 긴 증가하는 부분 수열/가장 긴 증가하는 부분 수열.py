n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
maximum = 1
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])
    if maximum < dp[i]:
        maximum = dp[i]
print(maximum)