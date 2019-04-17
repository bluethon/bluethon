Docker Note
===========

Note
----

### edit file in docker

> <https://stackoverflow.com/a/40471749/4757521>

``` sh
cat > file
# 1. type in your content
# 2. leave a newline at end of file
# 3. ctrl-c
cat file
```

### Registry Garbage Collection

    registry garbage-collect /etc/docker/registry/config.yml

### zsh下不能补全exec

> <https://github.com/moby/moby/commit/402caa94d23ea3ad47f814fc1414a93c5c8e7e58>

不能使用`-it`, 需要使用`-i -t`

安装docker(国内版)
----------------

### 阿里云

> <https://yq.aliyun.com/articles/110806>

``` bash
# update: 2018-08-24
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
sudo usermod -aG docker $USER

# old
# step 1: 安装必要的一些系统工具
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
# step 2: 安装GPG证书
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
# Step 3: 写入软件源信息(stable三月一次稳定版, edge每月一次更新版)
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable edge"
# Step 4: 更新并安装 Docker-CE
sudo apt-get -y update
sudo apt-get -y install docker-ce

# 不使用sudo
sudo usermod -aG docker $USER
```

### 清华(已更新)

``` sh
# docker本体
# https://mirror.tuna.tsinghua.edu.cn/help/docker-ce/
curl -fsSL https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce
```

docker hub mirror
-----------------

### official

``` shell
echo -e "{\n  \"registry-mirrors\": [\"https://registry.docker-cn.com\"]\n}" | sudo tee /etc/docker/daemon.json && sudo systemctl restart docker.service
```

### 中科大

``` sh
# https://lug.ustc.edu.cn/wiki/mirrors/help/docker
echo "{\n  \"registry-mirrors\": [\"https://docker.mirrors.ustc.edu.cn\"]\n}" | sudo tee /etc/docker/daemon.json && sudo systemctl restart docker.service
```

docker machine(批量操作工具)
--------------

> <https://github.com/docker/machine/releases>

``` sh
curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine &&
    chmod +x /tmp/docker-machine &&
    sudo cp /tmp/docker-machine /usr/local/bin/docker-machine
```
