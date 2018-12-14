OS X Note
=========

CMD
---

    open -a TextEdit filename           用写字板打开文件
    sudo spctl --master-disable         开启允许任何来源软件安装
    osascript -e 'display notification "通知内容" with title "标题" subtitle "子标题"'
                                        发送桌面通知
    networksetup -setairportnetwork $INTERFACE $SSID $PASSWORD
                                        WiFi连接(网卡名称 WiFi 密码)

Shortcuts
---------

    Ctrl-cmd-f          全屏/最大化
    Ctrl-cmd-q          lock screen
    Ctrl-Cmd-d          查词(同Forcetouch)

Packages
--------

    SizeUp              调整窗口(license, 可自定义快捷键, notes)
    VEEER               调整窗口(free, 不能自定义快捷键)
    CheatSheet          自动抓取快捷键(hold cmd)
    XtraFinder          文件管理器增强(较复杂)
    Karabiner-Elements  键盘映射
    Alfred              全局搜索
    MacPass             Keepass Mac开源版本
    iStat Menus         系统资源监控(license, notes)
    iTerm2              终端
    Smooze              外接鼠标滚轮速度/方向调节(license)
    Hopper Disassembler 反汇编工具(hack, license, notes)
    Key Codes           键盘码(Hex)<https://manytricks.com/keycodes/>

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

### iTerm2

    # 每次打开当前目录, 而非home
    Preferences / Profiles / Reuse previous session's directory
    # paste slow
    # https://apple.stackexchange.com/a/315515

### 安装GNU Linux版的 系统命令

``` sh
brew install coreutils
# All commands have been installed with the prefix 'g'.
# or Set below to .zshrc
PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
MANPATH="/usr/local/opt/coreutils/libexec/gnuman:$MANPATH"
```

### 修改ls color

> <https://geoff.greer.fm/lscolors/>

``` sh
brew coreutils
# .zshrc
test -r ~/.dircolors && eval "$(gdircolors -b ~/.dircolors)" || eval "$(gdircolors -b)"
if [ -n "$LS_COLORS" ]; then
    zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
fi
alias ls='gls --color=auto'
alias ll='ls -lh --color=always'
alias l='gls -alh --color=auto'
```

### python venv

``` shell
brew install pyenv
pip install --user pipenv

# .zshrc
eval "$(pyenv init -)"
pyenv install 3.6.6
# if zlib not available
CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install -v 3.6.6

# cd project
pyenv local 3.6.6
pipenv install
```
