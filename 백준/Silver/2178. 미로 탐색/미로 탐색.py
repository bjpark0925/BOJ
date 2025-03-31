from collections import deque

n, m = map(int, input().split())

# ✅ 미로 입력 방식 개선
miro = [list(map(int, input().strip())) for _ in range(n)]

# BFS 초기화
bfs_queue = deque([(0, 0)])
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1  # 시작 위치 방문 처리

# 이동 방향 (하, 우, 상, 좌)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# BFS 실행
while bfs_queue:
    x, y = bfs_queue.popleft()

    # 네 방향 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1 and not visited[nx][ny]:
            bfs_queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

# 최단 거리 출력
print(visited[n-1][m-1])
