# ABCDEFGHIJKLMNOPQRSTUVWXYZ 26
# N->A 13
# 1. 정순 2. 끝으로 갔다가 N찍고 부메랑
# JBCANMO JBCAANAAA JBCAAZA 정순
# JBCAAANMO 8 8. 중간에 A스킵 구간이 끝문자열보다 많다면 N찍고 부메랑
# JBCAAAANMO 9 8
# BCAAABCD 7 5. 정순으로 C찍고 부메랑
# 좌우 먼저 계산->상하 계산
def solution(name):
    answer = 0
    # A스킵 구간 담는 배열
    A_skip = [0] * len(name)
    for i in range(len(name)):
        if name[i] == 'A':
            if i == 0:
                A_skip[i]+=1
            else:
                A_skip[i] = A_skip[i-1] + 1
    
    A_max = max(A_skip)
    A_end_index = 0
    for i in range(len(name)):
        if A_skip[i] == A_max:
            A_end_index = i
            break
    
    last_string_len = len(name) - A_end_index - 1 # BAAADDDAAAANMO
    
    # 좌우 이동
    # 정순
    if A_end_index - A_max >= 0:
        answer = len(name) - 1 - A_skip[-1]
    
    left_start_count = 0 # A 스킵 구간의 왼쪽으로 커서 이동 후 순회
    right_start_count = 0
    if A_max > 0 and A_end_index - A_max >= 0:
        left_start_count = (A_end_index - A_max) * 2 + last_string_len
        answer = min(answer, left_start_count)
        
        right_start_count = last_string_len * 2 + (A_end_index - A_max)
        answer = min(answer, right_start_count)
    
    # 상하 이동
    for alphabet in name:
        if alphabet == 'A':
            continue
        
        if alphabet > 'N':
            answer += 26 - (ord(alphabet) - ord('A'))
        else:
            answer += ord(alphabet) - ord('A')
        
    return answer