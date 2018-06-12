重装步骤
=======

**ibus不能卸载!!! 与系统深度集成**

一键脚本
--------

``` sh
#!/bin/bash

#----------
# install
#----------

# 资源监视器
sudo apt-get install indicator-multiload

# 壁纸
sudo add-apt-repository ppa:peterlevi/ppa
sudo apt-get update
sudo apt-get install variety variety-slideshow

# ipython 智能shell
sudo apt install ipython3

# 任务管理器
sudo apt install htop

# theme
sudo add-apt-repository ppa:snwh/pulp
sudo apt-get update
# install icon theme
sudo apt-get install paper-icon-theme
# install cursor theme
sudo apt-get install paper-cursor-theme
# install gtk theme
sudo apt-get install paper-gtk-theme

#-------------------
# uninstall
#-------------------

# amazon ad
sudo apt remove webbrowser-app
```

### Fonts

> [10楼](http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=463088&hilit=fontconfig)
安装及配置文件
链接: https://pan.baidu.com/s/1mi6pqUs 密码: gp9m

> [金步国的blog](http://www.jinbuguo.com/gui/linux_fontconfig.html)


### ohmyzsh

[补全插件](https://github.com/zsh-users/zsh-autosuggestions)

``` shell
sudo dpkg --add-architecture i386
sudo add-apt-repository ppa:wine/wine-builds
sudo apt-get update
sudo apt-get install --install-recommends winehq-devel

git clone https://github.com/hillwoodroc/winetricks-zh.git

cd wintricks-zh
cp winetricks-zh /usr/bin/
# https://github.com/hillwoodroc/winetricks-zh#未安装-winetricks
winetricks-zh qqlight

# 修复输入后是方块
vim ~/.local/share/applications/wine/Programs/腾讯软件/QQ轻聊版/QQ轻聊版.desktop
# 环境变量增加 LC_ALL=zh_CN.utf8
Exec=env LC_ALL=zh_CN.utf8 WINEPREFIX=/home/blue/.local/share/wineprefixes/qqlight wine "C:\Program Files (x86)\Tencent\QQLite\Bin\QQScLauncher.exe"
```

### compiz manager(软件商店)

关闭alt键(Desktop -> Ubuntu Unity Plugin -> General)

其他
----

[见此](http://www.cnblogs.com/xionghj/p/4211417.html)
