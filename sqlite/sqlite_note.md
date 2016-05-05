sqlite 笔记
==========

#### Linux下安装与使用

``` bash

# install
sudo apt-get install sqlite3 sqlite3-doc

# 打开或新建数据库
sqlite3 sample.db

# 设置格式化查询结果
.mode column
.header on
.timer on

# 获取所有表和视图
.tables

# 查询所有表结构
.schema

```
