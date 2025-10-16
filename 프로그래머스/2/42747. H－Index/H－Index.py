def solution(citations):
    answer = 0
    citations.sort() # 0 1 3 5 6 7 8
    l = len(citations)
    for i in range(l-1, -1, -1):
        if citations[i] >= l-i:
            answer = l-i
    
    return answer