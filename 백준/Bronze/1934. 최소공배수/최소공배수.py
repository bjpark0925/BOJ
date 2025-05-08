import math

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    print(a*b//gcd)