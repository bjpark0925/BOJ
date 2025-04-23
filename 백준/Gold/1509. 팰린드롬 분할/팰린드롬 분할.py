import sys
#input = sys.stdin.readline

string = input()
n = len(string)
palindrome = [[False for _ in range(n)] for _ in range(n)] # P[0][4] = True이면, start=0, end=4인 문자열은 팰린드롬

for i in range(n): # 길이가 1인 팰린드롬
    palindrome[i][i] = True

for i in range(n-1): # 길이가 2인 팰린드롬
    if string[i] == string[i+1]:
        palindrome[i][i+1] = True

for leng in range(3, n+1): # 길이가 3이상인 팰린드롬
    for start in range(n-leng+1):
        end = start + leng - 1
        if string[start] == string[end] and palindrome[start+1][end-1]: # 처음과 끝이 같고, 내부 문자열이 팰린드롬
            palindrome[start][end] = True

dp = [0] * n # dp[-1] = 0(배열의 끝값)
dp[0] = 1
# <문자열> + 'B'의 dp값은?
# 단순히 이전 dp배열 값에서 1 추가 or B가 end인 거대 팰린드롬이 완성되어 dp[start-1]+1
for end in range(1, n):
    min_val = dp[end-1] + 1
    for start in range(end):
        if palindrome[start][end]: 
            min_val = min(min_val, dp[start-1] + 1)
    dp[end] = min_val

print(dp[n-1])