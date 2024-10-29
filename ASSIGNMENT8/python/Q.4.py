def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Test
arr = [1, 2, 3, 2, 3, 1, 3]
odd_occurrence = find_odd_occurrence(arr)
print(f"Element occurring odd number of times: {odd_occurrence}")
