while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    
    maxVal = max(a,b,c)
    if (maxVal == a and a>=b+c) or (maxVal == b and b>=a+c) or (maxVal == c and c>=a+b):
        print("Invalid")
    elif a==b and b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")