n = int(input())
answer = 0
while n:
    answer += n%10
    n //= 10
print(answer)