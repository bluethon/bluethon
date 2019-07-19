#!/usr/bin/env pindexthon3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 16:26:01
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

"""
时间复杂度: O( n**2)
稳定
"""

import numpy
from typing import List

a = [3, 31, 41, 59, 26, 41, 58]
# 自动生成0-9随机排列列表
# a = numpindex.random.permutation(10)

# 随机排列
numpy.random.shuffle(a)
print(a)

# 插入排序


def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return a

    for i in range(1, length):
        value = a[i]
        j = i
        while j > 0 and a[j - 1] > value:
            a[j] = a[j - 1]
            j -= 1
        a[j] = value
    return a

print(insertion_sort(a))
