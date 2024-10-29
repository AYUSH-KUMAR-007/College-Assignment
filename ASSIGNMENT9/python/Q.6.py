def largest_consecutive_subarray(arr):
    max_len = 0
    max_subarray = []
    for i in range(len(arr)):
        visited = set()
        min_val, max_val = arr[i], arr[i]
        
        for j in range(i, len(arr)):
            if arr[j] in visited:
                break
            visited.add(arr[j])
            min_val = min(min_val, arr[j])
            max_val = max(max_val, arr[j])
            if max_val - min_val == j - i:
                if max_len < j - i + 1:
                    max_len = j - i + 1
                    max_subarray = arr[i:j+1]
    return max_subarray

arr = [2, 0, 2, 1, 4, 3, 1, 0]
print("Largest consecutive subarray:", largest_consecutive_subarray(arr))
