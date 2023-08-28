a,b=map(int,input().split())
a_r=[]
while (a>0):
  a_r.append(a%10)
  a=a//10

b_r=[]
while (b>0):
  b_r.append(b%10)
  b=b//10

new_a=100*a_r[0]+10*a_r[1]+a_r[2]
new_b=100*b_r[0]+10*b_r[1]+b_r[2]

max=new_a
if (max<new_b):
  max=new_b

print(max)