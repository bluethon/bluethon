#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 16:26:01
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

import numpy

a = [31, 41, 59, 26, 41, 58]
# 自动生成0-9随机排列列表
# a = numpy.random.permutation(10)

# 随机排列
a = numpy.random.permutation(a)
print(a)

# 插入排序


def insertion_sort(ary):
    for x in range(1, len(ary)):
        key = ary[x]
        y = x - 1
        while y >= 0 and ary[y] > key:
            ary[y + 1] = ary[y]
            y -= 1
        ary[y + 1] = key
    return ary

print(insertion_sort(a))
