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

# 查找最近的一条数据库记录
# http://stackoverflow.com/questions/15675672/django-get-the-latest-record-with-filter
obj= Model.objects.filter(testfield=12).order_by('-id')[0]
obj= Model.objects.filter(testfield=12).latest('testfield')

# template for 渲染表单
{% for field in form %}
    {{ field }}
{% endfor %}

# nginx http https
# http://stackoverflow.com/questions/8153875/how-to-deploy-an-https-only-site-with-django-nginx
# django settings.py
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# nginx settings
location / {
    # ... 
    proxy_set_header X-Forwarded-Proto $scheme;
}

# template获取当前url
# http://stackoverflow.com/questions/2882490/how-to-get-the-current-url-within-a-django-template
{{ request.path }}
{{ request.get_full_path }}

# logging
# app.module
# getLogger中为指定的名称或__name__ 动态
logger = logging.getLogger('django')
__name__  # weixin.views

# 实例属性复制 模型继承
new_invoice.__dict__.update(invoice_info.__dict__)


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

1 [Django Signals Example](http://www.koopman.me/2015/01/django-signals-example/)
- [设置model的电话 使用正则Regex 校验](http://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models)
