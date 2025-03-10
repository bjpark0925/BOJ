n = int(input())
while(n!=0):
    #에라토스테네스의 체
    arr = [1 for _ in range(2*n+1)]
    arr[1] = 0
    for i in range(2, 2*n+1):
        if i*i > 2*n:
            break
        for j in range(i*i, 2*n+1, i):
            arr[j] = 0

    cnt=0
    for i in range(n+1, 2*n+1):
        if arr[i] == 1:
            cnt+=1
    print(cnt)
    n = int(input())