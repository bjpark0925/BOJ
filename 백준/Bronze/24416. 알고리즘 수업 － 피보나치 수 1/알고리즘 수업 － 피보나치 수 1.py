def fib_recur(n):
    recur_cnt = []
    recur_cnt.append(1)
    recur_cnt.append(1)
    
    for i in range(2, n):
        recur_cnt.append(recur_cnt[i-1] + recur_cnt[i-2])
    
    return recur_cnt[n-1]

def fib_dp(n, dp_cnt):
    f = []
    f.append(1)
    f.append(1)
    
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
        dp_cnt+=1
    return dp_cnt

n = int(input())
dp_cnt = 0

print(fib_recur(n), fib_dp(n, dp_cnt))