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

ctrl+p  #自动补全
u   #撤销
Ctrl+r  #恢复
2x  #删除2个字符
dd  #删除行
3dd #3行
dG  #全部

g~~ #大小写对换
guu #小写
gUU #大写

#折叠------------------
zR  #打开全部；
zr  #打开当前；
zM  #折叠全部；
zm  #折叠当前

#可视 块
Ctrl+q

#宏----------------------
#录制宏a
qa
#使用a 6次
6@a
