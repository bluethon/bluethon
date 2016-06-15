VIM学习笔记
==========

.vimrc
------

``` shell

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

```

---


替换
---

`%` 全文
`s` 替换a为b
`/gc` 一直替换 需要确认
`:%s/a/b`
`:10,100s/OLD/NEW/g` 10到100行替换

回车: `\r`

被替换部分: `&`

---

宏
--

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
