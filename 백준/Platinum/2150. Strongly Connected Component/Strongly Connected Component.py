# 코사라주 알고리즘 = 정방향 dfs 후 스택을 pop하여 나오는 정점부터 역방향 dfs
# 타잔 알고리즘 = 부모가 같다면 같은 사이클이다
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())

graph = defaultdict(list)
reverse_graph = defaultdict(list)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

stack = []
visited = set()
reverse_visited = set()

def dfs(node):
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
    stack.append(node)

def reverse_dfs(now, scc):
    reverse_visited.add(now)
    scc.append(now)
    
    for neighbor in reverse_graph[now]:
        if neighbor not in reverse_visited:
            scc = reverse_dfs(neighbor, scc)
    return scc

def kosaraju():
    answer = []
    # 정방향 dfs
    for node in range(1, v+1):
        if node not in visited:
            dfs(node)

    while stack:
        scc = []
        now = stack.pop()
        if now in reverse_visited:
            continue
        # 역방향 dfs
        scc_result = reverse_dfs(now, scc)
        answer.append(sorted(scc_result))
    
    return answer

answer = kosaraju()
print(len(answer))
for line in sorted(answer): # 각 줄 끝 -1 출력
    print(*line, -1)