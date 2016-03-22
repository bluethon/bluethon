sqlite 笔记
==========

#### Linux下安装

``` bash
sudo apt-get install sqlite3 sqlite3-doc
```

打开或新建数据库

    `sqlite3 test.db`

设置格式化查询结果

    `.mode column;`
    `.header on;`

获取所有表和视图

    `.tables;`
