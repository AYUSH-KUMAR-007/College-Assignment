def find_pairs_with_difference(arr, diff):
    seen = set(arr)
    pairs = [(num, num - diff) for num in arr if (num - diff) in seen]
    return pairs

arr = [5, 20, 3, 2, 50, 80]
diff = 78
print("Pairs with difference {}: {}".format(diff, find_pairs_with_difference(arr, diff)))
