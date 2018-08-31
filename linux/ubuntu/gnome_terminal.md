终端默认启动位置及大小自定义
=======================

原理
---

    gnome-terminal --help-window-options

- 修改ctrl+alt+t
  - 打开终端, 调整位置及大小
  - `xwininfo`, 点击窗口, 记下最后一行`-geometry ??x??-??-??`, 最后坐标有两种格式
  - 系统设置, System/Preferences/Keyboard Shortcuts/, 点击Add
  - Command: "gnome-terminal --geometry 80x24+554+210"
  - 设置快捷键
- 修改shell或Dash中启动选项
  - `sudo vim /usr/share/applications/gnome-terminal.desktop`
  - 修改`exec=`后为1中内容
