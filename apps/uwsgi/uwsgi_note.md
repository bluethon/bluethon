uwsgi note
==========

uwsgi paramter

    --http :9000            监听端口
    --wsgi-file foobar.py   使用文件
    --master                主进程, 工作进程挂了重启
    --processes 4           4进程
    --threads 2             2线程
    --stats 127.0.0.1:8001  监控端口, 输出json, 可通过uwsgitop(需安装)查看


辅助
---

### 查看监控输出

    nc localhost 8001

### uwsgitop

    pip install uwsgitop
    uwsgi localhost:8001
