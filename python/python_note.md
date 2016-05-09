Python学习笔记
=============

## 缩写

    repr        representation                  给解释器的显示类型
    pprint      pretty printer
    URI         Uniform Resource Identifier     统一资源标识符
    URL         Uniform Resource Locator        统一资源定位器
    SMTP        Simple Mail Transfer Protocol   简单邮件传输协议
    regex       Regular Expressions             正则表达式
    CSRF        Cross-Site Request Forgery      跨站请求伪造

    <div>       division                        层, 分区
    <ul>        Unordered List                  无序列表
    <ol>        Ordered List                    有序列表
    <li>        List Item                       列表项

## 名词解释

    metaclass       元类

---

## Python核心编程

    2.03    P022    文档字符串, 起在线文档功能
    2.05    P024    Python不支持自增, 会解释为+(+n)
    2.13    P030    [enumerate()同时循环索引和元素]


    2.14    P030    列表解析, 将for if等放到list中, 一行实现
    2.20    P036    实用内建函数
    3.5.4   P051    对象被回收的时机
    3.6     P053    使用局部变量替换模块变量加速原理
    3.6     P054    [for循环中print不换行]
    4.4.4   P060    切片操作d


``` python

# P030
for i, ch in enumerate(list):
    print(i, ch)

# P054
#for循环中print不换行
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

---

## 廖雪峰教程笔记

**文件头**

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

**web调试**

`__main__`中`app.run(debug=True)`开启调试

**查看帮助文档**

`pydoc function_or_module`

**类执行顺序**
从上向下执行, 定义需要放前面
或者采取如下格式, 就可以把代码放最上面了

``` python
def main():
    ...
def other_functions():
    ...
if __name__ == '__main__':
    main()
```

上面`if`格式最主要作用是当前`.py`文件如果执行, `__name__`为`__main__`
此时执行程序, 当被import时, __name__为文件名, 此时就不执行了
<http://stackoverflow.com/questions/419163/what-does-if-name-main-do>
<http://www.cnblogs.com/xuxm2007/archive/2010/08/04/1792463.html>

**判断变量是否为某类型***

``` python
isinstance(s, string)
```

**print格式化输出**

``` python
nHex = 0x20
#%x --- hex 十六进制
#%d --- dec 十进制
#%o --- oct 八进制
%015   长度15 不足前导0补齐
```

回车换行
` \n 10 \x0a` newline 换行
` \r 13 \x0d` return 回车

#### 字符串

字符串长度

    len('string')

字符串拼接 `+`

#### 数据类型和变量
**多行转义**

``` python
r'''
'''
```

**ASCII**
A = 65
z = 122
**ASCII转换**
`ord('A')`
`chr(65)`

**Unicode表示的字符串用`u''`表示**
`u'A' == u'\u0041'`
**把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法**
` u'ABC'.encode('utf-8')`
'ABC'
`u'中文'.encode('utf-8')`
'\xe4\xb8\xad\xe6\x96\x87'

英文字符转换后表示的`UTF-8`的值和`Unicode`值相等(但占用的存储空间不同)
反过来，把UTF-8编码表示的字符串`'xxx'`转换为`Unicode`字符串`u'xxx'`用`decode('utf-8')`方法:

`'abc'.decode('utf-8')`
u'abc'
`'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')`
u'\u4e2d\u6587'
`print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')`
中文

当Python解释器读取源代码时，为了让它按UTF-8编码读取，通常在文件开头写上两行
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照`UTF-8`编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

#### 使用list和tuple
**列表**
`list []`
**最后一个元素的索引**

``` python
len(list)-1
list[-1]
```

**类推倒二**
`list[-2]`
**追加元素到末尾**
`list.append('test')`
**元素插入到1位置**
`list.insert(1, 'test')`
**删除末尾元素**
`list.pop()`
**删除指定位置元素**
`list.pop(i)`
**替换**
`list[1] = 'test'`

