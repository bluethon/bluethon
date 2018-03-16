Python常用代码片段
================

CMD
---

``` python
# coding=utf-8
# encoding: utf-8

d = {key: value for (key, value) in interable}      # 生成字典    https://stackoverflow.com/a/1747827/4757521
bin(0x7f)                                           # 16hex to 2 bin
datetime.date.today()                               # 今天    > datetime
del lst[:]                                          # 清除列表, 且不成为空列表
a = a or None                                       # 过滤''和None 为 None
os.path.basename('path')                            # 获取文件(夹)名称
```

Usage
-----

### copy file

> https://stackoverflow.com/a/123212/4757521

``` python
from shutil import copyfile

copyfile(src, dst)
```

### try import

``` python
try:
    from local_settings import *
except ImportError as e:
    pass
```

### CamelCase to snake_case

Class Name 类名 转换 convert

> <https://stackoverflow.com/a/1176023/4757521>

``` python
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
```

or

    import inflection
    inflection.underscore('CamelCase')  # camel_case

### clear list

> <https://stackoverflow.com/a/1400622/4757521>

``` python
# actually removes the contents from the list, not replaces the old label with a new empty list
del lst[:]
# equal
lst[:] = []
# for Py3
lst.clear()

# !!!not do this
lst = []
# because if
b = lst
# b still have all element
```

### count directory files

> <https://stackoverflow.com/a/2632251/4757521>

``` python
import os, os.path

# simple version for working with CWD
print len([name for name in os.listdir('.') if os.path.isfile(name)])

# path joining version for other paths
DIR = '/tmp'
print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
```

### datetime

> <http://www.wklken.me/posts/2015/03/03/python-base-datetime.html>

### 某路径加入环境变量

``` python
import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(abspath(__file__))))
```

### SQL String Format

> <https://stackoverflow.com/a/9433548/4757521>

``` python
sql = ('select field1, field2, field3, field4 '
       'from table '
       'where condition1=1 '
       'and condition2=2 ')
```

### 生成随机数

``` python
import os
import binascii

print(binascii.hexlify(os.urandom(32)))
```

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

## List

### list拼接

    a = [1, 2]
    b = [3, 4]
    a.extend(b)     # [1, 2, 3, 4]

### list循环

> <https://stackoverflow.com/a/126533/4757521>

    a = []
    for i, v in enumerate(a):
        print i, v

### 获取list第一个元素

    return next(iter(user or []), None)

### py2 字典循环 dict for

    for key, value in d.iteritems():
        pass


## Dict

### 判断dict为空

> <https://stackoverflow.com/a/23177452/4757521>

利用空dict布尔值为False

    dct = {}
    bool(dct)       # False
    not dct         # True

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
