Shell Commands
==============

QuickList
---------

``` shell
man hier                                    # 介绍Linux文档结构
tzselect                                    # 时区选择工具
echo $0                                     # 当前
echo $SHELL                                 # 默认
exec $SHELL                                 # 刷新Shell
set -a && . ./<file> && set +a              # 导入文件变量
export $(grep -v '^#' .env | xargs -d '\n') # 导入文件变量(推荐)
RUN make; exit 0                            # 指定exit code (0=success)

# system
echo $XDG_SESSION_TYPE                      # 查看桌面 显示服务器 类型
cat /etc/X11/default-display-manager        # lightDM or gdm3
cat /etc/os-release                         # 发行版信息
nproc                                       # CPU数量
sudo update-alternatives --config editor    # 更改默认编辑器 editor vim
sudo update-alternatives --config java      # 更改默认java版本
sudo systemctl list-units --type service    # 显示系统所有自启动服务
sudo systemctl list-unit-files |grep nginx  # 显示nginx服务状态
sudo systemctl enable/disable nginx.service # 开启/关闭自启动
sudo systemctl daemon-reload                # 重载配置文件
sudo systemctl restart httpd.service        # 重启(更改文件后, 先重载)
fc-match <font>                             # 按tab可以查看系统有哪些字体
getent group | cut -d: -f1                  # 显示所有组(仅组名)
groups                                      # 查看用户组
groups $USER                                # 查看某用户的用户组
$USER                                       # 当前用户
setxkbmap -query | grep model               # 显示键盘布局
uname -a                                    # kernal version
lsb_release -a                              # 发行版信息
lsb_release -cs                             # 版本名称 xenail
ip r                                        # ip信息
ip route
hostname -I                                 # ip, 更推荐
sudo hostnamectl set-hostname rhel7         # 设置主机名
sudo vim /etc/hostname
sudo localectl set-locale LANG=en_GB.utf8   # 设置本地化参数
sudo chvt <num>                             # change tty
sudo systemd-analyze critical-chain         # 系统启动树
sar                                         # 记录各类系统情况, 可生成日报告
sudo systemctl start sysstat.service        # sar后端进程

# time
date                                        # 显示当前时间
date +%s                                    # 显示timestamp
date -d @<epoch>                            # 根据timestamp
date +%Y-%m-%d %H:%M:%S %Z                  # 2017-05-25 11:20:45 CST
ls -altr --time=atime                       # 显示所有文件, 按读取时间逆序
time <script>                               # 脚本运行时间
timedatectl status                          # 时间, 时区
sudo timedatectl set-timezone Asia/Shanghai # 设置时区
sudo dpkg-reconfigure tzdata                # 设置时区(图形界面)
/etc/timezone                               # 当前时区
/etc/localtime                              # 当前时区信息(binary)
/usr/share/zoneinfo                         # 所有时区
export TZ='Asia/Shanghai'                   # alpine 设置时区环境变量

# text
fc-list                                     # 查看字体及位置
ls -la | vim -                              # 使用vim查看STDIN的内容
sed -n -e 5p <file>                         # 查看第5行
sed -n 5,8p <file>                          # 查看5-8行
sed -i -- 's/foo/bar' <file>                # 修改内容
sed -i -- '/foo/a bar' <file>               # 在foo行后插入bar
sed -i -- '/foo/i bar' <file>               # 在foo行前插入bar
sed -n -- 's/foo/bar/p' <fiel>              # 只显示更改的内容
                                            # -n 阻止输出所有行
                                            # /p 后缀p为只显示替换匹配到的
sudo tail -f /var/log/auth.log              # 刷新查看文件末尾
tail -f /proc/<pid>/fd/1                    # 看进程输出(1=stdout, 2=err)
     -n 1000                                # 末尾1000行
less <file>                                 # 打开后按`F`, = tail -f
     -N                                     # 显示行号
     +GG                                    # 打开末尾
                                            # p n%, 跳到`n%`处

cp -rp foo bar                              # 复制 保留权限
   -p                                       # same as --preserve=mode,ownership,timestamps
   -P                                       # 保留软链接 symbolic links
cat -n                                      # 行号

# zip
pigz                                        # 使用多核心
zip -s 0 ori.zip --out des.zip              # 将分卷压缩ori合并为des
unzip file                                  # 解压缩
gzip < file > file.gz                       # 压缩文件

# test value
if [ ! -z "$var1" ]                         # variable not empty
if [[ ! -z $var1 ]]
if [ <var> = 'test' ]                       # <var> equal 'test'

# kill
pidof fcitx | xargs kill                    # 结束程序
lsof -ti :8000 |xargs kill                  # 根据端口占用结束程序

# debug
set -x                                      # 显示参数和命令
    -v                                      # 显示输入
    +x                                      # 关闭调试
#!/bin/bash -xv                             # (同上)

# network
socat TCP-LISTEN:2375,reuseaddr,fork UNIX-CLIENT:/var/run/docker.sock

# other
stat foo.txt                                # 查看文件详细信息
echo -ne "n\0m\0k" | od -c                  # od -c 显示各种转义字符
CWD=$(dirname $(readlink -f $0))            # pwd path 当前文件路径
${PWD##*/}                                  # 当前文件夹名(PWD, Bash内置变量)
pw=$[ pw + 0 ]                              # 文本转数字(数据库拼接密码需数字)
export DEBUG=false                          # 设置环境变量
unset DEBUG                                 # 清除
ln -s prefix_{old,new}_suffix               # 创建只修改括号的链接(new -> old)
find /usr/ -name libproxychains.so.3        # 查找/usr/下 xx.so.3名字的文件
echo "deb https://mirrors.tuna.tsinghua.edu.cn/docker/apt/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
sudo su - <user>                            # 切换用户(无需输入<user>密码)
netstat -tuplen                             # 查看22端口
nmap -sP 192.168.1.0/24                     # ping扫描, 列出响应主机
wget -nv http://foo/ -O -                   # 访问, 输出到stdout
```

Usage
-----

``` shell

### PATH
# 系统服务位置
/etc/systemd/system/multi-user.target.wants
# pdf 默认
~/.config/mimeapps.list
# alpine version 版本
cat /etc/alpine-release

## double dash (--), 用来区分参数和正则表达式
# > https://unix.stackexchange.com/a/11382/181922

# 查看进程输出
# > https://unix.stackexchange.com/a/308666/181922

# 替换文件内容
# > https://unix.stackexchange.com/questions/112023/how-can-i-replace-a-string-in-a-files

### 当前文件夹名
# > <https://stackoverflow.com/a/1371283/4757521>
currentdir=${PWD##*/}
echo "${PWD##*/}"

### ssh登录后sudo不输入密码(no password)
sudo visudo
# last of the file, add below
<username>  ALL=(ALL:ALL) NOPASSWD: ALL
# restart
sudo systemctl restart sudo.service

### read
read -r -d '\n'     # 读取, 转义不生效, 读取结束符设为\n(默认)

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
