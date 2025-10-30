from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    weight_limit = 0
    
    while len(truck_weights) > 0:
        answer += 1
        weight_limit -= q.popleft()
        
        if weight_limit + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            weight_limit += truck
            q.append(truck)
        else:
            q.append(0)
        #print(answer, q)
    
    answer += bridge_length
    
    return answer