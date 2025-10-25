from collections import defaultdict
def solution(n, results):
    # 위상정렬 아님
    # 플루이드 와샬 이용하되, 나 기준으로 다 연결됐는지만 확인
    answer = 0
    board = [[0]*n for _ in range(n)]
    
    for a, b in results:
        board[a-1][b-1] = 1 # 승리
        board[b-1][a-1] = -1 # 패배
    #print(board)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j: # 대각선 방향 무시
                    continue
                if board[i][j] != 0: # 이미 값이 들어있으면 무시
                    continue
                if board[i][k] == board[k][j] == 1: # i->k->j 경로가 존재
                    board[i][j] = 1
                    board[j][i] = -1
    #print(board)
    for row in board:
        if row.count(0) == 1:
            answer += 1
    
    return answer