def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_stack, pickup_stack = [], []
    # stack 이용한 greedy
    for i in range(n):
        if deliveries[i] != 0:
            deliver_stack.append(i)
        if pickups[i] != 0:
            pickup_stack.append(i)
            
    #print(deliver_stack, pickup_stack)
    
    while deliver_stack or pickup_stack:
        flag = cap
        # 거리 계산
        if len(deliver_stack) != 0 and len(pickup_stack) == 0:
            answer += (deliver_stack[-1]+1)*2
        elif len(deliver_stack) == 0 and len(pickup_stack) != 0:
            answer += (pickup_stack[-1]+1)*2
        elif deliver_stack[-1] >= pickup_stack[-1]:
            answer += (deliver_stack[-1]+1)*2
        else:
            answer += (pickup_stack[-1]+1)*2
        # 배달
        while deliver_stack and flag != 0:
            index = deliver_stack.pop()
            if deliveries[index] <= flag:
                flag -= deliveries[index]
                deliveries[index] = 0
            else:
                deliveries[index] -= flag
                flag = 0
                deliver_stack.append(index)
        # 수거
        flag = cap # 돌아올 때 택배차 공간 확보
        while pickup_stack and flag != 0:
            index = pickup_stack.pop()
            if pickups[index] <= flag:
                flag -= pickups[index]
                pickups[index] = 0
            else:
                pickups[index] -= flag
                flag = 0
                pickup_stack.append(index)
    
    
    return answer