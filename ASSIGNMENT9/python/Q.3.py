def print_zero_sum_subarrays(arr):
    subarrays = []
    sum_map = {}
    current_sum = 0
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum == 0:
            subarrays.append(arr[:i+1])
        if current_sum in sum_map:
            for start in sum_map[current_sum]:
                subarrays.append(arr[start+1:i+1])
        sum_map.setdefault(current_sum, []).append(i)
    return subarrays

arr = [3, 4, -7, 3, 1, 3, 1, -4]
print("Zero-sum subarrays:", print_zero_sum_subarrays(arr))
