from typing import List


def selection_sort(a: List[int]):
    """ 遍历, 每次选出最小的, 插入队头 """
    length = len(a)
    if length <= 1:
        return a

    for i in range(length):
        min_index = i
        for j in range(i, length):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

