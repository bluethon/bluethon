ss note
=======

``` sh
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
