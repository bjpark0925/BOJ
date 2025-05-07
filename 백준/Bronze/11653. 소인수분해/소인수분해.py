import math

n = int(input())
arr = [1] * (int(math.sqrt(n)) + 1)
for i in range(2, int(math.sqrt(len(arr)-1))+1):
    j = i
    while i*j < len(arr):
        arr[i*j] = 0
        j+=1
#print(arr)
while n > 1:
    flag = True
    for i in range(2, len(arr)):
        if arr[i] and n%i == 0:
            print(i)
            n = n//i
            flag = False
            break
    if flag:
        print(n)
        break