Heroku Note
===========

#### 设定环境变量

    heroku config:set ABC=heroku

#### 添加一个repo到现有app

    heroku git:remote -a appname
    
Error
-----

#### Heroku: Cannot run more than 1 Free size dynos

- `heroku ps`
- `heroku ps:stop <DYNO>`
- <DYNO> like `run.5656`
