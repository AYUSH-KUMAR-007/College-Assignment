def find_pair_with_sum(arr, target_sum):
    seen = set()
    for num in arr:
        if target_sum - num in seen:
            return (target_sum - num, num)
        seen.add(num)
    return None

arr = [8, 7, 2, 5, 3, 1]
target_sum = 10
print("Pair with sum {}: {}".format(target_sum, find_pair_with_sum(arr, target_sum)))
