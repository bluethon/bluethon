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

# params 参数
session.query(User).filter(text('id<:value and name=:name')). \
    params(value=224, name='fred')

# from_statement 直接使用SQL
session.query(User).from_statement(
    text('SELECT * FROM users WHERE name=:name')).params(name='ed')

# stmt.columns 自定义SQL列与ORM字段对应关系
stmt = text('SELECT name, id, fullname, password FROM users WHERE name=:name')
stmt = stmt.columns(User.name, User.id, User.fullname, User.password)
res = session.query(User).from_statement(stmt).params(name='ed').all()
# 不返回Model, 返回单列
res = session.query(User.name).from_statement(stmt).params(name='ed').all()

# func.count() 列统计
from sqlalchemy import func
session.query(func.count(User.name), User.name).group_by(User.name).all()
# count table
session.query(func.count('*')).select_from(User).scalar()
# 如果使用列名, select_from()可省
session.query(func.count(User.id)).scalar()

# ### Using Aliases
from sqlalchemy.orm import aliased

adalias1 = aliased(Address)
adalias2 = aliased(Address)
for username, email1, email2 in \
        session.query(User.name, adalias1.email_address, adalias2.email_address). \
                join(adalias1, User.addresses). \
                join(adalias2, User.addresses). \
                filter(adalias1.email_address == 'jack@google.com'). \
                filter(adalias2.email_address == 'j25@yahoo.com'):
    print(username, email1, email2)
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
