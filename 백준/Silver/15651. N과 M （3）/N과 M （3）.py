def dfs():
    if len(myStack) == m:
        print(*myStack)
        return
    
    for i in range(1, n+1):
        myStack.append(i)
        dfs()
        myStack.pop()

n,m = map(int, input().split())
myStack = []
dfs()