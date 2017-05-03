Package Control设置shadowsocks代理
=================================

Package Control的代理只能使用http, 而shadowsocks使用的是socks5代理, 所以需要使用privoxy中转
> [refer][0]
> [配置方法详细说明][1]

``` bash
# 安装包
sudo apt install privoxy

# 更改设置为ss的配置
sudo vim /etc/privoxy/config

# 增加如下(也可搜索对比原生写法)
forward-socks5 packagecontrol.io 127.0.0.1:1080 .

# 搜索查找监听端口, 默认如下
listen-address  127.0.0.1:8118

# 更改Package Control的settings user
{
    "http_proxy": "http://127.0.0.1:8118",
    "https_proxy": "http://127.0.0.1:8118",
}

# 启动privoxy服务
/etc/init.d/privoxy start
```


[0]: http://blog.csdn.net/yanzi1225627/article/details/51064306
[1]: https://program-think.blogspot.com/2014/12/gfw-privoxy.html
