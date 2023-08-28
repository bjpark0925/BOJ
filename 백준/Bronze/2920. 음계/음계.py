num=list(map(int, input().split()))

is_ascending=1
is_descending=1

if (num[0]!=1):
  is_ascending=0
if (num[0]!=8):
  is_descending=0

for i in range(7):
   if (num[i+1]!=num[i]+1):
     is_ascending=0
     break

for i in range(7):
  if (num[i]!=num[i+1]+1):
    is_descending=0
    break

if (is_ascending==1):
  print("ascending")
elif (is_descending==1):
  print("descending")
else:
  print("mixed")
