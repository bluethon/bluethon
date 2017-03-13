docker note
===========

TODO
----

https://docs.gitlab.com/omnibus/docker/

https://yeasy.gitbooks.io/docker_practice/content/container/daemon.html

https://docs.gitlab.com/omnibus/docker/#after-starting-a-container

https://docs.docker.com/compose/install/

http://wiki.jikexueyuan.com/project/docker/userguide/dockerizing.html

部署
----

> <https://docs.docker.com/compose/install/>



ref
---

[设置代理部分](https://segmentfault.com/a/1190000006146697)
[代理cow](https://github.com/cyfdecyf/cow)

国内版
-----

``` sh
# docker本体
# https://mirror.tuna.tsinghua.edu.cn/help/docker/
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
# 16.04 LTS
echo "deb https://mirrors.tuna.tsinghua.edu.cn/docker/apt/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install docker-engine

# dockerhub镜像
# https://lug.ustc.edu.cn/wiki/mirrors/help/docker
sudo -i
# 编辑或者创建
vim /etc/docker/daemon.json
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}
echo "{\n  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]\n}" | tee /etc/docker/daemon.json
sudo service docker restart
```

Install for ubuntu 16.04[LTS]
-------

> <https://docs.docker.com/engine/installation/linux/ubuntulinux/#/prerequisites>

``` bash
# Update package information, ensure that APT works with the https method, and that CA certificates are installed.
sudo apt-get update
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
