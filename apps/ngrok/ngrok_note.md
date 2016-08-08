Ngrok Note
==========

教程

> [blog](https://imququ.com/post/self-hosted-ngrokd.html)

``` shell

# 复制服务器编译客户端到本地
sudo scp -i "aws_herock.pem" ubuntu@ec2-52-192-24-183.ap-northeast-1.compute.amazonaws.com:/home/ubuntu/ngrok_new/bin/ngrok .

# 启动服务端
sudo ./bin/ngrokd -tlsKey=server.key -tlsCrt=server.crt -domain="weixin.lengqidong.com" -httpAddr=":80" -httpsAddr=":8082" -tunnelAddr=":44433"

# 本地启动客户端 子域名youkeneng1
sudo ./ngrok -config ~/ngrok.cfg -subdomain youkeneng1 8000

# ngrok.cfg
eerver_addr: "weixin.lengqidong.com:44433"
trust_host_root_certs: false

```
