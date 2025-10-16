from collections import deque

def solution(n, computers):
    parent = [i for i in range(n)]
    
    def find(a):
        if parent[a] == a:
            return a
        parent[a] = find(parent[a])
        return parent[a]
    
    def union(a, b):
        x, y = find(a), find(b)
        
        if x > y:
            parent[x] = y
        elif x < y:
            parent[y] = x
    
    q = deque()
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue
        q.append(i)
        while q:
            now = q.popleft()
            visited[now] = True
            
            for idx in range(n):
                if idx == now or computers[now][idx] == 0 or visited[idx] == True:
                    continue
                q.append(idx)
                union(i, idx)
        
    #print(parent)
    parent = set(parent)
        
    return len(parent)