Python常用代码片段
================

### 获取list第一个元素

    return next(iter(user or []), None)

### dcit add(字典 增加)

    dict.update({})

### datetime时间格式化

``` python
datetime.strftime('%Y年%m月%d日 %H:%M')
```

### 获取上一个对象

``` python
old = '123'
new = _         # new: '123'
```

### 输出解释器路径

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
