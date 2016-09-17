Django Debug Note
=================

migrate error - relation already exists
---------------------------------------

``` shell
python3 manage.py makemigrations [app_name]

# 虚假合并
python3 manage.py migrate [app_name] --fake

# 修改上次的migrations_file, 删掉最新的改动

# 重新生成
python3 manage.py makemigrations [app_name]

# 再次合并
python3 manage.py migrate [app_name]
```
