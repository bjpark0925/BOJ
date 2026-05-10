def dfs(row, col, size):
    num = arr[row][col]
    for i in range(row, row+size):
        for j in range(col, col+size):
            if arr[i][j] != num:
                half = size // 2
                result.append('(')
                dfs(row, col, half)
                dfs(row, col+half, half)
                dfs(row+half, col, half)
                dfs(row+half, col+half, half)
                result.append(')')
                return
    result.append(str(num))

n = int(input())
arr = list(input() for _ in range(n))
result = []
dfs(0,0,n)
print(*result, sep='')
