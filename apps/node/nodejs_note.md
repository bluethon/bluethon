# Node.js Note

## Install

> <https://github.com/nodesource/distributions/blob/master/README.md>

``` shell
# Using Ubuntu
curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## 更新源

    npm config edit
    # add
    registry = https://registry.npm.taobao.org
    registry = https://npmreg.proxy.ustclug.org
    # or
    npm config set registry https://npmreg.proxy.ustclug.org

## 包

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
