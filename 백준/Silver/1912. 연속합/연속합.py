n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
answer = dp[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
    if answer < dp[i]:
        answer = dp[i]

print(answer)