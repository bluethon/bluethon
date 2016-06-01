将Caps Lock改为Esc键
===================

- 编辑`.profile`文件, 增加

    xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape'

- source重新载入文件生效


> [参考(win & linux)](http://mingxinglai.com/cn/2013/05/change-capslock-to-esc/)
