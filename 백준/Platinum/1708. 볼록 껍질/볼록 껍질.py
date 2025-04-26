# 모노톤 체인
n = int(input())

# 점을 x좌표 순으로 정렬(같으면 y좌표 순)
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x,y])
points.sort(key=lambda x:(x[0],x[1]))
    
def ccw(p1, p2, p3): # 외적 값이 마이너스이면 cw. 플러스이면 ccw
    # 외적 값 = ad - bc
    # 점 (a, b) = (x2-x1, y2-y1)
    # 점 (c, d) = (x3-x1, y3-y1)
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

# 순서대로 스택에 넣기
# 스택의 마지막 두 점과 새로 들어올 점끼리 CW 계산 - 윗껍질 생성
cw_stack = []
for p3 in points:
    while len(cw_stack) >= 2:
        p1, p2 = cw_stack[-2], cw_stack[-1]
        if ccw(p1, p2, p3) < 0:
            break
        cw_stack.pop() # ccw==0이라 같은 직선 내 p2, p3 존재할 경우에도 p2 제거 필요(이미 정렬되어 있어 p3가 더 멀리 있으므로 p3가 채택되도록)
    cw_stack.append(p3)
#print(cw_stack)
#print(len(cw_stack))

# CCW 계산 - 아랫껍질(위의 CW코드에서 points의 마지막 값부터 순회하면 코드 중복 피할 수 있음)
ccw_stack = []
for p3 in points:
    while len(ccw_stack) >= 2:
        p1, p2 = ccw_stack[-2], ccw_stack[-1]
        if ccw(p1, p2, p3) > 0:
            break
        ccw_stack.pop()
    ccw_stack.append(p3)
#print(ccw_stack)
#print(len(ccw_stack))

print(len(cw_stack) + len(ccw_stack) - 2) # 윗껍질과 아랫껍질은 점 2개가 중복됨