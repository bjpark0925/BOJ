from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
dq = deque()
for i in range(n):
    order = list(map(int, input().split()))
    a = 0
    b = 0
    if len(order) > 1:
        a, b = order[0], order[1]
    else:
        a = order[0]
    if a == 1:
        dq.appendleft(b)
    elif a == 2:
        dq.append(b)
    elif a == 3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif a == 4:
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif a == 5:
        print(len(dq))
    elif a == 6:
        if dq:
            print(0)
        else:
            print(1)
    elif a == 7:
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif a == 8:
        if dq:
            print(dq[-1])
        else:
            print(-1)