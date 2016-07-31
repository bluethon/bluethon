Python格式化输出dict等集合对象
====================

官方实现

``` python
import pprint

dic = {}
for i in xrange(201):
    dic[i] = "value for %d" % i

# 自定义缩进为4空格
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dic)
```

> [老高的技术博客](https://blog.phpgao.com/python_print_formatted.html)
