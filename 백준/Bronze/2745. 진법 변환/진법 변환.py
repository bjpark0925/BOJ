n, b = input().split()
n = list(n)
b = int(b)

answer = 0
power = 0
while n:
    digit = n.pop()
    if digit >= 'A' and digit <= 'Z':
        digit = ord(digit) - ord('A') + 10
    else:
        digit = int(digit)
    answer += digit * (b**power)
    power+=1
print(answer)