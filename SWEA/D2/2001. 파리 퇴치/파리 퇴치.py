T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    prefixSum = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]

    answer = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = prefixSum[i+m][j+m] - prefixSum[i][j+m] - prefixSum[i+m][j] + prefixSum[i][j]
            answer = max(answer, total)

    print("#{} {}".format(tc+1, answer))
