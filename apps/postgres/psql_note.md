PostgreSQL Note
===============

shell版
-------

``` shell

# 创建数据库
createdb [DB_NAME]

# 启动特定数据库
psql [DB_NAME]

# 新建数据库用户并指定为超级用户
sudo -u postgres createuser --superuser dbuser

```

db版
----

``` shell

# 查看数据库
\l

# 查看数据库角色
\du

```
