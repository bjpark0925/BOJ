from collections import deque

def dfs():
  if len(myStack) == m:
    combination.append(list(myStack))
    return

  for i in range(1, n+1):
    if visited.get(i) == True:
      continue
    myStack.append(i)
    visited[i] = True
    dfs()
    myStack.pop()
    visited[i] = False

n, m = map(int, input().split())
myStack = deque()
combination = []
visited = {}

dfs()
for i in range(len(combination)):
  print(*combination[i], sep=' ')