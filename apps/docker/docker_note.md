docker note
===========

TODO
----

https://yeasy.gitbooks.io/docker_practice/content/container/daemon.html

http://wiki.jikexueyuan.com/project/docker/userguide/dockerizing.html

---------------------------------------------------------


安装docker(国内版)
----------------

### 阿里云

> https://yq.aliyun.com/articles/110806

``` sh
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

### 清华(旧版本)

``` sh
# docker本体
# https://mirror.tuna.tsinghua.edu.cn/help/docker/
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
# 16.04 LTS
echo "deb https://mirrors.tuna.tsinghua.edu.cn/docker/apt/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install docker-engine

dockerhub镜像(中科大)
-------------------

``` sh
# https://lug.ustc.edu.cn/wiki/mirrors/help/docker
echo "{\n  \"registry-mirrors\": [\"https://docker.mirrors.ustc.edu.cn\"]\n}" | sudo tee /etc/docker/daemon.json
sudo service docker restart
```

### docker-compose

``` sh
pyvenv venv
pip install docker-compose
```

docker machine(批量操作工具)
--------------

> https://github.com/docker/machine/releases

``` sh
curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine &&
    chmod +x /tmp/docker-machine &&
    sudo cp /tmp/docker-machine /usr/local/bin/docker-machine
```

docker-completion
-----------------

> https://github.com/leonhartX/docker-machine-zsh-completion

``` sh
git clone https://github.com/leonhartX/docker-machine-zsh-completion.git ~/.oh-my-zsh/custom/plugins/docker-machine

vim .zshrc

### add below
plugins+=(docker-machine)
autoload -U compinit && compinit
```

--------------------------------------------------------

部署使用docker-compose
--------------------

> <https://docs.docker.com/compose/install/>

命令行补全
--------

oh-my-zsh自带

> <https://docs.docker.com/compose/completion/>


代理
---

[设置代理部分](https://segmentfault.com/a/1190000006146697)

Install for ubuntu 16.04[LTS]
-------

> <https://docs.docker.com/engine/installation/linux/ubuntulinux/#/prerequisites>

``` bash
# Install packages to allow apt to use a repository over HTTPS:
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
# Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo vim /etc/apt/sources.list.d/docker.list
# Ubuntu Xenial 16.04 (LTS)
deb https://apt.dockerproject.org/repo ubuntu-xenial main
# set up the stable repository.
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

### INSTALL
sudo apt update
# Purge the old repo if it exists.
sudo apt purge lxc-docker
# Verify that APT is pulling from the right repository.
apt-cache policy docker-engine

# For Ubuntu Trusty, and Xenial, it’s recommended to install the linux-image-extra-* kernel packages. The linux-image-extra-* packages allows you use the aufs storage driver.
sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual

# install
sudo apt-get update
sudo apt-get install docker-engine

# Start the docker daemon.
sudo service docker start
# Verify docker is installed correctly.
sudo docker run hello-world

# Configure Docker to start on boot
sudo systemctl enable docker

# 不使用sudo使用docker
# Create a Docker group
# 显示所有group(不能加sudo)
# groups
sudo groupadd docker
sudo usermod -aG docker $USER
# relogin
docker run hello-world
```
