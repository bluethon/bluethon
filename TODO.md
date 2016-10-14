未整理笔记
=========

ssh
----

``` sh
# 测试是否有ssh服务
ps -e | grep ssh

# 安装服务端
sudo apt install openssh-server

# 开关服务
sudo service ssh stop
sudo service ssh start

# 连接
ssh <user>@<host>

# 查看22端口
netstat -tuplen

# 进行ping扫描，打印出对扫描做出响应的主机：　
nmap -sP 192.168.1.0/24

# 重启网卡
sudo service network restart
sudo ifconfig eth0 down
sudo ifconfig eth0 up

```

[ubuntu关闭盖子不睡眠](http://askubuntu.com/a/742662/537695)
------------------

``` sh
sudo vim /etc/UPower/UPower.conf
# change to
IgnoreLid=True
# Restart
sudo service upower restart
```

shell
-----

``` sh
# 测试网络
curl baidu.com
```
