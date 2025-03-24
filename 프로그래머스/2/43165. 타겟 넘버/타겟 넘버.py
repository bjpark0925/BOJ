def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(idx, current_sum):
        global answer
        if idx == len(numbers):
            if current_sum == target:
                answer+=1
            return
        
        dfs(idx+1, current_sum+numbers[idx])
        dfs(idx+1, current_sum-numbers[idx])
    
    dfs(0,0) # -> dfs(1,4) -> dfs(2,5) -> dfs(3,7)
    
    return answer