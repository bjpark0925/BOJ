n = int(input())
string = input()
v = input()

tokens = string.split()

answer = 0
for token in tokens:
    if token == v:
        answer+=1

print(answer)