import sys
input = sys.stdin.readline
n, m = map(int, input().split())

def dfs(arr):
    if len(arr) > 1 and arr[-2] > arr[-1]:
        return
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n+1):
        arr.append(i)
        dfs(arr)
        arr.pop()

    return

dfs([])