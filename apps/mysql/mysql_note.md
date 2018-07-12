MySQL笔记
=========

NOTE
----

### increase max_allowed_packet size in mysql docker

    version: "3"
    services:
        data:
            image: "mysql:5.7"
            command: --max_allowed_packet=32505856

### 远程连接数据库

> <http://stackoverflow.com/a/11225588/4757521>

    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password';

    # comment out my.cnf
    # path: `mysql --help` 里面有加载顺序
    # /etc/mysql/my.cnf
    #bind-address = 127.0.0.1

    # restart mysql
    sudo service mysql restart

    # check(sudo 否则看不到)
    sudo netstat -tupan | grep mysql
    sudo lsof -Pni :3306


### error

``` sh
# mysql_config not found
sudo apt-get install libmysqlclient-dev
# command 'x86_64-linux-gnu-gcc' failed with exit
sudo apt-get install python-dev
```

### init

mysql -u root -p < init.sql

``` sql
create database foo;
grant all on foo.* to user@localhost with grant option;
```

### rename database 重命名数据库

> <http://stackoverflow.com/a/1072988/4757521>

``` shell
mysqldump -u username -p -v olddatabase > olddbdump.sql
mysqladmin -u username -p create newdatabase
mysql -u username -p newdatabase < olddbdump.sql
# or
mysqladmin -u username -p create newdatabase
mysqldump -u username -v olddatabase -p | mysql -u username -p -D newdatabase
```

### 查看内置信息

    # 版本
    select version();
    # 日期
    select current_date;
    # 用户
    select user();
    # 数据库
    show databases;
    # 使用数据库(分号不是必须)
    use test
    # 表
    show tables;
    # 开启补全
    \#

#### 重启mysql
`sudo service mysql restart`

#### 查看数据库用户-密码
`SELECT User, Host, Password FROM mysql.user;`
#### 设置密码
`SET PASSWORD FOR 'root'@'host_name' = PASSWORD('newpwd');`

#### 输出到文件
- 带列名
`mysql -u root -p123 test -e "select * from t1 where id <10" > xxx.txt`
- 不带列名
`select * from t1 where id <10 into outfile "D:\\xxx.txt"`

---

操作
---

#### update

    update tables set name='simaopig' where name='xiaoxiaozi'

#### delete

    delete from table where column_name = value

权限
---

> <https://serverfault.com/a/115954/380738>

### 查看某用户权限

    show grants for 'root'@'localhost';

### 撤销权限

    revoke all privileges on *.* from 'user'@'host';

### 创建用户 把指定的权限分配给特定的用户，如果这个用户不存在，则会创建一个用户

    grant 权限 on 数据库名.表名 to 用户名@登陆主机 identified by '密码';

### 刷新权限

    flush privileges;

> 权限

- all/alter/create/drop/select/update/delete

> 数据库

- *.* 所有库所有表
- test.* test库所有表
- test.table test库table表

> 登录主机

- '192.168.10.10' 允许登录mysql server的ip
- '%' 所有IP
- 'localhost' 本机

----

用户管理
-------

#### 1.新增

    insert into mysql.user(Host,User,Password) values("localhost","lionbule",password("hello1234"));
#### 2.修改密码

    update mysql.user set password=password('new password') where User="lionbule" and Host="localhost";


安装
---

### Ubuntu

``` sh
# mysql
sudo apt install mysql-server

# dependencies
sudo apt install python-pip python-dev libmysqlclient-dev
# python
pip install MySQL-python
```

### 补全设置

``` cnf
[mysql]
auto-rehash
```
