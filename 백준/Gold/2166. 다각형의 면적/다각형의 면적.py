# 행렬식 = 두 벡터가 만드는 평행사변형의 넓이 = 두 벡터끼리의 외적
n = int(input())
matrix = []
'''
x1 y1
x2 y2
x3 y3
...
xn yn
x1 y1
'''
for _ in range(n):
    a, b = map(int, input().split())
    matrix.append((a,b))
matrix.append(matrix[0])

answer = 0
for i in range(n):
    answer += (matrix[i][0] * matrix[i+1][1]) - (matrix[i+1][0] * matrix[i][1])
    
print(round(abs(answer/2), 1))