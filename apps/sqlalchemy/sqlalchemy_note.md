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

### filter dynamic from dict

> <https://stackoverflow.com/a/7605366/4757521>

### object to json

> [最好的]<https://stackoverflow.com/a/37350445/4757521>
> [Hybrid_property]<https://stackoverflow.com/a/30280750/4757521>

> <https://stackoverflow.com/a/10664192/4757521>
> <http://blog.mmast.net/sqlalchemy-serialize-json>