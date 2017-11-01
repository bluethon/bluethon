Index
-----

- [数据库链接配置](http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls)

---

cmd
---

``` python
# text 使用 文本 实现sql
from sqlalchemy import text
session.query(User).filter(text('id<224')).order_by(text('id'))

# params
session.query(User).filter(text('id<:value and name=:name')). \
    params(value=224, name='fred')
```

---

Note
----

### Sequence

仅Oracle定义主键时需要

### length

Column字段长度仅在创建数据库表时才会使用

### `__init__()`

默认使用参数赋值同名Column, 可以自定义, 覆盖默认
