pip相关笔记
==========

DEBUG
-----

### TypeError: '>' not supported between instances of 'Version' and 'SetuptoolsVersion'

重装pip

    pip install pip -I      # ignore == --force

### ModuleNotFoundError: No module named 'pip._internal'

    sudo python3 -m pip install -U pip

pip
---

### cmd

``` bash
pip install
            -U pip                              # 升级单个包
            -i https://pypi.douban.com/simple   # 源
               https://pypi.tuna.tsinghua.edu.cn/simple
            -r requirements.txt
            'ipython>=5,<6'         # 安装 大于5且小于6 的版本
            --user                  # 在用户目录下安装(非虚拟环境)
            -I                      # ignore, force

pip list --outdated                 # 查看需要升级的包
pip list -o

pip install pip-review              # 升级所有包
pip-review --local --interactive

pip freeze | grep -i -E 'foo|bar'   # 过滤生成(or), 忽略大小写

pip completion --zsh              # 自动补全代码, 复制到.zshrc
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
