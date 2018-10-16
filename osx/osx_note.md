OS X Note
=========

CMD
---

    open -a TextEdit filename           用写字板打开文件

Shortcuts
---------

    ctrl+cmd+f          全屏/最大化
    ctrl+cmd+q          lock screen

Packages
--------

    SizeUp              调整窗口(可收费, 可自定义快捷键, Used)
    VEEER               调整窗口(free, 不能自定义快捷键)
    CheatSheet          自动抓取快捷键(hold cmd)
    XtraFinder          文件管理器增强(较复杂)
    Karabiner-Elements  键盘映射
    Alfred              全局搜索
    MacPass             Keepass Mac开源版本
    iStat Menus         系统资源监控(收费, 有笔记)
    iTerm2              终端

Website
-------

[Mac soft crack](https://www.macsoftdownload.com/)

Note
----

### Dock icon disable

> <https://www.jianshu.com/p/75bc85cebd8e>

    vim /Applications/xxx.app/Contents/Info.plist

add(顶层dict下, 即只缩进2space)

    <key>LSUIElement</key>
    <true/>