## hotkey
`ctrl+d`键盘输入结束,用来关闭shell
`ctrl+a`光标移动到命令行开始
`ctrl+e`光标移动到命令行末尾
`ctrl+u`清除光标位置前的所有字符
`ctrl+w`清除左边的字段
`ctrl+k`清除提示符到命令行末尾的字符
`ctrl+y`粘贴u/w/k清除的字符
`ctrl+r`自动在命令历史缓存中增量搜索后面的字符(先按快捷键)
`ctrl+super+d`显示桌面

## shell
`ls-ah`查看隐藏文件

## [ubuntu修改屏幕默认亮度](http://blog.csdn.net/hustrains/article/details/8469633)
- 查询亮度
`cat /sys/class/backlight/acpi_video0/max_brightness`
`sudo vim /etc/rc.local`
- 在“exit 0”前面一行添加一行文字
`echo 4 > /sys/class/backlight/acpi_video0/brightness`

## top
任务管理器

## 看版本号
`cat /etc/os-release` 

## 搜索定位
`which xx`

## python pip 库 路径
> /usr/local/lib/python2.7/dist-packages

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
