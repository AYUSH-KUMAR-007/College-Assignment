def has_zero_sum_subarray(arr):
    seen_sums = set()
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum == 0 or current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)
    return False

arr = [4, 2, -3, 1, 6]
print("Subarray with 0 sum exists:", has_zero_sum_subarray(arr))
