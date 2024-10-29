def find_triplet(arr, target):
    arr.sort()
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                return [arr[i], arr[left], arr[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return []

# Test
arr = [1, 4, 45, 6, 10, 8]
target = 22
triplet = find_triplet(arr, target)
print(f"Triplet with sum {target}: {triplet}")