#### 元组
tuple一旦初始化就不能修改
也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
tuple()
**tuple的陷阱**：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
` t = (1, 2)`

定义一个只有1个元素的tuple,必须加一个逗号,，来消除歧义
Python显示只有1个元素的tuple时，也会加一个逗号,以免误解成数学计算意义上的括号
`t = (1,)`

#### 条件判断和循环

只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
``` python
if x:
    print 'True'
```


#### 字典
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。


``` python
# init
d = {'Michael': 95, 'Tracy': 85}

# 添加
d['Adam'] = 67
# 删除 2 ways
d.pop('Adam')
del mydic['key1']

# 判断Key是否存在
'Thomas' in d   # back 'False'

# 判断Key是否存在2
# 如果key不存在，可以返回None，或者自己指定的value：
# 注意：返回None的时候Python的交互式命令行不显示结果。
d.get('Thomas')
d.get('Thomas', -1) # back '-1'
```

#### set
- 无序
- set和dict的唯一区别仅在于没有存储对应的value

init 需要一个list, 但是s内的并不是list,所以s内不能存在变量 且重复值会被过滤
``` python
>>>s = set([1, 2, 3, 1])
>>>s
set([1, 2, 3])
```

**增删**
`s.add(4)`
`s.remove(4)`

set 可看成无序和无重复的集合, 可做交 并集操作
``` python
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
set([2, 3])
>>> s1 | s2
set([1, 2, 3, 4])
```
#### 函数参数
`def fn(a, b, c=0, *args, **kw):`
必选参数, 默认参数, 可变参数, 关键字参数
`*args`是可变参数，`args`接收的是一个`tuple`
`**kw`是关键字参数，`kw`接收的是一个`dict`。
对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论它的参数是如何定义的
``` python
print 'a=', a, ' b=', b, ' c=', c, ' args=', args, ' kw=', kw
print '\n==>fn(1, 2)'
fn(1, 2)
print '\n==> fn(1, 2, 3)'
fn(1, 2, 3)
print '\n==> fn(1, 2, 3, 4)'
fn(1, 2, 3, 4)
print '\n==> fn(1, 2, k1=8, k2=9)'
fn(1, 2, k1=8, k2=9)
print '\n==> fn(1, 2, 3, k1=8, k2=9)'
fn(1, 2, 3, k1=8, k2=9)
print '\n==> fn(1, 2, 3, 4, k1=8, k2=9)'
fn(1, 2, 3, 4, k1=8, k2=9)
# interesting part:
print '\n==> fn(*(1, 2))'
fn(*(1, 2))
print '\n==> fn(*(1, 2, 3))'
fn(*(1, 2, 3))
print '\n==> fn(*(1, 2, 3, 4))'
fn(*(1, 2, 3, 4))
print '\n==> fn(*(1, 2, 3, 4), **{ \'k1\': 8, \'k2\': 9 })'
fn(*(1, 2, 3, 4), **{ 'k1': 8, 'k2': 9 })
# TypeError: fn() takes at least 2 arguments (1 given)
print '\n==> fn(*(1, ))'
fn(*(1, ))
```

#### 切片(Slice)
*list和tuple均支持*

`l = range(100)`

从第二开始 取到10(不含), 步长2
`l[1:10:2]`
倒数第一个和第二个元素
`l[-2:-1]`
逆序list
`l[::-1]`


#### 迭代
`d = {'a': 1, 'b': 2, 'c': 3}`

`d.iterkeys()`-- `a, b, c`
`d.itervalues()` 默认` 1, 2, 3`
`d.iteritems()`--`('a', 1)('c', 3)('b', 2)`
``` python
for x in d.iteritems():
    print x
```
**判断对象是否可迭代**
``` python
>>>from collections import Iterable
>>>isinstance('abc', Iterable) #str是否可迭代
True
```

#### 对list实现类似Java那样的下标循环
``` python
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
```

