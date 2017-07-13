Ubuntu apps bash cmd
====================

原生
---
``` bash

# 系统更新
update-manager

# 制作启动盘
usb-creator-gtk

# 清除ppa
sudo apt install ppa-purge
sudo ppa-purge ppa:no1wantdthisname/ppa

# 截图
gnome-screenshot

# 日志查看工具
lnav

# 窗口信息查看(如坐标位置)
xwininfo

```

---

第三方
-----

``` shell
# Albert - linux版Alfred
sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt update; sudo apt install albert

# atom
sudo add-apt-repository ppa:webupd8team/atom
sudo apt update; sudo apt install atom

# 包管理 & 查找
sudo apt install synaptic

# zsh & ohmyzsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# 取色器
sudo apt-get install gpick

# 资源监视器
sudo apt-get install indicator-multiload

# 壁纸
sudo add-apt-repository ppa:peterlevi/ppa
sudo apt-get update
sudo apt-get install variety variety-slideshow

# 鼠标全局手势
sudo apt install easystroke

# ssh key管理 自动加入
sudo apt install keychain
vim ~/.zshrc
eval `keychain --eval --agents ssh id_rsa_github_jhb`
```
