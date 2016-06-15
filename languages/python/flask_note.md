Flask学习笔记
============

## 《Flask Web开发》读书笔记

#### 重点目录(页码使用pdf分页)

    P052    基模板引入moment.js
    P091    blueprint('name', __name__), 第一个为蓝本命名空间名称

---

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
- `Flask-Moment`, 本地化日期和时间

#### flask-script

为Flask程序添加命令行解释器
> Flask默认的启动设置选项只能在脚本中作为参数传递给app.run()

**安装**

    pip install flask-script

**使用**

``` python
from flask.ext.script import Manager, Server
manager = Manager(app)
# 调试模式
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()
```

**参数**

``` bash
# 两种调试模式
python3 hello.py runserver -d
manager.add_command("runserver", Server(use_debugger=True))


# 服务器监听公共网络接口上的连接, 允许同网络的其他计算机访问, 使用http://1.2.3.4:5000/访问, `1.2.3.4`为服务器外网IP地址
# --host 设定监听哪个网络接口上的连接, 默认为localhost
python3 hello.py runserver --host 0.0.0.0

# 多线程
python3 hello.py runserver --threaded
```

#### Bootstrap

Twitter开发的一个开源框架, 提供用户界面组件, 且兼容所有现代Web浏览器

**安装**

    pip install flask-bootstrap

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

#### Flask-Moment

