# dijkstra
import heapq
C = int(input())
for i in range(C):
    n = int(input())
    arr = []
    for _ in range(n):
        line = list(map(int, list(input())))
        arr.append(line)
    #print(arr)
    queue = []
    heapq.heappush(queue, (0, 0, 0)) # (dist, node_row, node_col)
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    distances[0][0] = 0
    while queue:
        dist, node_row, node_col = heapq.heappop(queue)
        if dist > distances[node_row][node_col]:
            continue

        neighbor = [(node_row, node_col + 1), (node_row + 1, node_col), (node_row, node_col - 1), (node_row - 1, node_col)]
        for next_node in neighbor:
            next_row = next_node[0]
            next_col = next_node[1]
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                continue

            depth = arr[next_row][next_col]
            cost = dist + depth
            if cost < distances[next_row][next_col]:
                distances[next_row][next_col] = cost
                heapq.heappush(queue, (cost, next_row, next_col))
    #print(distances)
    print("#{} {}".format(i+1, distances[n-1][n-1]))