Note
====

Flask
-----

### app

``` python
# app, Flask实例, 接收包或者模块名字作为参数
# flask.helpers.get_root_path 通过参数获得根目录
# 来获得静态文件和模板文件的目录
app = Flask(__name__)


# app.route 会将URL和执行的视图函数的关系保存到 app.url_map 属性上
@app.route('/')


# 服务器启动后, 会调用 werkzeug.serving.run_simple 进入轮询,
# 默认使用单进程单线程的 werkzeug.serving.BaseWSGIServer 处理请求,
# 实际还是使用标准库 BaseHTTPServer.HTTPServer,
# 通过 select.select 做0.5s的 'while True' 的事件轮询
# 其他的werkzeug自带类型还包括 ThreadedWSGIServer 和 ForkingWSGIServer
app.run(host='0.0.0.0', port=9000)


# http://flask.pocoo.org/docs/latest/config/#builtin-configuration-values
# 配置 硬编码
app.config['DEBUG'] = True
# app.config 是flask.config.Config类的实例, 继承自Python的dict,
# 所以可以用 update 方式
app.config.update(
    DEBUG=True,
    SECRET_KEY='...'
)
```

### 配置

``` python
# #1 配置文件
app.config.from_object('settings')  # 通过字符串的模块名字
# 或者引用之后直接传入模块对象
import settings
app.config.from_object(settings)

# #2 文件名字(不限于.py文件?)
# 默认当配置文件不存在时会抛出异常, 使用 silent=True 的时候只是返回False, 但不会抛出异常
app.config.from_pyfile('settings.py', silent=True)

# #3 环境变量(支持silent参数, 获得路径后还是使用from_pyfile)
$ export LOCAL_SETTINGS='settings.py'
app.config.from_envvar('LOCAL_SETTINGS')
```

### 调试模式

``` python
# #1
app.debug = True
app.run()

# #2
app.run(debug=True)
```

设置PIN码

    $ WERKZEUG_DEBUG_PIN=123 python debug.py

### 动态URL规则

指定多种类型

    @app.route('/<any(a, b):page_name>/')

### HTTP方法

    @app.route('/', methods=['GET', 'POST'])

如果存在GET, 那么也会自动添加HEAD, OPTIONS方法

- GET: 获取资源, 幂等
- HEAD: 获取信息, 但只关心消息头, 处理同GET, 但不返回实际内容
- POST: 创建一个新的资源
- PUT: 完整替换资源或者创建资源, 有副作用, 但幂等
- DELETE: 删除资源, 有副作用, 但幂等
- OPTIONS: 获取资源支持的所有HTTP方法
- PATCH: 局部更新, 修改某个已有资源

> 幂等表示在相同的数据和参数下, 执行一次或多次产生的效果是一样的
> [理解HTTP幂等性](https://www.cnblogs.com/weidagang2046/archive/2011/06/04/2063696.html)

### 跳转和重定向(redirect)

- 跳转(301), 多用于旧网站在废弃前转向新网址以保证用户的访问, 有网页被永久移走的概念
- 重定向(302), 页面暂时性的转移, 不建议经常使用

``` python
from flask import redirect
redirect(location)  # 默认302
redirect(location, code=301)    # 指定状态码
```

### 响应(response)

视图函数的返回值会被自动转换为一个响应对象, **部分**逻辑如下:

- 如果返回的是一个字符串, 会用字符串数据和默认参数创建以字符串为主体, 状态码为200, MIME类型是`text/html的`werkzeug.wrappers.Response`响应对象
- 可以直接指定状态字符串('201 CREATED1'), 替代数字的201

``` python
return {'headers': [1, 2, 3]}, 201, [('X-Request-Id', '100')]
return {'headers': [1, 2, 3]}, '201 CREATED1', [('X-Request-Id', '100')]
```

### 静态文件管理(static)

- 推荐使用Ngnix等管理静态文件
- 使用`url_for`生成路径
- 也可以定制静态文件的真实目录

``` python
url_for('static', filename='static')    # "/static/style.css"

# 访问`http://localhost:9000/static/style.css`, 即访问`/tmp/style.css`文件
app = Flask(__name__, static_folder='/tmp')
```

### 即插视图

- 标准视图继承自`flask.views.View`, 必须实现`dispatch_request`(app_view.py)
- 调度方法视图(API), 可使用`MethodView`的`decorators`属性添加装饰器, 做登录验证等
