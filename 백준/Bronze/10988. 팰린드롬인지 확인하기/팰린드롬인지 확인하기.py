word = input()

start = 0
end = len(word) - 1
answer = 1

while start < end:
    if word[start] != word[end]:
        answer = 0
        break
    start+=1
    end-=1

print(answer)