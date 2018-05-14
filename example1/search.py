def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guss = list[mid]
        if guss > item:
            high = mid - 1
        else:
            low = mid + 1
    return mid
