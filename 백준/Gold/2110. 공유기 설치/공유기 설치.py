import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

left = 1
right = (arr[n-1] - arr[0]) // (c - 1) # ideal max length
result = 0
while left <= right:
    mid = (left + right) // 2
    cur = arr[0] # important
    cnt = 1
    for i in range(n):
        if arr[i] - cur >= mid:
            cur = arr[i]
            cnt+=1

    if cnt < c:
        right = mid - 1
    else:
        left = mid + 1
        result = mid
print(result)