## [ubuntu修改屏幕默认亮度](http://blog.csdn.net/hustrains/article/details/8469633)
- 查询亮度
`cat /sys/class/backlight/acpi_video0/max_brightness`
`sudo vim /etc/rc.local`
- 在“exit 0”前面一行添加一行文字
`echo 4 > /sys/class/backlight/acpi_video0/brightness`

## 看版本号
`cat /etc/os-release` 

## 搜索定位
`which xx`

## python pip 库 路径
> /usr/local/lib/python2.7/dist-packages

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
