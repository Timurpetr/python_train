def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    score = 0
    while low <= high:
        score += 1
        mid = (low + high) // 2
        mid_val = lst[mid]
        if mid_val == item:
            return mid_val
        elif mid_val > item:
            high = mid - 1
        else:
            low = mid + 1
        print(score)
    return None


print(
    binary_search(
        [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 23, 123, 432, 1234, 52345, 62345], 62345
    )
)
