A=int(input())
B=int(input())
C=int(input())
ans=A*B*C

arr=[0 for i in range(10)]

while (ans>=1):
  arr[ans%10]+=1
  ans=ans//10

for i in range(len(arr)):
  print(arr[i])