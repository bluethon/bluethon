from typing import List


def bubble_sort(a: List[int]):
    """ 比较相邻, 前大后小交换 """
    length = len(a)
    # 边界处理
    if length <= 1:
        return a

    for i in range(length):
        is_swap = False
        for j in range(length - i - 1):
            # 前后两个大小相反, 交换
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                is_swap = True
        # 优化, 无交换跳过后续
        if not is_swap:
            break
    return a

