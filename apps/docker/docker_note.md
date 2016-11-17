docker note
===========

Install for ubuntu 16.04[LTS]
-------

> <https://docs.docker.com/engine/installation/linux/ubuntulinux/#/prerequisites>

``` bash
# Update package information, ensure that APT works with the https method, and that CA certificates are installed.
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates
# Add the new GPG key.
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

sudo vim /etc/apt/sources.list.d/docker.list
# Ubuntu Xenial 16.04 (LTS)
deb https://apt.dockerproject.org/repo ubuntu-xenial main

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
