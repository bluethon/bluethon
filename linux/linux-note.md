Note For Linux
==============

hotkey
------

`ctrl+a` 光标移动到命令行开始
`ctrl+c` 强制终止当前命令
`ctrl+d` 键盘输入结束,用来关闭shell
`ctrl+e` 光标移动到命令行末尾
`ctrl+k` 清除提示符到命令行末尾的字符
`ctrl+l` 清屏
`ctrl+r` 自动在命令历史缓存中增量搜索后面的字符(先按快捷键)
`ctrl+u` 清除光标位置前的所有字符
`ctrl+w` 清除左边的字段
`ctrl+y` 粘贴u/w/k清除的字符
`ctrl+z` 把命令放入后台

`ctrl+super+d` 显示桌面
`shift+PageUp` 向上滚屏
`shift+PageDown` 向下滚屏

Linux Settings
--------------

#### 输入法短语自定义

输入法设置->附加组件->快速输入->设置快捷键(暂定F2)->快速输入列表自定义
[参考](https://fcitx-i m.org/wiki/QuickPhrase/zh-cn)

#### [ubuntu修改屏幕默认亮度](http://blog.csdn.net/hustrains/article/details/8469633)

- 查询亮度
    `cat /sys/class/backlight/acpi_video0/max_brightness`
    `sudo vim /etc/rc.local`
- 在“exit 0”前面一行添加一行文字
    `echo 4 > /sys/class/backlight/acpi_video0/brightness`

#### python pip 库 路径

> /usr/local/lib/python2.7/dist-packages

#### top

任务管理器

#### 看版本号

`cat /etc/os-release`

#### bash git不能自动补全

1. 修改/etc/bash.bashrc
    把下面内容的注释符去掉

    ``` bash
    if [ -f /etc/bash_completion ] &&! shopt -oq posix; then
        . /etc/bash_completion
    fi
    ```

2. 然后重启bash

#### Ubuntu 获取最快的源
- 备份源列表:

    `sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup`

- 刷新列表:

    `sudo apt-get update`

- 安装 apt-spy

    `wget http://ftp.us.debian.org/debian/pool/main/a/apt-spy/apt-spy_3.2.2-1_amd64.deb`
    `dpkg -i apt-spy_3.2.2-1_amd64.deb`

- 使用 apt-spy 获取最快的源

    `apt-spy -d stable -s CN -t 5`

#### home下文件夹中文改为英文

``` shell
export LANG=en_US    #改变支持的语言为英语
xdg-user-dirs-gtk-update   #更新系统语言，按照中文对应的英语进行翻译
export LANG=zh_CN.UTF-8    #重新支持中文
```

