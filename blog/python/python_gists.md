Python常用代码片段
================

获取上一个对象
-----------

``` python
old = '123'
new = _         # new: '123'
```

输出解释器路径
---

``` python
# http://stackoverflow.com/a/2589722/4757521
import sys
print(sys.executable)
```

转码
----
``` python
# 字母转ascii
ord('c')
# 十进制转十六进制
hex(number)
# 字符串转换为字符列表
list('string')
# 二进制书写
chr(0b01110111)
```