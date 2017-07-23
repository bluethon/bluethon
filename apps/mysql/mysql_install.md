Mysql Install Note
==================

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
