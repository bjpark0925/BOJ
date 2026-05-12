from collections import deque

t = int(input())
for _ in range(t):
  m,n,k = map(int, input().split()) # col, row, 배추 개수
  cabbages = [list(map(int, input().split())) for _ in range(k)]
  
  graph = [[0] * m for _ in range(n)]
  for cabbage in cabbages:
    row = cabbage[1]
    col = cabbage[0]
    graph[row][col] = 1
    
  q = deque()
  answer = 0
  for i in range(k):
    if graph[cabbages[i][1]][cabbages[i][0]] == 1:
      q.append(cabbages[i])
      graph[cabbages[i][1]][cabbages[i][0]] = -1 # visited 대신 -1 표시
      answer += 1
    while q:
      cabbage = q.popleft()
      row = cabbage[1]
      col = cabbage[0]
  
      directions = [(-1,0),(1,0),(0,-1),(0,1)]
      for dir in directions:
        dy = row + dir[0]
        dx = col + dir[1]
        if 0 <= dy < n and 0 <= dx < m and graph[dy][dx] == 1:
          q.append([dx, dy])
          graph[dy][dx] = -1

  print(answer)
  
