Sentry Note
===========

引用
----

### 服务端安装 python版本

<https://docs.sentry.io/server/installation/python/>

### 客户端配置 django版本

<https://docs.sentry.io/clients/python/integrations/django/>

### sentry 服务端配置, 复杂版, 供参考

<https://tech.liuchao.me/2015/06/monitor-service-error-logs-by-using-sentry/>

### django settings.py 配置(官网也有)

<https://micropyramid.com/blog/using-sentry-to-track-django-live-events/>

### 生成环境使用 server端 各部分 介绍 (供参考)

<http://blog.gaoyuan.xyz/2013/12/18/deploy-sentry-in-product/>

---

安装依赖
-------
``` sh
sudo apt install python-setuptools python-pip python-dev libxslt1-dev gcc libffi-dev libjpeg-dev libxml2-dev libxslt-dev libyaml-dev libpq-dev

sudo pip2 install virtualenv

virtualenv venv

source venv/bin/activate

pip install raven

sentry init <path to the folder>

SENTRY_CONF=. sentry upgrade

SENTRY_CONF=/etc/sentry sentry run web

visiting http://localhost:9000/




```

### Creating Team and Project. 获取dsn

- Click on Create Team button in Dashboard.
- decide a Team Name and save changes
- create a Project.
- In Project DashBoard> Settings >  Client Keys, you can find DSN (reffered in this tutorial as dsn) and DSN (Public) - (Reffered in this tutorial as public-dsn)

