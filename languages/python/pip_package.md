Package List
============

pip manage tools
----------------

### pipdeptree

查看 已安装 pip包依赖关系

### pip-tools

requirements.txt自动管理工具(包含升级功能)

> <https://github.com/jazzband/pip-tools>

#### install

    pip install pip-tools

#### usage

    # requirements.in
    Flask
    ipython<5                           # 限定版本

    pip-compile                         # create requirements.txt
    pip-compile dev-requirements.in     # create dev-requirements.txt

    pip-compile --upgrade               # 如果已有txt, 必须使用此才能升级
    pip-compile -U                      # upgrade

    pip-sync                            # install package
    pip-sync dev-requirements.txt       # install package

#### ps

分开dev-requirement.in放仅dev需要的包, requirements.in保持不变

    pip-compile dev-requirements.in
    pip-compile requirements.in
    pip-sync dev-requirements.txt requirements.txt

---

flask
-----

### flask-debugtoolbar

> <https://github.com/mgood/flask-debugtoolbar>

扩展调试工具(django版本的移植)

---

json
----

### jsonpickle

> <https://github.com/jsonpickle/jsonpickle>

json格式话工具, json to object
