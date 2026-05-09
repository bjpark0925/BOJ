n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
cnt = n
for i in range(n):
  answer += arr[i] * cnt
  cnt-=1
print(answer)
