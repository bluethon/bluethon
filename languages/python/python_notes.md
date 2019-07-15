# Python学习笔记

## Debug(易错)

``` py
# set添加, add, 不是append
a = set()
a.add('123')
```

## Note

### 函数可变参数(定义时初始化, 而不是每次调用)

> <https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments>

### 展开map为list

    [*map(LIST, SET)]

### 文件是否存在

``` python
from os.path import exists
# return True or False
exists(foo.py)
```

### %r

调试时尽量使用`%r`, `%r`可以显示变量的"原始"数据值, 打印时重现其代表的对象

### print不换行

``` python
# py2
print x,
# py3
# print函数原型, 所以一句中输出多个中间会加空格, 末尾会加换行符
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# 重载为不换行
print(x, end='')
# 输出换行符
print()
```
