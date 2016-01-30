## 修复sublime不能输入中文

1. 从论坛讨论的cjacker大神最后的回复扒到原始代码
(https://forum.sublimetext.com/t/input-method-support/5446/31)
2. 此为1中解决方法路径修复版
(http://liberize.me/tech/sublime-text-upgrade-notes.html)

## 使用方法

1. 使用如下命令编译

``` shell
gcc -shared -o libsublime-imfix.so sublime_imfix.c  `pkg-config --libs --cflags gtk+-2.0` -fPIC
```

2. copy`libsublime-imfix.so` to `/opt/sublime_text/`
3. copy `subl` to `/user/bin/` to replace the original one.
4. copy `sublime_text.desktop` to `/usr/share/applications/` replace the original one.
