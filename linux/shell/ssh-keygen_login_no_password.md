SSH免密码登陆
===========

``` bash
# 用ssh-keygen创建公钥(回车3次)
ssh-keygen -t rsa -f ~/.ssh/id_rsa_xxx

# 复制公钥到ssh 访问的主机, 然后需输入密码登陆
scp -P <port> ~/.ssh/id_rsa_xxx.pub root@<host>:~/.ssh/authorized_keys
# 升级版本(默认时可省去两个参数)
ssh-copy-id -i <identity_file.pub> -p <port> <user>@<host>

# 然后就可正常使用
ssh root@192.168.1.1 -P 8888

```
