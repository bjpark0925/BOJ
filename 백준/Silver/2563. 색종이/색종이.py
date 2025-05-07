n = int(input())
# 우측 위 좌표 체크
check = set()
for _ in range(n):
    x, y = map(int, input().split())
    for a in range(x+1, x+11):
        for b in range(y+1, y+11):
            check.add((a,b))
print(len(check))