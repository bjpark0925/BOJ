student = set()
for _ in range(28):
    tmp = int(input())
    student.add(tmp)
cnt=0
for i in range(1,31):
    if i not in student:
        print(i)
    if cnt >= 2:
        break