n = int(input())
arr = list(input() for _ in range(n))
# 왼쪽 위는 괄호 열기, 오른쪽 아래는 괄호 닫기
def dfs(la, len):
  # la = left_above
  # row = la[0], col = la[1]
  if len < 1:
    return

  total_zflag = False
  total_oflag = False
  for i in range(la[0], la[0]+len):
    for j in range(la[1], la[1]+len):
      if arr[i][j] == '0':
        total_zflag = True
      else:
        total_oflag = True

  if (total_zflag == True and total_oflag == False) or (total_zflag == False and total_oflag == True):
    if total_zflag:
      print('0', end='')
    else:
      print('1', end='')
    return

  rect_len = len//2
  for row_place in range(2):
    for col_place in range(2):
      zflag = False
      oflag = False
      row_start = la[0] + (rect_len*row_place)
      col_start = la[1] + (rect_len*col_place)
      for i in range(row_start, row_start+rect_len):
        for j in range(col_start, col_start+rect_len):
          if arr[i][j] == '0':
            zflag = True
          else:
            oflag = True
      
      if row_place == 0 and col_place == 0:
        print('(', end='')

      if zflag and oflag == False:
        print('0', end='')
      elif oflag and zflag == False:
        print('1', end='')
      else:
        dfs((row_start, col_start), rect_len)

      if row_place == 1 and col_place == 1:
        print(')', end='')
          
dfs((0, 0), n)
