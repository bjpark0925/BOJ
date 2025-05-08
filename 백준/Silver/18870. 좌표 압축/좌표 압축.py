import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # 2 4 -10 4 -9

arr_set = set(arr)
arr_list = list(arr_set)
arr_list.sort() # -10 -9 2 4

arr_dict = {}
for i in range(len(arr_list)):
    arr_dict[arr_list[i]] = i

for x in arr:
    print(arr_dict[x], end=' ')