依赖`moment.js`, `jquery.js`  
[全部方法文档](http://momentjs.com/docs/#/displaying/)

**安装**

    pip install flask-moment

**使用**

``` python
from flask.ext.moment import Moment
from datetime import datetime

moment = Moment(app)
# 其假定服务器端程序处理的时间戳是标准datetime的UTC表示
# 标准详见标准库中datetime包的文档
# https://docs.python.org/3/library/datetime.html
current_time = datetime.utcnow()
```

``` html
<!-- 基模板 -->
{% block scripts %}
    {{ super() }}
    {{ moment.include_moment() }}
    <!-- 本地化 -->
    {{ moment.lang('zh-cn') }}
{% endblock scripts %}
```

#### Flask-WTF

Web表单

**安装**

    pip install flask-wtf

**使用**

``` python
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# 设置密匙, 环境变量获取, 设置到app.config中可通用
SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

# 定义表单类
class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

**WTForms支持的HTML标准字段**

    StringField         文本字段
    TextAreaField       多行文本字段
    PasswordField       密码文本字段
    HiddenField         隐藏文本字段
    DateField           文本字段, 值为datetime.date格式
    DateTimeField       文本字段,值为 datetime.datetime 格式
    IntegerField        文本字段,值为整数
    DecimalField        文本字段,值为 decimal.Decimal
    FloatField          文本字段,值为浮点数
    BooleanField        复选框,值为 True 和 False
    RadioField          一组单选框
    SelectField         下拉列表
    SelectMultipleField 下拉列表,可选择多个值
    FileField           文件上传字段
    SubmitField         表单提交按钮
    FormField           把表单作为字段嵌入另一个表单
    FieldList           一组指定类型的字段

**WTForms验证函数**

    Email       验证电子邮件地址
    EqualTo     比较两个字段的值;常用于要求输入两次密码进行确认的情况
    IPAddress   验证 IPv4 网络地址
    Length      验证输入字符串的长度
    NumberRange 验证输入的值在数字范围内
    Optional    无输入值时跳过其他验证函数
    DataRequired    确保字段中有数据
    Regexp      使用正则表达式验证输入值
    URL         验证 URL
    AnyOf       确保输入值在可选值列表中
    NoneOf      确保输入值不在可选值列表中

#### Flask-Migrate

数据库迁移

**安装**

    pip install flask-migrate

**使用**

``` python
from flask.ext.migrate import Migrate, MigrateCommand

# 为导出数据库迁移命令, 使用MigrateCommand类作为 db 命令的 (附加)参数
migrate = Migrate(app=app, db=db, directory='migrations')
manager.add_command('db', MigrateCommand)
```
``` bash
# 使用init子命令创建迁移仓库, 生成migrations文件夹
python3 hello.py db init
# migrate子命令自动创建迁移脚本
python3 hello.py db migrate -m 'initial migration'
# 更新数据库
python3 hello.py db upgrade
```

#### Flask-Mail

数据库迁移

**安装**

    pip install flask-mail

**使用**

``` python
from threading import Thread
from flask.ext.mail import Mail, Message

mail = Mail(app=app)

# 异步程序
def send_async_email(app, msg):
    # mail.send()使用current_app, 此处为另一线程, 需要手动激活context
    with app.app_context():
        mail.send(msg)

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    # template只写名称, 方便分别渲染
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # 直接发
    # mail.send(msg)

    # 异步发
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


# 使用, 收件人在FLASKY_ADMIN中
send_email(app.config['FLASKY_ADMIN'], 'New User',
            'mail/new_user', user=user)
```

``` bash
# 设置环境变量
# Linux, 在.bashrc中, 否则为临时, 重启失效
export MAIL_USERNAME=<you@example.com>
export MAIL_PASSWORD=<password>
# Win
set MAIL_USERNAME=<you@example.com>
# 设置管理员账号
export FLASKY_ADMIN=<admin@example.com>
```

**SMTP服务器配置**

    配置             默认值      说  明
    MAIL_SERVER     localhost   电子邮件服务器的主机名或 IP 地址
    MAIL_PORT       25          电子邮件服务器的端口(TLS=587, SSL=465)
    MAIL_USE_TLS    False       启用传输层安全(Transport Layer Security,TLS)协议
    MAIL_USE_SSL    False       启用安全套接层(Secure Sockets Layer,SSL)协议
    MAIL_USERNAME   None        邮件账户的用户名
    MAIL_PASSWORD   None        邮件账户的密码


#### Flask-Login

**使用**

``` python
# 设置登陆页面的端点
login_manager.login_view = 'auth.login'

```

**LoginManager.session_protection属性**

    None
    basic
    strong      记录客户端IP和浏览器的用户代理信息, 发现异常则登出

**Usermixin类实现的默认方法**

    方法                  说  明
    is_authenticated()  如果用户已经登录,必须返回 True ,否则返回 False
    is_active()         如果允许用户登录,必须返回 True ,否则返回 False 。如果要禁用账户,
                        可以返回 False
    is_anonymous()      对普通用户必须返回 False
    get_id()            必须返回用户的唯一标识符,使用 Unicode 编码字符串

#### forgerypy

自动化创建虚拟信息

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

#### 静态文件

调用`url_for('static', filename='css/style.css', _external=True)`
生成(http://localhost:5000/static/css/style.css)

``` html
{% block head %}
    <!-- 保留基模板的原始内容 -->
    {{ super() }}

    <!-- link:favicon -->
    <link rel="shortcut icon" type="image/x-icon" href="{{ url_for('static', filename = 'favicon.ico') }}">
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename = 'favicon.ico') }}">
{% endblock head %}
```

---

## 数据库(Flask-SQLAlchemy)

#### 数据库URL

    数据库引擎       URL
    MySQL           mysql://username:password@hostname/database
    Postgres        postgres://username:password@hostname/database
    SQLite(Unix)    sqlite:///absolute/path/to/database
    SQLite(Win)     sqlite:///c:/absolute/path/to/database

#### 键

    SQLALCHEMY_DATABASE_URI         数据库URL
    SQLALCHEMY_COMMIT_ON_TEARDOWN   请求结束后自动提交数据库中的变动

#### 常用列类型

    类型名           Python类型              说明
    Integer         int                     普通整数,一般是 32 位
    SmallInteger    int                     取值范围小的整数,一般是 16 位
    BigInteger      int                     或 long 不限制精度的整数
    Float           float                   浮点数
    Numeric         decimal.Decimal         定点数
    String          str                     变长字符串
    Text            str                     变长字符串,对较长或不限长度的字符串做了优化
    Unicode         unicode                 变长 Unicode 字符串
    UnicodeText     unicode                 变长 Unicode 字符串,对较长或不限长度的字符串做了优化
    Boolean         bool                    布尔值
    Date            datetime.date           日期
    Time            datetime.time           时间
    DateTime        datetime.datetime       日期和时间
    Interval        datetime.timedelta      时间间隔
    Enum            str                     一组字符串
    PickleType      任何Python对象            自动使用 Pickle 序列化
    LargeBinary     str                     二进制文件

#### 常用列选项

    选项名           说明
    primary_key     如果设为 True ,这列就是表的主键
    unique          如果设为 True ,这列不允许出现重复的值
    index           如果设为 True ,为这列创建索引,提升查询效率
    nullable        如果设为 True ,这列允许使用空值;如果设为 False ,这列不允许使用空值
    default         为这列定义默认值

#### 常用的SQLAlchemy关系选项

    backref                     在关系的另一个模型中添加反向引用
    primaryjoin                 明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
    lazy                        指定如何加载相关记录。
    uselist                     如果设为 Fales ,不使用列表,而使用标量值
    order_by                    指定关系中记录的排序方式
    secondary                   指定 多对多 关系中关系表的名字
    secondaryjoin SQLAlchemy    无法自行决定时,指定多对多关系中的二级联结条件

> lazy可选值 
- select (首次访问时按需加载)
- immediate (源对象加载后就加载)
- joined (加载记录,但使用联结)
- subquery (立即加载,但使用子查询)
- noload (永不加载)
- dynamic (不加载记录,但提供加载记录的查询)

#### 操作

``` python
db.create_all()                         # 新建数据库
db.drop_all()                           # 删除
admin_role = Role(name='Admin')         # 插入行
db.session.add(admin_role)              # 添加到会话
db.session.add([admin_role, mod_role])  # 一次添加多个
db.session.commit()                     # 提交会话
db.session.rollback()                   # 回滚
admin_role.name = 'Administrator'       # 修改行
db.session.delete(mod_role)             # 删除行

