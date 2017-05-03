git-webhook notes
=================

Install
-------

> <https://github.com/NetEaseGame/git-webhook>

> 2017-05-03 仅支持py2, py3正在支持中

### pip

    sudo apt install python-dev
    pip install git-webhook

### configuration

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

访问`localhost:18340`, github账号登录
