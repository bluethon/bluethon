Shell Commands
==============

QuickList
---------

``` shell
man hier                                    # 介绍Linux文档结构
tzselect                                    # 时区选择工具
set -a && . ./<file> && set +a              # 导入文件变量
export $(grep -v '^#' .env | xargs -d '\n') # 导入文件变量(推荐)
while read -r line; do export $line; done < .env
                                            # 导入文件变量
RUN make; exit 0                            # 指定exit code (0=success)
exit 1                                      # fail

### special variables
$USER                                       # 当前用户
$_                                          # last argument of previous command
$0                                          # 当前shell
$SHELL                                      # 默认shell
$RANDOM                                     # 生成随机数(0-32767)

### system
chsh -s `which zsh` <user>                  # change shell
du                                          # 文件夹大小
du -hs .                                    # 查看当前文件夹
du -hs *                                    # 查看所有文件
cat /etc/X11/default-display-manager        # lightDM or gdm3
cat /etc/os-release                         # 发行版信息
cat /etc/alpine-release                     # alpine version 版本
nproc                                       # CPU数量
update-alternatives --config editor         # 更改默认编辑器 editor vim
update-alternatives --config java           # 更改默认java版本
fc-match <font>                             # 按tab可以查看系统有哪些字体
getent group | cut -d: -f1                  # 显示所有组(仅组名)
groups                                      # 查看用户组
groups $USER                                # 查看某用户的用户组
setxkbmap -query | grep model               # 显示键盘布局
uname -a                                    # kernal version
lsb_release -a                              # 发行版信息
lsb_release -cs                             # 版本名称 xenail
ip r                                        # ip信息
ip route
hostname -I                                 # ip, 更推荐
hostnamectl set-hostname rhel7              # 设置主机名(记得同步更改/etc/hosts)
vim /etc/hostname
chvt <num>                                  # change tty
sar                                         # 记录各类系统情况, 可生成日报告
systemctl start sysstat.service             # sar后端进程
id -Gn                                      # 当前用户 groups
exec $SHELL                                 # 刷新Shell
hash -r                                     # 清除shell缓存
sudo iptables-save                          # 查看防火墙(firewall)规则
type -a <cmd>                               # 显示程序的所有位置
which -a <cmd>                              # 显示程序的所有位置

systemd-analyze
                critical-chain              # 系统启动树
                time                        # kernal各部分用时
                blame                       # 按服务耗时逆序排列
systemctl
          list-units --type service         # 显示系统所有自启动服务
          list-unit-files | grep nginx      # 显示nginx服务状态
          enable/disable nginx.service      # 开启/关闭自启动
          daemon-reload                     # 重载配置文件
          restart httpd.service             # 重启(更改文件后, 先重载)
          --state=not-found --all           # 不存在的服务
ulimit
        -n                                  # 文件句柄数
        -a                                  # 所有信息
strace
        -r                                  # 打印相对时间戳(print relative timestamp)
        -o <file>                           # 输出到文件
df
    -T                                      # 文件系统类型
usermod
    -a                                      # append(不加则覆盖原有group)
    -G <group>                              # 加入用户组
    -s $(which <shell>)                     # 更改shell
getent
    passwd [user]                           # 查看所有[指定]用户设置
    group [group]                           # 查看所有[指定]用户组成员



### time
date                                        # 显示当前时间
     +%s                                    # 显示timestamp
     -d @<epoch>                            # 根据timestamp
     +%Y-%m-%d %H:%M:%S %Z                  # 2017-05-25 11:20:45 CST
TZ='America/Los_Angeles' date               # 显示洛杉矶时间
ls -altr --time=atime                       # 显示所有文件, 按读取时间逆序
time <script>                               # 脚本运行时间
timedatectl status                          # 时间, 时区
timedatectl set-timezone Asia/Shanghai      # 设置时区
dpkg-reconfigure tzdata                     # 设置时区(图形界面)
/etc/timezone                               # 当前时区
/etc/localtime                              # 当前时区信息(binary)
/usr/share/zoneinfo                         # 所有时区
export TZ='Asia/Shanghai'                   # alpine 设置时区环境变量
for i in $(seq 1 10); do /usr/bin/time $SHELL -i -c exit; done
                                            # shell time speed

### text
b=${a:12:5}                                 # string slice
cp -rp foo bar                              # 复制 保留权限
cp ./.??* foo                               # 仅复制隐藏文件(zsh可用)
cat -n                                      # 行号
echo 'foo' | tee bar.txt                    # 写入
echo 'foo' | tee -a bar.txt                 # 追加
fc-list                                     # 查看字体及位置
ls -la | vim -                              # 使用vim查看STDIN的内容
read -r -d '\n'                             # 读取, 转义不生效, 读取结束符设为\n(默认)
tee                                         # 支持sudo
tail -f /var/log/auth.log                   # 刷新查看文件末尾
tail -f /proc/<pid>/fd/1                    # 看进程输出(1=stdout, 2=err)
echo -n <str> | base64                      # -n不输出换行
echo -n <str> | base64 -d                   # base64解码

echo
        -n                                  # 不输出换行符
sed
    -n -e 5p <file>                         # 查看第5行
    -n 5,8p <file>                          # 查看5-8行
    -i -- 's/foo/bar' <file>                # 修改内容
    -i -- '/foo/a bar' <file>               # 在foo行后插入bar
    -i -- '/foo/i bar' <file>               # 在foo行前插入bar
    -n -- 's/foo/bar/p' <fiel>              # 只显示更改的内容
                                            # -n 阻止输出所有行
                                            # /p 后缀p为只显示替换匹配到的
        's/\(foo\)/\1bar'                   # group match, =foobar
        's/foo/&bar'                        # add(追加模式), =foobar
        '/[[:alpha:]]*/'                    # regex=\w*
                                            # > https://www.tutorialspoint.com/unix/unix-regular-expressions.htm
less
     -n 1000                                # 末尾1000行
     -N                                     # 显示行号
     +GG                                    # 打开末尾
     +F                                     # 末尾
less <file>                                 # 打开后按`F`, = tail -f
                                            # p n%, 跳到`n%`处
cp
   -p                                       # same as --preserve=mode,ownership,timestamps
   -P                                       # 保留软链接 symbolic links
cut
    -d ' '                                  # 分隔符, 此处为空格
    -f x                                    # 取第x个元素
grep
    -v                                      # 匹配文本中包含`-`
    --                                      # 同上
    -E                                      # 使用正则表达式
grep -E 'http (output filter|script (set|value))' foo.log
                                            # 正则过滤, 允许如下
                                            # http output filter
                                            # http script set
                                            # http script value
tree
    -N                                      # output UTF-8
find
    !                                       # 取反(配合其他条件使用)
    -newermt yyyy-mm-dd                     # 比此时间更新的
    -type d                                 # 类似是文件夹
    -delete                                 # 删除
find . ! -newermt 2013-11-22 ! -type d -delete
                                            # 删除当前文件夹内老于特定时间的非文件夹文件
awk
    '{print $1}' ORS=' '                    # ORS, 输出分隔符, kong


### zip
pigz                                        # 使用多核心
unzip file                                  # 解压缩
gzip < file > file.gz                       # 压缩文件
zip -s 0 ori.zip --out des.zip              # 将分卷压缩ori合并为des
tar
    -z                                      # use gzip
    -x                                      # 解包
    -c                                      # 打包
    -v                                      # verbose
    -f <name>                               # 指定生成name
    -t                                      # 查看内容（=test)
    --exclude <dir>                         # 排除文件夹
tar -zcvf des.tgz source1 source2           # 多文件

# test value
if [ ! -z "$var1" ]                         # variable not empty
if [[ ! -z $var1 ]]
if [ <var> = 'test' ]                       # <var> equal 'test'
[ $foo -eq 0 ] && echo $foo                 # 等于0, 输出

# kill
pidof fcitx | xargs kill                    # 结束程序
lsof -ti :8000 |xargs kill                  # 根据端口占用结束程序

### debug
set -x                                      # 显示参数和命令
    -v                                      # 显示输入
    +x                                      # 关闭调试
#!/bin/bash -xv                             # (同上)
man 2 connect                               # 查看Linux内核connect()方法的帮助

### network
ping -c <num> <IP>                          # ping <num> times
/etc/NetworkManager/system-connections      # 网络连接confX
sudo lsof -Pni :8118                        # 查看端口占用
sudo netstat -ano | grep 8118               # 查看端口
socat TCP-LISTEN:2375,reuseaddr,fork UNIX-CLIENT:/var/run/docker.sock

scp
scp file vps:                               # copy file to vps's home
scp -3 host1: host2:foo/bar                 # host1->local->host2
nc                                          # net connection
    -w 1                                    # wait time out 1s
    -u                                      # use UDP
nc -w 1 -u localhost 8125                   # UDP监听8125端口
rsync
rsync -av source des:/dest/ination          # 远程复制保持权限
netstat
    -t                                      # TCP port
    -u                                      # UDP port
    -l                                      # only listen socket
    -p                                      # show process name
    -n                                      # no DNS
    -a                                      # show all connect port
netstat -tuplen                             # 查看端口
curl
    -O                                      # 输出文件
    -J                                      # 使用远程文件名
    -L                                      # 下载

### locale
agi `check-language-support -l zh-hans`     # 安装简中
/var/lib/locales/supported.d                # 语言包
check-language-support -a                   # 列出所有未安装语言包
agi language-pack-gnome-zh-hans             # 安装简中语言包
locale                                      # 目前系统区域设置
locale -a                                   # 可用的区域
dpkg-reconfigure locales                    # 所有区域(设置是否开启, 更改后默认执行locale-gen)
/etc/locale.gen                             # 上述文件路径
locale-gen                                  # 手动更改.gen后执行
localectl list-locales                      # 显示开启的区域(和locale -a略有不同)
localectl set-locale LANG=en_US.utf8        # 设置区域 语言参数
/etc/default/locale                         # 上述位置

### log
dmesg                                       # 启动日志

### keymap
alt+.                                       # insert last paramter

### other
echo -ne "n\0m\0k" | od -c                  # od -c 显示各种转义字符
echo "deb https://mirrors.tuna.tsinghua.edu.cn/docker/apt/repo ubuntu-xenial main" | tee /etc/apt/sources.list.d/docker.list
stat foo.txt                                # 查看文件详细信息
CWD=$(dirname $(readlink -f $0))            # pwd path 当前文件路径
${PWD##*/}                                  # 当前文件夹名(PWD, Bash内置变量)
pw=$[ pw + 0 ]                              # 文本转数字(数据库拼接密码需数字)
export DEBUG=false                          # 设置环境变量
unset DEBUG                                 # 清除
ln -s prefix_{old,new}_suffix               # 创建只修改括号的链接(new -> old)
find /usr/ -name libproxychains.so.3        # 查找/usr/下 xx.so.3名字的文件
sudo su - <user>                            # 切换用户(无需输入<user>密码)
nmap -sP 192.168.1.0/24                     # ping扫描, 列出响应主机(sudo 可显示MAC)
wget -nv http://foo/ -O -                   # 访问, 输出到stdout
find / -name .DS_Store -print0 | xargs -0 rm
                                            # 删除特定目录下指定文件
sudo mount <ip>:/volume1/foo /path/to/bar   # 挂载网络硬盘
```

Usage
-----

``` shell

### PATH
# 系统服务位置
/etc/systemd/system/multi-user.target.wants
# pdf 默认
~/.config/mimeapps.list

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

### 7z 解压
sudo apt install p7zip
# x 解压 -o 设置解压目录(注意中间没有空格)
7z x foo.7z -onew_folder

### 进程名称 查看进程信息
ps -ef | grep '[f]oobar'
# -a 所有
pgrep -a foobar
pgrep -fl foobar
```
