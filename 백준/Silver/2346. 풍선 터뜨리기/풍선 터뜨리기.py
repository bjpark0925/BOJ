from collections import deque

n = int(input())
ballons = deque(enumerate(map(int, input().split())))
#print(ballons)
answer = []

while ballons:
    idx, paper = ballons.popleft()
    answer.append(idx+1)

    length = len(ballons)
    if paper > 0:
        ballons.rotate(-(paper-1))
    else:
        ballons.rotate(-paper)

print(*answer)