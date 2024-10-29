def max_len_subarray_with_sum(arr, target_sum):
    sum_map = {}
    current_sum = 0
    max_len = 0
    end_index = -1
    
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum == target_sum:
            max_len = i + 1
            end_index = i
        if current_sum - target_sum in sum_map:
            if max_len < i - sum_map[current_sum - target_sum]:
                max_len = i - sum_map[current_sum - target_sum]
                end_index = i
        sum_map.setdefault(current_sum, i)
    
    return arr[end_index - max_len + 1:end_index + 1] if end_index != -1 else []

arr = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target_sum = 8
print("Max length subarray with sum {}: {}".format(target_sum, max_len_subarray_with_sum(arr, target_sum)))
