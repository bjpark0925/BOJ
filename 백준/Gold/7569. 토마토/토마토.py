from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
#print(arr)
answer = 0

def counting(box):
    z_cnt = 0
    o_cnt = 0
    for i in box:
        for j in i:
            for tomato in j:
                if tomato == 0:
                    z_cnt+=1
                elif tomato == 1:
                    o_cnt+=1
    return z_cnt, o_cnt

zero_cnt, one_cnt = counting(arr)
#print(zero_cnt, one_cnt)
if zero_cnt == 0:
    print(answer)
else:
    # 초기 상태
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    q.append((i,j,k,0))

    while q:
        now_i,now_j,now_k,now_day = q.popleft()
        for next_i, next_j, next_k in ((now_i+1, now_j, now_k), (now_i-1, now_j, now_k), (now_i, now_j+1, now_k), (now_i, now_j-1, now_k), (now_i, now_j, now_k+1), (now_i, now_j, now_k-1)):
            if 0<=next_i<h and 0<=next_j<n and 0<=next_k<m and arr[next_i][next_j][next_k] == 0:
                answer = max(answer, now_day+1)
                arr[next_i][next_j][next_k] = 1
                q.append((next_i,next_j,next_k,now_day+1))

    zero_cnt, one_cnt = counting(arr)
    if zero_cnt == 0:
        print(answer)
    else:
        print(-1)