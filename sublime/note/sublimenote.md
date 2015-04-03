Windows设置sublimeREPL
=====================================
#1.
~/.config/sublime-text-2/Packages/SublimeREPL/config/Python/Main.sublime-menu
"id": "repl_python"中cmd行改为:
"cmd": ["python", "-i", "-u", "$file_basename"],
#2.增加快捷键

修改Sublime 新建和保存文件时的默认格式
======================================
常见的Markdown文件有 .md、.mdown、.markdown 等多种形式，sublime默认是使用 .mdown为后缀，而 octopress new_post时默认是使用 .markdown 为后缀，为了保持简洁统一的风格可以将他们默认设置为 .md 后缀。

###修改保存文件时的默认后缀形式

1.新建一个空白文件，设置 Syntax - Markdown

2.然后 Preference > Setting - more > Syntax Specific - User 会打开 Markdown.sublime-settings，然后将下面的内容保存 （文件名应该是：Packages/User/Markdown.sublime-settings）

    {
      "extensions": [ "md" ]
    }

试验下新建 markdown 文件，保存时的后缀是否为 .md

###设置新建文件的默认格式和语法高亮 （cmd+n）

1.使用 package control 安装 Default File Type
2.新建文件 Packages/User/default_file_type.sublime-settings, 并保存

    {
      "default_new_file_syntax": "Packages/Markdown/Markdown.tmLanguage"
      , "use_current_file_syntax": true
    }

3.重启 Sublime text 2，试验下新建文件，看下右下角指示是否为 Markdown
