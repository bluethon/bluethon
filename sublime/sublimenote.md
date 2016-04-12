Debug
-----

**Troubleshooting**

do this by using the console:

``` js
// 获得设置的当前值
view.settings().get('font_face')
// 操作日志 开启 
sublime.log_commands(True)
```

Settings
--------

#### snippet 自定义代码片段
中文
http://www.bluesdream.com/blog/sublime-text-snippets-function.html
英文
http://docs.sublimetext.info/en/sublime-text-3/extensibility/snippets.html

#### Linux下输入中文

见`sublime_imfix/`

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

#### anacoda 

**venv project设置**

linux环境下可能为`$venv/bin/python` 具体视python执行文件而定
`$venv`为自己创建virtualenv环境目录
linux下测试`$venv`格式无需改动

``` json
{
    "settings":
    [
        {
            "python_interpreter": "$venv/bin/python3"
        }
    ]
}

```
