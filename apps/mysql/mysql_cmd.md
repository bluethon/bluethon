Command Notes
=============

Quick List
----------

``` sql
SELECT DATABASE();                  # 当前数据库
```

Usage
-----

### 创建和更新日期

``` sql
CREATE TABLE foo (
    `creation_time`     DATETIME DEFAULT CURRENT_TIMESTAMP,
    `modification_time` DATETIME ON UPDATE CURRENT_TIMESTAMP
)
```

### shell中登录数据库

``` shell
# mysql -u $user -p$pw $db
# 上面会导致输出`-p $pw`的样子
mysql -u $user -p"$(echo $pw)" $db      # String格式变量
```

### 时间相关内置函数

    DATE('2017-05-23')          # 格式化字符串为日期
    CURDATE()                   # 当前日期
    NOW() - INTERVAL 10 DAY     # 当前时间的10天前

### 格式化日期

    DATE_FORMAT(date, format)
    DATE_FORMAT(NOW(), '%Y年%m月%d日')

### mysqldump

    -d                  # 不导出数据
    -no-data            # 同上

    --compact           # 紧凑结构?

### 查看表结构

    DESCRIBE table;
    SHOW CREATE TABLE table;        # 可以看编码

### 刷新权限

    flush privileges;

### 创建数据库

    create database data_name;
    grant all on foo.* to user@localhost with grant option;

### insert

    insert into table (key1, key2) values ( value1, value2);

### 导出表结构

> [导出数据库结构](http://stackoverflow.com/a/6175506/4757521)
> [仅包含X表或除了X表](https://dba.stackexchange.com/a/9309)

    # -d (--no-data)    不导出数据
    mysqldump -u blue -p123 -d hkgj_test customer_label customer_customerlabel product_label product_productlabel > ~/github/hkgj-api/20170517_labels_schema.sql
