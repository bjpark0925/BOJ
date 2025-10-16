def solution(numbers):
    answer = 0
    chae = [True] * 10**7
    chae[0] = False
    chae[1] = False
    for i in range(2, len(chae)):
        if i*i > len(chae):
            break
        if chae[i] == False:
            continue
        for j in range(i*2, len(chae), i):
            chae[j] = False
    #print(chae)
    
    l = len(numbers)
    answer_set = set()
    
    def dfs(old, new, visited_index):
        nonlocal answer
        num = old+new
        num_int = int(num)
        if chae[num_int] and num_int not in answer_set:
            #print(num_int)
            answer += 1
            answer_set.add(num_int)
        
        if len(num) == l:
            return
        
        for i in range(l):
            if i in visited_index:
                continue
            dfs(num, numbers[i], visited_index|{i})
        
        
    for i in range(l):
        if numbers[i] == '0':
            continue
        dfs('', numbers[i], {i})
    
    
    return answer