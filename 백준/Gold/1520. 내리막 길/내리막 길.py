import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]

def dfs(row, col):
    if row == 0 and col == 0:
        return 1
    if dp[row][col] != -1:
        return dp[row][col]
    
    dp[row][col] = 0
    if row > 0 and arr[row][col] < arr[row-1][col]:
        dp[row][col] += dfs(row-1,col)
    if row < m-1 and arr[row][col] < arr[row+1][col]:
        dp[row][col] += dfs(row+1,col)
    if col > 0 and arr[row][col] < arr[row][col-1]:
        dp[row][col] += dfs(row,col-1)
    if col < n-1 and arr[row][col] < arr[row][col+1]:
        dp[row][col] += dfs(row,col+1)

    return dp[row][col]

print(dfs(m-1,n-1))
