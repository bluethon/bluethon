Package List
============

pip manage tools
----------------

### pipdeptree

查看 已安装 pip包依赖关系

### pip-tools

requirements.txt自动管理工具(包含升级功能)

    pip install pip-tools

    # add package to below file
    vim requirement.in

    # create r.txt
    pip-compile
    # install and uninstall packages
    pip-sync

    # alternative
    pip-compile dev-re.in
    pip-sync dev-re.txt

flask
-----

### flask-debugtoolbar

> <https://github.com/mgood/flask-debugtoolbar>

扩展调试工具(django版本的移植)

json
----

### jsonpickle

> <https://github.com/jsonpickle/jsonpickle>

json格式话工具, json to object
