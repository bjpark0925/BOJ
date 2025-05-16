import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

kplus_index = n
for i in range(n):
    if arr[i] > k:
        kplus_index = i
        break

index = kplus_index - 1
cnt = 0
while k > 0:
    if k >= arr[index]:
        cnt += k // arr[index]
        k = k % arr[index]
    else:
        index-=1

print(cnt)    