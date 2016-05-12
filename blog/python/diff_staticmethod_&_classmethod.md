@staticmethod与@classmethod辨析
===============================

#### 相同

为了防止代码扩散到类外, 造成维护困难

#### 不同

`@classmethod`

-   希望方法仅与类而不是实例交互
-   无论实例还是类调用方法, 被修饰函数第一个参数必为类

`@staticmethod`

-   跟类有关系, 但运行时不需要实例和类参与的静态方法
-   如 更改环境变量 或 修改其他类的属性
-   不隐含传入类或实例, 即`self`

参考: [知乎][1], [SO][2]

[1]: https://www.zhihu.com/question/20021164
[2]: http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
