n = int(input())
#print(2**n)
arr = [[0]*i for i in range(1, n+2)]

for row in range(n+1):
    arr[row][0] = 1
    arr[row][row] = 1

for row in range(2,n+1):
    for col in range(1,row):
        arr[row][col] = arr[row-1][col-1] + arr[row-1][col]

#print(arr)
answer = 0
for num in arr[n]:
    answer+=num
print(answer)