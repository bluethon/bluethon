#### hotkey
`ctrl+a` 光标移动到命令行开始
`ctrl+c` 强制终止当前命令
`ctrl+d` 键盘输入结束,用来关闭shell
`ctrl+e` 光标移动到命令行末尾
`ctrl+k` 清除提示符到命令行末尾的字符
`ctrl+l` 清屏
`ctrl+r` 自动在命令历史缓存中增量搜索后面的字符(先按快捷键)
`ctrl+u` 清除光标位置前的所有字符
`ctrl+w` 清除左边的字段
`ctrl+y` 粘贴u/w/k清除的字符
`ctrl+z` 把命令放入后台

`ctrl+super+d` 显示桌面
`shift+PageUp` 向上滚屏
`shift+PageDown` 向下滚屏

#### 输入法短语自定义
输入法设置->附加组件->快速输入->设置快捷键(暂定F2)->快速输入列表自定义

参考https://fcitx-i m.org/wiki/QuickPhrase/zh-cn

#### diff
`diff [options] files`
`-B` 忽略空行
`-w` 忽略空格
`-I RE` 匹配正则, 则忽略该行
`-u` 对比 上下文(合并)
`-c` 对比 上下文
`-y` 对比 左右并排
`-q` 只显示是否相同
`-r` 递归比较子目录的文件

**eg**

``` shell
diff -B -u -w -I 'author|FileSystemEvent' www/ ../liao/awesome-python3-webapp/www/ >diff.log
```

#### ls
a all
l long
h human 文件大小带k m
`ll` == `ls -l`

#### `rm` remove
-r recursive 递归 可删除目录
-f force 强制删除 不提示

#### `cp` copy & rename
-a == -pdr 完全复制, 包括创建时间等

#### pwd == print working directory

#### shell
`ls-ah`查看隐藏文件

#### [ubuntu修改屏幕默认亮度](http://blog.csdn.net/hustrains/article/details/8469633)
- 查询亮度
`cat /sys/class/backlight/acpi_video0/max_brightness`
`sudo vim /etc/rc.local`
- 在“exit 0”前面一行添加一行文字
`echo 4 > /sys/class/backlight/acpi_video0/brightness`

#### top
任务管理器

#### 看版本号
`cat /etc/os-release`

#### 搜索定位
`which xx`

#### python pip 库 路径
> /usr/local/lib/python2.7/dist-packages

#### 删除文件夹及内所有
**rm -rf name**

#### bash git不能自动补全
修改/etc/bash.bashrc

把下面内容的注释符去掉
```
>if [ -f /etc/bash_completion ] &&! shopt -oq posix; then

>    . /etc/bash_completion

>fi
```

然后重启bash

#### Ubuntu 获取最快的源
- 备份源列表:

`sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup`

- 刷新列表:

`sudo apt-get update`

- 安装 apt-spy

`wget http://ftp.us.debian.org/debian/pool/main/a/apt-spy/apt-spy_3.2.2-1_amd64.deb`
`dpkg -i apt-spy_3.2.2-1_amd64.deb`

- 使用 apt-spy 获取最快的源

`apt-spy -d stable -s CN -t 5`

#### home下文件夹中文改为英文
```
export LANG=en_US    #改变支持的语言为英语
xdg-user-dirs-gtk-update   #更新系统语言，按照中文对应的英语进行翻译
export LANG=zh_CN.UTF-8    #重新支持中文
```

#### find
完全匹配

`iname`
不区分大小写
find /root -iname install.log

`user`
按照所有者搜索

`nouser`
查找没有所有者的文件
find /root -nouser

`find /var/log/ -mtime +10`
查找10天前修改的文件

-10 10天内修改文件
10  10天当天修改的文件
+10 10天前修改的文件

`find . -size 25k`
`find . -size 25M`
查找文件大小是25KB的文件/25MB

-25k  小于25KB的文件
25k   等于25KB的文件
+25k  大于25KB的文件

`find /etc -size +20k -a -size -50k -exec ls -lh {} \;`
查找/etc/目录下 大于20kb小于50kb 的文件, 并显示详细信息
`-a` and 与
`-o` or  或
`-exec/-ok 命令 {} \;` 对搜索结果执行操作,`{} \;`是固定结尾格式

#### grep

`grep [选项] 字符串 文件名`
在文件中搜索字符 包含匹配
`-i` 忽略大小写
`-v` 排除指定字符串

#### man
在帮助中打`/d`可以查找包含d的帮助文本, 类似VIM
此时按n键向下查找, N向上查找

**帮助级别**
帮助界面左上角括号内数字, 范围1-9, 具体含义可以`man man`查看
`-f` 查看命令拥有的帮助级别, 相当于`whatis`
`man -5 passwd` 可进入5级别的该命令帮助
`whereis 命令` 找到命令相关文件 也可通过文件路径等 获取相关信息
`-k` 模糊查找关键字 等于`apropos`命令

**选项帮助**
`xx --help`
只获取命令的选项帮助(如果是中文系统, 部分帮助可显示中文)

**shell内部命令帮助**
`help xx`
获取shell内部帮助
`whereis xx` 如果存在可执行文件, 就不是shell内部命令

**详细命令帮助**
`info xx`
- enter  进入子帮助页面(带有*号标记)
- u      进组上层页面
- n      进入下一个帮助小节
- p      进入上一个帮助小节
- q      退出


#### 压缩和解压缩

**.zip**
`zip 压缩文件名 源文件` 压缩文件
压缩文件名不强制要写扩展名, 但是为了自己知道是压缩文件, 写上对应后缀
一般linux显示为*红色*

`zip -r 压缩文件名 目录源` 压缩目录

`unzip 压缩文件` 解压缩

