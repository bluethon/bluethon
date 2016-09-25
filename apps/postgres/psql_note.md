PostgreSQL Note
===============

shell版
-------


``` shell

# 启动管理数据库
sudo -u postgres psql

# 创建数据库
sudo -u postgres createdb [DB_NAME]

# 启动特定数据库
psql [DB_NAME]

# 新建数据库用户并指定为超级用户
sudo -u postgres createuser --superuser [dbuser]

```

db版
----

``` shell

# 查看数据库
\l

# 查看数据库角色
\du

# 删除表
DROP TABLE IF EXISTS backup_tbl;
```
