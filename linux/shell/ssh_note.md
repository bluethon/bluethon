SSH Notes
=========

DEBUG
-----

### ssh too many authentication failures

没有复制pubkey到server, 使用`ssh-copy-id`复制后修复

Usage
-----

### 1. 生成ssh key时指定文件名

`-t` 指定加密类型 默认rsa

    ssh-keygen -t rsa -f ~/.ssh/id_rsa_xxx -C "email"
    ssh-keygen -f ~/.ssh/id_rsa_xxx -C "email"

### 2. 设置config文件

1. 编辑或者创建

    touch ~/.ssh/config

2. 添加

``` bash
Host *.xxx.com
    IdentityFile ~/.ssh/id_rsa_xxx
    User [your username]
```

### 3. 更新ssh-add

``` bash

# add private key
ssh-add ~/.ssh/id_rsa_xxx

# if error:  Permission denied (publickey)
ssh-agent bash

# or
# > <http://www.funtoo.org/Keychain>
sudo apt install keychain
vim ~/.zshrc
# 不需要路径
eval `keychain --eval --agents ssh id_rsa_xxx`

# go on

# if need delete cache
ssh-add -D

# check
ssh-add -l
```

### 4. 复制到剪贴板

``` bash
# 可能需要安装xsel
cat ~/.ssh/id_rsa_xxx.pub | xsel -b
```

### 5. 粘贴到github或者目标服务器

- if remote host

    ~/.ssh/authorized_keys

- if github

> Settings > SSH and GPG keys > New SSH key

### 6. 测试

    ssh -T git@github.com