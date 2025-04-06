from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
'''
1:[6,4],
2:[4],
3:[5,6],
4:[1,2,7],
5:[3],
6:[1,3],
7:[4]
'''
visited = [0] * (n+1)
def dfs(node):
    for neighbor in tree[node]:
        if visited[neighbor] == 0:
            visited[neighbor] = node
            dfs(neighbor)
dfs(1)

for i in range(2, n+1):
    print(visited[i])