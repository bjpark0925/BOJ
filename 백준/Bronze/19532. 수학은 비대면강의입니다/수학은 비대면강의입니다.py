a1, b1, c1, a2, b2, c2 = map(int, input().split())

# X = A^(-1)*B (AX = B)
det = a1*b2 - a2*b1
x = int((b2*c1 - b1*c2)/det)
y = int((a1*c2 - a2*c1)/det)

print("{} {}".format(x, y))