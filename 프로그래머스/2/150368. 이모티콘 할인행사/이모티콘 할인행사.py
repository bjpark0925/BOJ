answer0 = 0
answer1 = 0

def solution(users, emoticons):
    answer = []    
    
    def dfs(e_index, sum_list):
        global answer0
        global answer1
        
        if e_index == len(emoticons):
            temp_answer0 = 0
            temp_answer1 = 0
            for percent, limit in users:
                temp_sum = 0
                for i in range(len(sum_list)):
                    if percent <= sum_list[i][0]:
                        temp_sum += sum_list[i][1]
                if limit <= temp_sum:
                    temp_answer0 += 1
                else:
                    temp_answer1 += temp_sum
            
            if answer0 == temp_answer0:
                if answer1 < temp_answer1:
                    answer1 = temp_answer1
            elif answer0 < temp_answer0:
                #print(sum_list)
                answer0 = temp_answer0
                answer1 = temp_answer1
            
            return
        
        for d in range(10, 41, 10):
            sum_list.append([d, emoticons[e_index]*(100-d)//100])
            dfs(e_index+1, sum_list)
            sum_list.pop()
            
    dfs(0, [])
    answer.append(answer0)
    answer.append(answer1)
    
    return answer