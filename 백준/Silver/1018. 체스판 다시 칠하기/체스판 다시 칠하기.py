size=8

def counting(x,y,chess):
  cnt1=0
  cnt2=0

  #좌상단 W 기준 cnt
  for i in range(size):
    for j in range(size):
      if ((i+j)%2==0):
        if (chess[x+i][y+j]!='W'):
          cnt1+=1

      else:
        if (chess[x+i][y+j]!='B'):
          cnt1+=1

  #좌상단 B 기준 cnt
  for i in range(size):
    for j in range(size):
      if ((i+j)%2==0):
        if (chess[x+i][y+j]!='B'):
          cnt2+=1
      else:
        if (chess[x+i][y+j]!='W'):
          cnt2+=1
  
  min=cnt1
  if (cnt1>cnt2):
    min=cnt2
  return min

#main
n,m=map(int, input().split())
chess=[]
for i in range(n):
  chess.append(input())

#cnt들 저장하는 배열 선언(8*8은 아무 곳에나 잡아도 되므로)
color_cnt=[[0 for col in range(m-size+1)]for row in range(n-size+1)]

for x in range(n-size+1):
  for y in range(m-size+1):
    color_cnt[x][y]=counting(x,y,chess)

#최솟값 찾기
min=color_cnt[0][0]
for i in range(n-size+1):
  for j in range(m-size+1):
    if (min>color_cnt[i][j]):
      min=color_cnt[i][j]

print(min)