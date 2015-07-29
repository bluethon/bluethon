## Linux下输入中文
`InputHelper`
使用方法：
按 Ctrl + Shift + z，调出输入框，然后就可以输入中文，之后按 Enter 即可。
调出的快捷键 可以在 Default (Linux).sublime-keymap 文件修改，如下，我已经改为 Ctrl+空格 了（因为我Linux下 Ctrl+空格  是切换输入法，所以，想在 Sublime Text 下输入中文，按两下Ctrl+空格 即可）
>[
  // { "keys": ["ctrl+shift+z"], "command": "input_helper" }
  { "keys": ["ctrl+space"], "command": "input_helper" }
]

## Windows设置sublimeREPL
1.
~/.config/sublime-text-2/Packages/SublimeREPL/config/Python/Main.sublime-menu
"id": "repl_python"中cmd行改为:
"cmd": ["python", "-i", "-u", "$file_basename"],

2. 增加快捷键

## 修改保存文件时的默认后缀形式

1. 新建一个空白文件，设置 Syntax - Markdown

2. 然后 Preference > Setting - more > Syntax Specific - User 会打开 **Markdown**.sublime-settings，然后将下面的内容保存 （文件名应该是：Packages/User/Markdown.sublime-settings）

    {
      "extensions": [ "md" ]
    }

试验下新建 markdown 文件，保存时的后缀是否为 .md

## 设置新建文件的默认格式和语法高亮 （`cmd+n`）

1. 使用`package control`安装`Default File Type`

2. 新建文件 `Packages/User/default_file_type.sublime-settings`, 并保存

``` json
    {
      "default_new_file_syntax": "Packages/Markdown/Markdown.tmLanguage"
      , "use_current_file_syntax": true
    }
```

3. 重启 Sublime text 2，试验下新建文件，看下右下角指示是否为 Markdown
