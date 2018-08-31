Ubuntu apps bash cmd
====================

原生
---

``` bash
# 监控进程网络流量
nethogs

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

``` bash
# 网络
ngrep

# 日志查看工具
ksystemlog

# download
uget                                # 下载(./apps)

# 截图
shutter

# 开机启动小键盘
# 加入开机启动: numlockx on
sudo apt install numlockx

# 图片编辑工具
sudo apt insatll gimp

# Albert - linux版Alfred
wget -qO - "https://download.opensuse.org/repositories/home:manuelschneid3r/xUbuntu_$(lsb_release -rs)/Release.key" | sudo apt-key add -
echo "deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_$(lsb_release -rs)/ /" > /etc/apt/sources.list.d/home:manuelschneid3r.list
sudo apt update
sudo apt install albert
# autostart
# > https://albertlauncher.github.io/docs/faq/#how-can-i-autostart-albert
ln -s /usr/share/applications/albert.desktop ~/.config/autostart/

# 包管理 & 查找
sudo apt install synaptic

# zsh & ohmyzsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# 取色器
sudo apt-get install gpick

# 壁纸
sudo add-apt-repository ppa:peterlevi/ppa
sudo apt-get update
sudo apt-get install variety variety-slideshow

# ssh key管理 自动加入
sudo apt install keychain
vim ~/.zshrc
eval `keychain --eval --agents ssh id_rsa_github_jhb`

# theme
sudo add-apt-repository ppa:snwh/pulp
sudo apt-get update
sudo apt-get install paper-icon-theme
sudo apt-get install paper-cursor-theme
sudo apt-get install paper-gtk-theme

# markdown工具
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
sudo add-apt-repository 'deb http://typora.io linux/'
sudo apt-get update
sudo apt-get install typora
```
