from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    graph = defaultdict(set)
    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)
    '''
    1:2,3
    2:1,3,4,5
    3:1,2,4,6
    4:2,3
    5:2
    6:3
    '''
    dist = [0] * (n+1)
    visited = {1}
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
            dist[neighbor] = dist[node] + 1
    
    #print(dist)
    long_dist = max(dist)
    for i in range(len(dist)):
        if dist[i] == long_dist:
            answer+=1
    
    return answer