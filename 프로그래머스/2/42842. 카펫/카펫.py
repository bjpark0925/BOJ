def solution(brown, yellow):
    answer = []
    # 48의 약수: 1,2,3,4, 6*8, 12,16,24,48
    # 노랑 24의 약수: 1,2,3, 4(6-2)*6(8-2), 8,12,24
    # 갈색 24 = (6+8)*2-4
    
    num = brown + yellow
    for i in range(3, num):
        if i*i>num:
            break
        if num%i == 0: # 48의 약수일 때
            if ((i-2)*(num//i - 2) == yellow) and ((i+(num//i))*2 - 4 == brown):
                if i>num//i:
                    answer.append(i)
                    answer.append(num//i)
                else:
                    answer.append(num//i)
                    answer.append(i)
    
    return answer