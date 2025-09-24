import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
#print(arr)
air_row = 0
for row in range(2,r-2):
    if arr[row][0] == -1:
        air_row = row
        break
#print(air_row)

for _ in range(t):
    next_arr = [[0]*c for _ in range(r)]
    # 확산
    for row in range(r):
        for col in range(c):
            if (row == air_row or row == air_row + 1) and col == 0:
                continue
            # 자기한테 남는거
            if arr[row][col] != 0:
                direction_cnt = 0
                for neighbor_row, neighbor_col in ((row-1, col), (row, col-1), (row, col+1), (row+1, col)):
                    if (neighbor_row==air_row or neighbor_row==air_row+1) and neighbor_col==0:
                        continue
                    if 0<=neighbor_row<r and 0<=neighbor_col<c:
                        direction_cnt+=1
                next_arr[row][col] = arr[row][col] - ((arr[row][col]//5)*direction_cnt)

            # 옆에서 받는거
            for neighbor_row, neighbor_col in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
                if (neighbor_row == air_row or neighbor_row == air_row + 1) and neighbor_col == 0:
                    continue
                if 0 <= neighbor_row < r and 0 <= neighbor_col < c:
                    next_arr[row][col] += (arr[neighbor_row][neighbor_col]//5)
    #print("확산:",next_arr)

    next_arr2 = [[0]*c for _ in range(r)]
    # 순환
    for row in range(r):
        for col in range(c):
            # 아래로
            if (col == 0 and 0 < row < air_row) or (col == c-1 and row > air_row+1):
                next_arr2[row][col] = next_arr[row-1][col]
            # 왼쪽
            elif (row == 0 or row == r-1) and col < c-1:
                next_arr2[row][col] = next_arr[row][col+1]
            # 위로
            elif (col == c-1 and row < air_row) or (col == 0 and air_row+1 < row < r-1):
                next_arr2[row][col] = next_arr[row+1][col]
            # 오른쪽
            elif (row == air_row or row == air_row+1) and col > 1:
                next_arr2[row][col] = next_arr[row][col-1]
            # 공청 바로 오른쪽
            elif (row == air_row or row == air_row+1) and col == 1:
                next_arr2[row][col] = 0

            # 노 순환
            else:
                next_arr2[row][col] = next_arr[row][col]
    #print("순환:",next_arr2)
    arr = next_arr2

answer = 0
for row in range(r):
    for col in range(c):
        answer += arr[row][col]

print(answer)
