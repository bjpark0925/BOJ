import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    op = input().strip()
    if op == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif op == '3':
        print(len(stack))
    elif op == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif op == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        temp, num = op.split(' ')
        stack.append(int(num))