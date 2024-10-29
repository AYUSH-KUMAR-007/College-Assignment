def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test
arr = [3, 4, 5, 1, 9]
target = 5
result = linear_search(arr, target)
print(f"Element {target} found at index: {result}")
