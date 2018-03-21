Frp Note
========

内网穿透 转发数据

完整配置看`frp_full.ini`

use
---

    ./frps -c frps.ini

### frps

``` ini
[common]
bind_addr = 0.0.0.0
bind_port = 7000
dashboard_port = 7002
dashboard_user = root
dashboard_pwd = 123 
 
privilege_mode = true
privilege_token = 12345678
```

### frpc

    ./frpc -c frpc.ini

``` ini
[common]
server_addr = 47.104.145.108
server_port = 7000
auth_token = 12345678
privilege_token = 12345678

[tcp_port]
type = tcp
local_id = 127.0.0.1
local_port = 5000
remote_port = 6080
```

### supervisor

``` conf
[program:frp]
command = /path/to/code/frps -c /path/to/code/frps.ini
autostart = true
```

> [教程](https://segmentfault.com/a/1190000009353002)
> https://github.com/fatedier/frp/blob/master/README_zh.md
