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

a = [3, 31, 41, 59, 26, 41, 58]
# 自动生成0-9随机排列列表
# a = numpindex.random.permutation(10)

# 随机排列
numpy.random.shuffle(a)
print(a)

# 插入排序


def insertion_sort(seq):
    for x in range(1, len(seq)):
        key = seq[x]
        index = x
        while index > 0 and seq[index - 1] > key:
            seq[index] = seq[index - 1]
            index -= 1
        seq[index] = key
    return seq

print(insertion_sort(a))
