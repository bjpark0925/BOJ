def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    # 아직 제거할 숫자가 남은 경우, 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
    return "".join(stack)
    '''
    answer = ''
    # 뒤에서부터 max값 찾기. 개수 안 맞으면 버리고 맞으면 픽스
    front = 0
    rear = k+1
    cnt = k # 제거해야 할 개수
    while len(answer) < len(number) - k:
        block = number[front:rear]
        if len(block) == 1:
            answer += number[front:]
            break
        elif len(block) > 1:
            fix_num = max(block)
            f = front
            r = rear
            for j in range(f, r):
                if number[j] == fix_num:
                    answer += fix_num
                    cnt -= j - front # 제거된 개수만큼 감소
                    front = j+1
                    rear = front + cnt + 1
                    break
    
    return answer
    '''