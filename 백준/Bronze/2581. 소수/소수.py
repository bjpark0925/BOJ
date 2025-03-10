m = int(input())
n = int(input())

result = 0
is_prime = True
is_first = True
minimum = -1

for i in range(m, n+1):
    if i < 2:
        continue
        
    for j in range(2, i):
        if i < j*j:
            break
        if i%j == 0:
            is_prime = False
            break
            
    if is_prime:
        if is_first:
            minimum = i
            is_first = False
        result += i
    
    is_prime = True

if minimum == -1:
    print(-1)
else:
    print("{}\n{}".format(result, minimum))
            