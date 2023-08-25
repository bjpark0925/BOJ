def minimum(min, n):
  if min>n:
    min=n
  return min
x,y,w,h=map(int, input().split())
n1=w-x
n2=h-y

#x,y,n1,n2 중 최솟값 찾기

min=x
min=minimum(min, y)
min=minimum(min, n1)
min=minimum(min, n2)
print(min)