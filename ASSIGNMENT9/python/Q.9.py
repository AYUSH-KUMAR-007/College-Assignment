def min_index_of_repeating_element(arr):
    seen = {}
    min_index = len(arr)
    for i, num in enumerate(arr):
        if num in seen:
            min_index = min(min_index, seen[num])
        else:
            seen[num] = i
    return min_index if min_index != len(arr) else None

arr = [1, 2, 3, 2, 1]
print("Minimum index of repeating element:", min_index_of_repeating_element(arr))
