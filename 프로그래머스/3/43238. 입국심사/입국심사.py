def solution(n, times):
    left = 0
    right = min(times) * n
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        for time in times:
            cnt += mid // time
        
        if cnt >= n:
            right = mid-1
        else:
            left = mid+1
    
    return left