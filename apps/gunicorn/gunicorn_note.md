Gunicorn Notes
==============

cmd
---

### 使gunicorn支持环境变量配置

``` python
import os

for k,v in os.environ.items():
    if k.startswith("GUNICORN_"):
        key = k.split('_', 1)[1].lower()
        locals()[key] = v
```

    $ export GUNICORN_WORKERS=2
    $ export GUNICORN_BACKLOG=4096
    $ export GUNICORN_BIND=0.0.0.0:8080
    $ gunicorn --config gunicorn.conf myapp:app

> https://sebest.github.io/post/protips-using-gunicorn-inside-a-docker-image/

### log to console

    --log-file=-

R19版本后, 默认不输出到console

Usage
-----

    pip install gunicorn

    # flask
    app = web.application(urls, globals())
    #  在这里加入下面这句，即可
    application = app.wsgifunc()

    # start
    gunicorn main:application

    # option
    # host:port
    -b localhost:8000
    # worker 多进程
    -w 8
