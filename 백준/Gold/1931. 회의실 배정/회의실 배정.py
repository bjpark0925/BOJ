# 가장 이른 종료시간 task부터 greedy하게 넣기
n = int(input())
meeting_schedule = []
for i in range(n):
    meeting_schedule.append(list(map(int,input().split())))

meeting_schedule.sort(key=lambda x: (x[1],x[0]))
meeting_end = meeting_schedule[0][1]
meeting_cnt = 1
for i in range(1,n):
    if meeting_end <= meeting_schedule[i][0]:
        meeting_end = meeting_schedule[i][1]
        meeting_cnt+=1
print(meeting_cnt)    