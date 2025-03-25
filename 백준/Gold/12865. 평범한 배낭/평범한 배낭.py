n, m = map(int, input().split())
arr = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, m+1):
        if j >= w:
            arr[i][j] = max(v+arr[i-1][j-w], arr[i-1][j])
        else:
            arr[i][j] = arr[i-1][j]

print(arr[n][m])