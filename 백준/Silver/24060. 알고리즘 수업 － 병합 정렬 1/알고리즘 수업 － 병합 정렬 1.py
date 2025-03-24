def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = (len(arr)//2)+(len(arr)%2)
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    i, j = 0, 0
    sorted_arr = []
    global save_values
    
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted_arr.append(left_arr[i])
            save_values.append(left_arr[i])
            i+=1
        else:
            sorted_arr.append(right_arr[j])
            save_values.append(right_arr[j])
            j+=1
    
    if i<len(left_arr):
        sorted_arr+=left_arr[i:]
        save_values+=left_arr[i:]
        
    if j<len(right_arr):
        sorted_arr+=right_arr[j:]
        save_values+=right_arr[j:]
    
    return sorted_arr

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    save_values = []
    sorted_list = merge_sort(arr)
    if len(save_values) < k:
        print(-1)
    else:
        print(save_values[k-1])