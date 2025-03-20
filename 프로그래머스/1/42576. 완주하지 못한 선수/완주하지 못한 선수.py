def solution(participant, completion):
    p = set(participant)
    s = set(completion)
    dict = {}
    
    for name in participant:
        dict[name] = dict.get(name,0) + 1
        
    for name in completion:
        dict[name] -= 1
    
    for name, cnt in dict.items():
        if cnt != 0:
            return name