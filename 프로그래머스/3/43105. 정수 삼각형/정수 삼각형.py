def solution(triangle):
    for depth in range(len(triangle)-2, -1, -1):
        for index in range(depth+1):
            triangle[depth][index] += max(triangle[depth+1][index], triangle[depth+1][index+1])
    return triangle[0][0]