# [表类].query.[过滤器].[执行函数]
Role.query.all()                        # 查询行
User.query.filter_by(role=user_role).all()  # 过滤器
str(User.query.filter_by(role=user_role).all()) # 查看生成的原生SQL, 即转为string
```

#### 常用SQLAlchemy查询过滤器

[完整的列表参见 SQLAlchemy 文档](http://docs.sqlalchemy.org)

    filter()        把过滤器添加到原查询上,返回一个新查询
    filter_by()     把等值过滤器添加到原查询上,返回一个新查询
    limit()         使用指定的值限制原查询返回的结果数量,返回一个新查询
    offset()        偏移原查询返回的结果,返回一个新查询
    order_by()      根据指定条件对原查询结果进行排序,返回一个新查询
    group_by()      根据指定条件对原查询结果进行分组,返回一个新查询

#### 常用SQLAlchemy查询执行函数


    all()           以列表形式返回查询的所有结果
    first()         返回查询的第一个结果,如果没有结果,则返回 None
    first_or_404()  返回查询的第一个结果,如果没有结果,则终止请求,返回 404 错误响应
    get()           返回指定主键对应的行,如果没有对应的行,则返回 None
    get_or_404()    返回指定主键对应的行,如果没找到指定的主键,则终止请求,返回 404 错误响应
    count()         返回查询结果的数量
    paginate()      返回一个 Paginate 对象,它包含指定范围内的结果
    
##### paginate()分页对象属性和方法

    items       当前页面中的记录
    query       分页的源查询
    page        当前页数
    prev_num    上一页的页数
    next_num    下一页的页数
    has_prev    如果有上一页, 返回True
    has_next    如果有下一页, 返回True
    pages       总页数
    per_page    每页显示记录数量
    total       记录总数

    iter_pages          迭代器, 返回在分页导航中显示的页数列表
    (left_edge=2,       最左
    left_current=2,     当前页左
    right_current=5,    当前页右
    right_edge=2)       最右
                        ex: 100页的列表, 当前页50, 页数间隔None, 页面中对应[...]
                        1, 2, None, 48,49, 50, 51, 52, 53, 54, 55, None, 99, 100
    prev()              上一页的分页对象
    next()              下一页的分页对象
