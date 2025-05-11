# LIS = Longest Increasing Subsequence
# 이진탐색으로 lis 배열에 크기별로 삽입
import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# arr: [10, 20, 10, 30, 15, 50]
# lis: [10, 15, 30, 50]
# lis 수열은 실제 정답인 [10, 20, 30, 50]과 다르지만
# 20 대신 15를 넣음으로써 나중에 15 이상 20 이하의 수가 와도 문제 없도록 함
lis = []
for i in range(n):
    index = bisect.bisect_left(lis, arr[i])
    if index == len(lis):
        lis.append(arr[i])
    else:
        lis[index] = arr[i]

print(len(lis))