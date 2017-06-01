Python常用代码片段
================

### 对象有没有属性

> <https://stackoverflow.com/q/610883/4757521>

``` python
if hasattr(a, 'property'):
    a.property

try:
    val = a.property
except AttributeError:
    otherStuff()
else:
    doStuff(val)
```

### json to dict to object

> <http://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html>

``` python
import json
s = '{"name": "ACME", "shares": 50, "price": 490.1}'

# support nested
class JSONObject():
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
data.time

# alternative
# nested can't work 嵌套的json会有问题
class Payload():
    def __init__(self, j):
        self.__dict__ = json.loads(j)

data = Payload(j)
```

### list循环

> <https://stackoverflow.com/a/126533/4757521>

    a = []
    for i, v in enumerate(a):
        print i, v

### py2 字典循环 dict for

    for key, value in d.iteritems():
        pass

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
