Flask Debug Note
================

### Flask application not registered on Redis instance

> https://stackoverflow.com/a/19438054/4757521

``` python
def create_app():
    app = flask.Flask("app")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.register_blueprint(api)
    db.init_app(app)
    admin_.init_app(app)
    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        admin_.add_view(rediscli.RedisCli(redis))
    return app
```
