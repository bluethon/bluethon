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

### 上下文

产生请求的上下文

``` python
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