####生成器(generator)
保存的是算法
- 方法一 由List生成
``` python
g = (x for x in range(10))
for x in g:
    print x
```
- 方法二 由函数生成
``` python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        #··· “=”右边先进行计算，即生成一个新的tuple：（b,a+b），
        #之后依次赋值给左边a,b。在内存里是开辟了一个新空间来存储这个计算结果的
        a, b = b, a + b
        n = n + 1

for x in fib(6):
    print x
```

####高阶函数
map/reduce

**map 序列依次代入第一个函数**
`reduce`序列[1, 2]return的值再与后面的第三项作用`f(f(x1, x2),x3)`
``` python
def char2num(s):
    #等价 d{}   d['1']
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))
```

#### 匿名函数
`lambda`

**参数x, y  返回x+y的值**
`lambda x,y: x+y`


#### 闭包(closure)
难点 仍未完全理解

**sum可以直接使用args, 且返回函数本身**
#### 高阶函数
map/reduce

**map 序列依次代入第一个函数**
`reduce`序列[1, 2]return的值再与后面的第三项作用`f(f(x1, x2),x3)`
``` python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
```

#### 偏函数
给函数设定默认参数并生成新函数

`import functools`

**int 参数从base进制转换为10进制**
``` python
4
print int('100', base=2)
4
int2 = functools.partial(int, base=2)
print int2()
```
**多参数固定**
``` python
fun3 = functools.partial(fun, b=2, c=3)
```


#### 别名

**应用场景**
``` python
try:
    import cStringIO as StringIO #cStringIO用C写的 速度快
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
```

#### 类(Class)和实例(Instance)
类内函数(Method)第一个参数永远是实例变量self,
并且,调用时,不用传递该参数
成员不需要预定义,可以直接在实例中增加(不影响其他实例)

#### 获取对象信息
`type()`
**判断对象的引用  的类型**
``` python
>>>type(123)
<type 'int'>
>>>import types
>>>type('abc')==types.StringType
>>>type(int)==types.TypeType
```
**instance()**
`isinstance('a', str)`
**判断变量是某些类型中的一种**
`isinstance('a', (str, unicode))`
**dir()**
> 获得一个对象的所有属性和方法
`>>>dir('abc')`
成员不需要预定义,可以直接在实例中增加(不影响其他实例)

#### 获取对象信息
`type()`
**判断对象的引用  的类型**
``` python
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.xclass MyObject(object):
obj = MyObject()
hasattr(obj, 'x') #是否存在?True
setattr(obj, 'y', 19) #设置
getattr(obj, 'y') #获取属性
getattr(obj, 'y', 404) #获取属性,若不存在,返回默认值404
```

#### `__slots__`
限定可以绑定的方法和属性
仅对当前类起作用, 子类需增加`__slots__`才能继承
`type()`
**判断对象的引用  的类型**
``` python
class Sample(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性
```

#### 定制类
下列均为方法
- `__str__()`
**定义打印类时输出(用户)**
``` python
c = class()
print '%s' % c
```
- `__repr__()`
**定义直接显示变量时输出(开发者), 且一般与`__str__`一致**
`__repr__ = __str__`
`print '%r' % c`

- **`__iter__()`**
#实现循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
for n in Fib():
    print n

- **`__getitem__()`**
自定义实现类似list[1]取出下标元素的方法名

- **`__getattr__()`**
动态返回属性或者方法, 区别为返回值, 见下面
此方法默认返回None, 否则需要抛出AttributeError
当调用不存在的属性或者方法时,会尝试调用`__getattr__`来获得
``` python
def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        elif attr=='name':
            return 'Hello'
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s.name #attr return attr
s.age() #method return lambda: attr
```
这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

上述用例 SDK调用API时
``` python
class Chain2(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print 'self._path:{0}\tpath:{1}'.format(self._path, path)
        #返回一个完整的字符串作为新的Chain2的输入
        return Chain2('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, user):
        print 'self._path:{0}\tuser:{1}'.format(self._path, user)
        return Chain2('%s/%s' % (self._path, user))
```
/users/:user/repos
`print Chain2().users('michael').repos`

