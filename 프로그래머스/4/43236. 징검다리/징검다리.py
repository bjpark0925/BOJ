from collections import deque
def solution(distance, rocks, n):
    rocks.sort() # 2 11 14 17 21
    #print(rocks)
    diff = [] # 2 9 3 3 4 4
    diff.append(rocks[0])
    for i in range(len(rocks)-1):
        diff.append(rocks[i+1] - rocks[i])
    diff.append(distance - rocks[-1])
    #print(diff)
    
    left = 0
    right = distance
    while left <= right:
        mid = (left + right) // 2 # answer
        cnt = 0 # 치운 돌 수
        q = deque(diff)
        while q:
            x = q.popleft()
            if x < mid:
                cnt += 1
                if q:
                    y = q.popleft()
                    q.appendleft(x+y)
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
        
    return right