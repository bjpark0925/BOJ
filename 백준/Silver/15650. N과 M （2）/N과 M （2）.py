from collections import deque

def dfs(number):
    if len(myStack) == m:
        print(*myStack)
        return
    
    for i in range(number, n+1):
        if i not in myStack:
          myStack.append(i)
          dfs(i+1)
          myStack.pop()

n, m = map(int, input().split())
myStack = deque()
dfs(1)