num=[]
for i in range(9):
  num.append(int(input()))
max=num[0]
max_num=0

for i in range(9):
  if(max<num[i]):
    max=num[i]
    max_num=i

print(max, max_num+1, sep='\n')