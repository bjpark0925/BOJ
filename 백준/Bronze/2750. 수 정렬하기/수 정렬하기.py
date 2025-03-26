n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

A.sort()
print(*A, sep="\n")