**.gz**
`gzip 源文件`
压缩为.gz格式的文件, 源文件消失

`gzip -c 源文件 > 压缩文件`
压缩为.gz格式, 源文件保留
`gzip -c xx > xx.gz`
gzip本身不支持保留, 但是`-c`将压缩后数据输出, 利用`>`重定向到某文件中储存压缩结果

`gzip -r 目录`
压缩目录下所有子文件, 但是不能压缩目录本身

`gzip -d 压缩文件`
解压缩
or
`gunzip 压缩文件`

`gunzip -r 文件夹` 解压文件夹内所有文件

**.bz2**
不能压缩目录

`bzip2 源文件`
压缩为.bz2格式, 不保留源文件
`bzip2 -k 源文件`
压缩后保留源文件

`bzip2 -d 压缩文件`
解压 -k保留压缩文件
or
`bunzip2 压缩文件`

**.tar**
打包命令

`tar -cvf 打包文件名 源文件`
-c: 打包
-v: 显示过程
-f: 指定打包后的文件名

`tar -xvf 打包文件名`
-x: 解打包

`tar -zcvf 压缩包名.tar.gz 源文件`
-z: 压缩为.tar.gz格式
`tar -zxvf 压缩包名.tar.gz`
解压

`tar -jcvf 压缩包名.tar.bz2 源文件`
-z: 压缩为.tar.bz2格式
`tar -jxvf 压缩包名.tar.bz2`
解压

`tar -zcvf /tmp/压缩包名.tar.gz 源文件1 源文件2`
压缩到指定位置, 多个文件空格分割
`tar -jxvf 压缩包名.tar.bz2 -C /tmp/`
制定位置解压 -C位置必须在后面

`tar -ztvf 文件名`
-t: =test 仅查看压缩包


#### 关机和重启

**shutdown**
`shutdown [选项] 时间`
关机, 关机前会保存数据, 安全, 推荐
-c: 取消前一个关机命令
-h: 关机
-r: 重启

其他关机命令, 不推荐
``` shell
halt
poweroff
init0
```

其他重启命令
``` shell
reboot # 较安全, 可用
init 6
```

**init**
系统运行级别, 0-6
详查`cat /etc/inittab`

`runlevel` 查询系统运行级别, 第一个N表示none 即前一个级别为空

#### 挂载
`mount` 查看已挂载的设备
`mount -a` 依据/etcfstab的内容, 自动挂载

`mount [-t 文件系统] [-o 特殊选项] 设备文件名 挂载点`

挂载光盘
dev下的cdrom为sr0的软链接, `ll`可查看, -t可不写
`mount -t iso9660 /dev/cdrom /mnt/cdrom/`
`mount /dev/sr0 /mnt/cdrom/`

卸载
`umount 设备文件名或者挂载点`

挂载U盘
`fdisk -l` 查看U盘设备文件名
`mount -t vfat /dev/sdb1 /mnt/usb/` vfat已淘汰 sdb1不固定, 由上一步确定


#### 其他

**查看登录用户信息**
`w`
输出:

- USER 登录的用户名
- TTY 登录终端
- FROM 从哪个IP地址登录
- LOGIN@ 登录时间
- IDEL 用户闲置时间
- JCPU 指连接该终端的所有进程占用的时间(不包括过去的后台作业时间, 包括当前正在运行的后台作业占用的时间)
- PCPU 当前进程所占用时间
- WHAT 正在运行的命令

``` shell
 21:48:37 up  3:28,  2 users,  load average: 0.35, 0.62, 0.65
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
blue     :0       :0               18:20   ?xdm?   1:16m  0.87s /sbin/upstart --user
blue     pts/2    :0               21:41    4.00s  0.07s  0.00s w
```
第一行
当前时间 运行时间    共登录2个用户 用户在1, 5, 15分钟内的评价负载

`who`
输出: 用户名 登录终端 登录时间(登录IP)

**查询当前登录和过去登录的用户信息**

`last`
last命令默认读取`/var/log/wtmp`下文件数据, 但数据为二进制, 只能用命令查看, 防篡改
输出: 用户 终端 IP 登录时间 退出时间(在线时间)

`lastlog`
默认读取`/var/log/lastlog`下文件数据, 但数据为二进制, 只能用命令查看, 防篡改
输出: 用户 终端 IP 最后一次登录时间
显示内容内置很多系统不允许的账户, 所以都是从未登录

#### Shell

查询当前linux支持的Shell
`/etc/shells`

查看当前使用的Shell
`echo $SHELL`

**echo**
`echo [选项] [输出内容]`
-e 支持反斜线控制的字符转换

显示颜色
`echo -e "\e[1;31m Hello World \e[0m"`
`\e` 调用颜色
`[1` 开启颜色选项
`\e[0m` 关闭颜色
`31m` 红色, 数字范围30-37 黑-白

**脚本**
新建文件为`xx.sh`

文件头必须为
`#!/bin/Bash`

执行
1. 赋予执行权限, 直接运行(相对路径)

``` bash
chmod 755 hello.sh
./hello.sh
```

2. 通过Bash调用执行脚本
`bash hello.sh`


**别名&快捷键**

查看别名
`alias`

设置别名(重启丢失)
`alias 别名= '原命令'`

别名永久生效, 写入(需重启)
`~/.bashrc`
不重启直接生效, 使用
`source ./bashrc`

删除别名(临时)
`unalias 别名`

**命令生效顺序**
1. 用绝对路径或相对路径执行的命令
2. 别名
3. Bash的内部命令
4. 按照$PATH环境变量定义的目录查找顺序找到的第一个命令

查看$PATH(冒号分割)
`echo $PATH`


**历史命令**
`history [选项] [历史命令保存文件]`
-c 清空历史命令
-w 把缓存中的历史命令写入历史
