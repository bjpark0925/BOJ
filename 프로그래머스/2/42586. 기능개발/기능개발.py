def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    flag = [False] * length
    cnt = 0
    
    while cnt < length:
        for i in range(length):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
                if progresses[i] >= 100:
                    flag[i] = True
        
        for i in range(cnt, length):
            if flag[i] == False:
                if i != cnt:
                    answer.append(i-cnt)
                    cnt = i
                break
        else:
            answer.append(length-cnt)
            cnt = length
    
    return answer