import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

white_cnt = 0
blue_cnt = 0
def cut(la_index, length): # left above 좌상단 index
    global white_cnt
    global blue_cnt

    la_row, la_col = la_index[0], la_index[1]
    color_set = set()
    for i in range(la_row, la_row + length):
        for j in range(la_col, la_col + length):
            color_set.add(arr[i][j])
            if len(color_set) > 1:
                break
        if len(color_set) > 1:
            break

    if len(color_set) == 1:
        if color_set.pop() == 0:
            white_cnt+=1
        else:
            blue_cnt+=1

    else:
        for row_offset in range(2):
            for col_offset in range(2):
                next_length = length // 2
                cut((la_row + row_offset*next_length, la_col + col_offset*next_length), next_length)

cut((0,0), n)
print(white_cnt)
print(blue_cnt)