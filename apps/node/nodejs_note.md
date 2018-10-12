Node.js Note
============

Install
-------

``` shell
# 安装npm node包管理
sudo apt install npm
# node version管理
sudo npm install -g n
# 安装node稳定版
sudo n stable
# 安装最新的npm
sudo npm install -g npm
```

更新源
-----

    npm config edit
    # add
    registry = https://registry.npm.taobao.org
    registry = https://npmreg.proxy.ustclug.org

包
---

### nvm node版本管理

> nvm_note.md

### nrm 源管理器

``` shell
# install
sudo npm install -g nrm
# list
nrm ls
# change
nrm use taobao
# add
nrm add <registry> <url> [home]
# delete
nrm del <registry>
# speed test
nrm test
```
