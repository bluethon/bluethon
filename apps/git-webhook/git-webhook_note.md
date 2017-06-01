git-webhook notes
=================

Install
-------

> <https://github.com/NetEaseGame/git-webhook>

> 2017-05-03 仅支持py2, py3正在支持中

### pip

    sudo apt install python-dev
    pip install git-webhook

Configuration
-------------

    gitwebhook config

    vim ~/.git-webhook/git_webhook_config.py

``` python
# for sqlite 
DATABASE_URI = 'sqlite:////home/ubuntu/code/git-webhook/git_webhook.db' 
# for mysql 
# DATABASE_URI = 'mysql+pymysql://dev:dev@127.0.0.1/git_webhook' 
 
# 无密码格式
CELERY_BROKER_URL = 'redis://:@127.0.0.1:6379/0' 
# 有密码
CELERY_RESULT_BACKEND = 'redis://:[passwd]@127.0.0.1:6379/0' 
 
SOCKET_MESSAGE_QUEUE = 'redis://:@127.0.0.1:6379/0' 
 
# github生成的oauth信息, 用于当前版本的登录系统
# call back
# http://host:18340/github/callback
GITHUB_CLIENT_ID = 'foo' 
GITHUB_CLIENT_SECRET = 'passwd'
```

### db

    gitwebhook createdb

### run

    # server
    gitwebhook runserver
    # celery async task
    gitwebhook celery

### supervisor

``` shell
[group:git-webhook]
programs=git-hookserver,git-hookcelery
priority = 999

[program:git-hookserver]
directory = /home/ubuntu/code/git-webhook
user=ubuntu
command= /home/ubuntu/.pyenv/versions/2.7.12/envs/git-webhook-2.7.12/bin/gitwebhook runserver
redirect_stderr = true
stdout_logfile = /home/ubuntu/code/git-webhook/webhook-web.log
autostart = true
autorestart = true

[program:git-hookcelery]
directory = /home/ubuntu/code/git-webhook
user=ubuntu
command=/home/ubuntu/.pyenv/versions/2.7.12/envs/git-webhook-2.7.12/bin/gitwebhook celery
# 不设置环境变量 celery找不到
environment = PATH="/home/ubuntu/.pyenv/versions/2.7.12/envs/git-webhook-2.7.12/bin:%(ENV_PATH)s"
redirect_stderr = true
stdout_logfile = /home/ubuntu/code/git-webhook/webhook-celery.log
autostart = true
autorestart = true
```

### 访问`localhost:18340`, github账号登录

### 设置 server信息

    Cname 随便 名字

    cat id_rsa_forwebhook.pub >> authorized_keys

### 设置web hook

    Git Repository      仅仓库名
