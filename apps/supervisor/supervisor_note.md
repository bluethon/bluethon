Supervisor Note
===============

``` sh
# 安装
pip install supervisor

# 生成配置文件
echo_supervisord_conf > /etc/supervisord.conf
```

### 修改日志输出位置

``` sh
# /var/log/syslog
stdout_logfile=syslog

stdout_logfile=/home/haibo/subserver.log

```

### 引入自己的任务

``` sh
# /path/to/foo.conf
touch foo.conf
# make soft link
# /etc/supervisor/supervisor.conf tail will include this
ln -s /etc/supervisor/conf.d/foo.conf /path/to/foo.conf
```

### sample

``` sh
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

``` sh
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