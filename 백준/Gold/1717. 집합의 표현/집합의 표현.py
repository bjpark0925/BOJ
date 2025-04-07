import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
# [0,1,2,3,4,5,6,7]
# 두 원소의 루트 노드가 같다면 두 원소는 같은 그룹에 속해 있다.
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(a, b):
    A = find_parent(a)
    B = find_parent(b)
    # A,B 중 더 작은 걸 루트 노드로 설정
    if A < B:
        parent[B] = A
    elif A > B:
        parent[A] = B

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(a, b)
    elif op == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")