pip相关笔记
==========

#### 运维相关

``` bash
# 升级单个包
pip install pip -U

# 生成requirementst.txt
pip freeze > requirements.txt

# 查看需要升级的包
pip list --outdated

# 升级所有包
# http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```





#### pip使用代理安装package
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
