Ubuntu字体美化
=============

[安装及卸载Infinality][0]
-------------

``` bash

# 安装
sudo add-apt-repository ppa:no1wantdthisname/ppa
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install fontconfig-infinality

# 选择linux, 后面会改
sudo bash /etc/fonts/infinality/infctl.sh setstyle

# 编辑
sudo -H gedit /etc/profile.d/infinality-settings.sh

# 对应字段改为如下
USE_STYLE='UBUNTU'

# 卸载详见原文

```

[字体配置][2]
--------

详见原文, 自定义的两个文件在`dotfiles/fonts/`下

最后一行更改为(对应目录下执行)

    sudo ./infctl.sh setstyle

另[此文章][3]也可参考理解


[0]: http://www.webupd8.org/2013/06/better-font-rendering-in-linux-with.html
[2]: http://forum.ubuntu.org.cn/viewtopic.php?f=155&t=369212&start=0
[3]: http://blog.csdn.net/tao_627/article/details/24180781
