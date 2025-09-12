def calc(op, total_op, result):
    global arr
    global max_answer
    global min_answer
    if total_op == 0:
        if result > max_answer:
            max_answer = result
        if result < min_answer:
            min_answer = result
        return

    idx = n - total_op
    for i in range(len(op)):
        if op[i]:
            op[i] -= 1
            if i == 0:
                calc(op, total_op - 1, result + arr[idx])
            elif i == 1:
                calc(op, total_op - 1, result - arr[idx])
            elif i == 2:
                calc(op, total_op - 1, result * arr[idx])
            elif i == 3:
                if result >= 0:
                    calc(op, total_op - 1, result // arr[idx])
                else:
                    calc(op, total_op - 1, (-1)*(abs(result)//arr[idx]))
            op[i] += 1


n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))  # +-*/

max_answer = int(-1e9)
min_answer = int(1e9)
calc(op, n - 1, arr[0])
print(max_answer)
print(min_answer)