#### hotkey
`ctrl+d` 键盘输入结束,用来关闭shell
`ctrl+a` 光标移动到命令行开始
`ctrl+e` 光标移动到命令行末尾
`ctrl+u` 清除光标位置前的所有字符
`ctrl+w` 清除左边的字段
`ctrl+k` 清除提示符到命令行末尾的字符
`ctrl+y` 粘贴u/w/k清除的字符
`ctrl+r` 自动在命令历史缓存中增量搜索后面的字符(先按快捷键)
`ctrl+super+d` 显示桌面
`Ctrl+L` 清屏

`shift+PageUp` 向上滚屏
`shift+PageDown` 向下滚屏

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
`diff -B -u -w -I 'author|FileSystemEvent' www/ ../liao/awesome-python3-webapp/www/ >diff.log`

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
>if [ -f /etc/bash_completion ] &&! shopt -oq posix; then

>    . /etc/bash_completion

>fi

然后重启bash

#### Ubuntu 获取最快的源
- 备份源列表:

> sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup

- 刷新列表:

> sudo apt-get update

- 安装 apt-spy

> wget http://ftp.us.debian.org/debian/pool/main/a/apt-spy/apt-spy_3.2.2-1_amd64.deb
> dpkg -i apt-spy_3.2.2-1_amd64.deb

- 使用 apt-spy 获取最快的源

> apt-spy -d stable -s CN -t 5

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
