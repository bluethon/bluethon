Supervisor Note
===============

### 配置文件command字段使用变量

在config中加入此section, 未在3.2中测试

    [supervisord]
    environment = PATH="/foo/bar:%(ENV_PATH)s"

`%(ENV_XXX)s`在`command`中使用需要version >= 3.2

### 生成配置文件

``` shell
#!/bin/bash
# 安装
pip install supervisor

# 生成配置文件
echo_supervisord_conf > /etc/supervisord.conf
```

### 修改日志输出位置

``` shell
#!/bin/bash
# /var/log/syslog
stdout_logfile=syslog
stdout_logfile=/home/haibo/subserver.log
```

### 引入自己的任务

``` shell
#!/bin/bash
# /path/to/foo.conf
touch foo.conf
# make soft link
# /etc/supervisor/supervisor.conf tail will include this
sudo ln -sf $(pwd)/supervisor.conf /etc/supervisor/conf.d/foo.conf
```

### sample

``` shell
#!/bin/bash
[program:sentry-web]
directory=/home/haibo/sentry/
environment=SENTRY_CONF="/home/haibo/.sentry"
command=/home/haibo/sentry/bin/sentry run web
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/haibo/sentry.log
stderr_logfile=syslog

[program:sentry-worker]
directory=/home/haibo/sentry/
environment=SENTRY_CONF="/home/haibo/.sentry"
command=/home/haibo/sentry/bin/sentry run worker
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

[program:sentry-cron]
directory=/home/haibo/sentry/
environment=SENTRY_CONF="/home/haibo/.sentry"
command=/home/haibo/sentry/bin/sentry run cron
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

```

``` shell
#!/bin/bash
[program:sentry-web]
directory=/home/haibo/sentry/
environment=SENTRY_CONF="/home/haibo/.sentry"
command=/home/haibo/sentry/bin/sentry run web
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/haibo/sentry.log
stderr_logfile=syslog

[program:sentry-worker]
directory=/home/haibo/sentry/
environment=SENTRY_CONF="/home/haibo/.sentry"
command=/home/haibo/sentry/bin/sentry run worker
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

[program:sentry-cron]
directory=/home/haibo/sentry/
environment=SENTRY_CONF="/home/haibo/.sentry"
command=/home/haibo/sentry/bin/sentry run cron
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog
```
