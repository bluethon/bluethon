Flask学习笔记
============

#### Flask上下文全局变量

变量名       |上下文     | 说明
------------|---------|----
current_app |程序上下文 |当前激活程序的实例
g           |程序上下文 |处理请求时用作临时存储对象, 每次请求都会重设
request     |请求上下文 |请求对象, 封装了客户端发出的HTTP请求中的内容
session     |请求上下文 |用户会话, 用户存储请求之间需要"记住"的值的字典

#### 请求调度

实例app的
`app.url_map`显示URL映射

#### 请求钩子

使用修饰器实现

- `before_first_request` 注册一个函数, 在处理第一个请求前运行
- `before_request` 注册一个函数, 在每次请求前运行
- `after_request` 注册一个函数, 如无 未处理 的异常抛出, 在每次请求后运行
- `teardown_request` 注册一个函数, 即使有 未处理 的异常抛出, 也在每次请求后运行

#### 响应

状态码

- 200 请求成功处理
- 302 重定向
- 400 请求无效
- 404 abort

---

## Flask扩展

专为Flask开发的扩展都在flask.ext命名空间下

#### flask-script

为Flask程序添加命令行解释器
> Flask默认的启动设置选项只能在脚本中作为参数传递给app.run()

**安装**

    `pip install flask-script`

**使用**

``` python
from flask.ext.script import Manager
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
```

服务器监听公共网络接口上的连接, 允许同网络的其他计算机访问, 使用http://1.2.3.4:5000/访问, `1.2.3.4`为服务器外网IP地址
> --host 设定监听哪个网络接口上的连接, 默认为localhost

    `python hello.py runserver --host 0.0.0.0`

#### Bootstrap

Twitter开发的一个开源框架, 提供用户界面组件, 且兼容所有现代Web浏览器

**安装**

    `pip install flask-bootstrap`

**使用**

``` python
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)
```

**Flask-Bootstrap基模板中定义的块**

    doc             整个HTML文档
    html_attribs    <html>标签的属性
    html            <html>标签的内容
    head            <head>标签的内容
    title           <title标签的内容
    metas           一组<meta>标签
    styles          层叠样式表定义
    body_attribs    <body>标签的属性
    body            <body>标签的内容
    navbar          用户定义的导航条
    content         用户定义的页面内容
    scripts         文档底部的JavaScript声明

上表很多块都是Flask-Bootstrap自用的, 直接重定义会有问题  
需要使用Jinja2提供的`super()`函数  

**重定义scripts块**

``` html
{% block scripts %}
    {{ super() }}
    <script src="my-script.js"></script>
{% endblock%}
```

---

## 模板

#### 过滤器

**Jinja2变量过滤器**

    safe        渲染值时不转义
    capitalize  把值的首字母转换成大写, 其他字母转换成小写
    lower       把值转换成小写形式
    upper       把值转换成大写形式
    title       把值中每个单词的首字母转换成大写
    trim        把值的首尾空格去掉
    striptags   渲染之前把值中所有的HTML标签都删掉

[完整Jinja2过滤器列表](http://jinja.pocoo.org/docs/templates/#builtin-filters)

#### 宏

类似Python中的函数

``` html
{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}
```

#### 链接

`url_for()` 使用程序URL映射中保存的信息生成URL

``` html
<!-- 使用视图函数做参数, 返回对应路由, 即 / -->
url_for('index') 

<!-- 返回绝对地址, 即http://localhost:5000/ -->
<!-- 用户生成外链 -->
url_for('index', _external=True)

<!-- 生成动态地址 -->
<!-- 返回http://localhost:5000/user/blue -->
url_for('user', name='blue', _external=True)

<!-- 其他参数 -->
<!-- 返回/?page=2 -->
url_for('index', page=2)
```
