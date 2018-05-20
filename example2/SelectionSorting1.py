# 选择排序
def find_smallest(attr):
    smallest = attr[0]
    smallest_index = 0
    for i in range(1, len(attr)):
        if attr[i] < smallest:
            smallest=attr[i]
            smallest_index = i
    return smallest_index
