vimrc Note
==========

One Key for Server
------------------

    curl https://raw.githubusercontent.com/wklken/vim-for-server/master/vimrc > ~/.vimrc

.vimrc
------

``` vimrc
colorscheme molokai                 " 设置主题(k-vim也可)
autocmd FileType yaml set tabstop=2 shiftwidth=2 expandtab ai
                                    " yml缩进
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab
                                    " 另一种yaml设置(缩写)
```

Map
---

> <http://yyq123.blogspot.com/2010/12/vim-map.html>

``` shell

### 屏蔽键

<nop>

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
# http://vim.wikia.com/wiki/Keep_your_cursor_centered_vertically_on_the_screen
set scrolloff=7
set so=7
set so=0        # set default

# syntax 语法高亮
sy on
sy clear

# set 一般性设置
# go gui option 为空
set go=
# 显示normal模式下已输入按键
set showcmd
set noshowcmd

# colo 调色方案
colo evening

# 显示中文 依次使用序列中的编码方式, 最优的在左
set fileencodings=utf-8,gbk,big5
```
