def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Test (array should be sorted)
arr = [10, 20, 30, 40, 50]
target = 30
result = interpolation_search(arr, target)
print(f"Element {target} found at index: {result}")
