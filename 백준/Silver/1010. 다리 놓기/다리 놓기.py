# M개 중 N개 뽑는 경우의 수 mCn과 같음
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    
    result = 1
    if n!=m:
        if m-n>m//2:
            for i in range(m, m-n, -1):
                result*=i
            for j in range(n, 0, -1):
                result//=j
        else: # 8C6
            for i in range(m, n, -1):
                result*=i
            for j in range(m-n, 0, -1):
                result//=j

    print(int(result))