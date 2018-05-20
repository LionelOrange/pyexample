# 选择排序运行程序，对数组进行排序
from example2.SelectionSorting1 import find_smallest


def selection_sort(attr):
    new_attr = []
    for i in range(len(attr)):
        smallest = find_smallest(attr)
        new_attr.append(attr.pop(smallest))
    return new_attr
