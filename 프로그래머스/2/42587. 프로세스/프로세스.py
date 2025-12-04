from collections import deque
def solution(priorities, location):
    answer = 0
    pq = deque(priorities)
    lq = [i for i in range(len(priorities))]
    lq = deque(lq)
    #print(pq, lq)
    maximum = max(pq)
    while pq:
        pnum = pq.popleft()
        lnum = lq.popleft()
        if pnum == maximum:
            if lnum == location:
                answer += 1
                return answer                    
            else:
                answer += 1
                maximum = max(pq)
        else:
            pq.append(pnum)
            lq.append(lnum)
    
    return answer