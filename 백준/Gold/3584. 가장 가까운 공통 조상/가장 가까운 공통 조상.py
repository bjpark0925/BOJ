# parent 리스트에 각 노드의 부모 저장
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a
        
    tc_a, tc_b = map(int, input().split())
    a_parents = deque([tc_a, 0]) # tc_a, tc_b가 부모 자식 관계인 경우 인덱스 에러 방지
    now = tc_a
    while now != 0:
        now = parent[now]
        a_parents.appendleft(now) # 뒤에서부터 탐색하기 위해 거꾸로 append
        
    b_parents = deque([tc_b, 0])
    now = tc_b
    while now != 0:
        now = parent[now]
        b_parents.appendleft(now)
    
    i = 0
    while True:
        if a_parents[i] != b_parents[i]: # 달라지는 부모 직전이 가장 가까운 공통 조상
            print(a_parents[i-1])
            break
        i+=1