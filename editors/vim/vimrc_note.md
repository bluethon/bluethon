vimrc Note
==========

``` shell

### 缩进
# tab缩进4
set tabstop=4
# tab转换为空格
set expandtab
# > 缩进4空格
set shiftwidth=4

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
