from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)
visited = [0] * 100001
answer = 0
while q:
    now = q.popleft()
    if now == k:
        answer = visited[now]
        break
    
    for i in (now-1, now+1, now*2):
        if 0<=i<=100000 and visited[i] == 0:
            visited[i] = visited[now]+1
            q.append(i)
    
print(answer)