PostgreSQL Note
===============

shell版
-------

``` shell

# 创建数据库并授权
sudo -u postgres createdb -O <dbuser> <exampledb>
# 启动管理数据库
sudo -u postgres psql
# 查看现有数据库
sudo -u postgres psql
    \l


# 创建数据库
sudo -u postgres createdb [DB_NAME]
# 删除数据库
dropdb [DB_NAME]
# 启动特定数据库
psql [DB_NAME]
# 新建数据库用户并指定为超级用户
sudo -u postgres createuser --superuser [dbuser]
# 创建普通角色
sudo -u postgres createuser owning_user


# 导入数据库
# 如果数据库不存在, 先创建
createdb -T template0 [DB_NAME]
# 导入
psql [DB_NAME] < infile.db

```
---

备份
---

#!/bin/bash
# 导出
pg_dump [DB_NAME] > outfile.db
# 创建数据库(以template0为模板)
createdb -T template0 [DB_NAME]
# 导入 出错时停止
psql --set ON_ERROR_STOP=on [DB_NAME] < outfile.db

```


---

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

参数
----

-p 端口
