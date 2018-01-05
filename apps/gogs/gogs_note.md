Gogs Notes
==========

bug
---

### Default-Start contains no runlevels

    sudo vim /etc/init.d/gogs

增加

``` sh
#!/bin/sh
### BEGIN INIT INFO
# Provides: catfish.xin
# Required-Start:
# Required-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: nat123 auto start
# Description: nat123 auto start and login service
### END INIT INFO
```

    sudo systemctl enable gogs      # 开机启动

Note
----

### custom configuration

默认的自定义`custom/conf/app.ini`在`/opt/gogs/`

`GOGS_CUSTOM`决定自定义目录位置

package.io打包版本位置如下

    vim /etc/gogs/config/app.ini

### web hook

- 推送地址由webserver那边定
- 钩子内有推送记录, 可以重复发送某次记录, 或者创建新的测试记录
