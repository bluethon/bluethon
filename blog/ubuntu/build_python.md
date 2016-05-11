手动安装python
=============

``` bash
# 安装编译用包
sudo apt-get install build-essential libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.1-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev

# 下载压缩包
wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz

# 解压
tar -zxvf Python-3.5.1.tgz

cd Python-3.5.1

# 生成Makefile(安装顺序文件)
./configure

# 编译
make

# 把生成的执行文件拷贝到/usr/local/bin 目录下
make install
```

PS: 另可参考 自定义安装位置及软链接

http://www.cnblogs.com/ibgo/p/3905779.html

https://yuzibo.github.io/InstallPython3.html
