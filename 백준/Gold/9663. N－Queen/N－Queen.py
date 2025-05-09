import sys
input = sys.stdin.readline
n = int(input())

cnt = 0
visited = [-1] * n
visited_set = set() # not in 연산 위해 visited 리스트와 동일한 set 생성

def dfs(row):
    global cnt
    if row == n:
        cnt+=1
        return

    else:
        for col in range(n):
            if col not in visited_set: # 기존 퀸과 같은 열인지 조사
                for prev_row in range(row):
                    # 기존 퀸과 같은 대각선(가로 거리와 세로 거리가 동일)인지 조사
                    if row - prev_row == abs(col - visited[prev_row]): # 왼쪽 대각선은 음수, 오른쪽 대각선은 양수이므로 절댓값 필요
                        break
                else: # 현재 퀸의 위치가 보증되면
                    visited[row] = col # (row, col) 좌표에 퀸 놓기
                    visited_set.add(col)
                    dfs(row+1) # 다음 row에 퀸 놓기. 퀸은 row 하나에 하나씩만 존재
                    visited[row] = -1 # 초기화
                    visited_set.remove(col)

dfs(0)
print(cnt)