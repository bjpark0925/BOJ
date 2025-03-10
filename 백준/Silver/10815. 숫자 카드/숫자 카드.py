n = int(input())
S = set(map(int, input().split()))
m = int(input())
D = list(map(int, input().split()))

for d in D:
    if d in S:
        print(1, end=' ')
    else:
        print(0, end=' ')