Sentry Note
===========

> <https://blog.stevem.io/posts/quick-start-installing-sentry-on-ubuntu-14-04>
> <http://dustindavis.me/setting-up-your-own-sentry-server/>

DEBUG
-----

### supervisor worker always starting

``` sh
# if use root, add C_FORCE_ROOT
[program:sentry-worker]
directory=/www/sentry/
environment=SENTRY_CONF="/etc/sentry",C_FORCE_ROOT=true
```

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

# default conf in ~/.sentry
sentry init <path to the folder>

# SENTRY_CONF=<path to the folder> sentry upgrade
sentry upgrade

# create a new user
sentry createuser

# SENTRY_CONF=/etc/sentry sentry run web
sentry run web

visiting http://localhost:9000/




```

### Creating Team and Project. 获取dsn

- Click on Create Team button in Dashboard.
- decide a Team Name and save changes
- create a Project.
- In Project DashBoard> Settings >  Client Keys, you can find DSN (reffered in this tutorial as dsn) and DSN (Public) - (Reffered in this tutorial as public-dsn)




docker - debian
---------------

``` sh
sudo vim /etc/apt/sources.list.d/backports.list

deb http://http.debian.net/debian wheezy-backports main

sudo apt-get update

apt-get purge "lxc-docker*"
apt-get purge "docker.io*"

 $ apt-get update
 $ apt-get install apt-transport-https ca-certificates

 apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

 lsb_release -a

 vim /etc/apt/sources.list.d/docker.list

deb https://apt.dockerproject.org/repo debian-wheezy main

apt-get update

apt-cache policy docker-engine

sudo apt-get install docker-engine

sudo service docker start

sudo docker run hello-world
```
