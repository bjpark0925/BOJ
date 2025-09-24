from collections import deque

T = int(input())
directions = ((-1,0),(1,0),(0,-1),(0,1))
for i in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer_room = n*n
    answer_cnt = 1
    for row in range(n):
        for col in range(n):
            q = deque()
            q.append((row, col, 1))
            visited = set()
            visited.add(arr[row][col])
            while q:
                x, y, cnt = q.popleft()
                if (cnt > answer_cnt) or (cnt == answer_cnt and arr[row][col] < answer_room):
                    answer_cnt = cnt
                    answer_room = arr[row][col]

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny] not in visited and arr[nx][ny] == arr[x][y]+1:
                        q.append((nx, ny, cnt+1))
                        visited.add(arr[nx][ny])

    print("#{} {} {}".format(i, answer_room, answer_cnt))