- `__call__()`
s()状态下(即实例(instance)本身上调用)调用, 而不是调用s.method()
此时对象和函数的界限已区别不大
没有`__call__`, 返回`TypeError`

判断一个变量是否能被调用
```
>>>callable(Chain2())
True
>>>callable(max)
True
>>>callable('string')
False
```

#### 错误处理
错误捕获可以跨越多层调用, 即子函数错误可由父函数捕获


#### 常见的错误类型和继承关系
https://docs.python.org/2/library/exceptions.html#exception-hierarchy

#### `try`
**try运行,执行出错,跳转except**
``` python
try:
    pass
# 捕获异常,处理后跳转finally
except Exception, e:
    raise
# 如果没有捕获错误, 则会执行else
else:
    pass
# 可没有, 如果存在finally, 则一定会执行
finally:
    pass
```
#### logging
记录错误, 捕获错误后程序会继续执行
``` python
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'
```

#### raise
raise语句如果不带参数，就会把当前错误原样抛出
此例中捕获错误后有raise错误,在于当前函数不知道怎么处理错误,继续向上抛出,让上层调用者处理
raise还可以抛出其他类型错误(转换错误类型,但应做到逻辑合理)
``` python
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise

def main():
    bar('0')

main()
```

#### 调试

**断言**
如果表达式false, 输出后半句, 同时抛出AssertionError
`assert n!=0, 'n is zero!'`
程序运行时可以用-O参数关闭, 此时assert语句相当于 pass
`python -O err.py`

**logging**
允许指定信息记录的级别,debug, info, warning, error
`import logging`
指定level=INFO时,logging,debug就不起作用了,类推
`logging.basicConfig(level=logging.INFO)`
``` python
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
```

**pdb**
- 单步调试
- l 查看代码
- n 下一步
- s 步进+
- r 返回-
- h help
- p [变量] 查看变量值
- q 结束调试

`$ python -m pdb err.py`
`pdb.set_trace()`
- p 查看变量
- c 继续运行
`err.py`
``` python
import pdb
..........
pdb.set_trace() #运行到这里自动暂停
..........
```

#### 文件读写

with语句来自动帮我们调用close()方法
``` python
with open('/path/to/file', 'r') as f:
    print f.read()
```
读取非ASCII编码的文本文件, 必须要二进制打开, 再解码
``` python
import codecs
with codecs.open('/usr/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() #u'\u6d4b\u8bd5'
```
**文件写入同读取 'w' 'wb'->二进制**


**操作文件和目录**

**显示操作系统名称**
`os.name #nt->Windows posix->Linux Unix Mac OS X`
**获取系统详细信息(非Windows)**
`os.uname`
**环境变量**
`os.environ` #查看
`os.getenv('PATH')` #获取
**操作文件和目录**
`import os.path`
**查看当前目录的绝对路径**
`os.path.abspath('.')`
**当前目录下新建目录**
`os.mkdir('./testdir')`
**删除目录**
`os.rmdir('./testdir')`

路径合成,不要直接拼接字符串, 可以正确处理不同操作系统的路径分隔符
不要求路径真实存在,仅是对字符串进行操作
`os.path.join('./part-1', 'part-2')`
- Linux/Unix/Mac
`part-1/part-2`
- Windows
`part-1\part-2`

**路径拆分**
`os.path.split()`
**拆分路径, 后一部分总是最后级别的目录或文件名**
``` python
>>>os.path.split('Users/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
```
**可以直接得到文件扩展名**
```
>>>os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
```
重命名
`os.rename('test.txt', 'test.py')`
删除文件
`os.remove('test.py')`
复制,不在os模块, 在shutil中
```
import shutil
shutil.copyfile(src, dst)
```
列出当前目录下的所有目录(利用Python的特性来过滤文件)
```
x for x in os.listdir('.') if os.path.isdir(x)
```
列出所有.py文件
```
x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'
```

