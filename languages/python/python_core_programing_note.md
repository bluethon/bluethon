Python核心编程 

    2.03    P022    文档字符串, 起在线文档功能
    2.05    P024    Python不支持自增, 会解释为+(+n)
    2.13    P030    [enumerate()同时循环索引和元素]


    2.14    P030    列表解析, 将for if等放到list中, 一行实现
    2.20    P036    实用内建函数
    3.5.4   P051    对象被回收的时机
    3.6     P053    使用局部变量替换模块变量加速原理
    3.6     P054    [for循环中print不换行]
    4.4.4   P060    切片操作d
    4.5.2   P062    对象身份比较 is
    4.6     P064    标准内建类型 repr() str() type() 等
    4.6.3   P066    反引号操作符(``), obj == eval(repr(obj))
    4.6.4   P067    type() & isinstance()
    4.6.4   P069    对象身份比较 is
    4.6.4   P070    判断对象类型 isinstance(), 可接受tuple作参数
    4.10    P075    可以用内建函数dir()查看模块内成员
    5.2.2   P078    八进制和十六进制赋值方法
    5.5.3   P083    地板除
    5.5.3   P085    Py3八进制需使用0o前缀
    5.6.3   P093    整型内建函数 chr() hex()等
    5.7.1   P093    布尔 __nonzero__() 真值判断, py3改为__bool__()


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
