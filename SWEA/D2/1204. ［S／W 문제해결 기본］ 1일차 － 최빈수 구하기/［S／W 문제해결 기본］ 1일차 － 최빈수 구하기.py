T = int(input())
for i in range(T):
    tc = int(input())
    arr = list(map(int, input().split()))
    score = [-1] * 101
    for num in arr:
        score[num]+=1
    maximum = score[0]
    answer = 0
    for j in range(1, len(score)):
        if score[j] >= maximum:
            maximum = score[j]
            answer = j
    print("#{} {}".format(tc, answer))