Ngrok Note
==========

教程

> [blog](https://imququ.com/post/self-hosted-ngrokd.html)

原理解释+脚本
http://nullget.sourceforge.net/?q=node/873&lang=zh-hant


参数说明
https://toontong.github.io/blog/about-ngrok.html

``` shell

# 复制服务器编译客户端到本地
sudo scp -i "aws_herock.pem" ubuntu@ec2-52-198-154-215.ap-northeast-1.compute.amazonaws.com:/home/ubuntu/github/ngrok/bin/ngrok .

# 启动服务端
sudo ./bin/ngrokd -tlsKey=server_yokeneng.key -tlsCrt=server_yokeneng.crt -domain="weixin.yokeneng.com" -httpAddr=":80" -httpsAddr=":443" -tunnelAddr=":44433"
sudo ./bin/ngrokd -tlsKey=device.key -tlsCrt=device.crt -domain="weixin.yokeneng.com" -httpAddr=":80" -httpsAddr=":443" -tunnelAddr=":44433"

# 本地启动客户端 子域名youkeneng1
sudo ./ngrok -config ~/ngrok.cfg -subdomain xcx 8000

# ngrok.cfg
eerver_addr: "weixin.lengqidong.com:44433"
trust_host_root_certs: false

```

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
# git clone https://github.com/inconshreveable/ngrok
### 请使用下面的地址，修复了无法访问的包地址
git clone https://github.com/tutumcloud/ngrok.git ngrok
cd ngrok

make release-server release-client
```
