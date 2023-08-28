num=list(map(int, input().split()))
sum=0
for i in range(5):
  sum+=num[i]**2
gou=sum%10
print(gou)