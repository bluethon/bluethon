SSH Notes
=========

CMD
---

``` sh
ssh-copy-id -i ~/.ssh/id_rsa.pub root@localhost
ssh-copy-id -i ~/.ssh/id_rsa.pub <alias>
ssh -G <hostname> | awk '/^hostname / { print $2 }'     # 显示host ip

ssh
    -R                                      # 远程转发模式
    -f                                      # 后台运行
    -N                                      # N, 仅连接, 不打开shell
    -T                                      # T, 不分配TTY
    -S                                      # socket
    -M                                      # Master Mode
    -F                                      # ssh config path
ssh -R :15000:localhost:5000 remote         # 让远程remote:15000转发到本地5000
ssh -R remote:15000:localhost:5000 remote   # 等价

ssh -NMf -S /tmp/a.sock -R :5000:localhost:5000 <server>
                                            # 远端转发, socket控制, master mode
ssh -S /tmp/a.sock -O exit <server>         # 停止端口转发, 避免使用kill process
```

> [教程](http://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html)
> [控制端口转发进程](https://unix.stackexchange.com/a/164656/181922)

DEBUG
-----

### Pseudo-terminal will not be allocated because stdin is not a terminal

> <https://stackoverflow.com/a/7122115/4757521>

    # in Makefile
    ssh -T

### publickey auth fail

出现过`/home/user/.ssh`目录权限不是755的情况

    sudo vim /var/log/auth.log

### ssh too many authentication failures

> <https://serverfault.com/a/580864/380738>
> [example](https://gist.github.com/rubo77/e01ac25450df5521d6fa)

没有复制pubkey到server, 使用`ssh-copy-id`复制后修复

Usage
-----

### -R listen 0.0.0.0

    sudo vim /etc/ssh/sshd.config
    # modify blow to yes
    GatewayPorts yes

### 1. 生成ssh key时指定文件名

`-t` 指定加密类型 默认rsa

    ssh-keygen -t rsa -f ~/.ssh/id_rsa_xxx -C "email"
    ssh-keygen -f ~/.ssh/id_rsa_xxx -C "email"

### 2. 设置config文件

1. 编辑或者创建

    touch ~/.ssh/config

2. 添加

``` sh
Host *
    # local -> server1 -> server2
    # 使用本地pk登录server2
    ForwardAgent yes
    # 仅使用设定的private key, 避免too many auth failure
    IdentitiesOnly yes

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
