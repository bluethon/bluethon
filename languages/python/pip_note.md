pip相关笔记
==========

pip-tools
---------

> <https://github.com/jazzband/pip-tools>

### install

    pip install pip-tools

### usage

    # requirements.in
    Flask
    ipython<6                           # 限定版本

    pip-compile                         # create requirements.txt
    pip-compile dev-requirements.in     # create dev-requirements.txt

    pip-compile --upgrade               # 如果已有txt, 必须使用此才能升级
    pip-compile -U                      # upgrade

    pip-sync                            # install package
    pip-sync dev-requirements.txt       # install package

### notes

分开dev-requirement.in放仅dev需要的包, requirements.in保持不变

    pip-compile dev-requirements.in
    pip-compile requirements.in
    pip-sync dev-requirements.txt requirements.txt

---------------------

pip
---

### cmd

``` bash
pip install -U pip                  # 升级单个包
pip install -r requirements.txt
pip install 'ipython>=5,<6'         # 安装 大于5且小于6 的版本

pip list --outdated                 # 查看需要升级的包
pip list -o

pip install pip-review              # 升级所有包
pip-review --local --interactive

pip freeze | grep -i -E 'foo|bar'   # 过滤生成(or), 忽略大小写
```

### windows升级package

> <http://stackoverflow.com/questions/32126940/windows-10-and-pip-upgrading-access-denied>

    python -m pip install --upgrade pip

### 生成requirementst.txt

``` shell
pip freeze > requirements.txt
# 过滤生成(or), 忽略大小写
pip freeze | grep -i -E 'foo|bar'
pip freeze | grep -i 'foo\|bar' # \转义|
# 与现有requirements.txt文件对比
pip freeze -r requirements.txt
```

### 升级所有package

``` shell

pip install pip-review              # 升级所有包
pip-review --local --interactive

### alternative
# http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip
#                                     切片 -d 等号分割符 -f 分割后第一列
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
pip freeze --local | cut -d = -f 1 | xargs pip install -U
```

### Windows下非官方包源

[Python Extension Packages for Windows - Christoph Gohlke](http://www.lfd.uci.edu/~gohlke/pythonlibs/)



### pip使用代理安装package
``` shell
# UNIX
export http_proxy=<user>:<password>@<proxy_ip_address>:<port>
export set https_proxy=<user>:<password>@<proxy_ip_address>:<port>

# Windows
c:\> set http_proxy=<user>:<password>@<proxy_ip_address>:<port>
c:\> set https_proxy=<user>:<password>@<proxy_ip_address>:<port>
```

**域下临时设置**
`export set https_proxy=xxxx.com\\user:pwd@<proxy_ip_address>:<port>`
