num=[0 for i in range(42)]

for i in range(10):
  a=int(input())
  num[a%42]+=1

cnt=0

for i in range(42):
  if (num[i]!=0):
    cnt+=1

print(cnt)
