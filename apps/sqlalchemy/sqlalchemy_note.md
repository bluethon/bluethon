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
