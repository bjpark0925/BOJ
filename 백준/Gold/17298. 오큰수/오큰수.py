import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)