# segment tree
import sys
input = sys.stdin.readline

def makeTree(start, end, index):
    if start == end:
        segment_tree[index] = arr[start]
        return segment_tree[index]
    mid = (start + end) // 2
    # 1번 노드(0번부터 4번까지 합) = 왼쪽 자식(0번부터 2번까지 합) + 오른쪽 자식(3번부터 4번까지 합)
    segment_tree[index] = makeTree(start, mid, 2*index) + makeTree(mid+1, end, 2*index + 1)
    return segment_tree[index]

def updateTree(start, end, index, target_index, value):
    # target_index가 범위 밖
    if target_index < start or target_index > end:
        return
    # 범위 내
    segment_tree[index] += value
    if start == end: # 리프 노드 시 종료(중요)
        return
    
    mid = (start + end) // 2
    updateTree(start, mid, 2*index, target_index, value) # 왼쪽 자식
    updateTree(mid+1, end, 2*index + 1, target_index, value) # 오른쪽 자식

def calcSum(start, end, index, target_start, target_end):
    # 범위 밖
    if target_end < start or target_start > end:
        return 0 # int형 리턴값 존재해야 함(중요)
    # hit
    if target_start <= start and end <= target_end:
        return segment_tree[index]
    # 범위 내지만 더 탐색 필요
    mid = (start + end) // 2
    return calcSum(start, mid, 2*index, target_start, target_end) + calcSum(mid+1, end, 2*index + 1, target_start, target_end)    

n,m,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

segment_tree = [0] * (n*4) # 리프노드 수가 17(2의 제곱수+1)인 경우 생각하면, 기존 트리 노드(2*n개) 외 빈 공간이 2*n만큼 더 필요
makeTree(0, n-1, 1) # 루트(0부터 n-1까지의 합을 저장)의 index가 1부터 시작해야, 왼쪽 자식은 2*index, 오른쪽 자식은 2*index+1이 됨
for _ in range(m+k):
    a,b,c = map(int, input().split())
    if a == 1:
        updateTree(0, n-1, 1, b-1, c-arr[b-1]) # 새 값과 기존 값의 차를 범위 내의 트리 노드들에 더하기
        arr[b-1] = c # 중요
    elif a == 2:
        print(calcSum(0, n-1, 1, b-1, c-1))