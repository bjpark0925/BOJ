text = input()
pattern = input()

def failure_func(pattern):
    F = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = F[j-1]
        if pattern[i] == pattern[j]:
            F[i] = j+1
            j+=1
    return F
'''
abaaba의 F는
001123
'''
def KMPmatch(text, pattern, F):
    cnt = 0
    indices = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = F[j-1]
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                cnt+=1
                indices.append(i - j + 1)
                j = F[j] # 중요
            else:
                j+=1
    return cnt, indices

F = failure_func(pattern)
cnt, indices = KMPmatch(text, pattern, F)
print(cnt)
print(*indices)