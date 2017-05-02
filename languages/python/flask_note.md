Flask 笔记
=========

deploy
------

### migrate

``` shell
# 创建迁移仓库, 本身不改动数据
python manage.py db init
python manage.py db migrate -m 'message'
python manage.py db upgrade
python manage.py db downgrade
python manage.py db current
```

note
----

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

