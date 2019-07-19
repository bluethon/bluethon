from typing import List


def quick_sort(a: List[int]):
    """
    取随意值(此处使用数组第一个元素), 进行分区操作
    分成小于等于pivot的, 和大于的(由和小于的元素进行交换操作得到)
    递归子问题
    """
    def _qsort(a, start, end):
        # 退出条件, 下标重合或者越界
        if start >= end:
            return

        # partition操作, 可抽象成func
        # 分区值依据
        mid = start         # key
        pivot = a[start]    # value
        # 循环数组内其他值, 注意都有+1, end+1因为边界右开
        # 循环完毕后从[start+1, mid]为小于等于的值
        for i in range(start+1, end+1):
            # 分组依据, 小于等于
            if a[i] <= pivot:
                # 每有满足条件, mid右移, 最终指向最后一个满足条件k的位置
                mid += 1
                # 每次a[i]满足条件, 交换mid和i的指向值
                a[mid], a[i] = a[i], a[mid]
        # 将pivot(此处为start指向, 由上面得出)与最后一个满足的位置[mid]交换
        a[start], a[mid] = a[mid], a[start]
        # 执行完毕, 形成 [小等] pivot [大] 格局

        # 递归子问题, 区间均不包含pivot
        _qsort(a, start, mid - 1)
        _qsort(a, mid + 1, end)
        return a
    # 传入下标, 注意右边界
    return _qsort(a, 0, len(a)-1)
