#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 16:26:01
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

import numpy

a = [31, 41, 59, 26, 41, 58]


def insertion_sort(ll):
    for x in range(1, len(ll)):
        key = ll[x]
        y = x - 1
        while y >= 0 and ll[y] > key:
            ll[y + 1] = ll[y]
            y -= 1
        ll[y + 1] = key
    return ll

print(insertion_sort(a))
