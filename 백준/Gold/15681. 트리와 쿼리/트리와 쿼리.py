from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
tree = defaultdict(set)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].add(v)
    tree[v].add(u)

countSize = [0] * (n+1)
def countSubTree(currentNode, parent):
    countSize[currentNode] = 1
    for neighbor in tree[currentNode]:
        if neighbor == parent:
            continue
        countSubTree(neighbor, currentNode)
        countSize[currentNode] += countSize[neighbor]

countSubTree(r, -1)

for _ in range(q):
    query = int(input())
    print(countSize[query])