import math
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

diff = []
for i in range(1, n):
    diff.append(arr[i] - arr[i-1])

gcdVal = diff[0]
for i in range(1, len(diff)):
    gcdVal = math.gcd(gcdVal, diff[i])
print(sum(diff)//gcdVal - len(diff))