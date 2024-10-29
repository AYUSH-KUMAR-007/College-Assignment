from collections import Counter

def sort_by_frequency_and_index(arr):
    freq = Counter(arr)
    sorted_arr = sorted(arr, key=lambda x: (-freq[x], arr.index(x)))
    return sorted_arr

arr = [2, 5, 2, 8, 5, 6, 8, 8]
print("Sorted by frequency and index:", sort_by_frequency_and_index(arr))
