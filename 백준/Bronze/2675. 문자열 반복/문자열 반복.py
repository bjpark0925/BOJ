def output(R,S):
  answer=[]
  for i in range(len(S)):
    for j in range(R):
      answer.append(S[i])
  return answer

def revive():
  R,S=input().split()
  R=int(R)
  S=list(S)
  return output(R,S)

test_num=int(input())
result=[]
for i in range(test_num):
  result.append(revive())

for i in range(test_num):
  for j in range(len(result[i])):
    print(result[i][j],end="")
  print()