Alembic Note
============

Cmd
---

    alembic init [folder]           # 初始化
    alembic revision --autogenerate -m 'message'
    alembic upgrade

script
------

``` python
op.execute('UPDATE bills SET bill_createtime = CURRENT_TIMESTAMP WHERE bill_birthday = 0;')
alter_column('表名', '先有的列名', new_column_name='重命名后的列名', existring_type=字段类型)
```


env.py
------

``` python
# ----- custom -----------
import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(abspath(__file__))))  # Insert <.>/src

from lib import SQLALCHEMY_DATABASE_URI
from lib.model_sa import Base, OldBase

config.set_main_option('sqlalchemy.url', SQLALCHEMY_DATABASE_URI)
target_metadata = Base.metadata
target_metadata = [Base.metadata, OldBase.metadata]

context.configure(
    # custom
    compare_type=True,      # 列类型变动
    compare_server_default=True,    # 数据库默认值
)
# ------- custom end --------------
```
