Pycharm学习笔记
===========

Setting Help
------------

- **关闭**enter智能缩进, 否则导致不产生多行div的中间缩进(但开启python中冒号后才能缩进)

> Editor | General | Smart Keys | Enter | Smart indent

- Project忽略文件类型

> Editor | File Types | Ignore files and folders

- 文件代码最后一行可以移动到顶部

> Editor | GeneralGeneral | Virtual Space | Show virtual space at file bottom

- 设置环境变量

> Build, Execution, Deployment | Console | Python Console | Environment variable

---

中文输入
----

<https://segmentfault.com/q/1010000002641274/a-1020000006061111>

在pycharm.sh中加入下面3个选项：

    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS=@im=fcitx
    
    
openjdk8
--------

详见bluethon/editors/pycharm/pycharm.sh

导入Python live template
----------------------

<http://peter-hoffmann.com/2010/python-live-templates-for-pycharm.html>

配置启动参数
------

1. 右上角项目图标
- "Edit Configurations"
- Python
    - "Script"  文件位置
    - "Script Parameters"   参数设置
    - "Python interpreter"  Python解释器

快捷方式
----

**pycharm 创建图标和快捷方式**
> Tools | Creat Desktop Entry

快捷键
---

Ctrl+鼠标 查看内置函数

`Alt+Enter` 万能键 各种提示和自动功能

`Ctrl+w` 扩展选取

`Ctrl+Shift+F10` 运行当前文件

`Ctrl+q` 差帮助

`Shift+Enter` 向下插行, 等于sublime的ctrl+enter

双击`Shift` 搜索一切

美化字体
----

1. http://www.webupd8.org/2013/06/better-font-rendering-in-linux-with.html
2. http://www.webupd8.org/2013/06/install-openjdk-patched-with-font-fixes.html
3. https://github.com/achaphiv/ppa-fonts/blob/master/openjdk-fontfix/README.md
   自定义版本见pycharm.sh
