VIM学习笔记
==========

doc site
--------

<http://vim.wikia.com/wiki/Vim_Tips_Wiki>

hotkey
------

    :e!     重新加载(!从local disk)
    :sp     文件名水平分割窗口
    :vs     文件名垂直分割窗口
    C-w     快速切换窗口
    F3      快速打开或关闭树形目录
    F9      查看当前代码结构及自动补全
    F5      一键运行程序
    F6      代码格式化
    F8      调试C和C++
    F2      去除代码中的空行(个人觉得不实用)

    S+j     拼接两行 join lines
    =       格式化代码(format code)
    C-g     显示文件名
    1C-g    显示文件名(full path)
    1C-g    显示文件名(full path)
    2C-g    显示文件名(full path & buffer)

.vimrc
------

``` shell

# 折行
set textwidth=80
set wrap
set nowrap

# ctrl-u转换当前单词为大写
# 也可选中, U
inoremap <C-u> <esc>gUiwea

# 滚屏时保留的行数
set scrolloff=7
set so=7

# syntax 语法高亮
sy on
sy clear

# set 一般性设置
# go gui option 为空
set go=

# colo 调色方案
colo evening

# 显示中文 依次使用序列中的编码方式, 最优的在左
set fileencodings=utf-8,gbk,big5
```

---

cmd
---

### 获取键盘映射时的internal code

    # insert mode
    <kbd>Ctrl</kbd><kbd>K</kbd>
    # then press any key
    # will output the internal code

### 行排序 去重

> <http://vim.wikia.com/wiki/Sort_lines>

    # style
    :{range}sort u
    # all sort ignore case
    :%sort i
    # all sort reverse
    :%sort!


### 使用系统剪贴板

    sudo apt install vim-gnome

### 乱码

    set encoding=utf8

### 全部自动缩进

    gg=G

### 粘贴不自动缩进(进入粘贴模式)

    set paste
    Shift+Insert

#### 执行shell命令

    # 仅执行
    :![cmd]
    # 输入vim中
    :r ![cmd]

#### 关闭搜索高亮

    nohl

#### 复制

    ggyG    # 全部复制
    yaw     # 复制光标单词

#### 复制提取系统剪贴板

```
# 查看寄存器
:reg

# 复制一行
"+yy

# 全部复制
gg"+yG

# 选中复制
"+y

# 粘贴
"+p

```

---

#### 批量注释

- Ctrl+v
- 方向选择
- 大写I进入插入模式
- 输入完成2次Esc

#### 模式命令

``` shell
vim + abc       # 打开定位最后一行
vim +5 abc      # 定位到第5行, 若超出, 则到最后行
vim +/imooc abc # 定位到imooc第一次出现的地方, n可切换其他匹配
vim aa bb ccc   # 同时打开3个文件, :n->下一个, (:N or :prev)->上一个

# 底行模式

:e              # 重载, !强制
:ls             # 查看打开的文件列表
:15             # 定位到15行
/xxx            # 从光标位置向后搜索
?xxx            # 光标向前
:tabnew path    # 新标签 path为路径

# command_mode 命令模式

Ctrl+f          # 向下翻页 front
Ctrl+b          # 向上翻页 back
Ctrl+d          # 下翻半页 down
Ctrl+u          # 上翻半夜 up
Ctrl+e          # 往后滚动一行
Ctrl+y          # 往前滚动一行

>>              # 缩进
~               # 大小写转换

```

---

替换
---

> <http://vim.wikia.com/wiki/Search_and_replace>

### 替换可使用其他分隔符

You can use other delimiters with substitute:

    :s#http://www.example.com/index.html#http://example.com/#

### 使用`\zs` 和 `\ze` 进行匹配替换

Save typing by using \zs and \ze to set the start and end of a pattern. For example, instead of:

    :s/Copyright 2007 All Rights Reserved/Copyright 2008 All Rights Reserved/
Use:

    :s/Copyright \zs2007\ze All Rights Reserved/2008/

#### 简单替换表达式

    :[range]s/from/to/[flags]

#### range 搜索范围

    none    当前行
    %       全部
    1,$     全部
    1,10    1到10行
    10      第10行

#### flags

    c   confirm     每次替换前询问
    e   error       不显示错误
    g   global      整行替换, 不加只替换每行第一个
    i   ignore      忽略大小写

支持正则, `\(\)`内部分可以在替换中使用`\1`提取, 使用时括号需要转义

`:%s/a/b`
`:10,100s/OLD/NEW/g` 10到100行替换

回车: `\r`

被替换部分: `&`

---

宏
---

#### 录制宏a
qa

#### 使用a 6次
6@a

---

#### 调整光标位置

zz 屏幕中间
zt 屏幕顶端
zb 屏幕底端

#### 剪切
用v选中文本,y复制,d剪切,p粘贴

#### 单词移动
W w #移到下个单词开头
E e #移到下个单词结尾
B b #移到上个单词开头

#### 编辑

yy  #复制一行
p   #粘贴
shift+r #覆盖
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

#### 折叠
zR  #打开全部
zr  #打开当前
zM  #折叠全部
zm  #折叠当前


#### 可视 块

Ctrl+q  # for win
Ctrl+v  # for linux
