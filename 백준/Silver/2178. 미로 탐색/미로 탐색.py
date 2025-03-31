from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(n)]

bfs_queue = deque([(0,0)])
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1

directions = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우

while bfs_queue:
    prev_row, prev_col = bfs_queue.popleft()
    
    for d_row, d_col in directions:
        row = prev_row + d_row
        col = prev_col + d_col
        if row >= 0 and row < n and col >= 0 and col < m and miro[row][col] and not visited[row][col]:
            bfs_queue.append((row, col))
            visited[row][col] = visited[prev_row][prev_col] + 1

print(visited[n-1][m-1])