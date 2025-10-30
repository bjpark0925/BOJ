def solution(s):    
    stack = []
    for br in s:
        if stack and stack[-1] == '(' and br == ')':
            stack.pop()
        else:
            stack.append(br)
    
    if stack:
        return False

    return True