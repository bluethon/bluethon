Shadowsocks Note
================

new
---

> https://github.com/shadowsocks/shadowsocks-libev
> https://wiki.archlinux.org/index.php/Shadowsocks_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

### install

``` shell
# For Ubuntu 14.04 and 16.04 users, please install from PPA:
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:max-c-lv/shadowsocks-libev -y
sudo apt-get update
sudo apt install shadowsocks-libev

# For Ubuntu 16.10 or higher
sudo apt-get update
sudo apt install shadowsocks-libev
```

### use(server)

``` shell
# Edit the configuration file
sudo vim /etc/shadowsocks-libev/config.json

# Edit the default configuration for debian
sudo vim /etc/default/shadowsocks-libev

# Start the service
sudo systemctl start shadowsocks-libev.service
```

### use(local)

``` shell
cd /lib/systemd/system
sudo cp shadowsocks-libev-local@.service shadowsocks-libev-local.service
# edit local config name
sudo vim shadowsocks-libev-local.service

# auto start
sudo systemctl enable shadowsocks-libev-local.service
```

### config

``` json
{
    "server": "0.0.0.0",
    "server_port": 25,
    "password": "you_guess",
    "local_address": "127.0.0.1",
    "local_port": 1080,
    "timeout": 300,
    "method": "chacha20-ietf-poly1305",
    "fast_open": false,
    "worker": 1
}
```

---

old(decrepit)
---

#!/bin/bash
sudo apt install python-pip
pip install shadowsocks

sudo vim /etc/shadowsocks.json
{
    "server":"my_server_ip",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword",
    "timeout":300,
    "method":"rc4-md5",
    "fast_open": false
}

# run in the foreground
ssserver -c /etc/shadowsocks.json

# run in the background
ssserver -c /etc/shadowsocks.json -d start
ssserver -c /etc/shadowsocks.json -d stop

# check the log
sudo less /var/log/shadowsocks.log

# auto start on System Boot
sudo vim /etc/rc.local

ssserver -c /path/to/shadowsocks.json -d start
```
