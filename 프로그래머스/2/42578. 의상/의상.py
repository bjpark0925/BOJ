from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(set)
    
    for name, typ in clothes:
        clothes_dict[typ].add(name)
    
    for typ in clothes_dict:
        answer *= len(clothes_dict[typ])+1
    
    return answer-1