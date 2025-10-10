def solution(nums):
    pick = len(nums) // 2
    
    nums_set = set(nums)
    nums_set_len = len(nums_set)  
    
    return min(pick, nums_set_len)