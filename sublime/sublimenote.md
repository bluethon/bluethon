#### snippet 自定义代码片段
中文
http://www.bluesdream.com/blog/sublime-text-snippets-function.html
英文
http://docs.sublimetext.info/en/sublime-text-3/extensibility/snippets.html

#### Linux下输入中文
见sublime_imfix/

#### Windows设置sublimeREPL
1.
~/.config/sublime-text-2/Packages/SublimeREPL/config/Python/Main.sublime-menu
"id": "repl_python"中cmd行改为:
"cmd": ["python", "-i", "-u", "$file_basename"],

2. 增加快捷键

#### 修改保存文件时的默认后缀形式

1. 新建一个空白文件，设置 Syntax - Markdown

2. 然后 Preference > Setting - more > Syntax Specific - User 会打开 **Markdown**.sublime-settings，然后将下面的内容保存 （文件名应该是：Packages/User/Markdown.sublime-settings）

    {
      "extensions": [ "md" ]
    }

试验下新建 markdown 文件，保存时的后缀是否为 .md

#### 设置新建文件的默认格式和语法高亮 （`cmd+n`）

1. 使用`package control`安装`Default File Type`

2. 新建文件 `Packages/User/default_file_type.sublime-settings`, 并保存

``` json
    {
      "default_new_file_syntax": "Packages/Markdown/Markdown.tmLanguage"
      , "use_current_file_syntax": true
    }
```

3. 重启 Sublime text 2，试验下新建文件，看下右下角指示是否为 Markdown

#### SublimeGit User设置
``` json
{
    "git_executables": {
        "git": ["D:/Program Files/Git/bin/git.exe"],
        "git_flow": ["D:/Program Files (x86)/Git/bin/git.exe", "flow"],
        "legit": ["legit"]
    }
}
```
