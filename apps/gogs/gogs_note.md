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

### web hook

- 推送地址由webserver那边定
- 钩子内有推送记录, 可以重复发送某次记录, 或者创建新的测试记录
