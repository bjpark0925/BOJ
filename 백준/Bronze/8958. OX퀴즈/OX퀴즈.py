def calculate(ox):
  score=[0 for i in range(80)]
  for i in range(len(ox)):
    if (ox[i]=='O'):
      if (i==0):
        score[i]=1
      elif (ox[i-1]=='O'):
        score[i]=score[i-1]+1
      else:
        score[i]=1
    elif (ox[i]=='X'):
      score[i]=0
  
  sum=0
  for i in range(len(score)):
    sum+=score[i]
  
  print(sum)

n=int(input())
for i in range(n):
  ox=input()
  calculate(ox)