Ngrok Note
==========

教程

> [blog](https://imququ.com/post/self-hosted-ngrokd.html)

原理解释+脚本
http://nullget.sourceforge.net/?q=node/873&lang=zh-hant


参数说明
https://toontong.github.io/blog/about-ngrok.html

记录
----

### 生成证书

``` sh
#!/bin/sh

domain="yourdomain.com"

openssl genrsa -out rootCA.key 2048
openssl req -x509 -new -nodes -key rootCA.key -subj "/CN=$domain" -days 5000 -out rootCA.pem
openssl genrsa -out device.key 2048
openssl req -new -key device.key -subj "/CN=$domain" -out device.csr
openssl x509 -req -in device.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out device.crt -days 5000

cp rootCA.pem ../assets/client/tls/ngrokroot.crt
cp device.crt ../assets/server/tls/snakeoil.crt
cp device.key ../assets/server/tls/snakeoil.key
```

### 编译ngrok

``` sh
# 装必要的工具
sudo apt-get install build-essential golang mercurial git

# git clone https://github.com/inconshreveable/ngrok
### 请使用下面的地址，修复了无法访问的包地址
git clone https://github.com/tutumcloud/ngrok.git ngrok
cd ngrok

make release-server release-client
```

### 使用(可以使用-h查看帮助)

``` shell
# 复制服务器编译客户端到本地
sudo scp -P <port> <user>@<host>:[path to dirname] .

# 启动服务端
sudo ./bin/ngrokd -domain yourdomain.com [-httpAddr :86]

# 本地启动客户端 子域名j1
./ngrok -config cfg.yaml -subdomain test <local_port>
# 主机方式
./ngrok -config cfg.yaml -hostname yourdomain.com[:port] <local_port>
# 后台启动
./ngrok -config cfg.yaml -subdomain test -log=stdout <local_port> > /dev/null &
```

cfg.yaml 可自定义端到端通信端口, 默认4443, 可多配置写在同一设置文件里

``` yaml
server_addr: "yourdomain.com:4443"
trust_host_root_certs: false

tunnels:
    <subdomain1>:
        proto:
            # 此处80对应服务端的httpAddr
            http: 80
    <subdomain2>:
        proto:
            http: 80
```
