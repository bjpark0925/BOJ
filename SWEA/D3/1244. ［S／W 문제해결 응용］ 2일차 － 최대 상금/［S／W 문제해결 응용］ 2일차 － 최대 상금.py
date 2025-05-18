def dfs(cnt):
    global answer
    if cnt == switch_cnt:
        answer = max(answer, int("".join(num_list)))
        return
    for i in range(L-1):
        for j in range(i+1, L):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            if (cnt, int("".join(num_list))) not in v:
                dfs(cnt+1)
                v.add((cnt, int("".join(num_list))))
            num_list[j], num_list[i] = num_list[i], num_list[j]

C = int(input())
for tc in range(C):
    num, switch_cnt = map(int, input().split())
    num_list = list(str(num))
    L = len(num_list)
    v = set()
    answer = 0
    dfs(0)
    print("#{} {}".format(tc+1, answer))
