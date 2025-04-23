# 선들을 오름차순으로 정렬 후 순회
# 이전 값의 end가 다음 값의 start보다 크거나 같다면 겹치는 경우임
# 아니면 안 겹치므로 지금까지의 선 길이를 answer에 저장한 후 다음 값을 새 start, end로 업데이트
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x,y])
arr.sort(key = lambda x: x[0])

answer = 0
start, end = arr[0][0], arr[0][1] # arr[0] 해도 무방
for i in range(1, n):
    if end >= arr[i][0]: # 겹침
        end = max(end, arr[i][1])
    else: # 안 겹침
        answer += end - start
        start, end = arr[i][0], arr[i][1]

answer += end - start
print(answer)