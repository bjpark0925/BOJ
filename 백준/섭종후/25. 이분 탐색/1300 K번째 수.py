n = int(input())
k = int(input())

left = 1
right = n*n
while left < right:
  mid = (left+right)//2
  cnt = 0
  for i in range(1, n+1):
    val = mid // i
    if val > n:
      cnt += n
    else:
      cnt += val

  #print(mid, cnt)
  # lower_bound
  if cnt >= k:
    right = mid
  elif cnt < k:
    left = mid + 1
print(left)
'''
for i in range(1, n+1):
  for j in range(1, n+1):
    B.append(i*j)

B.sort()
print(B[k-1])
'''
