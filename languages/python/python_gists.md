# Python常用代码片段

## Code

``` py
# coding=utf-8
# encoding: utf-8

# https://stackoverflow.com/a/1747827/4757521
d = {key: value for (key, value) in interable}      # 生成字典
bin(0x7f)                                           # 16hex to 2 bin
del lst[:]                                          # 清除列表, 且不成为空列表
a = a or None                                       # 过滤''和None 为 None
os.path.basename('path')                            # 获取文件(夹)名称
id(object)                                          # 获取对象id, 用来区分
time func()                                         # 计算用时
list.index(value)                                   # 通过值获取下标
list1 + list2                                       # 数据拼接(list concatenate)
f'{foo:<8}'                                         # 制表, 左对齐, 8宽度
fr'{foo\n}'                                         # Raw f-strings
for _ in range(n)                                   # loop n
a, b = 1, 2                                         # 等式右边求值后一次性赋值, 左边从左向右依次接收
                                                    # 链表逆序写作, 先写node, 再写node.next
float('-inf')                                       # 表示最小值
float('inf')                                        # 表示最大值
x % 2                                               # 取余, True为奇数
x & 1                                               # 与操作, True为奇数
x //= 2                                             # 地板除(天花板5, 地板4, 4.5在中间, //就是4), 向下取整
x >>= 1                                             # 右移操作, 结果类似向下取整
```

## DateTime

``` py
from datetime import date, datetime, time

# date to datetime
datetime.combine(date(2019, 3, 4), time.min)
# today
datetime.date.today()
# format to str
datetime.strftime('%Y年%m月%d日 %H:%M')
```

## Usage

### 计数(字符串)

``` py
from collections import Counter
a = Counter('manager')
# Counter({'m': 1, 'a': 2, 'n': 1, 'g': 1, 'e': 1, 'r': 1})
```

### print traceback

``` py
import traceback
traceback.print_exc()
```

### str2bool

    string.lower() in ('true', 'false')

### 单词首字母大写

    string.title()

### 转码

``` py
# 字母转ascii
ord('c')
# 十进制转十六进制
hex(number)
# 字符串转换为字符列表
list('string')
# 二进制书写
chr(0b01110111)
```

### logger level

> <https://stackoverflow.com/a/30086809/4757521>

``` py
import logging
from flask import Flask
app = Flask(__name__)  # or instead of __name__ provide the name of the module
app.logger.setLevel(logging.ERROR)
```

### 多错误(multiple exceptions in one line)

``` py
except (IDontLikeYouException, YouAreBeingMeanException) as e:
    pass
```

### 多进程

``` py
from concurrent.futures import ProcessPoolExecutor

with futures.ProcessPoolExecutor() as executor:
    # default max_workers=os.cpu_count()
    do_something
```

### 随机

``` py
import random
# 随机选择
random.choice(FOO_LIST)
# 区间随机生成
random.randint(0, 9)
```

### copy file

> <https://stackoverflow.com/a/123212/4757521>

``` py
from shutil import copyfile

copyfile(src, dst)
```

### try import

``` py
try:
    from local_settings import *
except ImportError as e:
    pass
```

### CamelCase to snake_case

Class Name 类名 转换 convert

> <https://stackoverflow.com/a/1176023/4757521>

``` py
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
```

or

    import inflection
    inflection.underscore('CamelCase')  # camel_case

### clear list

> <https://stackoverflow.com/a/1400622/4757521>

``` py
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

``` py
import os, os.path

# simple version for working with CWD
print len([name for name in os.listdir('.') if os.path.isfile(name)])

# path joining version for other paths
DIR = '/tmp'
print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
```

### 某路径加入环境变量

``` py
import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(abspath(__file__))))
```

### SQL String Format

> <https://stackoverflow.com/a/9433548/4757521>

``` py
sql = ('select field1, field2, field3, field4 '
       'from table '
       'where condition1=1 '
       'and condition2=2 ')
```

### 生成随机数

``` py
import os
import binascii

print(binascii.hexlify(os.urandom(32)))
```

### 对象有没有属性

> <https://stackoverflow.com/q/610883/4757521>

``` py
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

``` py
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

### list和字符串操作

``` py
a = []
b = 'abc'
a.append(b)     # ['abc',]
a += b          # ['a', 'b', 'c']
a += b,         # ['abc',], 注意逗号
a += [b]        # ['abc',], 等价上面
```

### list按内部元素特定规则排序

    # 按元素的第三子元素项排序
    unsorted_list.sort(key=lambda x: x[3])
    # 有返回值
    sorted(unsorted_list, key = lambda x: int(x[3]))

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

## Dict

### 判断dict为空

> <https://stackoverflow.com/a/23177452/4757521>

利用空dict布尔值为False

    dct = {}
    bool(dct)       # False
    not dct         # True

### dict add(字典 增加)

    dict.update({})

### 获取上一个对象

``` py
old = '123'
new = _         # new: '123'
```

### 输出解释器路径

``` py
# http://stackoverflow.com/a/2589722/4757521
import sys
print(sys.executable)
```

### 3.7 breakpoint 断点

``` py
breakpoint()
# equal
import pdb; pdb.set_trace()

# disable
PYTHONBREAKPOINT=0 python3.7 foo.py

# use pudb
PYTHONBREAKPOINT=pudb.set_trace python3.7 foo.py
# equal
import pudb; pudb.set_trace()

# web debug(when use WSGI)
pip install web-pdb
export PYTHONBREAKPOINT='web_pdb.set_trace'
# localhost:5555
```
