新系统设定
========

package
-------

``` sh
shellcheck                  # vscode shellcheck依赖

# 壁纸
sudo add-apt-repository ppa:peterlevi/ppa
sudo apt-get update
sudo apt-get install variety variety-slideshow
```

### max_user_watches

> <https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc>

    cat /proc/sys/fs/inotify/max_user_watches
    # /etc/sysctl.conf
    fs.inotify.max_user_watches=524288
    sudo sysctl -p --system

### ohmyzsh

[补全插件](https://github.com/zsh-users/zsh-autosuggestions)

其他
----

[见此](http://www.cnblogs.com/xionghj/p/4211417.html)
