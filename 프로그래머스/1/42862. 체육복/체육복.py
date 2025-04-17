def solution(n, lost, reserve):
    # 도난 and 여분 학생 고려
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    # set는 숫자 데이터에 한해 자동정렬됨
    # 따라서 체육복 빌려주기는 나보다 앞번호 먼저 수행해야 함
    for reserve_index in new_reserve:
        if reserve_index-1 in new_lost:
            new_lost.remove(reserve_index-1)
        elif reserve_index+1 in new_lost:
            new_lost.remove(reserve_index+1)
    
    return n - len(new_lost)