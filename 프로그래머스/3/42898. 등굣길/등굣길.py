def solution(m, n, puddles):
    graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for row in range(1, n+1):
        graph[row][1] = 1
    for col in range(1,m+1):
        graph[1][col] = 1
    for pud_col, pud_row in puddles:
        if pud_row == 1:
            while pud_col <= m:
                graph[pud_row][pud_col] = 0
                pud_col+=1
        if pud_col == 1:
            while pud_row <= n:
                graph[pud_row][pud_col] = 0
                pud_row+=1

    for row in range(2, n+1):
        for col in range(2, m+1):
            if [col, row] in puddles:
                graph[row][col] = 0
            else:
                graph[row][col] = graph[row][col-1] + graph[row-1][col]

    return graph[n][m] % 1000000007