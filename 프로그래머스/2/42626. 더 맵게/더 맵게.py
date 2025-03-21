import heapq

def solution(scoville, K):
    answer = 0
    flag = True
    
    heapq.heapify(scoville)
    
    while len(scoville)>0:
        if scoville[0]>=K:
            flag = False
            break
            
        if len(scoville)==1:
            break
            
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer+=1
    
    if flag:
        answer = -1
    
    return answer