for i in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for j in range(2, n-2):
        view = max(arr[j-2], arr[j-1], arr[j+1], arr[j+2])
        if arr[j] > view:
            answer += arr[j] - view
    print("#{} {}".format(i, answer))
