Django Note
===========

library
-------

``` python

# 修饰器,关闭csrf exempt-免除
from django.views.decorators.csrf import csrf_exempt

#       正则匹配url     视图函数        别名, 唯一, 模板中使用
# http://foofish.net/blog/55/django-url
url(r'^wx_activity$', wx_activity, name='wx_activity'),

```

---

manual
------

``` python

# init
pip install django

cd dj

# new project
django-admin startproject [mysite]

# mysite/
#     manage.py
#     mysite/
#         __init__.py
#         settings.py
#         urls.py
#         wsgi.py

# create new app
python3 manage.py startapp [app]

# start project for others
python3 manage.py runserver 0.0.0.0:8000

# 创建模型迁移脚本
python3 manage.py makemigrations [app]

# 执行迁移任务
python3 manage.py migrate

# 查看迁移的SQL
python3 manage.py sqlmigrate [app] [0001]

```

reference
---------

[Django Signals Example](http://www.koopman.me/2015/01/django-signals-example/)
