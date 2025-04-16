# 비트마스킹(visited = set() 대신)
# 이진수 1101 -> 3,2,0번 방문 상태를 의미
# 임의의 점 0번부터 출발 -> DFS로 다음 점 순회 -> 이전에 계산된 루트라면 DP 테이블에서 값 가져옴
import sys
input = sys.stdin.readline

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]

dp = {}

def dfs(now, visited):
    if visited == (1<<n) - 1: # 모든 점 방문 완료. 이땐 next를 찾지 않고 출발점(0번)으로 돌아가기
        if W[now][0]:
            return W[now][0]
        else: # 출발점(0번)으로 가는 경로 없으면
            return int(1e9)

    if (now, visited) in dp:
        return dp[(now, visited)]
    
    min_cost = int(1e9)
    for next in range(1,n):
        if W[now][next] == 0 or visited & (1<<next): # 비용이 0 or 이미 방문은 next에서 제외
            continue
        cost = dfs(next, visited|(1<<next)) + W[now][next]
        min_cost = min(cost, min_cost)

    dp[(now, visited)] = min_cost
    return min_cost
    
print(dfs(0,1))
'''
점 4개 예시: 0 1 2 3
dp[(0,방문0)]의 cost = dfs(1,방문01) + W[0][1] # 1부터 나머지 경로의 비용 + 0 ->1 비용
			                = dfs(2,방문012) + W[1][2]
				                    = dfs(3,방문0123) + W[2][3]
					                        = W[3][0]
여기서 계산된 경로의 cost 중 최솟값은 min_cost에 업데이트
dp[(now, visited)]에 min_cost 기록
	dp[(2,방문012)]에 2->3->0 비용 기록됨
	dp[(1,방문01)]에 1->2->3->0 비용 기록됨. 반복문 돌며 1->3->2->0 비용과 비교해 더 작은 값이 기록됨.
	dp[(0,방문0)]에 0->1->2->3->0 비용 기록됨

dp 사용처: 점이 0부터 6까지인 상태에서
0->1->2->3 순회로 dp[(3,방문0123)]이 기록되고(ex. 3->4->5->6->0의 최솟값), 이후
0->2->1->3 순회할 경우 3부터 도착점까지(ex. 3->4->5->6->0)의 경로는 이미 알고 있으므로 이미 계산된 값을 활용.
'''