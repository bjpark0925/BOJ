n,m = map(int, input().split())
bucket = [num+1 for num in range(n)]

for itr in range(m):
    i,j = map(int, input().split())
    while(i<j):
        #swap
        tmp = bucket[i-1]
        bucket[i-1] = bucket[j-1]
        bucket[j-1] = tmp
        
        i+=1
        j-=1

for pos in range(n):
  print(bucket[pos], end=' ')