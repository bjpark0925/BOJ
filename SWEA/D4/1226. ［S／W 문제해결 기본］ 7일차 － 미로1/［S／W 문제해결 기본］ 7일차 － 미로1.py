for _ in range(10):
    T = int(input())
    maze = [list(input()) for _ in range(16)]
    start_row = -1
    start_col = -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                start_row = i
                start_col = j

    answer = 0
    visited = set()
    def dfs(row, col):
        global answer
        if maze[row][col] == '1' or answer == 1:
            return
        elif maze[row][col] == '3':
            answer = 1
            return

        visited.add((row, col))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for d_row, d_col in directions:
            n_row = row + d_row
            n_col = col + d_col
            if n_row < 0 or n_row > 15 or n_col < 0 or n_col > 15:
                continue
            if (n_row, n_col) not in visited:
                #print(row + d_row, col + d_col)
                dfs(n_row, n_col)

    dfs(start_row, start_col)

    print("#{} {}".format(T, answer))
