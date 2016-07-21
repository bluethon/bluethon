@staticmethod与@classmethod辨析
===============================

#### 相同

为了防止代码扩散到类外, 造成维护困难

#### 不同

`@classmethod`

-   希望方法仅与类而不是实例交互
-   无论实例还是类调用方法, 被修饰函数第一个参数必为类
-   不需要`self`参数, 但第一个参数需要是表示自身类的`cls`(不固定)参数

`@staticmethod`

-   跟类有关系, 但运行时不需要实例和类参与的静态方法
-   如 更改环境变量 或 修改其他类的属性
-   不隐含传入类或实例, 即表示自己的`self`和自身类的`cls`参数

参考: [知乎][1], [SO][2]

[1]: https://www.zhihu.com/question/20021164
[2]: http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
