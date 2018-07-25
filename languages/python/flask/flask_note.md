Flask 笔记
=========

debug
-----

### TypeError: __init__() takes at most 2 arguments (3 given)

出错位置如果如下

    validator(form, self)

则form中`DataRequired`改为`DataRequired()`

packages
--------

    # https://stackoverflow.com/a/25696535/4757521
    Flask-JsonTools

note
----

### 环境变量方法设置CLI启动参数

    # pattern
    # FLASK + 命令 + 参数
    # FLASK_COMMAND_OPTION
    export FLASK_RUN_PORT=8000

### jinja block minus

block中的加减号是清除空格相关功能

> <http://jinja.pocoo.org/docs/dev/templates/#whitespace-control>

### 查看SQLAlchemy生成的原生SQL查询语句

    str(User.query.all())

### sqlite url 路径设置(sqlalchemy规定)

    # 绝对写法
    # sqlite:/// + /tmp/foo.db
    sqlite:////tmp/foo.db
    # 相对写法 文件所在目录下
    # sqlite:/// + tmp/foo.db
    sqlite:///tmp/foo.db
    sqlite:///./tmp/foo.db
