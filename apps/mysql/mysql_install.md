Mysql Install Note
==================

Init
----

``` sql
CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'%';
FLUSH PRIVILEGES;
```

``` shell
vim /etc/mysql/mysql.conf.d/mysqld.cnf
# comment out
# bind-address 127.0.0.1
sudo service mysql restart
```


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
