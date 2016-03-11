#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-10 10:34:41
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

"""
时间复杂度: O(n lg n)
稳定
"""
import numpy

a = [3, 41, 52, 26, 38, 57, 9, 49]

print(a)
numpy.random.shuffle(a)
# a = numpy.random.permutation(a)
print(a)


def merge_sort(result):
    # 中分为2个序列, 递归求解
    r = len(result)
    if r <= 1:
        return result
    mid = int(r / 2)
    left = merge_sort(result[:mid])
    right = merge_sort(result[mid:])
    return merge(left, right)


def merge(left, right):
    # 两个有序的序列合并, 当一个序列已空, 直接合并另一个序列剩余值
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

print(merge_sort(a))
