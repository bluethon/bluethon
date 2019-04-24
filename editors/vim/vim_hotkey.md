Vim Hotkey Note
===============

## 启动参数

    # 可同时打开多个文件
    -o          horizontal split
    -O          vertical split

## hotkey

    # 特殊操作
    :w !sudo tee %                          保存只读文件<http://www.geekyboy.com/archives/629>
    git config --global core.editor vim    使用vim编辑文件
    :h key-notation                         键盘字符说明<Up>

    # vim surround
    # https://github.com/tpope/vim-surround
    ysiw"       增加双引号
    ysiw(       括号(带空格)
    ysiw)       括号(不带空格)
    ysiw<div>   标签
    ysiw>       书名号
    yss         整行

    # mark
    ma          加书签a
    'a          跳转到行
    `a          跳转到位置
    d'a         删除光标到行
    :marks      list
    ''          跳回
    ``          跳回
    :delm a     删除书签

    # 查找
    ggN     定位最后一个查找

    # 替换
    :%s/foo/bar/gc      Change each 'foo' to 'bar', ask for every confirmation first.
    :s/Copyright \zs2007\ze All Rights Reserved/2008/

    # 大小写
    gUiw    大写当前单词
    gUU     大写当前行

    # 删除
    D       d$
    C       c$
    dt<c>   删到c(不包含)    delete until <c>
    df<c>   删到c(包含)     delete find <c>
    di<c>   删除c内(不包含)
    da<c>   删除c内(包含)
    dib     删除圆括号内
    diB     删除花括号内
    :[start_line_no],[end_line_no]d
    d66G    从当前位置删除到66行
    :22,33d 22行删到33行

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
