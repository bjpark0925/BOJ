import heapq

def solution(operations):
    # 힙큐 = 최솟값부터
    # -642 -45 45 97 333 653
    # heapq[0]이 최솟값인건 신뢰할 수 있지만, heapq[-1]이 최댓값인건 신뢰할 수 없음
    answer = []
    min_heap = []
    max_heap = []
    visited = [False] * len(operations) # i번째 넣은 값이 유효한지
    
    for i, op in enumerate(operations):
        if op[0] == 'I':
            num = int(op[2:])
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        elif op[0] == 'D':
            if op[2:] == '1':
                while max_heap and visited[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and visited[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
    while max_heap and visited[max_heap[0][1]] == False:
        heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0][1]] == False:
        heapq.heappop(min_heap)
    
    if not max_heap:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(-max_heap[0][0])
        answer.append(min_heap[0][0])
    
    return answer