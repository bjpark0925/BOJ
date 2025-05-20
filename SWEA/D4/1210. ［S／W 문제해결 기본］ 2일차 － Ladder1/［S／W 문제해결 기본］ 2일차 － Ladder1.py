for tc in range(10):
    T = int(input())
    size = 100
    arr = [list(map(int, input().split())) for _ in range(size)]

    destination_col = 0
    for floor_col in range(size):
        if arr[size-1][floor_col] == 2:
            destination_col = floor_col

    now_row, now_col = size-2, destination_col
    while now_row > 0:
        #print(now_row, now_col)
        if now_col > 0 and arr[now_row][now_col-1] == 1:
            now_col-=1
            while arr[now_row-1][now_col] == 0 and arr[now_row][now_col] == 1:
                now_col-=1
        elif now_col < size - 1 and arr[now_row][now_col+1] == 1:
            now_col+=1
            while arr[now_row-1][now_col] == 0 and arr[now_row][now_col] == 1:
                now_col+=1

        if arr[now_row-1][now_col] == 1:
            now_row-=1

    print("#{} {}".format(T, now_col))
