## MySQL笔记

#### 重启mysql
`sudo service mysql restart`

#### 查看数据库用户-密码
`SELECT User, Host, Password FROM mysql.user;`

#### 设置密码
`SET PASSWORD FOR 'root'@'host_name' = PASSWORD('newpwd');`

#### 创建数据库
`create batabase data_name`

#### 把指定的权限分配给特定的用户，如果这个用户不存在，则会创建一个用户
`grant 权限 on 数据库名.表名 to 用户名@登陆方式 identified by '密码'`

#### 输出到文件
- 带列名
`mysql -u root -p123 test -e "select * from t1 where id <10" > xxx.txt`
- 不带列名
`select * from t1 where id <10 into outfile "D:\\xxx.txt"`
