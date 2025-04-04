n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
left = 0
right = n-1
answer = 0
while left < right:
    lr_sum = arr[left] + arr[right]
    if lr_sum == x:
        left+=1
        right-=1
        answer+=1
    elif lr_sum > x:
        right-=1
    else:
        left+=1
print(answer)