TinyProxy Note
==============

Install
-------

### apt

``` sh
sudo apt install tinyproxy
```

Config
------

> /etc/tinyproxy.conf

``` conf
# 允许连入得IP, 注释后为0.0.0.0
Allow 127.0.0.1
```

    sudo systemctl restart tinyproxy.service

Test
----

``` sh
# 以下为tinyproxy的服务器IP和其开放端口, 默认8888
# terminal
curl -x <IP>:<Port> www.baidu.com
# or
export HTTP_PROXY=<IP>:<Port>