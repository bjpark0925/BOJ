N=int(input())
score=list(map(int, input().split()))

sum=0
M=score[0]
for i in range(N):
  sum+=score[i]
  if(M<score[i]):
    M=score[i]
avg=sum/N

print(avg/M*100)
'''
숫자 고치기
sum=0
for i in range(N):
score[i]=score[i]/M*100
sum+=score[i]

avg=sum/N
print(avg)
'''