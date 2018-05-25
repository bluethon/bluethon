Mysql Install Note
==================

Init
----

``` sql
# 创建用户
CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';
# 赋权(未来此命令不可直接创建用户了)
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'%';
FLUSH PRIVILEGES;
```

Settings
--------

    vim /etc/mysql/mysql.conf.d/mysqld.cnf

``` conf
[mysqld]
bind-address 127.0.0.1      # 哪些IP可以访问
max_allowed_packet          # Error 2006(增大可以避免?)
```
    sudo service mysql restart


Driver
------

### 安装MySQL驱动

    pip install mysqlclient

### old

- `mysql-connector-python`是MySQL官方的纯Python驱动
    - `sudo pip install mysql-connector-python --allow-external mysql-connector-python`
- `MySQL-python`封装了MySQL C驱动的Python驱动
    - `sudo apt-get install libmysqld-dev`
    - `sudo pip install MySQL-python`
