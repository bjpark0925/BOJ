import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dutdo = set()
bodo = set()
for _ in range(n):
    dutdo.add(input().strip())
for _ in range(m):
    bodo.add(input().strip())

answer = dutdo & bodo
answer = list(answer)

print(len(answer))
print(*sorted(answer))