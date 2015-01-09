#配置文件在VIM目录下
_vimrc

#syntax 语法高亮
:sy on
:sy clear

#set 一般性设置
#go gui option 为空
:set go=

#colo 调色方案
:colo evening

#新标签 path为路径
:tabnew path

#% 全文
#s 替换a为b
#/gc 一直替换 需要确认
:%s/a/b

#回车
\r
#被替换部分
&

#移动----------------------
gg  #开头
$   #行尾
^   #行首

#编辑------------------

u   #撤销
Ctrl+r  #恢复
2x  #删除2个字符
dd  #删除行
3dd #3行
dG  #全部
