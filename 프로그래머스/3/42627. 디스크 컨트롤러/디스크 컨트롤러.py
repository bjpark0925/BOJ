import heapq

def solution(jobs):
    jobs.sort()

    current_time = 0
    prev_time = -1
    
    total_time = 0 # answer = total_time / len(jobs)
    finish_cnt = 0 # 완료한 job 수
    wait_q = []
    
    while finish_cnt < len(jobs):
        for job in jobs:
            if prev_time < job[0] <= current_time:
                heapq.heappush(wait_q, (job[1],job[0])) # 소요시간, 요청시각 순
        
        if wait_q:
            running_job = heapq.heappop(wait_q)
            prev_time = current_time
            current_time += running_job[0]
            total_time += (current_time - running_job[1])
            finish_cnt += 1
            
        else:
            current_time+=1

    answer = int(total_time / len(jobs))
    return answer