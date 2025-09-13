import sys, heapq
input = sys.stdin.readline

n = int(input())
pos_q = []
neg_q = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(pos_q, x)
    elif x < 0:
        heapq.heappush(neg_q, (-1)*x) # 절댓값 작은 값 pop하도록
    else:
        if pos_q and neg_q:
            abs_pos = heapq.heappop(pos_q)
            abs_neg = heapq.heappop(neg_q)
            if abs_pos >= abs_neg:
                print((-1)*abs_neg)
                heapq.heappush(pos_q, abs_pos)
            else:
                print(abs_pos)
                heapq.heappush(neg_q, abs_neg)
        
        elif pos_q:
            print(heapq.heappop(pos_q))
        elif neg_q:
            print((-1)*heapq.heappop(neg_q))
        
        else:
            print(0)
                