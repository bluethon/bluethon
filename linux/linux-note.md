## 显示桌面
**ctrl+super+d**

## 删除文件夹及内所有
**rm -rf name**

## bash git不能自动补全
修改/etc/bash.bashrc

把下面内容的注释符去掉
>if [ -f /etc/bash_completion ] &&! shopt -oq posix; then

>    . /etc/bash_completion

>fi

然后重启bash

## Ubuntu 获取最快的源
- 备份源列表:

> sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup

- 刷新列表:

> sudo apt-get update

- 安装 apt-spy

> wget http://ftp.us.debian.org/debian/pool/main/a/apt-spy/apt-spy_3.2.2-1_amd64.deb
> dpkg -i apt-spy_3.2.2-1_amd64.deb

- 使用 apt-spy 获取最快的源

> apt-spy -d stable -s CN -t 5
