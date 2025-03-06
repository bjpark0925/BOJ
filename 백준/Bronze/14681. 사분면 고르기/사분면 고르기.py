x = int(input())
y = int(input())
A = 0

if x>0:
    if y>0:
        A = 1
    else:
        A = 4
else:
    if y>0:
        A = 2
    else:
        A = 3
 
print(A)