#### 序列化

cPickle是C语言写的,速度快,pickle是纯Python写的
**仅能用于Python**
``` python
try:
    import cPickle as pickle
except ImportError:
    import pickle
```
把对象序列化为一个str
``` python
d = dict()
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
```

#### 反序列化
``` python
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
```

#### JSON
``` python
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d) #dumps返回一个str,内容是标准JSON
```
#### 反序列化
```
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{u'age': 20, u'score': 88, u'name': u'Bob'}
```
dumps,loads 针对字符串, dump load 针对file-like Object
反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。


#### 多进程
`multiprocessing`


#### 进程池(Pool)
``` python
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time() #起始时间
    time.sleep(random.random() * 3) #延时
    end = time.time() #停止时间
    #%0.2f 0->有效数字位数 .2->小数点后保留位数
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    print 'Parent process %s' % os.getpid()
    #Pool默认大小CPU的核数
    #p = Pool(5) 可修改
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocess done...'
    p.close()
    #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()
    print 'All subprocesses done.'
```

#### 进程间通信
以Queue为例，父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据

``` python
from multiprocessing import Process, Queue
import os, time, random
```

#### 写数据进程执行的代码:
``` python
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())
```

# 读数据进程执行的代码
``` python
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__ == '__main__':
    # 父进程创建Queue, 并传给各个子进程:
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw, 写入:
    pw.start()
    # 启动子进程pr, 读取:
    pr.start()
    #等待pw结束:
    pw.join()
    #pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```

#### 多线程

Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
`import threading`

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
**Lock**

``` python
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
```

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

#### ThreadLocal
常用于为每个线程绑定一个数据库连接,HTTP请求,用户身份信息等
`import threading`

创建全局ThreadLocal对象:
`local_school = threading.local()`

``` python
def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
```

#### 分布式进程

见`distributed process`


#### 正则表达式


应用 切分字符串

```
>>>re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']
```
#### 分组
用()表示要提取的分组

```
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object at 0x1026fb3e8>
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'
```

#### 编译
如果一个正则表达式要重复使用, 出于效率考虑, 可以预编译
`>>> import re`
编译:
`>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')`
使用：

``` python
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
```

#### collections
Python内建的一个集合模块，提供了许多有用的集合类


#### namedtuple
创建自定义的tuple对象，规定tuple元素的个数，可用属性来引用tuple的某个元素

``` python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2
```

#### deque 双向队列

``` python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
q.popleft()
```

#### defaultdict
使用dict， key不存在， 抛出KeyError， 使用defaultdict, 返回一个默认值

``` python
>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1存在
'abc'
>>> dd['key2'] # key2不存在，返回默认值
'N/A'
```

#### OrderedDict
dict, Key是无序的， OrderedDict保持Key的顺序
OrderedDict的Key按照 插入顺序 排列
可以实现FIFO

``` python
>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

#可以实现FIFO
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)
```

#### Counter
计数器

``` python
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
```

#### base64
用64个字符来表示任意二进制数据的方法

