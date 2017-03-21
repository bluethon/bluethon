pip相关笔记
==========

### 运维相关

``` bash
# 升级单个包
pip install -U pip
# Win下有bug, 改用
# http://stackoverflow.com/questions/32126940/windows-10-and-pip-upgrading-access-denied
python -m pip install --upgrade pip

# 生成requirementst.txt
pip freeze > requirements.txt
# 过滤生成(or), 忽略大小写
pip freeze | grep -i -E 'foo|bar'
pip freeze | grep -i 'foo\|bar' # \转义|
# 与现有requirements.txt文件对比
pip freeze -r requirements.txt

# 安装
pip install -r requirements.txt

# 查看需要升级的包
pip list --outdated
pip list -o

# 升级所有包
# http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip
#                                     切片 -d 等号分割符 -f 分割后第一列
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
pip freeze --local | cut -d = -f 1 | xargs pip install -U
# 推荐
pip install pip-review
pip-review --local --interactive
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
