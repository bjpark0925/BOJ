# 이분 매칭: 제가 이 일 처리할 테니 님 다른 일 가능한지 한번 알아보시고 불가능하시면 제가 다른 일 알아볼게요
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]  # 사람 번호는 1부터 시작
# 사람: 일
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for job in data[1:]:
        graph[i].append(job)

matched = [0] * (m+1)  # 각 일에 배정된 사람 번호 저장, 0은 미배정 상태
# matched[일 번호] = 사람 번호
def dfs(person, visited):
    for job in graph[person]:
        if visited[job]:
            continue
        visited[job] = True
        # 일(job)이 아직 비어있으면 바로 배정. 그 일을 맡은 사람을 다른 일로 옮길 수 있는지 재귀적 확인
        if matched[job] == 0 or dfs(matched[job], visited):
            matched[job] = person
            return True
    return False

result = 0
for person in range(1, n+1): # 모든 사람에 대해 가능한 매칭 시도
    visited = [False] * (m+1)
    if dfs(person, visited):
        result += 1

print(result)
