重装步骤
=======

**ibus不能卸载!!! 与系统深度集成**

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

### Chrome

[sina下载地址](http://down.tech.sina.com.cn/page/43719.html)

### Vim

`wget -qO- https://raw.github.com/ma6174/vim/master/setup.sh | sh`


其他
----

[见此](http://www.cnblogs.com/xionghj/p/4211417.html)
