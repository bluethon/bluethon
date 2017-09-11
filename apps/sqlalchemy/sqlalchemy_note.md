SQLAlchemy Note
===============

Cmd
---

``` python
session.query(User.name.label('name_label')).all()
```

``` sql
SELECT users.name AS name_label
FROM users
```

Gist
----

### 设置数据库自动时间

``` python
from sqlalchemy.sql import func

DT = Column(DateTime(timezone=True), default=func.now())
```

Note
----

### deaclare_attr

下面的地方**不能**使用@classmethod, cls最好改为self

否则会导致method失效

``` python
class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
```

### relationship

``` python
# 增加
# > http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#association-object
a = A()
b = B()
a.bs.append(b)
a.bs.extend([b1, b2])

```

### filter dynamic from dict

> <https://stackoverflow.com/a/7605366/4757521>

### object to json

> [最好的]<https://stackoverflow.com/a/37350445/4757521>
> [Hybrid_property]<https://stackoverflow.com/a/30280750/4757521>

> <https://stackoverflow.com/a/10664192/4757521>
> <http://blog.mmast.net/sqlalchemy-serialize-json>
