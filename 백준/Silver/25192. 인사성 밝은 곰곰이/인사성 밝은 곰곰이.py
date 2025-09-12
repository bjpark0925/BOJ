import sys
input = sys.stdin.readline

n = int(input())
record = set()
answer = 0

for _ in range(n):
    string = input().strip()
    if string == "ENTER":
        record = set()
    else:
        if string not in record:
            answer+=1
        record.add(string)

print(answer)