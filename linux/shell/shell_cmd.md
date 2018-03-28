Shell Commands
==============

QuickList
---------

``` shell
man hier                                    # 介绍Linux文档结构
tzselect                                    # 时区选择工具

sudo systemctl list-units --type service    # 显示系统所有自启动服务
sudo systemctl list-unit-files |grep nginx  # 显示nginx服务状态
sudo systemctl enable/disable nginx.service # 开启/关闭自启动
fc-match <font>                             # 按tab可以查看系统有哪些字体

echo $0                                     # 当前
echo $SHELL                                 # 默认
exec $SHELL -l                              # 刷新Shell

getent group | cut -d: -f1                  # 显示所有组(仅组名)
groups                                      # 查看用户组
groups $USER                                # 查看某用户的用户组
$USER                                       # 当前用户

uname -a                                    # kernal version
lsb_release -a                              # 发行版信息
lsb_release -cs                             # 版本名称 xenail#

echo $XDG_SESSION_TYPE                      # 查看桌面 显示服务器 类型
cat /etc/X11/default-display-manager        # lightDM or gdm3

CWD=$(dirname $(readlink -f $0))            # pwd path 当前文件路径
currentdir=${PWD##*/}                       # 当前文件夹名

sudo update-alternatives --config editor    # 更改默认编辑器 shell editor vim

date +%Y-%m-%d %H:%M:%S %Z                  # 2017-05-25 11:20:45 CST
pw=$(( pw + 0 ))                            # 文本转数字(数据库拼接密码需数字)
ls -altr --time=atime                       # 显示所有文件, 按读取时间逆序
stat foo.txt                                # 查看文件详细信息
echo -ne "n\0m\0k" | od -c                  # od -c 显示各种转义字符

export DEBUG=false                          # 设置环境变量
unset DEBUG                                 # 清除

pidof fcitx | xargs kill                    # 结束程序
lsof -ti:8000 |xargs kill                   # 根据端口占用结束程序

ln -s prefix_{old,new}_suffix               # 创建只修改括号的链接(new -> old)

find /usr/ -name libproxychains.so.3        # 查找/usr/下 xx.so.3名字的文件
echo "deb https://mirrors.tuna.tsinghua.edu.cn/docker/apt/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
```

Usage
-----

``` shell

### 系统服务位置
/etc/systemd/system/multi-user.target.wants

### 当前文件夹名
# > <https://stackoverflow.com/a/1371283/4757521>
currentdir=${PWD##*/}
echo "${PWD##*/}"

### ssh登录后sudo不输入密码
sudo visudo
# last of the file, add below
<username>  ALL=(ALL:ALL) NOPASSWD: ALL

### read
read -r -d '\n'     # 读取, 转义不生效, 读取结束符设为\n(默认)

### restart shell
exec $SHELL

### 当前文件夹 current directory
CWD=$(dirname $(readlink -f $0))


### 试试查看文件末尾
less +F ...

### 查看service 信息
service --status-all

### tar exclude 打包 排除
tar -cvf name dir1 --exclude dir2

### 查看文件夹大小
du -sh .
du -sh *    #list all files

### copy keep own perrmission 复制 移动 保留权限
# -p     same as --preserve=mode,ownership,timestamps
cp -rp foo bar

### change shell
sudo chsh username -s /bin/zsh

### 7z 解压
sudo apt install p7zip
# x 解压 -o 设置解压目录(注意中间没有空格)
7z x foo.7z -onew_folder

### scp 复制
# 复制文件file到vps主机的用户目录
scp file vps:
# remote to remote
# host1的默认用户目录 to host2的./foo/bar
scp -3 host1: host2:foo/bar

### 进程名称 查看进程信息
ps -ef | grep '[f]oobar'
# -a 所有
pgrep -a foobar
pgrep -fl foobar

### 通过端口 查看端口占用(注意权限, 否则可能会看不到)
sudo lsof -i:8118
sudo lsof -Pni:8118
sudo netstat -ano | grep 8118

### 获取发行版名称 ubuntu release version
# 添加源时使用
lsb_release -cs
echo $(lsb_release -cs) > foo.txt


### I/O写入文件 支持sudo tee
# -a  add 追加
echo 'foo' | tee bar.txt
echo 'foo' | tee -a bar.txt
```
