from collections import deque

n = int(input())
graph = [input() for _ in range(n)]
group = []
visited = set()
directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

for row in range(n):
    for col in range(n):
        if graph[row][col] == '1' and (row, col) not in visited:
            cnt = 1
            q = deque([(row, col)])
            visited.add((row, col))
            while q:
                now_row, now_col = q.popleft()
                for dr, dc in directions:
                    next_row = now_row + dr
                    next_col = now_col + dc
                    if next_row < 0 or next_row >= n:
                        continue
                    if next_col < 0 or next_col >= n:
                        continue
                    if graph[next_row][next_col] == '1' and (next_row, next_col) not in visited:
                        q.append((next_row, next_col))
                        visited.add((next_row, next_col))
                        cnt+=1
            group.append(cnt)

group.sort()
print(len(group))
for i in range(len(group)):
    print(group[i])