Note For Ubuntu
===============

Settings
--------

### 用户config 自动运行 xxx.desktop

    $ ~/.config/autostart/

### 启用fcitx并开机启动

    alt+f2
    im-config
    fcitx

### 自动挂载USB

> <https://help.ubuntu.com/community/Mount/USB>

    $ dconf-editor
    org.gnome.desktop.media-handling.automount-open

### 重装package

    $ sudo apt install --reinstall [package]

### 开机运行

    $ /etc/rc.local

### bash中运行显示加载字体相关

    export FC_DEBUG=1

### [GPG error NO_PUBKEY](http://askubuntu.com/a/15272/537695)

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <PUBKEY>

where `<PUBKEY>` is your missing public key for repository, e.g. `8BAF9A6F`(in error message)


#### 重启X

    sudo /etc/init.d/lightdm restart

#### 升级发行版

    sudo update-manager -d

#### 显示硬件和显卡驱动信息

    lspci
    sudo lshw -C display

---
其他设置
-------

### virtualbox无法调整更大分辨率

管理 | 全局设定 | 显示 | 最大屏幕尺寸 | 空

### wps无法启动

链接中有文件位置, 这次无法启动是路径文件夹没有权限, `chmod 755`后修复bug
<http://www.cnblogs.com/bluestorm/p/3320920.html>

#### 开机进入tty

- `sudo vim /etc/default/grub`
- change line `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"` to
    `GRUB_CMDLINE_LINUX_DEFAULT="text"`
- `sudo update-grub`
- `sudo reboot`

> [stackoverflow](http://askubuntu.com/questions/148717/how-do-i-boot-into-the-console-and-then-launch-the-ubuntu-desktop-from-it)

#### 添加自启动

1. dash | startup | add

2. `cd ~/.config/autostart/` and create `.desktop` file

ref: (http://askubuntu.com/questions/814/how-to-run-scripts-on-start-up)

#### 重启桌面 Xorg

    `ctrl+alt+f1`
    `ps -t tty1`
    `sudo kill 9 PID`  # 结束当前会话
    `sudo service lightdm restart`

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

2. 重启bash

#### 备份源列表:

    `sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup`

#### home下文件夹中文改为英文

``` shell
export LANG=en_US    #改变支持的语言为英语
xdg-user-dirs-gtk-update   #更新系统语言，按照中文对应的英语进行翻译
export LANG=zh_CN.UTF-8    #重新支持中文
```