**原理**
准备一个包含64个字符的数组
['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
对二进制数据处理，每3个字节一组， 一共是3x8=24bit， 划分为4组，每组6bit

b1       b2       b3
11111111 11111111 11111111
111111 111111 111111 111111
n1      n2      n3      n4
得到4个数字为索引，查表，得到4个字符，就是编码后的字符串

**特性**
3字节二进制数据编码为4字节的文本，长度增加33%，但编码后的文本数据可以直接在页面显示
**补齐**
当要编码的二进制数据不是3的倍数，出现剩下1个或2个字节。Base64用\x00字节在末尾补足,再在编码的末尾加上1或2个=号,表示补了多少字节,解码时,自动去掉

标准Base64编码后可能出现+和/, 在URL中就不能直接作为参数
#url safe把 + 和 / 换为 - 和 _

**=号**
`=`在URL Cookie中会造成歧义, 很多Base64编码后会去掉=, 但Base64编码长度永远是4的倍数, 所以解码是补足缺少位数即可

``` python
import base64

def b64de(s):
    lack = len(s)%4
    print lack
    s += '=' * lack
    print s
    print base64.b64decode(s)

b64de('YWJjZA')
b64de('YWJjZA=')
b64de('YWJjZA==')
```

#### hashlib
摘要算法

对任意长度的数据data计算出固定长度的摘要digest,目的是为了发现原始数据是否被人篡改过
由于常用的MD5值很容易被计算出来, 所以, 要确保存储的用户口令不是已被计算出来的常用口令的MD5,需要对原始口令加一个复杂字符串来实现,俗称"加盐"

**Ex 根据用户输入注册并登陆验证**

``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    pwd_md5 = get_md5(password + username + 'the-Salt')
    if db[username] == pwd_md5:
        print True
    else:
        print False

username = raw_input('input your name:')
password = raw_input('input your password:')

register(username, password)
login(username, password)
```

#### GUI(图形界面)

**Tkinter**

``` python
from Tkinter import *
import tkMessageBox

class Application(Frame):
    """docstring for Application"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text='Hello', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()
```

#### TCP编程

另见code/socket/

**socket访问新浪首页**

``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

# AF_INET指定使用IPv4协议, AF_INET6->IPv6
# SOCK_STREAM指定使用面向流的TCP协议
# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接 参数是一个tuple
s.connect(('www.sina.com.cn', 80))

# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnetion: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

# 关闭连接:
s.close()

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
```

#### SMTP发送邮件
见/email/

参考https://docs.python.org/2/library/email.mime.html
构造一个邮件对象就是一个Message对象, 如果构造一个MIMEText对象, 就是文本邮件对象, 如果构造一个MIMEImage对象, 就表示一个作为附件的图片, 多个对象组合, 使用MIMEMultipart对象, 而MIMEBase可以表示任何对象. 它们的继承关系如下
```
Message
+- MIMEBase
    +- MIMEMultipart
    +- MIMENonMultipart
        +- MIMEMessage
        +- MIMEText
        +- MIMEImage
```

#### Http
######## chrome F12
`Elements` 显示网页结构
`Network`显示浏览器和服务器的通信
- 选择`Network`
- 第一个小红灯亮
- 输入`www.sina.com.cn`
- `Network`中点击`sina.com`
- 点击右侧的`view source`

> GET / HTTP/1.1
- `GET`读取请求
- `/`URL路径 首页
- `HTTP/1.1`采用HTTP协议 版本是1.1
> Host: www.sina.com.cn
- 请求的域名
- 如果一个服务器有多个网站, 服务器需要通过Host来区分浏览器请求的是哪个网站
########`Response Headers`
- 点击`view source`

> 200 OK
- `200`成功响应
- `OK` 是说明
- `404 Not Found`网页不存在
- `500 Internal Server Error` 服务器内部出错

> Content-Type: text/html
- `Content-Type`响应的内容
- `text/html`HTML网页

######## HTTP响应
- `200`成功
- `3XX`重定向
- `4XX`客户端请求有误
- `5XX`服务器端处理出错

######## HTTP格式
**HTTP GET请求的格式**
> GET /path HTTP/1.1
> Header1: Value1
> Header2: Value2
> Header3: Value3

每个Header一行一个，换行符是`\r\n`

**HTTP响应的格式**
> 200 OK
Header1: Value1
Header2: Value2
Header3: Value3

> body data goes here...

当遇到连续两个`\r\n`时，Header部分结束，后面的数据全部是Body
HTTP响应如果包含body，也是通过`\r\n\r\n`来分隔的

**例子**
socket tcp请求`send('GET / HTTP/1.1\r\nHost:www.sina.com.cn'\r\nConnection:close\r\n\r\n)`
