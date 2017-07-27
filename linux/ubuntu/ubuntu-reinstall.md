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

# 图片编辑工具
sudo apt insatll gimp

#-------------------
# uninstall
#-------------------

sudo apt remove webbrowser-app
```

### Fonts

> [10楼](http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=463088&hilit=fontconfig)
安装及配置文件
链接: https://pan.baidu.com/s/1mi6pqUs 密码: gp9m

> [金步国的blog](http://www.jinbuguo.com/gui/linux_fontconfig.html)


### ohmyzsh

[补全插件](https://github.com/zsh-users/zsh-autosuggestions)

### ss

1. 打开`/etc/rc.local`
- 在`exit 0`前加入要执行的命令
- `nohup /usr/local/bin/sslocal -c /home/blue/shell/shadowsocks.json &> /home/blue/shell/myss.log &`
- 需要`sudo`, 需要写绝对路径

### QQ

- 下载
[下载地址](http://www.ubuntukylin.com/applications/showimg.php?lang=cn&id=23)
- 安装
    - 在wine-qqintl目录下打开终端输入： `sudo dpkg -i fonts-wqy-microhei_0.2.0-beta-2_all.deb ttf-wqy-microhei_0.2.0-beta-2_all.deb wine-qqintl_0.1.3-2_i386.deb`
    - 如果报依赖错误，输入： `sudo apt-get install -f`
    - 自动解决依赖后再执行步骤1

**new**

> <https://www.sstype.com/read/317.html>

- [wine直接安装](https://github.com/hillwoodroc/winetricks-zh)
- [清风博客 一个qq正式版](http://phpcj.org/wineqq/)
- [野狼博客](https://www.sstype.com/read/317.html)
https://ubuntuforums.org/archive/index.php/t-865265.html

sudo add-apt-repository ppa:wine/wine-builds


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

### Chrome

[sina下载地址](http://down.tech.sina.com.cn/page/43719.html)

### Vim

`wget -qO- https://raw.github.com/ma6174/vim/master/setup.sh | sh`


其他
----

[见此](http://www.cnblogs.com/xionghj/p/4211417.html)
