uwsgi note
==========

sample
------

``` ini
[uwsgi]
# 地址和端口
socket = /tmp/foo.sock
# TODO: 研究权限, 暂时只能666
chmod-socket = 666
uid = www-data
gid = www-data
# 目录
chdir = /path/to/dir
# 启动文件
wsgi-file = manage.py
# 文件内启动application的变量名
callable = app
processes = 4
threads = 2
# 状态检测地址
stats = localhost:9191
master = true
buffer-size = 32768
```

uwsgi paramter
--------------

    --http localhost:8000           使用http协议, 端口暴露在外
    --http-socket localhost:8000    httpP
    --socket localhost:8000         默认protocol
    --uwsgi-socket localhost:8000   uwsgi protocol
    --wsgi-file foobar.py   使用文件
    --master                主进程, 工作进程挂了重启
    --processes 4           4进程
    --threads 2             2线程
    --stats 127.0.0.1:8001  监控端口, 输出json, 可通过uwsgitop(需安装)查看
    --callable app


辅助
---

### 查看监控输出

    nc localhost 8001

### uwsgitop

    pip install uwsgitop
    uwsgi localhost:8001
