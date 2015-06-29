## 配置文件在VIM目录下
`_vimrc`

## 显示中文 依次使用序列中的编码方式, 最优的在左
set fileencodings=utf-8,gbk,big5

## 调整光标位置
zz 屏幕中间
zt 屏幕顶端
zb 屏幕底端
Ctrl+f            往前滚动一整屏
Ctrl+b            往后滚动一整屏
Ctrl+d            往前滚动半屏
Ctrl+u            往后滚动半屏

Ctrl+e            往后滚动一行
Ctrl+y            往前滚动一行

#插入
i   #左插
a   #右插
o   #下插
O   #上插

#剪切
用v选中文本,y复制,d剪切,p粘贴

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

#### 替换
`%` 全文
`s` 替换a为b
`/gc` 一直替换 需要确认
`:%s/a/b`
`:10,100s/OLD/NEW/g` 10到100行替换

#回车
\r
#被替换部分
&

#移动----------------------
gg  #开头
$   #行尾
^   #行首

#单词移动----------------------
W w	#移到下个单词开头
E e	#移到下个单词结尾
B b	#移到上个单词开头

#编辑------------------

yy	#复制一行
p	#粘贴
shift+r	#覆盖
ctrl+p  #自动补全
u   #撤销
Ctrl+r  #恢复
2x  #删除2个字符
dd  #剪切行,可用作删除
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

