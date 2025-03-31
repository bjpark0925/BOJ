from collections import deque

string = list(input())
explode = list(input())
stack = deque()
answer = []

for alphabet in string:
    if alphabet == explode[0]:
        stack.append(0)
    elif stack and alphabet == explode[stack[-1]+1]:
        stack.append(stack[-1]+1)
    else: # 현재 탐색 문자가 폭발 문자가 아니면
        while stack:
            answer.append(explode[stack.popleft()])
        answer.append(alphabet)

    if stack and stack[-1]+1 == len(explode): # 폭발
        for i in range(len(explode)):
            stack.pop()

# 마지막 문자가 폭발 문자인 채로 폭발 문자열 성립이 안된 경우, stack 비우기
while stack:
    answer.append(explode[stack.popleft()])

if answer:
    print(*answer, sep='')
else:
    print("FRULA")