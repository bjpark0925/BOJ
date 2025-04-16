import sys
input = sys.stdin.readline
S = [0] * 21

def check(x):
    if S[x]:
        return 1
    return 0

def add(x):
    if not check(x):
        S[x] = 1

def remove(x):
    if check(x):
        S[x] = 0

def toggle(x):
    if check(x):
        S[x] = 0
    else:
        S[x] = 1

def all_func():
    for i in range(1, len(S)):
        S[i] = 1

def empty():
    for i in range(1, len(S)):
        S[i] = 0

m = int(input())
for _ in range(m):
    temp = input().split()
    op = temp[0]
    if len(temp) == 2:
          x = int(temp[1])

    if op == "add":
        add(x)
    elif op == "remove":
        remove(x)
    elif op == "check":
        print(check(x))
    elif op == "toggle":
        toggle(x)
    elif op == "all":
        all_func()
    elif op == "empty":
        empty()