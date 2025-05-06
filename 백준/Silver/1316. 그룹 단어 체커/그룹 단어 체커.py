n = int(input())
answer = 0

for _ in range(n):
    string = input()
    group = set()
    group_flag = True
    for i in range(len(string)):
        if string[i] in group and string[i-1] != string[i]:
            group_flag = False
            break
        else:
            group.add(string[i])

    if group_flag:
        answer+=1

print(answer)