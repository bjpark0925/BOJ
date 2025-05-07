x_stack = []
y_stack = []
for _ in range(3):
    x, y = map(int, input().split())
    if x in x_stack:
        x_stack.remove(x)
    else:
        x_stack.append(x)
    
    if y in y_stack:
        y_stack.remove(y)
    else:
        y_stack.append(y)

print(x_stack[0], y_stack[0])