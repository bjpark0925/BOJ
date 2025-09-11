import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    a, b = map(int, input().split())
    print(a+b)