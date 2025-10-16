def solution(N, number):
    if N == number:
        return 1
    
    answer = -1
    dp = [set() for _ in range(8)]
    for i in range(8):
        temp = 0
        for j in range(i, -1, -1):
            temp += N*(10**j)
        dp[i].add(temp)
    #print(dp)
    
    for i in range(1, 8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if op2 != 0:
                        dp[i].add(op1//op2)
                    
        if number in dp[i]:
            answer = i+1
            break
    #print(dp)
    
    return answer