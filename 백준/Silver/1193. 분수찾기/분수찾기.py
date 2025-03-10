'''
n(n-1)/2
3(3+1)/2 = 6 < 8 < 4(4+1)/2 = 10
n = 4째줄

짝수는 위쪽부터, 홀수는 아래쪽부터
8-6 = 2
4째줄의 위쪽부터 2번째이므로
분자 = 2, 분모 = n+1-분자

n이 홀수라 아래쪽부터 m번째라면
분모 = m, 분자 = n+1-분모
'''

x = int(input())
n = 0
son, parent = 0, 0

for i in range(x+1):
    if x <= (i*(i+1)/2):
        n = i
        break

m = x - (n*(n-1)/2)

if n%2 == 0:
    son = m
    parent = n+1-m
else:
    parent = m
    son = n+1-m
    
print("{}/{}".format(int(son), int(parent)))