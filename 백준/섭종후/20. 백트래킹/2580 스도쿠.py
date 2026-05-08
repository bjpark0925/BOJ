import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      blank.append((i, j))

def check(num, row, col):
  # 가로 체크
  for i in range(9):
    if num == board[row][i]:
      return False

  # 세로 체크
  for i in range(9):
    if num == board[i][col]:
      return False

  # 정사각형 체크
  row_place = row // 3
  col_place = col // 3
  for i in range(row_place*3, row_place*3 + 3):
    for j in range(col_place*3, col_place*3 + 3):
      if num == board[i][j]:
        return False
  
  return True

def dfs(idx):
  if idx == len(blank):
    for i in range(9):
      print(*board[i])
    exit()

  row, col = blank[idx]
  for num in range(1, 10):
    if check(num, row, col):
      board[row][col] = num
      dfs(idx+1)
      board[row][col] = 0

dfs(0)
