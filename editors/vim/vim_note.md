# VIM学习笔记

## CMD

    :bo[tright] vs filename         右侧打开新文件

## doc site

<http://vim.wikia.com/wiki/Vim_Tips_Wiki>

## cheatsheet

[进阶版](http://michael.peopleofhonoronly.com/vim/)

## DEBUG

### PyUnicode_Check(obj)

    # 删掉git repo, 重新下载
    rm -rf YouCompleteMe

## Tips

### 官方教程

    vimtutor zh_cn

### 默认color(theme)路径(path)

    /usr/share/vim/vim74/colors

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
