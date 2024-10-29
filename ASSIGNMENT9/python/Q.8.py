from collections import OrderedDict

def group_by_first_occurrence(arr):
    result = list(OrderedDict.fromkeys(arr))
    return result

arr = [3, 5, 3, 2, 8, 2, 5]
print("Grouped by first occurrence:", group_by_first_occurrence(arr))
