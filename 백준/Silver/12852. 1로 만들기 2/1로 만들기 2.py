from collections import deque
n = int(input())
arr = [0] * (n+1)

for i in range(2,n+1):
    candidates = [arr[i-1]]
    if i%3 == 0:
        candidates.append(arr[i//3])
    if i%2 == 0:
        candidates.append(arr[i//2])
    arr[i] = min(candidates) + 1

queue = deque([n])
answer = deque()
while queue:
    node = queue.popleft()
    answer.append(node)
    if node == 1:
        break

    neighbor = [node-1]
    if node%3 == 0:
        neighbor.append(node//3)
    if node%2 == 0:
        neighbor.append(node//2)

    min_next = neighbor[0]
    for next in neighbor:
        if arr[next] < arr[min_next]:
            min_next = next
    queue.append(min_next)

print(arr[n])
print(*answer)