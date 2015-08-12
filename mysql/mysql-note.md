## MySQL笔记

#### 创建数据库
`create batabase data_name`
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

----

## 权限

#### 查看某用户权限
`show grants for 'root'@'localhost'
#### 把指定的权限分配给特定的用户，如果这个用户不存在，则会创建一个用户
`grant 权限 on 数据库名.表名 to 用户名@登陆主机 identified by '密码'`
权限 all/alter/create/drop/select/update/delete
数据库
- *.* 所有库所有表
- test.* test库所有表
- test.table test库table表
登录主机
- '192.168.10.10' 允许登录mysql server的ip
- '%' 所有IP
- 'localhost' 本机

----

## 用户管理

#### 1.新增
`insert into mysql.user(Host,User,Password) values("localhost","lionbule",password("hello1234"));`
#### 2.修改密码
`update mysql.user set password=password('new password') where User="lionbule" and Host="localhost";`
