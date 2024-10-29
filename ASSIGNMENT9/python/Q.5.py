def max_len_equal_zeros_ones(arr):
    sum_map = {}
    current_sum = 0
    max_len = 0
    end_index = -1
    
    for i, num in enumerate(arr):
        current_sum += -1 if num == 0 else 1
        if current_sum == 0:
            max_len = i + 1
            end_index = i
        if current_sum in sum_map:
            if max_len < i - sum_map[current_sum]:
                max_len = i - sum_map[current_sum]
                end_index = i
        sum_map.setdefault(current_sum, i)
    
    return arr[end_index - max_len + 1:end_index + 1] if end_index != -1 else []

arr = [0, 0, 1, 0, 1, 0, 0]
print("Max length subarray with equal 0’s and 1’s:", max_len_equal_zeros_ones(arr))
