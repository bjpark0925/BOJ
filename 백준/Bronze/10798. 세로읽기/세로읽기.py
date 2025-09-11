arr = [[-1]*15 for _ in range(5)]
for i in range(len(arr)):
    word = input()
    for j in range(len(word)):
        arr[i][j] = word[j]
#print(arr)

answer = []
for col in range(15):
    for row in range(len(arr)):
        if arr[row][col] != -1:
            answer.append(arr[row][col])

print(*answer, sep='')