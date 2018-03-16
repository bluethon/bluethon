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

deploy
------

### migrate

``` shell
# old from 2018.3
# new for flask db <cmd>
# 创建迁移仓库, 本身不改动数据
python manage.py db init
python manage.py db migrate -m 'message'
python manage.py db upgrade
python manage.py db downgrade
python manage.py db current
```

note
----

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
