将Caps Lock改为Esc键
===================

For Gnome(17.10 or later)
------------------

> https://askubuntu.com/a/969066/537695

    sudo apt install gnome-tweak-tool

Keyboard & Mouse -> Additional Layout Options -> Caps Lock key behavior

For Unity(before 17.10)
------------------

- touch .Xmodmap

- add

``` bash
# equal to
# xmodmap -e 'clear Lock' -e 'keycode 66 = Escape'
clear Lock
keycode 66 = Escape
```
- source .Xmodmap

> - [fcitx wiki](https://fcitx-im.org/wiki/FAQ#xmodmap_settings_being_overwritten)
> - [xev 提供按键代码](http://askubuntu.com/a/23493/537695)
> - [xmodmap设置参考](http://askubuntu.com/a/670033/537695)
> - [参考(win & linux)](http://mingxinglai.com/cn/2013/05/change-capslock-to-esc/)
