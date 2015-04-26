一、mysql服务操作
0、查看数据库版本 sql-> status;
1、net start mysql //启动mysql服务
2、net stop mysql //停止mysql服务　
3、mysql -h主机地址 -u用户名 －p用户密码 //进入mysql数据库
4、quit //退出mysql操作
5、mysqladmin -u用户名 -p旧密码 password 新密码 //更改密码
6、grant select on 数据库.* to 用户名@登录主机 identified by "密码" //增加新用户
exemple:
例2、增加一个用户test2密码为abc,让他只可以在localhost上登录，并可以对数据库mydb进行查询、插入、修改、删除的操作 （localhost指本地主机，即MYSQL数据库所在的那台主机），这样用户即使用知道test2的密码，他也无法从internet上直接访问数据 库，只能通过MYSQL主机上的web页来访问了。
grant select,insert,update,delete on mydb.* to test2@localhost identified by "abc";
如果你不想test2有密码，可以再打一个命令将密码消掉。
grant select,insert,update,delete on mydb.* to test2@localhost identified by "";

二、数据库操作
1、show databases; //列出数据库
2、use database_name //使用database_name数据库
3、create database data_name //创建名为data_name的数据库
4、drop database data_name //删除一个名为data_name的数据库

三、表操作
1、show databases;//列出所有数据库

use 数据库名; //到达某一数据库

show tables //列出所有表
create table tab_name(
id int(10) not null auto_increment primary key,
name varchar(40),
pwd varchar(40)
) charset=gb2312; 创建一个名为tab_name的新表
2、drop table tab_name 删除名为tab_name的数据表
3、describe tab_name //显示名为tab_name的表的数据结构
4、show columns from tab_name //同上
5、delete from tab_name //将表tab_name中的记录清空
6、select * from tab_name //显示表tab_name中的记录
7、mysqldump -uUSER -pPASSWORD --no-data DATABASE TABLE > table.sql //复制表结构

四、修改表结构
1、 ALTER TABLE tab_name ADD PRIMARY KEY (col_name)
说明：更改表得的定义把某个栏位设为主键。
2、ALTER TABLE tab_name DROP PRIMARY KEY (col_name)
说明：把主键的定义删除
3、 alter table tab_name add col_name varchar(20); //在tab_name表中增加一个名为col_name的字段且类型为varchar(20)
4、alter table tab_name drop col_name //在tab_name中将col_name字段删除
5、alter table tab_name modify col_name varchar(40) not null //修改字段属性，注若加上not null则要求原字段下没有数据
SQL Server200下的写法是：Alter Table table_name Alter Column col_name varchar(30) not null;
6、如何修改表名：alter table tab_name rename to new_tab_name
7、如何修改字段名：alter table tab_name change old_col new_col varchar(40); //必须为当前字段指定数据类型等属性，否则不能修改
8、create table new_tab_name like old_tab_name //用一个已存在的表来建新表，但不包含旧表的数据

五、数据的备份与恢复
导入外部数据文本:
1.执行外部的sql脚本
当前数据库上执行:mysql < input.sql
指定数据库上执行:mysql [表名] < input.sql
2.数据传入命令 load data local infile "[文件名]" into table [表名];
备份数据库：(dos下)
mysqldump --opt school>school.bbb
mysqldump -u [user] -p [password] databasename > filename (备份)
mysql -u [user] -p [password] databasename < filename (恢复)

六、卸载
卸载mysql:sudo apt-get remove mysql-server mysql-client
sudo apt-get autoremove
