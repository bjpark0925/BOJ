def solution(people, limit):
    # 투 포인터
    # 합이 limit보다 크면 end만 탑승, 아니면 둘다 탑승
    # 50 50 70 80
    people.sort()
    
    answer = 0
    start = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
            
    return answer