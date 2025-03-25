n = int(input())
arr = [0]*(n+1)

for i in range(2, n+1):
    candidates = [arr[i-1]]
    if i%3 == 0:
        candidates.append(arr[i//3])
    if i%2 == 0:
        candidates.append(arr[i//2])
    arr[i] = min(candidates) + 1
print(arr[n])