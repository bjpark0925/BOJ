n, m = map(int, input().split())
S = set()
for _ in range(n):
    S.add(input())

cnt = 0
for _ in range(m):
    temp = input()
    if temp in S:
        cnt+=1

print(cnt)