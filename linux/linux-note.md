## 显示桌面
**ctrl+super+d**

## 删除文件夹及内所有
**rm -rf name**

## bash git不能自动补全
修改/etc/bash.bashrc

把下面内容的注释符去掉
>if [ -f /etc/bash_completion ] &&! shopt -oq posix; then

>    . /etc/bash_completion

>fi

然后重启bash
