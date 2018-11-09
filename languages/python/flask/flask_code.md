FLask Code Note
===============

CONFIG
------

### CLI

``` sh
FLASK_RUN_PORT=8000         # 端口
FLASK_SKIP_DOTENV=1         # 即使安装`python-dotenv`也不加载
```

### APP

``` python
DATABASE_URI = 'sqlite://:memory:'
```

CODE
----

### Trace

``` py
track = get_current_traceback(skip=1, show_hidden_frames=True, ignore_system_exceptions=False)
track.log()
```

### Use Flask current_app.logger inside threading or Multiprocess

> <https://stackoverflow.com/a/39477756/4757521>

``` py
# pass app to threading
app = current_app._get_current_object()
```

### 上下文

产生请求的上下文

``` py
with app.test_request_context():
    print(url_for('item', id='1'))

# or
ctx = app.test_request_context()
ctx.push()
# jsonify({})
ctx.pop()
```

### 配置代理

`app.debug`就是`app.config['DEBUG']`

> flask.config.ConfigAttribute

    app.debug -> DEBUG
    app.testing -> TESTING
    app.secret_key - > SECRET_KEY
    app.session_cookie_name -> SESSION_COOKIE_NAME
    app.permanent_session_lifetime -> PERMANENT_SESSION_LIFETIME
    app.use_x_sendfile -> USE_X_SENDFILE
    app.logger_name -> LOGGER_NAME
