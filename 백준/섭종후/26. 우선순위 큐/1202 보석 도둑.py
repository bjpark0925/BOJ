from collections import deque
'''
작은 가방부터
가치가 큰 보석부터 보다가 처음으로 가방에 넣을 수 있는 무게의 보석 넣기

가방 무게 오름차순
가치 내림차순, 가치 같으면 무게 오름차순
'''
n, k = map(int, input().split())

jewelry = []
for i in range(n):
    w, v = map(int, input().split())
    jewelry.append((w, v))
jewelry.sort(key=lambda x:(-x[1], x[0]))
jewelry = deque(jewelry)
print(jewelry)

bag = []
for i in range(k):
    c = int(input())
    bag.append(c)
bag.sort()
print(bag)

answer = 0
for c in bag:
    rotate_num = 0
    re_cnt = len(jewelry)
    for _ in range(re_cnt):
        temp = jewelry.popleft()
        if c >= temp[0]:
            answer += temp[1]
            jewelry.rotate(rotate_num)
            break
        else:
            jewelry.append(temp)
            rotate_num += 1
print(answer)
