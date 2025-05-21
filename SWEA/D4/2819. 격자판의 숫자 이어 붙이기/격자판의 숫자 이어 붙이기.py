T = int(input())
for tc in range(T):
    arr = [list(input().split()) for _ in range(4)]
    num_set = set()

    def dfs(row, col, num_str):
        if len(num_str) == 7:
            num_set.add(num_str)
            return
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for d in directions:
            n_row = row + d[0]
            n_col = col + d[1]
            if n_row < 0 or n_row > 3 or n_col < 0 or n_col > 3:
                continue
            dfs(n_row, n_col, num_str + arr[n_row][n_col])

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    print("#{} {}".format(tc+1, len(num_set)))
