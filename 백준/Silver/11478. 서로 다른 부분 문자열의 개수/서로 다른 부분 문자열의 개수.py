s = input()
answer_set = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        answer_set.add(s[i:j])
print(len(answer_set))