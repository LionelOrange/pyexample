# 二分查找算法
def binary_search(col, item):
    low = 0
    high = len(col) - 1
    while low <= high:
        mid = (low + high) // 2
        guss = list[mid]
        if guss > item:
            high = mid - 1
        elif guss == item:
            return mid
        elif guss < item:
            low = mid + 1

    return None
