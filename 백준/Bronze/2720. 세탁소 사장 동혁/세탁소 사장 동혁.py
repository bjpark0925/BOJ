t = int(input())
for i in range(t):
    c = int(input())
    q=0; d=0; n=0; p=0
    q += c//25
    c %= 25
    d += c//10
    c %= 10
    n += c//5
    c %= 5
    p += c
    print(q, d, n, p)