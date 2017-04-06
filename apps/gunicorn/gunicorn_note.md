Gunicorn Notes
==============


### Usage

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
