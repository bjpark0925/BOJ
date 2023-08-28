is_yun=0
n=int(input())
if ((n%4==0) and (n%100!=0)) or (n%400==0):
  is_yun=1
print(is_yun)