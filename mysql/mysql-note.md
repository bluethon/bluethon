# MySQL笔记

## 重启mysql
`sudo service mysql restart`

## 查看数据库用户-密码
`SELECT User, Host, Password FROM mysql.user;`

## 设置密码
`SET PASSWORD FOR 'root'@'host_name' = PASSWORD('newpwd');`

## 创建数据库
`create batabase data_name`
