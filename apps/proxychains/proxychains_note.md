proxychains - linux 程序代理工具
==============================

### install

sudo apt install proxychains


### edit config
vim /etc/proxychains.conf

将`socks4 127.0.0.1 9095`改为

    socks5 127.0.0.1 1080

### use

    proxychains curl www.google.com
    proxychains curl ip.gs

